#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review specs
    Args:
        BaseModel : main model
    Attrs:
        user_id (int) : user_id of the review
        place_id (int) : place_id of the review
        text (str) : text of the review
    """
    user_id = ""
    place_id = ""
    text = ""
