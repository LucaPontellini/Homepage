from Pontellini_017 import Teacher, Student, Course  # type: ignore

def test_teacher_attributes():
    teacher = Teacher("Mario", "Rossi", "Piano")
    assert teacher.name == "Mario"
    assert teacher.surname == "Rossi"
    assert teacher.instrument == "Piano"
    assert teacher.students == []

def test_student_attributes():
    student = Student("Anna", "Verdi")
    assert student.name == "Anna"
    assert student.surname == "Verdi"
    assert student.courses == []
    assert student.teacher is None

def test_course_attributes():
    course = Course("Music Theory", "3 months")
    assert course.name == "Music Theory"
    assert course.duration == "3 months"
    assert course.students == []

def test_assign_teacher_to_student():
    teacher = Teacher("Mario", "Rossi", "Piano")
    student = Student("Anna", "Verdi")

    student.set_teacher(teacher)

    assert student.teacher == teacher
    assert student in teacher.students

def test_enroll_student_in_course():
    student = Student("Anna", "Verdi")
    course = Course("Music Theory", "3 months")

    student.enroll_in_course(course)

    assert course in student.courses
    assert student in course.students

def test_multiple_associations():
    teacher1 = Teacher("Mario", "Rossi", "Piano")
    teacher2 = Teacher("Luca", "Bianchi", "Guitar")
    student1 = Student("Anna", "Verdi")
    student2 = Student("Marco", "Neri")
    course1 = Course("Music Theory", "3 months")
    course2 = Course("Piano Technique", "6 months")

    student1.set_teacher(teacher1)
    student2.set_teacher(teacher2)
    student1.enroll_in_course(course1)
    student1.enroll_in_course(course2)
    student2.enroll_in_course(course1)

    # Verify associations for student1
    assert course1 in student1.courses
    assert course2 in student1.courses
    assert student1 in course1.students
    assert student1 in course2.students

    # Verify associations for student2
    assert course1 in student2.courses
    assert student2 in course1.students

    # Verify teachers
    assert student1.teacher == teacher1
    assert student2.teacher == teacher2
    assert student1 in teacher1.students
    assert student2 in teacher2.students

def test_no_duplicate_association():
    student = Student("Anna", "Verdi")
    course = Course("Music Theory", "3 months")

    student.enroll_in_course(course)
    student.enroll_in_course(course)  # Attempt to add the same course again

    assert len(student.courses) == 1
    assert len(course.students) == 1

def test_print_associations(capfd):
    teacher1 = Teacher("Mario", "Rossi", "Piano")
    student1 = Student("Anna", "Verdi")
    student2 = Student("Marco", "Neri")
    course1 = Course("Music Theory", "3 months")
    course2 = Course("Piano Technique", "6 months")

    student1.set_teacher(teacher1)
    student1.enroll_in_course(course1)
    student1.enroll_in_course(course2)
    student2.enroll_in_course(course1)

    # Function to print associations
    print(f"{student1.name} {student1.surname} is enrolled in the following courses:")
    for course in student1.courses:
        print(f"- {course.name} ({course.duration})")

    print(f"\n{course1.name} has the following enrolled students:")
    for student in course1.students:
        print(f"- {student.name} {student.surname}")

    captured = capfd.readouterr()

    assert "Anna Verdi is enrolled in the following courses:" in captured.out
    assert "- Music Theory (3 months)" in captured.out
    assert "- Piano Technique (6 months)" in captured.out
    assert "Music Theory has the following enrolled students:" in captured.out
    assert "- Anna Verdi" in captured.out
    assert "- Marco Neri" in captured.out