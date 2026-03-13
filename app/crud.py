from sqlalchemy.orm import Session
from.import models

def create_address(db: Session, address):
    db_address = models.Address(**address.dict())
    db.add(db_address)
    db.commit
    db.refresh(db_address)
    return db_address

def get_address(db: Session):
    return db.query(models.Address).all()

def update_address(db : Session, address_id : int, adress_data):
    address = db.query(models.Address).filter(models.Address.id == address_id).first()
    if not address:
        return None
    
    for key, value in adress_data.dict().items():
        setattr(address,key, value)
        db.commit()
        db.refresh(address)
    
    return address



def delete_address(db: Session, address_id : int):
    address = db.query(models.Address).filter(models.Address.id == address_id).first()
    if address :
        db.delete(address)
        db.commit()
    return address
