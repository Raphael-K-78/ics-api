# FastAPI ICS Calendar API

API créer avec **FastAPI** permettant de **télécharger, parser et filtrer des fichiers ICS** (iCalendar) à partir d’une URL distante.

---

## Fonctionnalités

- Téléchargement de fichier iCalendar depuis une URL
- Parse et liste des événements du calendrier
- Filtre les événements par **date de début** et **date de fin**
- Mise en cache local (10 minutes) pour éviter de retélécharger inutilement

---

## Dépendances
| Librairie | Rôle |
|------------|------|
| **fastapi** | Framework web asynchrone |
| **uvicorn** | Serveur ASGI pour exécuter FastAPI |
| **httpx** | Client HTTP asynchrone |
| **icalendar** | Parsing des fichiers `.ics` |

---

## Installation locale

### 1 - Cloner le repo

```bash
git clone https://github.com/Raphael-K-78/ics-api.git
cd ics-api
```

### 2 - Créer et activer un environnement virtuel
_Sous Linux / MacOS_
```bash
python3 -m venv venv
source venv/bin/activate
```
_Sous Windows_
```bash
python3 -m venv venv
venv\Scripts\activate
```

### 3 - Installer les dépendances
_Avec Requirements.txt_
```bash
pip install -r requirements.txt
```
_Sans Requirements.txt_
```bash
pip install fastapi uvicorn httpx icalendar httpx
```

```bash
pip freeze > requirements.txt
```

---

## Execution locale
```
uvicorn app:app --reload
```
puis ouvre ton navigateur sur [127.0.0.1:8000](http://127.0.0.1:8000)

---

## Utilisation
_Documentation_:
[Lien de la documentation](http://127.0.0.1:8000/docs)
_Requête_
```
http://127.0.0.1:8000/?url=https://url.ics.fr/fichier.ics&start_date=xxxx-xx-xx&end_date=xxxx-xx-xx
```
```
http://127.0.0.1:8000/?url=https://url.ics.fr/fichier.ics
```



## Structure du Projet
ics-api/
├── .gitignore
├── app.py
├── LICENSE
├── README.md
├── requirements.txt
└── venv/ 

---

## auteur
Created by [Raphaël K.](https://github.com/Raphael-K-78)

---

## Licence
Ce projet est distribué sous licence MIT.
Libre à toi de le modifier et le réutiliser.