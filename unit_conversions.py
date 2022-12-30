# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name(s):         Saylor Sherrodd
#                   Ricardo Mejia
#                   Andrew Spears
#                   Spencer Torres
#                   Anderson Loan
# Section:         574
# Assignment:   Lab 3.15
# Date:         6 9 2022
#

from math import *
#this ask the user to give the program a number to convert
convert = float(input("Please enter the quantity to be converted:\n"))
#these will convert the inputted value to the corrospodning conversion 
pound_to_force = round((convert * 4.44822195959),2)
meters_to_feet = round((convert * 3.28083991014),2)
atmospheres_to_kPa = round((convert * 101.325001795),2)
watts_to_BTU = round((convert * 3.4121435905),2)
Liters_to_Gallons = round((convert * 15.8503287894),2)
Celcius_to_Fahrenheit = round(((convert * 1.8)+32),2)

print(f"{convert:.2f} pounds force is equivalent to {pound_to_force} Newtons")
print(f"{convert:.2f} meters is equivalent to {meters_to_feet} feet")
print(f"{convert:.2f} atmospheres is equivalent to {atmospheres_to_kPa} kilopascals")
print(f"{convert:.2f} watts is equivalent to {watts_to_BTU} BTU per hour")
print(f"{convert:.2f} liters per second is equivalent to {Liters_to_Gallons} US gallons per minute")
print(f"{convert:.2f} degrees Celsius is equivalent to {Celcius_to_Fahrenheit} degrees Fahrenheit")
