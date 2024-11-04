#Esercizio: Associazioni N-N tra Classi in Python
#Prerequisiti
#Conoscenza delle classi e dell'ereditarietà in Python.
#Comprensione delle associazioni tra classi, in particolare le associazioni molti a molti.
#Familiarità con i metodi getter e setter.
#Obiettivo
#Creare due classi in Python che rappresentano un'associazione molti a molti.
#Utilizzare l'associazione per collegare istanze delle due classi in modo che ogni istanza di una classe possa essere associata a più istanze dell'altra classe e viceversa.

#Istruzioni
#Definisci una classe chiamata Studente con gli attributi di istanza nome e matricola.
#Definisci una classe chiamata Corso con gli attributi di istanza titolo e codice.
#Implementa metodi di istanza in entrambe le classi per accedere e modificare i loro attributi.
#Aggiungi un attributo di istanza in ciascuna classe per mantenere una lista di riferimenti all'altra classe (ad esempio, corsi in Studente e studenti in Corso).
#Implementa metodi in entrambe le classi per collegare le istanze tra loro, assicurando che l'associazione sia molti a molti.
#Crea diverse istanze di Studente e Corso, e associa ciascun Studente a più Corso e viceversa.
#Verifica che le associazioni siano correttamente stabilite in entrambe le direzioni.
#Esempio di Utilizzo
#Creazione delle istanze di Studente
#studente1 = Studente("Alice Rossi", "MAT123")
#studente2 = Studente("Marco Bianchi", "MAT456")

#Creazione delle istanze di Corso
#corso1 = Corso("Programmazione Python", "PY101")
#corso2 = Corso("Database Relazionali", "DB201")
#corso3 = Corso("Sistemi Operativi", "SO301")

# Associazione tra studenti e corsi
#studente1.aggiungi_corso(corso1)
#studente1.aggiungi_corso(corso2)
#studente2.aggiungi_corso(corso2)
#studente2.aggiungi_corso(corso3)

# Verifica delle associazioni
#print(f"{studente1.nome} è iscritto ai seguenti corsi:")
#for corso in studente1.corsi:
#    print(f"- {corso.titolo} ({corso.codice})")

#print(f"\n{corso2.titolo} ha i seguenti studenti iscritti:")
#for studente in corso2.studenti:
#    print(f"- {studente.nome} ({studente.matricola})")

#Output atteso
#Alice Rossi è iscritto ai seguenti corsi:
#- Programmazione Python (PY101)
#- Database Relazionali (DB201)

#Database Relazionali ha i seguenti studenti iscritti:
#- Alice Rossi (MAT123)
#- Marco Bianchi (MAT456)

class Student:
    def __init__(self, name: str, freshman: str):
        self.name = name
        self.freshman = freshman
        self.courses = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name:
            self._name = name
        else:
            self._name = "Unknown name"
    
    @property
    def freshman(self):
        return self._freshman

    @freshman.setter
    def freshman(self, freshman):
        if freshman:
            self._freshman = freshman
        else:
            self._freshman = "Unknown freshman"

    def add_course(self, course):
        self.courses.append(course)
        course.students.append(self)

    def get_courses(self):
        return self.courses


class Course:
    def __init__(self, title: str, code: int):
        self.title = title
        self.code = code
        self.students = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title:
            self._title = title
        else:
            self._title = "Unknown title"
    
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        if code:
            self._code = code
        else:
            self._code = "Unknown code"

    def add_student(self, student):
        self.students.append(student)
        student.courses.append(self)

    def get_students(self):
        return self.students

student1 = Student("Alice Rossi", "MAT123")
student2 = Student("Marco Bianchi", "MAT456")

course1 = Course("Python Programming", "PY101")
course2 = Course("Relational Databases", "DB201")
course3 = Course("Operating Systems", "SO301")

student1.add_course(course1)
student1.add_course(course2)
student2.add_course(course2)
student2.add_course(course3)

print(f"{student1.name} is enrolled in the following courses:")
for course in student1.get_courses():
    print(f"- {course.title} ({course.code})")

print(f"\n{course2.title} has the following enrolled students:")
for student in course2.get_students():
    print(f"- {student.name} ({student.freshman})")

#Alice Rossi is enrolled in the following courses:
#- Python Programming (PY101)
#- Relational Databases (DB201)

#Relational Databases has the following students enrolled:
#- Alice Rossi (MAT123)
#- Marco Bianchi (MAT456)