#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """User specs
    Args:
    BaseModel : main model
    Attrs:
    name (str) : name of user
    password (str) : password of user
    first_name (str) : first_name of user
    last_name (str) : last_name of user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
