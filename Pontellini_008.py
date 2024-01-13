#Esercizio: dato in input un numero n di pasticcini, dire quante scatole da 5 pezzi, da 3 pezzi e da 1 pezzo servono a contenerli. Nota bene: utilizzare il minor numero di scatole possibili, non lasciando nessuna scatola parzialmente vuota.

print ("We have three types of boxes to contain pastries:\n -boxes of 5 pieces;\n -boxes of 3 pieces;\n -boxes of 5 pieces.\n How many pastries do you have to hold?")
pastries = int (input ("Enter the number of pastries: '"))

box_1 = int (pastries // 5)
rest_1 = int (pastries % 5)

box_2 = int (rest_1 / 3)
rest_2 = int (rest_1 % 3)

box_3 = int (rest_2 / 1)
rest_3 = int (rest_2 % 1)

print (f"You need {box_1} boxes to group the pastries if you use the 5-piece box")
print (f"You need {box_2} boxes to group the pastries if you use the 3-piece box")
print (f"You need {box_3} boxes to group the pastries if you use the 1-piece box")