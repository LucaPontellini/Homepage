#Esercizio 2
#Manipolazione di un dizionario (gestione di un registro voti)
#1. Crea un dizionario vuoto per rappresentare un registro voti delgi studenti (es. registro_voti)
#2. Aggiungi alcuni studenti e i loro voti (in centesimi) al registro (Il nome dello studente è la chiave e il voto è il valore)
#3. Stampa il registro voti scorrendo il dizionario con un for (usa il metodo registro_voti.items ())
#4. Aggiungi un nuovo studente e il suo voto
#5. Stampa il registro voti aggiornato come nel punto 3
#6. Verifica se uno studente è nel registro e stampa il suo voto. Chiedere il nome all'utente con un input

import os

school = []
register = {}

print("1. Create a Blank Dictionary to Represent a Student Grade Book\n"
      "2. Add some students and their grades (in hundredths) to the roster (The student's name is the key and the grade is the value)\n"
      "3. Print the Grade Book\n"
      "4. Add a new student and their grade\n"
      "5. Print the updated grade book\n"
      "6. Check if a student is on the roster and print out their grade")

choice = str(input("Choose the one you want:"))

match choice:
    
    case '1':
      print("Create a Blank Dictionary to Represent a Student Grade Book")

      register = dict()
      school.append(register)
    
    case '2':
      print("Add some students and their grades (in hundredths) to the roster (The student's name is the key and the grade is the value)")

      number_of_students = int(input("Enter the number of student in your register: '"))
      
      for x in range (number_of_students):
        
        name = str(input("Enter the name of the student: '"))
        vote = int(input("Enter the vote of the student: '"))

        register["name"] = name
        register["vote"] = vote

        register.update()
    
    case '3':
      print("Print the Grade Book")
      
      for x, y in register.items():
        print(x, y)
    
    case '4':
      print("Add a new student and their grade")
      
      new_student_name = str(input("Enter the name of the student: '"))
      new_student_vote = str(input("Enter the vote of the student: '"))
      register["name"] = new_student_name
      register["vote"] = new_student_vote
      
      register.update()
    
    case '5':
      print("Print the updated grade book")
      
      for x, y in register.items():
        print(x, y)
    
    case '6':
      print("Check if a student is on the roster and print out their grade")
      
      answer_ = str(input("enter the name of the student: '"))
      
      if answer_ in register:
        vote_ = register.values()
        print(vote_)
    
    case _:
     input("Press enter to continue")