#Esercizio UML e Codice
#Obiettivo
#Si desidera modellare un sistema di gestione di una palestra.
#Il sistema deve includere diverse entità con i loro attributi e relazioni.

#Istruzioni
#Creare un diagramma UML delle classi utilizzando la sintassi di MermaidJS.
#Consegnare un file markdown con il diagramma UML in un blocco mermaid.
#Implementare il codice Python dell'esercizio utilizzando la programmazione orientata agli oggetti (OOP).
#Descrizione
#In una palestra, ci sono allenatori, membri e corsi.
#Ogni allenatore ha un nome, un cognome e una specializzazione.
#Ogni allenatore può allenare più membri, ma ogni membro ha un solo allenatore.

#I membri hanno un nome, un cognome e una lista di corsi a cui sono iscritti.
#Ogni corso ha un nome e una durata.
#I membri possono iscriversi a più corsi e ogni corso può avere più membri iscritti.

#Ogni corso è tenuto da un solo allenatore, ma un allenatore può tenere più corsi.

#Ogni membro ha una scheda di allenamento.
#La scheda di allenamento contiene una lista di esercizi e la loro descrizione.
#Ogni membro ha una sola scheda di allenamento e ogni scheda di allenamento appartiene a un solo membro.

#Esempio di main.py

#def main():
    # Creazione degli allenatori
    #allenatore1 = Allenatore("Giovanni", "Rossi", "Fitness")
    #allenatore2 = Allenatore("Luca", "Bianchi", "Yoga")

    # Creazione dei membri
    #membro1 = Membro("Anna", "Verdi")
    #membro2 = Membro("Marco", "Neri")

    # Assegnazione degli allenatori ai membri
    #membro1.set_allenatore(allenatore1)
    #membro2.set_allenatore(allenatore2)

    # Creazione dei corsi
    #corso1 = Corso("Pilates", "3 mesi", allenatore1)
    #corso2 = Corso("HIIT", "6 mesi", allenatore1)
    #corso3 = Corso("Yoga Avanzato", "4 mesi", allenatore2)

    # Iscrizione dei membri ai corsi
    #membro1.iscrivi_corso(corso1)
    #membro1.iscrivi_corso(corso2)
    #membro2.iscrivi_corso(corso3)

    # Creazione delle schede di allenamento
    #scheda1 = SchedaAllenamento(membro1, ["Esercizio 1: Squat", "Esercizio 2: Push-up"])
    #scheda2 = SchedaAllenamento(membro2, ["Esercizio 1: Plank", "Esercizio 2: Burpee"])

    # Assegnazione delle schede di allenamento ai membri
    #membro1.set_scheda_allenamento(scheda1)
    #membro2.set_scheda_allenamento(scheda2)

    # Stampa delle informazioni
    #print(membro1)
    #print(membro2)

#if __name__ == "__main__":
#    main()

class Coatch:
    def __init__(self, name, surname, specialization):
        self.name = name
        self.surname = surname
        self.specialization = specialization
    
    def __str__(self):
        return f"Teacher: {self.name} {self.surname}, Specialization: {self.specialization}"

class Members:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []
        self.coach = None
    
    def set_coatch(self, coatch):
        self.coatch = coatch

    def enroll_course(self, course):
        self.courses.append(course)
        course.members.append(self)
    
    def __str__(self):
        course_names = []
        for course in self.courses:
            course_names.append(course.name)

        courses_str = ", ".join(course_names)

        if self.coatch:
            coatch_str = f"{self.coatch.name} {self.coatch.surname}"
        else: coatch_str = "None"
    
        return (f"Member: {self.name} {self.surname}, Coatch: {coatch_str}, Courses: {courses_str}")

class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.coatch = []
    
    def __str__(self):
        coatchs = []
        for coatch in self.coatch:
            coatchs.append(coatch.name)

        coatch_str = ", ".join(coatchs)

        if self.coatch:
            coatch_str = f"{Coatch.name} {Coatch.surname}"
        else: coatch_str = "None"

        return (f"Course: {self.name}, Duration: {self.duration}, Coatch: {coatch_str}")
    
def main():

    trainer1 = Coatch("Giovanni", "Rossi", "Fitness")
    trainer2 = Coatch("Luca", "Bianchi", "Yoga")

    member1 = Members("Anna", "Verdi")
    member2 = Members("Marco", "Neri")

    member1.set_coatch(coatch1)
    member2.set_coatch(coatch2)

    course1 = Course("Pilates", "3 months", coatch1)
    course2 = Course("HIIT", "6 months", coatch1)
    course3 = Course("Advanced Yoga", "4 months", coatch2)

    member1.enroll_course(course1)
    member1.enroll_course(course2)
    member2.enroll_course(course3)

    plan1 = Training_Schedule(member1, ["Exercise 1: Squat", "Exercise 2: Push-up"])
    plan2 = Training_Schedule(member2, ["Exercise 1: Plank", "Exercise 2: Burpee"])

    member1.set_training_schedule(plan1)
    member2.set_training_schedule(plan2)

    print(member1)
    print(member2)

if __name__ == "__main__":
    main()