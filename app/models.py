# SQLAlchemy model representing an Address record stored in the database
from sqlalchemy import Column,Integer,String,Float
from.database import Base


class Address(Base):
    __tablename__ = "addresses"

    # Human readable address
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    street = Column(String)
    city = Column(String)

    # Latitude and longitude coordinates
    latitude = Column(Float)
    longitude  = Column(Float)