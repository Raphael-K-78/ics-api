from fastapi import FastAPI, Query
from typing import Optional
from icalendar import Calendar
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

    cal = Calendar.from_ical(response.text)
    CACHE[url_hash] = (now, cal)
    return cal


@app.get("/")
async def get_events(
    url: str = Query(..., description="URL du fichier ICS"),
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None)
):
    try:
        calendar = await fetch_calendar(url)
    except Exception as e:
        return {"error": f"Erreur téléchargement/parsing: {e}"}

    start_dt = datetime.fromisoformat(start_date).replace(tzinfo=timezone.utc) if start_date else None
    end_dt = datetime.fromisoformat(end_date).replace(tzinfo=timezone.utc) if end_date else None

    events = []

    for component in calendar.walk():
        if component.name != "VEVENT":
            continue

        ev_start = component.get("dtstart").dt
        ev_end = component.get("dtend").dt

        # normalisation datetime
        if isinstance(ev_start, datetime) and ev_start.tzinfo is None:
            ev_start = ev_start.replace(tzinfo=timezone.utc)

        if isinstance(ev_end, datetime) and ev_end.tzinfo is None:
            ev_end = ev_end.replace(tzinfo=timezone.utc)

        if start_dt and ev_end < start_dt:
            continue
        if end_dt and ev_start > end_dt:
            continue

        events.append({
            "name": str(component.get("summary")),
            "start": str(ev_start),
            "end": str(ev_end),
            "location": str(component.get("location")),
            "description": str(component.get("description"))
        })

    return {"count": len(events), "events": events}