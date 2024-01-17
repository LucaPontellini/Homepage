#Esercizio: dato in input il numero di secondi dire a quanti anni, mesi, giorni, ore, minuti e secondi corrispondono

second_0 = int (input ("Enter the number of seconds: '"))

second_1 = print (f"The seconds correspond to {second_0} s")

second_2 = float (second_0 / 60)
second_3 = float (second_0 / 3600) 
second_4 = float (second_0 / 86400)
second_5 = float (second_0 / 2629800)
second_6 = float (second_0 / 31557600)

print (f"The number of seconds you entered is equal to {second_2} minutes")
print (f"The number of seconds you entered is equal to {second_3} hours")
print (f"The number of seconds you entered is equal to {second_4} days")
print (f"The number of seconds you entered is equal to {second_5} months")
print (f"The number of seconds you entered is equal to {second_6} years")