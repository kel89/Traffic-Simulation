"""
   _____            _             _ _           
  / ____|          | |           | | |          
 | |     ___  _ __ | |_ _ __ ___ | | | ___ _ __ 
 | |    / _ \| '_ \| __| '__/ _ \| | |/ _ \ '__|
 | |___| (_) | | | | |_| | | (_) | | |  __/ |   
  \_____\___/|_| |_|\__|_|  \___/|_|_|\___|_|   
                                              
Kenneth Lipke 
September 2019
"""

import numpy as np

class Controller:
	"""
	This class serves as the object used to control the simulation
	Here the parameters will be set to control the number of vehicles
	the length of the simulation, following distances, speeds, etc.

	The controller will then do the work of creating the Vehicle objects 
	and ticking the simulation along

	There are also methods to introduce disturbances

	Methods:
	--------

	init:	Creates a simulation object, has the option of giving it 
			simulation parameters through a dictionary (where the keys
			are strings)

	initialize_simulation: 	creates the vehicles for the simulation and sets
			up all the requisite trackers

	start_simulation:	starts the simulation, can only be called AFTER the
			simulation has been initialized


	Fileds:
	--------

	sim_length: 	length of simulation in seconds
	num_vehicles:	the number of vehicles in the simulation
	following_dist:	following distance to set for vehicles
	speed_target:	target speed to give the vehicles
	"""

def __init__(self, *config, **kwargs):
	"""
	Takes in a config dictionary with possible fields
	and creates the Controller instance
	"""

	# set attributes from config
	for key in config:
		setattr(self, key, config[key])

	# set attributes from kwargs
	for key in kwargs:
		setarrt(self, key, kwargs[key])





