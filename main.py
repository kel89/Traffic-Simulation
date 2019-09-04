"""
                  _       
                 (_)      
  _ __ ___   __ _ _ _ __  
 | '_ ` _ \ / _` | | '_ \ 
 | | | | | | (_| | | | | |
 |_| |_| |_|\__,_|_|_| |_|
                          

 Kenneth Lipke
 September 2019
 """

import numpy as np
import matplotlib.pyplot as plt

from Sim_Controller import Sim_Controller
from Vehicle import Vehicle


if __name__ == "__main__":
	# Define the simulation parameters
	config = {
		"num_vehicles": 	100,
		"sim_length": 		300, # seconds (~5 minutes)
		"target_speed": 	45, # MPH
		"target_following_distance": 	20, # feet,
		"hz": 				2 # ticks per second
	}

	# Create a controller object
	controller = Sim_Controller(config)

	# initialize simulation
	controller.initialize_simulation()