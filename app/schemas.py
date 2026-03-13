from pydantic import BaseModel

class AddressCreate(BaseModel):
    name : str
    street : str
    city : str
    latitude : float
    longitude : float


class Address(AddressCreate):
    id : int
    class Config:
        from_attributes = True
        