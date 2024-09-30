#Esercizio: Progettare un applicativo che permetta di gestire il parco auto di una azienda di noleggio.
#Si consiglia di creare un dizionario al fine di modellare le caratteristiche/attributi di ogni singola auto
#(marca, modello, cilindrata, potenza_kw, anno_immatricolazione, costo_gestione, giorni_affitto, prezzo_giornaliero). Il parco auto sarà quindi memorizzato in una lista.
#L'applicativo dovrà permettere:
#1)aggiunta/rimozione di un veicolo
#2)Calcolo del bollo 
#3)Profitto del veicolo[giorno_affitto*(prezzo_giornaliero-IVA)- costo_gestione-bollo]
#4)Profitto (prima delle tasse) di tutto il parco auto

#Per il calcolo del bollo si consideri:
#2,58 euro a kW fino a 100kW
#3,87 euro per i kW eccedenti
#aggiungere 
#20 a kW oltre i 185kW

import os

rental_company = []

while True:
    os.system ("cls" if os.name == "nt" else "clear")

    print (
        """ 
    1) Adding/Removing a Vehicle
    2) Calculation of the vignette
    3) Vehicle profit
    4) Profit (before taxes) of the entire car fleet""")

    choice = input ("Choose the option you want: '")

    match choice:

        case "1":
            print ("Adding/Removing a Vehicle")

            answer_1 = str (input ("Do you want to add/remove a vehicle? '"))

            if answer_1 == "Yes":

                answer_2 = str (input ("Do you want to add a vehicle to your fleet? '"))

                if answer_2 == "Yes":

                    vehicles = list ()

                    number_of_vehicles = int (input ("Enter the number of vehicles you want to put in your fleet: '"))

                    for x in range (number_of_vehicles):

                        name = str (input ("Enter the name of the vehicle: '"))
                        model = str (input ("Enter your vehicle model: '"))
                        brand = str (input ("Enter the brand of the vehicle: '"))
                        power_kw = int (input ("Enter the power of the vehicle: "))

                        vehicle = {"name" : name , "model" : model , "brand" : brand , "power" : power_kw}

                        vehicles.append (vehicle)
                    rental_company.append (vehicles)

                    print (f"You put {len (vehicles)} cars in the fleet")

                    for vehicles in rental_company:
                    
                        for vehicle in vehicles:

                            print ("-----------------------------------------------")
                            print (f"Name: {vehicle ['name']}")
                            print (f"Model: {vehicle ['model']}")
                            print (f"Brand: {vehicle ['brand']}")
                            print (f"Power: {vehicle ['power']}")
                            print ("-----------------------------------------------")
                
                elif answer_2 == "No":

                    answer_3 = str (input ("Do you want to remove a vehicle out of your fleet? '"))

                    if answer_3 == "Yes":

                        while True:
                            
                            print ("Which vehicle do you want to remove?")

                            name_1 = str (input ("Enter the name of the vehicle: '"))
                            model_1 = str (input ("Enter your vehicle model: '"))
                            brand_1 = str (input ("Enter the brand of the vehicle: '"))
                            power_kw_1 = int (input ("Enter the power of the vehicle: "))

                            if not rental_company or not vehicles:

                                print ("There are no vehicles in the fleet")
                                print ("To remove vehicles from the fleet, there must be vehicles")

                            else:

                                for i in range (len (vehicles)):

                                    vehicle = vehicles [i]
                                    if vehicle ['name'] == name_1 and vehicle ['model'] == model_1 and vehicle ['brand'] == brand_1 and vehicle ['power'] == power_kw_1:

                                        del vehicles [i]

                                        print ("The vehicle you selected has been removed")
                                        break

                                    else: print ("The vehicle is not present in the fleet or does not exist")
                            
                            answer_5 = str (input ("Do you want to do anything else? '"))

                            if answer_5 == "Yes":
                                break
                            
                            else: print ("You will exit from the following site")

                    elif answer_3 == "No":

                        answer_4 = str (input ("Do you want to do anything else? '"))

                        if answer_4 == "Yes": 
                            break
                            
                        else: print ("You will exit from the following site")

                    else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
                
                else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
            
            elif answer_1 == "No":
            
                print ("You won't be able to add/remove a vehicle")

                while True:

                    answer_6 = str (input ("Are you sure you don't want to add/remove a vehicle? '"))

                    if answer_6 == "No":

                        print ("You will be able to add/remove a vehicle if you press 1")
                        break

                    elif answer_6 == "Yes":

                        print ("You won't be able to add/remove a vehicle")
                        break

                    else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
            
            else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
        
        case '2':
            print ("Calculation of the vignette")

            answer_8 = str (input ("Do you want to calculate the vignette? '"))

            if answer_8 == "Yes":

                for vehicles in rental_company:

                    for vehicle in vehicles:

                        power_kw = vehicle ['power']

                        if power_kw <= 100:
                        
                            stamp_duty_cost = 2.58 * power_kw

                        elif 100 < power_kw < 185:
                        
                            stamp_duty_cost = 2.58 * 100 + 3.87 * (power_kw - 100)

                        elif power_kw > 185:
                        
                            stamp_duty_cost = 2.58 * 100 + 3.87 * 85 + 20 * (power_kw - 185)
                            vehicle ['stamp'] = stamp_duty_cost

                        else: print ("Error")
                        continue

                    print ("-----------------------------------------------")
                    print (f"Name: {vehicle ['name']}")
                    print (f"Model: {vehicle ['model']}")
                    print (f"Brand: {vehicle ['brand']}")
                    print (f"Power: {vehicle ['power']}")
                    print (f"Stamp duty cost: {stamp_duty_cost}")
                    print ("-----------------------------------------------")
            
            elif answer_8 == "No":

                print ("You won't be able to calculate the vignette")

                while True:

                    answer_9 = str (input ("Are you sure you don't want to calculate the vignette? '"))

                    if answer_9 == "No":

                        print ("You will be able to calculate the vignette if you press 2")
                        break

                    elif answer_9 == "Yes":

                        print ("You won't be able to calculate the vignette")
                        break

                    else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
            
            else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
        
        case '3':
            print ("Vehicle profit")

            answer_10 = str (input ("Do you want to see the profit of the vehicle? '"))

            if answer_10 == "Yes":

                for vehicles in rental_company:

                    for vehicle in vehicles:
                        
                        rental_day = int (input ("Enter the number of days the vehicle was rented: '"))
                        daily_price = float (input ("Enter the daily price of the vehicle: '"))
                        iva = float (input ("Enter VAT: '"))
                        
                        profit = rental_day * (daily_price - iva) - stamp_duty_cost
                        vehicle ['profit'] = profit

                        print ("-----------------------------------------------")
                        print (f"Name: {vehicle ['name']}")
                        print (f"Model: {vehicle ['model']}")
                        print (f"Brand: {vehicle ['brand']}")
                        print (f"Power: {vehicle ['power']}")
                        print (f"Stamp duty cost: {stamp_duty_cost}")
                        print (f"Profit: {profit}")
                        print ("-----------------------------------------------")
            
            elif answer_10 == "No":

                while True:

                    answer_11 = str (input ("Are you sure you don't want to see the vehicle's profit? '"))

                    if answer_11 == "No":

                        print ("You will be able to see the vehicle's profit if you press 3")
                        break

                    elif answer_11 == "Yes":

                        print ("You won't be able to see the vehicle's profit")
                        break

                    else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
            
            else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
        
        case '4':
            print ("Profit (before taxes) of the entire car fleet")

            answer_12 = str (input ("Do you want to see the profit (before taxes) of the entire car fleet? '"))

            if answer_12 == "Yes":

                total_profit = 0

                for vehicles in rental_company:
                    for vehicle in vehicles:

                        total_profit += vehicle ['profit']
            
            elif answer_12 == "No":

                while True:

                    answer_13 = str (input ("Are you sure you don't want to see your car fleet profit (before taxes)? '"))

                    if answer_13 == "No":

                        print ("You will be able to see the profit of the car fleet (before taxes)")
                        break

                    elif answer_13 == "Yes":

                        print ("You won't be able to see the profit of the car fleet (before taxes)")
                        break

                    else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
            
            else: print ("Error: Invalid response. Enter 'Yes' or 'No'")

        case _:
            print("Invalid choice.")
    input("Press enter to continue...")