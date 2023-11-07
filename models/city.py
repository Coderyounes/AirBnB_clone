#!/usr/bin/python3
from models import BaseModel

class City(BaseModel):
	"""City specs

	Args:
	    BaseModel : main model
	Attrs:
	    state_id (int) : state_id of city
	    name (str) : name of city
	"""
	state_id = ""
	name = ""