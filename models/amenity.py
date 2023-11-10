#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity specs
    Args:
        BaseModel : main model
    Attrs:
        name (str) : name of the ameniy
    """
    name = ""
