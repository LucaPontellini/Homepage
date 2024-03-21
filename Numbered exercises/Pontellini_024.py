#Esercizio: Gestione di una Azienda:
#Immagina di dover gestire le risorse umane e finanziarie di un'azienda con dipendenti e progetti. Crea un programma che:

#1. Inizializza una lista di dizionari, ognuno rappresentante un dipendente con nome, ruolo e stipendio iniziale.
#2. Stampa la lista di dipendenti.
#3. Aggiungi un nuovo progetto alla tua azienda con un budget iniziale e costo orario per ora di lavoro su di esso.
#4. Assegna a ciascun dipendente un impegno in ore su questo nuovo progetto, sottraendo dal budget del progetto il costo dei dipendenti per le ore svolte e sommando allo stipendio iniziale i compensi accessori per i progetti su cui ha lavorato.
#5. Stampa la lista dei dipendenti con i relativi stipendi totali e le ore lavorate per ciascun progetto.
#6. Stampa le ore lavorate totali e il budget rimanente per ogni progetto.

#Questo esercizio richiede una gestione avanzata delle liste e dei dizionari, tenendo conto sia delle risorse umane che di quelle finanziarie. Buona gestione aziendale!

import os

company = []
projects = []

while True:

    os.system ('cls'if os.name == 'nt' else 'clear')

    print (""" 
    1) Initialize a list of company (name, role, and starting salary)
    2) Print the list of employees
    3) Add a new project to your company
    4) Assign each employee an hour commitment on this new project
    5) Print the list of employees with their total salaries and hours worked for each project
    6) Print the total hours worked and the remaining budget for each project""")

    choice = input ("Choose the option you want: '")

    match choice:

        case '1':
            print ("Initialize a list of company (name, role, and starting salary)")

            answer_1 = str (input ("Do you want to hire a new employee? '"))

            if answer_1 == "Yes":

                number_of_employees = int (input ("How many employees do you want to hire? '"))

                employees = list ()

                for x in range (number_of_employees):

                    name = str (input ("Enter the employee's name: '"))
                    role = str (input ("Enter the employee's role: '"))
                    starting_salary = int (input ("Enter the employee's starting salary: '"))

                    new_employee = {"name": name, "role": role, "starting salary": starting_salary}

                    employees.append (new_employee)
                company.append (employees)

                print (f"You have hired {number_of_employees} an employee at the company.")
            
            elif answer_1 == "No": 
                
                print (f"You haven't hired anyone at the company.")

                while True:

                    answer_2 = str (input ("Are you sure you don't want to hire new employees? '"))

                    if answer_2 == "No":

                        print ("You will be able to hire new employees if you press 1")
                        break

                    elif answer_2 == "Yes":

                        print ("You won't be able to hire new employees")
                        break

                    else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
            
            else: print ("Error: Invalid response. Enter 'Yes' or 'No'")

        case '2':
            print ("Print the list of employees")

            answer_3 = str (input ("Do you want to see the list of people in the company? '"))

            if answer_3 == "Yes":

                if not company:
                    
                    print ("There are no employees in the company.\nIt could be that you didn't hire them or that they weren't registered with the company")
                    print ("Try to watch if it has been recorded.\nIf it's not there, then press 1 to be able to hire some")

                else: 
                    
                    print (f"This is the list of the employees in the company:\n")

                    for employees in company:
                    
                        for employee in employees:

                            print ("-----------------------------------------------")
                            print (f"Name: {employee ['name']}")
                            print (f"Role: {employee ['role']}")
                            print (f"Starting salary: {employee ['starting salary']}")
                            print ("-----------------------------------------------")

            elif answer_3 == "No":

                print ("You won't see the list of employees")

                while True:

                    answer_4 = str (input ("Are you sure you don't want to see the company's employee list? '"))

                    if answer_4 == "No":

                        print ("You will be able to see the list of employees if you press 2")
                        break

                    elif answer_4 == "Yes":

                        print ("You won't be able to see the list of employees")
                        break

                    else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
            
            else: print ("Error: Invalid response. Enter 'Yes' or 'No'")

        case '3':
            print ("Add a new project to your company")

            answer_5 = str (input ("Do you want to create a new project? '"))

            if answer_5 == "Yes":

                number_of_projects = int (input ("How many projects do you want to create? '"))

                for y in range (number_of_projects):

                    name_of_the_project = str (input ("Enter the name of the project: '"))
                    initial_budget = int (input ("Enter the project's initial budget: '"))
                    hourly_cost = int (input ("Enter the hourly cost for the project: '"))

                    new_project = {"name of the project": name_of_the_project, "initial budget": initial_budget, "hourly cost": hourly_cost}

                    projects.append (new_project)
                    company.append (projects)

                    print (f"You have created {number_of_projects} projects")
            
            elif answer_5 == "No":
                
                print ("You won't create the projects")

                while True:

                    answer_6 = str (input ("Are you sure you don't want to create projects? '"))

                    if answer_6 == "No":

                        print ("You will be able to create projects if you press 3")
                        break

                    elif answer_6 == "Yes":

                        print ("You won't be able to create projects")
                        break

                    else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
            
            else: print ("Error: Invalid response. Enter 'Yes' or 'No'")

        case '4':
            print ("Assign each employee an hour commitment on a new project")
