#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place specs
    Args:
        BaseModel : main model
    Attrs:
        user_id (int) : user_id of the place
        name (str) : name of the place
        city_id (int) : city_id of the place
        description (str) : description of the place
        number_rooms (int) : number_rooms of the place
        number_bathrooms (int) : number_bathrooms of the place
        max_guest (int) : max_guest of the place
        price_by_night (int) : name of the place
        latitude (int) : latitude of the place
        longitude (int) : longitude of the place
        """
    user_id = ""
    name = ""
    city_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
