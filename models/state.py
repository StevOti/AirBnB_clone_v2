#!/usr/bin/python3
"""This is the state class"""
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
        cities = relationship between state and city tables.
    """

    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref='state', cascade="all, delete,")

    else:
        @property
        def cities(self):
            """Get a list of City instances with
            state_id equals to the current state.id.

            This is a getter attribute for FileStorage
            relationship between state and city
            """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.state_id:
                    city_list.append(city)
            return city_list
