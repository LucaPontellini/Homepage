#Esercizio: scrivi un programma che calcoli il valore della circonferenza e quello dell'area di tutti i cerchi con raggio compreso tra 1 e 20.

radius = int (input ("Enter one number for the radius: '"))

import math
circumference = (radius + radius) * math.pi
area_of_the_circle = (radius ** radius) * math.pi

print (f"The circumference is: {circumference}")
print ("------------------------------------------")

for radius in range (1,21): 
    print (f"The area of the circle is: {area_of_the_circle}")