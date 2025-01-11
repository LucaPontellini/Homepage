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

class Coach:
    def __init__(self, name, surname, specialization):
        self.name = name
        self.surname = surname
        self.specialization = specialization
        self.courses = []
        self.members = []
    
    def __str__(self):
        return f"Coach: {self.name} {self.surname}, Specialization: {self.specialization}"

class Members:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []
        self.coach = None
        self.training_schedule = None
    
    def set_coach(self, coach):
        self.coach = coach
        coach.members.append(self)
    
    def enroll_course(self, course):
        self.courses.append(course)
        course.members.append(self)
    
    def set_training_schedule(self, training_schedule):
        self.training_schedule = training_schedule
    
    def __str__(self):
        course_names = []

        for course in self.courses:
            course_names.append(course.name)

        courses_str = ", ".join(course_names)

        if self.coach:
            coach_str = f"{self.coach.name} {self.coach.surname}"
        else: coach_str = "None"

        return f"Member: {self.name} {self.surname}, Coach: {coach_str}, Courses: {courses_str}"

class Course:
    def __init__(self, name, duration, coach):
        self.name = name
        self.duration = duration
        self.coach = coach
        self.members = []
        coach.courses.append(self)
    
    def __str__(self):
        member_names = []
    
        for member in self.members:
            member_names.append(member.name)

        members_str = ", ".join(member_names)

        if self.coach:
            coach_str = f"{self.coach.name} {self.coach.surname}"
        else: coach_str = "None"

        return f"Course: {self.name}, Duration: {self.duration}, Coach: {coach_str}, Members: {members_str}"

class Training_Schedule:
    def __init__(self, member, exercises, descriptions):
        self.member = member
        self.exercises = exercises
        self.descriptions = descriptions
    
    def __str__(self):
        exercises_str = ", ".join(self.exercises)
        descriptions_str = ", ".join(self.descriptions)
        return f"Training Schedule for {self.member.name} {self.member.surname}: Exercises: {exercises_str}, Descriptions: {descriptions_str}"

def main():

    coach1 = Coach("Giovanni", "Rossi", "Fitness")
    coach2 = Coach("Luca", "Bianchi", "Yoga")

    member1 = Members("Anna", "Verdi")
    member2 = Members("Marco", "Neri")

    member1.set_coach(coach1)
    member2.set_coach(coach2)

    course1 = Course("Pilates", 3, coach1)
    course2 = Course("HIIT", 6, coach1)
    course3 = Course("Advanced Yoga", 4, coach2)

    member1.enroll_course(course1)
    member1.enroll_course(course2)
    member2.enroll_course(course3)

    training_schedule1 = Training_Schedule(member1, ["Squat", "Push-up"], ["Exercise 1: Squat", "Exercise 2: Push-up"])
    training_schedule2 = Training_Schedule(member2, ["Plank", "Burpee"], ["Exercise 1: Plank", "Exercise 2: Burpee"])

    member1.set_training_schedule(training_schedule1)
    member2.set_training_schedule(training_schedule2)

    print(member1)
    print(member2)

if __name__ == "__main__":
    main()