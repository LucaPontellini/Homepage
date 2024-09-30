#Esercizio: un cinema sta facendo la seguente promozione: adulto 10 euro e minorenne 6 euro. Il cinema lavora solo con gruppi su prenotazione. Visualizza la spesa complessiva dato il numero di persone nel gruppo.

a = int (input ("Enter the number of adult: '"))
m = int (input ("Enter the number of minor: '"))

a1 = int (10)
m1 = int (6)
cost = a*10 + m*6

print ("The cost is:" ,cost, "euro")