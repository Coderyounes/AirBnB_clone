#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """State specs
        Args:
            BaseModel : main model
        Atrs:
            name (str) : name of the state
    """
    name = ""
