#Esercizio 3: Chiesta all’utente una data in input nel formato giorno, mese e anno, memorizzate in tre variabili separate, dire in output se la data è valida o meno. Al fine di implementare il programma si ricorda che:
# • Gennaio, marzo, maggio, luglio, agosto, ottobre e dicembre hanno 31 giorni
# • Aprile, giugno, settembre e novembre hanno 30 giorni
# • Febbraio ha 29 giorni se l’anno è bisestile, 28 altrimenti

day = int (input ("Enter the number for the day: '"))
month = int (input ("Enter the number for the month: '"))
year_1 = int (input ("Enter the number for the year: '"))

print (f"Your date is {day}/{month}/{year_1}.")

year_2 = year_1 / 31
year_3 = year_2 % 31
year_4 = year_1 / 30
year_5 = year_4 % 30
year_6 = year_1 / 28
year_7 = year_6 % 28

if year_2 % 31:
    print ("The year is a leap year")
elif year_2 % 4:
    print ("The year is a leap year")
else: print ("The year is not a leap year")