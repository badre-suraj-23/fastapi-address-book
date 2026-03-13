from fastapi import FastAPI
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from geopy.distance import geodesic

from.database import SessionLocal,engine,Base
from. import models,schemas,crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book Api")

# @app.get("/")
# def read_root():
#     return {"message":"Fast Api Server is Running!"}



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/addresses/")
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    new_address = models.Address(**address.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address

@app.get("/addresses/")
def get_addresses(db : Session = Depends(get_db)):
    return crud.get_address(db)

@app.put("/addresses/{address_id}")
def update_address(address_id : int, address : schemas.AddressCreate, db : Session = Depends(get_db)):
    updated = crud.update_address(db, address_id, address)
    
    if not update:
        return {"error":"Address not found"}
    return updated

@app.delete("/address/{address_id}")
def delete_address(address_id : int, db : Session = Depends(get_db)):
    return crud.delete_address(db, address_id)



@app.get("/addresses/nearby/")
def get_nearby(lat : float, lon : float, distance_km : float, db : Session = Depends(get_db)):
    address = crud.get_address(db)
    
    result = []

    for addr in address:
        dist = geodesic((lat, lon), (addr.latitude, addr.longitude)).km
        if dist <= distance_km:
            result.append(addr)
    
    return result



