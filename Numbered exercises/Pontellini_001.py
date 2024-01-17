#Esercizio: dato i seguenti valori inseriti in input: nome di un alunno e 3 voti di una materia, visualizza la media dei voti.

name = input ("Enter your name:")
vote1 = input ("Enter your first vote:")
vote2 = input ("Enter your second vote:")
vote3 = input ("Enter your tird vote:")

name = str (name)
vote1 = float (vote1)
vote2 = float (vote2)
vote3 = float (vote3)

print (f"{name}, your school average is: {(vote1 + vote2 + vote3)/3}")