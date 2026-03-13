# CRUD helper functions for Address model
# This module handles all database interactions related to address records
from sqlalchemy.orm import Session
from.import models


def create_address(db: Session, address):
    """
    Create and store a new address record in the database.
    """
    db_address = models.Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def get_address(db: Session):
    """
    Retrieve all addresses stored in the database.
    """
    return db.query(models.Address).all()


def update_address(db : Session, address_id : int, address_data):
    """
    Update an existing address record using its ID.
    Returns the updated object if found, otherwise None.
    """
    address = db.query(models.Address).filter(models.Address.id == address_id).first()
    if not address:
        return None
    
    # Update fields dynamically from request data
    for key, value in address_data.dict().items():
        setattr(address,key, value)
        db.commit()
        db.refresh(address)
    
    return address



def delete_address(db: Session, address_id : int):
    """
    Delete an address record by ID.
    Returns the deleted object if it existed.
    """
    address = db.query(models.Address).filter(models.Address.id == address_id).first()
    if address :
        db.delete(address)
        db.commit()
    return address
