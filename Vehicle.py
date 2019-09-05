"""
 _    __     __    _      __   
| |  / /__  / /_  (_)____/ /__ 
| | / / _ \/ __ \/ / ___/ / _ \
| |/ /  __/ / / / / /__/ /  __/
|___/\___/_/ /_/_/\___/_/\___/

Kenny Lipke 
August 2019
"""

import numpy as np


class Vehicle:
	"""
	Fields:
	-------
		target_speed:     the velocity that is to be maintained, except when 
						  slowing for vehicle infront
		
		target_following_distance:    desired distance between this vehicle and
									  the one infront of it (to be tracked in FEET)
		
		vehicle_infront:   reference to the vehilce infront, None if 
						   this is the first in line
		
		vehicle_behind:    reference to the vehicle behind, None if this
						   is the last in line
						   
		sim_length:   length of simulation in ticks, used to set tracking array
		
		position_array:   this is a numpy array of the position of the vehicle
						  at ticks throughout the simulation
						  
		current_position:  the coordinate of the vehicle at the current stage of
						   the simulation
						   
		current_tick:   the current step of the simulation, in [0, sim_length)
	
	Methods:
	--------
	
		tick:  this is the main method that is called at each step of the simulation
			   takes no argument, and move the vehicle one step forward in time. 
			   This involes looking at the location of the vehicle infront 
			   and checking the following distance versus the target distnace, 
			   determine what to do with ones own speed for the next step, making
			   that adjustment, and taking a step in space and time. These are also
			   recorded
			   
		
	
	"""
	
	def __init__(self, target_speed, target_following_distance, vehicle_infront,
				vehicle_behind, sim_length, hz=1, start_position=0):
		"""
		Sets fields and initialize trackers
		"""
		# Set fields
		self.target_speed = target_speed # in mph
		self.target_following_distance = target_following_distance # in feet
		self.vehicle_infront = vehicle_infront
		self.vehicle_behind = vehicle_behind
		self.sim_length = sim_length
		self.speed_override = None
		self.hz = hz
		
		# Initialize trackers
		self.position_array = np.zeros(self.sim_length+1) # so we accomodate start
		self.current_position = start_position
		self.current_tick = 0
		self.current_speed = self.target_speed # start at desired speed

		self.FEET_PER_SECOND = 88
		
	def set_speed_override(self, val):
		"""
		Sets the speed override value
		"""
		self.speed_override = val
		
	def reset_speed_override(self):
		"""
		turns of the speed override
		"""
		print('reseting speed override')
		self.speed_override = None
		
	def tick(self):
		"""
		Moves the simulation forward by one step.
		Looks at the position of the vehicle infront to calculate the real 
		following distance to compare it to the target_following distnance
		Uses this to calculate a desired speed
		Moves forward one step.
		Tracks the new position, speed, and increments tick
		
		speed_override gives the simulation the option to set a new speed
		which will be independent
		"""
		
		# Calculate following distance
		current_following_distance = self.get_following_distance()
		
		# calculate speed
		next_speed = self.calculate_next_speed(current_following_distance, self.current_speed)
		
		# Check for override
		next_speed = next_speed if self.speed_override==None else self.speed_override
		
		# move simulation
		self.current_tick += 1
		self.current_position += next_speed*self.FEET_PER_SECOND/(self.hz)
		self.current_speed = next_speed
		
		# track changes
		self.position_array[self.current_tick] = self.current_position
		
	def get_following_distance(self):
		"""
		Looks at the current position of the vehicle, and 
		the current position of the vehicle infront
		returns the delta in feet
		"""
		# Get the position of the vehicle infront (if exists)
		if (self.vehicle_infront == None):
			in_front_position = np.inf
		else:
			in_front_position = self.vehicle_infront.get_position()
			
		delta = in_front_position - self.current_position
		return delta
	
	def calculate_next_speed(self, following_distance, current_speed):
		"""
		Takes in a current following distance and current speed (may not need the speed)
		and returns the speed that the model would dictate in an attempt to maintain
		the desired following distance the next step
		 = min(target_speed, delta_true/detla_target * target_speed)

		Here is where we need to figure out how to deal with the hertz

		Lets say a car can change speed at most 5mph/s, if following_distnace
		is less than the target, then we decrease the speed, if it
		is greater than the target than we speeed up (to a limit)

		Lets also add some random noise in there

		"""
		# proposed_speed = self.target_speed * ( following_distance / self.target_following_distance)
		# truncated_speed = np.min([proposed_speed, self.target_speed])
		# return truncated_speed
		
		if (following_distance < self.target_following_distance):
			# Slow down
			next_speed = current_speed - (1/self.hz)*5
		elif (following_distance > self.target_following_distance):
			# speed up
			next_speed = current_speed + (1/self.hz)*5
		else:
			# euquals
			next_speed = current_speed

		# add some noise
		next_speed += np.random.normal(0, 2)

		return next_speed
		
		
	"""
	   ___     _   _                             _   ___      _   _              
	  / __|___| |_| |_ ___ _ _ ___  __ _ _ _  __| | / __| ___| |_| |_ ___ _ _ ___
	 | (_ / -_)  _|  _/ -_) '_(_-< / _` | ' \/ _` | \__ \/ -_)  _|  _/ -_) '_(_-<
	  \___\___|\__|\__\___|_| /__/ \__,_|_||_\__,_| |___/\___|\__|\__\___|_| /__/
	"""


	def get_position(self):
		return self.current_position
	
	def get_speed(self):
		return self.current_speed
	
	def get_position_history(self):
		return self.position_array
	
	
	def __repr__(self):
		s = "-"*25
		s += "\nTick: \t\t" + str(self.current_tick)
		s += "\nPosition: \t" + str(self.current_position)
		s += "\nSpeed: \t\t" + str(self.current_speed)
		s += "\n" + "-"*25
		return s