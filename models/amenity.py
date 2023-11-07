#!/usr/bin/python3
from models import BaseModel

class Amenity(BaseModel):
	"""Amenity specs

	Args:
	    BaseModel : main model
	Atrs:
	    name (str) : name of the ameniy
	"""
	name = ""