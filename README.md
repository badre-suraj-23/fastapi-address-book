# FastAPI Address Book

# Project Structure

fastapi-address-book/
│
├─ app/
│   ├─ main.py           # FastAPI app entry point
│   ├─ models.py         # SQLAlchemy models
│   ├─ schemas.py        # Pydantic schemas
│   ├─ database.py       # SQLite connection setup
│   └─ crud.py           # Create, Read, Update, Delete logic
│
├─ requirements.txt      # Python dependencies
├─ .gitignore            # To ignore venv, __pycache__, etc.
└─ README.md             # Instructions to run

This is a small API project built using FastAPI and SQLite.  
The goal of this project is to create an address book where users can store addresses with coordinates and search for nearby locations.

The project does not include a GUI. APIs can be tested using FastAPI's built-in Swagger documentation.

---

## Tech Used

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Geopy (for distance calculation)
- Uvicorn

---

## Project Structure

fastapi-address-book

app/
- main.py
- models.py
- schemas.py
- crud.py
- database.py

address.db  
requirements.txt

---

## Setup Instructions

Clone the project

git clone <repo-link>

go inside the folder

cd fastapi-address-book

create virtual environment

python -m venv venv

activate environment (windows)

venv\Scripts\activate

install dependencies

pip install -r requirements.txt

---

## Run the application

Start the server

uvicorn app.main:app --reload

Server will run at

http://127.0.0.1:8000

Swagger API docs

http://127.0.0.1:8000/docs

---

## Available APIs

Create address

POST /addresses/

Get all addresses

GET /addresses/

Update address

PUT /addresses/{id}

Delete address

DELETE /addresses/{id}

Search nearby addresses

GET /addresses/nearby

Example

/addresses/nearby?lat=18.5204&lon=73.8567&distance_km=5

---

## Notes

- Address coordinates are stored in the SQLite database.
- Nearby address search is implemented using geodesic distance calculation.
- Swagger UI can be used to test all endpoints easily.
