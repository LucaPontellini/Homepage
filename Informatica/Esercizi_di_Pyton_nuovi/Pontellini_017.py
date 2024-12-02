#Esercizio UML e Codice

#Obiettivo

#Si desidera modellare un sistema di gestione di una scuola di musica.
#Il sistema deve includere diverse entità con i loro attributi e relazioni.

#Istruzioni

#Creare un diagramma UML delle classi utilizzando la sintassi di MermaidJS. Consegnare un file markdown con il diagramma UML in un blocco mermaid.
#Implementare il codice Python dell'esercizio utilizzando la programmazione orientata agli oggetti (OOP).
#Descrizione
#In una scuola di musica, ci sono insegnanti e studenti.
#Ogni insegnante ha un nome, un cognome e uno strumento musicale che insegna.
#Ogni insegnante può insegnare a più studenti, ma ogni studente ha un solo insegnante.

#Gli studenti hanno un nome, un cognome e una lista di corsi a cui sono iscritti.
#Ogni corso ha un nome e una durata. Gli studenti possono iscriversi a più corsi e ogni corso può avere più studenti iscritti.

#Esempio di main.py

#def main():
#    #Creazione degli insegnanti
#    insegnante1 = Insegnante("Mario", "Rossi", "Pianoforte")
#    insegnante2 = Insegnante("Luca", "Bianchi", "Chitarra")
#
#    #Creazione degli studenti
#    studente1 = Studente("Anna", "Verdi")
#    studente2 = Studente("Marco", "Neri")
#
#    #Assegnazione degli insegnanti agli studenti
#    studente1.set_insegnante(insegnante1)
#    studente2.set_insegnante(insegnante2)
#
#    #Creazione dei corsi
#    corso1 = Corso("Teoria Musicale", "3 mesi")
#    corso2 = Corso("Tecnica Pianistica", "6 mesi")
#
#    #Iscrizione degli studenti ai corsi
#    studente1.iscrivi_corso(corso1)
#    studente1.iscrivi_corso(corso2)
#    studente2.iscrivi_corso(corso1)
#
#    #Stampa delle informazioni
#    print(studente1)
#    print(studente2)
#
#if __name__ == "__main__":
#    main()
class Teacher:
    def __init__(self, name, surname, instrument):
        self.name = name
        self.surname = surname
        self.instrument = instrument

    def __str__(self):
        return f"Teacher: {self.name} {self.surname}, Instrument: {self.instrument}"
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []
        self.teacher = None

    def set_teacher(self, teacher):
        self.teacher = teacher

    def enroll_course(self, course):
        self.courses.append(course)
        course.students.append(self)

    def __str__(self):
    
        course_names = [course.name for course in self.courses]
        courses_str = ", ".join(course_names)

        if self.teacher:
            teacher_str = f"{self.teacher.name} {self.teacher.surname}"
        else: teacher_str = "None"

        return (f"Student: {self.name} {self.surname}, Teacher: {teacher_str}, Courses: {courses_str}")
class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.students = []

    def __str__(self):
        return f"Course: {self.name}, Duration: {self.duration}"

def main():
    teacher1 = Teacher("Mario", "Rossi", "Piano")
    teacher2 = Teacher("Luca", "Bianchi", "Guitar")

    student1 = Student("Anna", "Verdi")
    student2 = Student("Marco", "Neri")

    student1.set_teacher(teacher1)
    student2.set_teacher(teacher2)

    course1 = Course("Music Theory", "3 months")
    course2 = Course("Piano Technique", "6 months")

    student1.enroll_course(course1)
    student1.enroll_course(course2)
    student2.enroll_course(course1)

    print(student1)
    print(student2)

if __name__ == "__main__":
    main()