class Coach:
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
    
    def set_trainer(self, coach):
        self.coach = coach

    def enroll_course(self, course):
        self.courses.append(course)
        course.members.append(self)
    
    def __str__(self):
        course_names = [course.name for course in self.courses]
        courses_str = ", ".join(course_names)
        coach_str = f"{self.coach.name} {self.coach.surname}" if self.coach else "None"
        return f"Member: {self.name} {self.surname}, Coach: {coach_str}, Courses: {courses_str}"

class Course:
    def __init__(self, name, duration, coach=None):
        self.name = name
        self.duration = duration
        self.coach = coach
        self.members = []
    
    def __str__(self):
        coach_str = f"{self.coach.name} {self.coach.surname}" if self.coach else "None"
        return f"Course: {self.name}, Duration: {self.duration}, Coach: {coach_str}"
    
def main():
    trainer1 = Coach("Giovanni", "Rossi", "Fitness")
    trainer2 = Coach("Luca", "Bianchi", "Yoga")

    member1 = Members("Anna", "Verdi")
    member2 = Members("Marco", "Neri")

    member1.set_trainer(trainer1)
    member2.set_trainer(trainer2)

    course1 = Course("Pilates", "3 months", trainer1)
    course2 = Course("HIIT", "6 months", trainer1)
    course3 = Course("Advanced Yoga", "4 months", trainer2)

    member1.enroll_course(course1)
    member1.enroll_course(course2)
    member2.enroll_course(course3)

    print(member1)
    print(member2)
    print(course1)
    print(course2)
    print(course3)

if __name__ == "__main__":
    main()
