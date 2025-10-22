from fastapi import FastAPI, Query
from typing import Optional
from ics import Calendar
from datetime import datetime, timezone
import httpx
import hashlib

app = FastAPI()

CACHE = {}
CACHE_TTL = 60 * 10  # 10 minutes

async def fetch_calendar(url: str) -> Calendar:
    url_hash = hashlib.md5(url.encode()).hexdigest()
    now = datetime.now().timestamp()

    if url_hash in CACHE:
        ts, cal = CACHE[url_hash]
        if now - ts < CACHE_TTL:
            return cal

    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=10.0)
        response.raise_for_status()

    cal = Calendar(response.text)
    CACHE[url_hash] = (now, cal)
    return cal

@app.get("/")
async def get_events(
    url: str = Query(..., description="URL du fichier ICS"),
    start_date: Optional[str] = Query(None, description="Date début (YYYY-MM-DD)"),
    end_date: Optional[str] = Query(None, description="Date fin (YYYY-MM-DD)")
):
    try:
        calendar = await fetch_calendar(url)
    except Exception as e:
        return {"error": f"Impossible de télécharger/parsing {url} : {e}"}

    # Convertir start_date et end_date en datetimes aware (UTC)
    start_dt = datetime.fromisoformat(start_date).replace(tzinfo=timezone.utc) if start_date else None
    end_dt = datetime.fromisoformat(end_date).replace(tzinfo=timezone.utc) if end_date else None

    events = []
    for event in calendar.events:
        ev_start = event.begin.datetime
        ev_end = event.end.datetime

        # Filtrage par date
        if start_dt and ev_end < start_dt:
            continue
        if end_dt and ev_start > end_dt:
            continue

        events.append({
            "name": event.name,
            "start": str(ev_start),
            "end": str(ev_end),
            "location": event.location,
            "description": event.description
        })

    return {"count": len(events), "events": events}