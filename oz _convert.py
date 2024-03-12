# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:22:35 2024

@author: iamrs
"""

def oz_to_kg(ounces):
    kilograms = ounces * 0.0283495
    return kilograms

try:
    ounces = float(input("Enter the weight in ounces: "))
    kilograms = oz_to_kg(ounces)
    print(f"{ounces} ounces is equal to {kilograms} kilograms")
except ValueError:
    print("Please enter a valid number.")
