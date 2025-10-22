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
| **ics** | Parsing des fichiers `.ics` |

---

## Installation locale

### 1 - Cloner le repo

```bash
git clone https://github.com/Raphael-K-78/ics-api.git
cd ics-api
```

### 2 - Créer et activer un environnement virtuel
\_ Sous Linux / MacOS \_
```bash
python3 -m venv venv
source venv/bin/activate
```
\_ Sous Windows \_
```bash
python3 -m venv venv
venv\Scripts\activate
```

### 3 - Installer les dépendances
\_ Avec Requirements.txt \_
```bash
pip install -r requirements.txt
```
\_ Sans Requirements.txt \_
```bash
pip install fastapi uvicorn httpx ics
```

```bash
pip freeze > requirements.txt
```

---

## Execution locale
```
uvicorn main:app --reload
```
puis ouvre ton navigateur sur [127.0.0.1:8000](http://127.0.0.1:8000)

---

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