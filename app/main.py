# Main FastAPI application file
# This module exposes REST endpoints for managing address records.
# The API allows users to create, update, delete and search addresses
# stored in a SQLite database.

from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from geopy.distance import geodesic

from.database import SessionLocal,engine,Base
from. import models,schemas,crud

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book Api")

# @app.get("/")
# def read_root():
#     return {"message":"Fast Api Server is Running!"}

# Dependency function to provide a database session to API routes
# A new session is created per request and closed afterwards
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/addresses/")
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    """
    Create a new address record in the database.
    Accepts address details including latitude and longitude.
    """
    new_address = models.Address(**address.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address


@app.get("/addresses/")
def get_addresses(db : Session = Depends(get_db)):
    """
    Retrieve all stored addresses.
    """
    return crud.get_address(db)


@app.put("/addresses/{address_id}")
def update_address(address_id : int, address : schemas.AddressCreate, db : Session = Depends(get_db)):
    """
    Update an existing address using its ID.
    """
    updated = crud.update_address(db, address_id, address)
    
    if not update:
        return {"error":"Address not found"}
    return updated


@app.delete("/address/{address_id}")
def delete_address(address_id : int, db : Session = Depends(get_db)):
    """
    Delete an address record by ID.
    """
    return crud.delete_address(db, address_id)



@app.get("/addresses/nearby/")
def get_nearby(lat : float, lon : float, distance_km : float, db : Session = Depends(get_db)):
    """
    Retrieve addresses within a given distance (in KM)
    from the provided latitude and longitude.
    """
    address = crud.get_address(db)
    
    result = []

    # Calculate distance between input coordinates and stored addresses
    for addr in address:
        dist = geodesic((lat, lon), (addr.latitude, addr.longitude)).km
        if dist <= distance_km:
            result.append(addr)
    
    return result



