#!/usr/bin/python3
"""Place Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float
from os import getenv
from models.city import City
from sqlalchemy.orm import relationship
from models.amenity import Amenity


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id')),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id')))


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    if getenv("HBNB_TYPE_STORAGE") is "file":
        @property
        def cities(self):
            """getter for place"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

        @property
        def amenities(self):
            '''amenities getter'''
            #  list_amenity_place = []
            #  all_amenities = models.storage.all(Amenity)
            #  for amenity in all_amenities.values():
            #    if amenity.place_id == self.id:
            #        amenity_ids.append(amenity)
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            '''amenities setter'''
            if isinstance(obj, Amenity):  # and obj.place_id == self.id:
                self.amenity_ids.append(obj.id)
