"""
   _____ _              _____            _             _ _           
  / ____(_)            / ____|          | |           | | |          
 | (___  _ _ __ ___   | |     ___  _ __ | |_ _ __ ___ | | | ___ _ __ 
  \___ \| | '_ ` _ \  | |    / _ \| '_ \| __| '__/ _ \| | |/ _ \ '__|
  ____) | | | | | | | | |___| (_) | | | | |_| | | (_) | | |  __/ |   
 |_____/|_|_| |_| |_|  \_____\___/|_| |_|\__|_|  \___/|_|_|\___|_|   
																	   
											  
Kenneth Lipke 
September 2019
"""

import numpy as np

from Vehicle import Vehicle

class Sim_Controller:
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
	hz:				hertz, ticks per second for the simulation
	"""

	def __init__(self, config, **kwargs):
		"""
		Takes in a config dictionary with possible fields
		and creates the Controller instance
		"""

		#set attributes from config
		for key in config:
			setattr(self, key, config[key])

		# set attributes from kwargs
		for key in kwargs:
			setarrt(self, key, kwargs[key])


	def initialize_simulation(self):
		"""
		Initializes the simulation, creating the vehicle objects
		and setting up trackers
		"""

		# Initialize vehicle list
		self.vehicles = [0]*self.num_vehicles

		# Create vehicles
		for i in range(self.num_vehicles):
			# Get the vehicle in front for initialization
			vehicle_infront = self.vehicles[i-1] if i !=0 else None

			self.vehicles[i] = Vehicle(target_speed = self.target_speed,
					target_following_distance = self.target_following_distance, 
					vehicle_infront = vehicle_infront,
					vehicle_behind = None,
					sim_length = self.sim_length,
					start_position = (self.num_vehicles*10 - i*10),
					hz = self.hz)



	"""
	   ___     _   _                             _   ___      _   _              
	  / __|___| |_| |_ ___ _ _ ___  __ _ _ _  __| | / __| ___| |_| |_ ___ _ _ ___
	 | (_ / -_)  _|  _/ -_) '_(_-< / _` | ' \/ _` | \__ \/ -_)  _|  _/ -_) '_(_-<
	  \___\___|\__|\__\___|_| /__/ \__,_|_||_\__,_| |___/\___|\__|\__\___|_| /__/
	"""

	def set_sim_length(self, sim_length):
		self.sim_length = sim_length

	def set_num_vehicles(self, num_vehicles):
		self.num_vehicles = num_vehicles

	def set_speed_target(self, speed_target):
		self.speed_target = speed_target



