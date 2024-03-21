#Esercizio 4: Chiesto in input all’utente quante ore vuole sostare calcolare e mostrare in output il costo del posteggio. La tariffa è così calcolata:
# 1. 1.50 euro per la prima ora
# 2. 1.00 euro per la seconda, la terza e la quarta ora
# 3. 0.50 per la quinta e la sesta ora
# 4. Per soste superiori alle sei ore si applica una tariffa fissa di 6 euro per l’intera giornata
# 5. Non sono consentite soste superiori alle 24 ore

print ("Welcome to the parking. The cost of the parking is:\n -1.50 euro for the first hour\n -1.00 euro for the second, the third and the fourth hour\n -0.50 euro for the fifth and the sixth hour")
print ("For stops longer than six hours, a fixed rate of 6 euro applies for the whole day. Stops longer than 24 hours are not permitted.")

hour = int (input ("Enter the number of hours you want to stay: '"))

prize_1 = float (hour + 1.50)
prize_2 = float (hour + 1.00)
prize_3 = float (hour + 0.50)
prize_4 = float (hour + (6 * 24))

if hour == 1:
    print (f"You will spend {prize_1} euro")
elif hour >= 1 and hour <= 4:
    print (f"You will spend {prize_2} euro")
elif hour == 5 or hour == 6:
    print (f"You will spend {prize_3} euro")
elif hour > 6 and hour < 24:
    print (f"You will spend {prize_4} euro")
elif hour >= 24:
    print ("Stops longer than 24 hours are not permitted.")
else: print ("Error")