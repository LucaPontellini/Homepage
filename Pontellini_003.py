#Esercizio: chiedi in input il raggio. Visualizza la circonferenza e l'area del cerchio.

num1 = input ("Enter one number for the radius:")
num1 = float (num1)

import math

print (f"The circumference is: {(float (2 * num1 * math.pi))}")
print (f"The area is: {(float ((num1 ** 2) * math.pi))}")