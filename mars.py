# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:51:59 2024

@author: iamrs
"""

import time

class Satellite:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0, 0)  # Initial position in space

    def move_to_mars(self):
        print(f"Sending satellite {self.name} to Mars...")
        time.sleep(2)  # Simulating travel time
        self.position = (54.6, 220.3, 5.6)  # New position near Mars
        print(f"Satellite {self.name} has reached Mars!")

# Create a satellite object
mars_satellite = Satellite("MarsSatellite1")

# Send the satellite to Mars
mars_satellite.move_to_mars()

# Print the final position of the satellite
print(f"{mars_satellite.name} position after reaching Mars: {mars_satellite.position}")

