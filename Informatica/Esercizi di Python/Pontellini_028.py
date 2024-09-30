#Esercizio: scrivi una funzione che passati come parametro la classe ambientale (euro0, euro1,...., euro6), i kW e gli anni passati dall'immatricolazione di un autoveicolo, 
#calcoli il bollo auto e l'eventuale superbollo. Nel caso non sia previsto il superbollo si scelga se restituire 0 oppure None. Utilizzare la funzione in un programma di esempio.

#N.B.
#Crea una funzione specifica per il superbollo da usare nella funzione principale.
#es. def calcola_superbollo (kW: int, immatricolazione: int) -> float: ....

#signature metodo principale: def calcola_bollo (classe_ambientale:int, kW: int, immatricolazione: int) -> list [float] | None: ....
#N.B.
#La funzione può eseguire un controllo sui dati inseriti in ingresso e in caso di dati non validi (es. negativi) restituisce None

#utilizzo: bollo, superbollo = calcola_bollo (.......................................

#Calcolo bollo:
#Euro 0 fino a 100 kW pagano 3 euro a kW e 4,50 euro per ogni kW oltre i 100
#Euro 1 fino a 100 kW pagano 2,9 euro a kW e 4,35 euro per ogni kW oltre i 100
#Euro 2 fino a 100 kW pagano 2,8 euro a kW e 4,20 euro per ogni kW oltre i 100
#Euro 3 fino a 100 kW pagano 2,7 euro a kW e 4,05 euro per ogni kW oltre i 100
#Euro 4 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
#Euro 5 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
#Euro 6 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100

#Calcolo superbollo:
#Auto nuove e fino a 5 anni pagano 20 euro per ogni kW oltre i 185
#Dopo i primi 5 anni pagano 12 euro per ogni kW oltre i 185
#Dopo i 10 anni pagano 6 euro per ogni kW oltre i 185
#Dopo i 15 anni pagano 3 euro per ogni kW oltre i 185
#Dopo i 20 anni non pagano il superbollo

def user_input (environmental_class: int , kw: int , years_since_the_registration_of_a_motor_vehicle: int) -> tuple:

    '''The parameters of the environmental class, the kW and the registration of the vehicle are entered'''

    print ("""
          Euro 0 up to 100 kW pay €3 per kW and €4.50 for each kW over 100
          Euro 1 up to 100 kW pay €2.9 per kW and €4.35 for each kW over 100
          Euro 2 up to 100 kW pay €2.8 per kW and €4.20 for each kW over 100
          Euro 3 up to 100 kW pay €2.7 per kW and €4.05 for each kW over 100
          Euro 4 up to 100 kW pay €2.58 per kW and €3.87 for each kW over 100
          Euro 5 up to 100 kW pay €2.58 per kW and €3.87 for each kW over 100
          Euro 6 up to 100 kW pay €2.58 per kW and €3.87 for each kW over 100""")

    environmental_class = int (input ("Enter the vehicle's environmental class: '"))
    kw = int (input ("Enter the kilowatts of the vehicle: '"))
    years_since_the_registration_of_a_motor_vehicle = int (input ("Enter the years that have passed since the vehicle was registered: '"))

    return environmental_class , kw , years_since_the_registration_of_a_motor_vehicle

def calculation_of_the_stamp_duty (environmental_class: int , kw: int) -> list [float] | None:

    '''Depending on the environmental class, kw and registration of the vehicle you enter, it calculates the vehicle stamp duty'''

    prize = None

    if environmental_class == 0:
        
        if kw >= 0 and kw <= 100:
            prize = 3 * kw
        
        elif kw > 100:
            prize = 3 * 100 + 4.50 * (kw - 100)
        
        else: print ("Error")
        return None

    elif environmental_class == 1:

        if kw >= 0 and kw <= 100:
            prize = 2.9 * kw

        elif kw > 100:
            prize = 2.9 * 100 + 4.35 * (kw - 100)
    
        else: print ("Error")
        return None
    
    elif environmental_class == 2:

        if kw >= 0 and kw <= 100:
            prize = 2.8 * kw

        elif kw > 100:
            prize = 2.8 * 100 + 4.20 * (kw - 100)
    
        else: print ("Error")
        return None
    
    elif environmental_class == 3:

        if kw >= 0 and kw <= 100:
            prize = 2.7 * kw

        elif kw > 100:
            prize = 2.7 * 100 + 4.05 * (kw - 100)
    
        else: print ("Error")
        return None
    
    elif environmental_class == 4 or environmental_class == 5 or environmental_class == 6:
        if kw >= 0 and kw <= 100:

            prize = 2.58 * kw

        elif kw >= 100:

            prize = 2.58 * 100 + 3.87 * (kw - 100)
    
        else: print ("Error")
        return None
    
    else: print ("The environmental class of the vehicle entered does not correspond to the data provided")

def calculation_of_the_supervignette (kw: int, years_since_the_registration_of_a_motor_vehicle: int) -> float:

    '''The kw and the registration of the vehicle are used to calculate the supervignette'''

    print ("""
           New cars and cars up to 5 years old pay 20 euros for each kW over 185
           After the first 5 years they pay 12 euros for each kW over 185
           After 10 years they pay 6 euros for each kW over 185
           After the age of 15 they pay 3 euros for each kW over 185
           After the age of 20 they do not pay the supervignette""")

    if years_since_the_registration_of_a_motor_vehicle <= 5 and kw > 185:

        prize_1 = (kw - 185) * 20

    elif years_since_the_registration_of_a_motor_vehicle > 5 and years_since_the_registration_of_a_motor_vehicle <10 and kw > 185:

        prize_1 = (kw - 185) * 12
    
    elif years_since_the_registration_of_a_motor_vehicle > 10 and years_since_the_registration_of_a_motor_vehicle <20 and kw > 185:

        prize_1 = (kw - 185) * 6
    
    elif years_since_the_registration_of_a_motor_vehicle > 15 and years_since_the_registration_of_a_motor_vehicle <20 and kw > 185:

        prize_1 = (kw - 185) * 3
    
    elif years_since_the_registration_of_a_motor_vehicle > 20:

        prize_1 = 0
    
    else: print ("Error")
    return None

environmental_class, kw, years_since_the_registration_of_a_motor_vehicle = user_input ()
stamp_duty = calculation_of_the_stamp_duty (environmental_class, kw)
supervignette = calculation_of_the_supervignette (kw, years_since_the_registration_of_a_motor_vehicle)

prize = calculation_of_the_stamp_duty (environmental_class, kw)
prize_1 = calculation_of_the_supervignette (kw, years_since_the_registration_of_a_motor_vehicle)

print (f"The stamp duty is: {prize}")
print (f"The supervignette is: {prize_1}")