#4. Assegna a ciascun dipendente un impegno in ore su questo nuovo progetto, 
#sottraendo dal budget del progetto il costo dei dipendenti 
#per le ore svolte e sommando allo stipendio iniziale i compensi accessori 
#per i progetti su cui ha lavorato.
#5. Stampa la lista dei dipendenti con i relativi stipendi totali 
#e le ore lavorate per ciascun progetto.
#6. Stampa le ore lavorate totali e il budget rimanente per ogni progetto.

            answer_7 = str (input ("Do you want to assign each employee an hour commitment on this new project? '"))

            if answer_7 == "Yes":

                if not company or not projects:

                    print ("To assign each employee a time commitment to projects, you need employees and projects.")
                    print (f"Right now you have {len (company)} employees and {len (projects)} projects.")
                    print ("To hire employees, press 1 and to create projects, press 3")

                else:

                    for employees in company:
                    
                        for employee in employees:

                            employee_info = dict ()

                            hours_worked = int (input ("Enter the number of hours related to the work on the project that the employee has worked on: '"))
                            
                            ancillary_fees = 0
                            
                            answer_8 = str (input ("Employees are compensated separately for the projects they've worked on? '"))
                            
                            if answer_8 == "Yes":
                                
                                for employee_info in company:
                                    
                                    for employee in employees:
                                
                                        ancillary_fees = int (input ("Enter ancillary fees: '"))

                                        employee_info ["name of the employee"] = name
                                        employee_info ["role of the employee"] = role
                                        employee_info ["starting salary of the employee"] = starting_salary
                                        employee_info ["hours worked"] = hours_worked

                                        total_cost = hours_worked * hourly_cost * number_of_employees
                                        updated_budget = initial_budget - total_cost
                                        updated_salary = starting_salary + ancillary_fees

                                        employee_info.update ({"starting salary of the employee" : updated_salary})

                                        #da finire
                                        #tova un modo per sostituire il salario del dipendente con quello aggiornato e trova un modo per assegnare 
                                        #a tutti i dipendenti un impiego in ore e metterlo nel employee_info

                                        company.append (employee_info)
                            
                            elif answer_8 == "No":
                                
                                for employee_info in company:
                                    
                                    for employee in employees:
                                
                                        employee_info ["name of the employee"] = name
                                        employee_info ["role of the employee"] = role
                                        employee_info ["starting salary of the employee"] = starting_salary
                                        employee_info ["hours worked"] = hours_worked

                                        total_cost = hours_worked * hourly_cost * number_of_employees
                                        updated_budget = initial_budget - total_cost
                                        updated_salary = starting_salary

                                        employee_info.update ({"starting salary of the employee" : updated_salary})

                                        company.append (employee_info)

                                        #print ("-----------------------------------------------")
                                        #print (f"Name: {employee_info ['name of the employee']}") #da errore qui
                                        #print (f"Role: {employee_info ['role of the employee']}")
                                        #print (f"Updated salary: {employee_info ['updated salary of the employee']}")
                                        #print (f"Hours worked: {employee_info ['hours worked']}")
                                        #print ("-----------------------------------------------")
                            
                            else: print ("Error: Invalid response. Enter 'Yes' or 'No'")

        case '5':
            print ("Print the list of employees with their total salaries and hours worked for each project")
            
            #print ("-----------------------------------------------")
            #print (f"Name: {employee_info ['name of the employee']}")
            #print (f"Role: {employee_info ['role of the employee']}")
            #print (f"Updated salary: {employee_info ['updated salary of the employee']}")
            #print (f"Hours worked: {employee_info ['hours worked']}")
            #print ("-----------------------------------------------")
        
        case '6':
            print ("Print the total hours worked and the remaining budget for each project")

        case _: print("Invalid choice.")
    input("Press enter to continue...")