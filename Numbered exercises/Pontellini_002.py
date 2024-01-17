#Esercizio: dati i seguenti costi giornaliero di un bagnino: ombrellone 12 euro, lettini 5 euro e sedie a sdraio di 6.50 euro; chiedi in input il numero di giorni ed i servizi che vuole prenotare. Visualizza la spesa complessiva.

d = int (input ("How many days you would stay here? '"))
service = str (input ("What services do you want? We have beach umbrella, beach loungers and deck chairs. You can chose whatever you want."))
x1 = int (input ("How many beach umbrella do you want? '"))
y1 = int (input ("How many beach loungers do you want? '"))
z1 = int (input ("How many deck chairs do you want? '"))

x = float (12)
y = float (5)
z = float (6.50)
cost = (x * x1 + y * y1 + z * z1)*d

print ("The cost is:" ,cost, "euro")