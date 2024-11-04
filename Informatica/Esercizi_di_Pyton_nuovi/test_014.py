import pytest
from student_course import Student, Course  # Ensure the path is correct

def test_student_attributes():
    student = Student("Alice Rossi", "MAT123")
    assert student.name == "Alice Rossi"
    assert student.registration_number == "MAT123"
    assert student.courses == []

def test_course_attributes():
    course = Course("Python Programming", "PY101")
    assert course.title == "Python Programming"
    assert course.code == "PY101"
    assert course.students == []

def test_add_course_to_student():
    student = Student("Alice Rossi", "MAT123")
    course = Course("Python Programming", "PY101")

    student.add_course(course)

    assert course in student.courses
    assert student in course.students

def test_add_student_to_course():
    student = Student("Marco Bianchi", "MAT456")
    course = Course("Relational Databases", "DB201")

    course.add_student(student)

    assert student in course.students
    assert course in student.courses

def test_multiple_associations():
    student1 = Student("Alice Rossi", "MAT123")
    student2 = Student("Marco Bianchi", "MAT456")
    course1 = Course("Python Programming", "PY101")
    course2 = Course("Relational Databases", "DB201")
    course3 = Course("Operating Systems", "SO301")

    student1.add_course(course1)
    student1.add_course(course2)
    student2.add_course(course2)
    student2.add_course(course3)

    # Verify associations for student1
    assert course1 in student1.courses
    assert course2 in student1.courses
    assert student1 in course1.students
    assert student1 in course2.students

    # Verify associations for student2
    assert course2 in student2.courses
    assert course3 in student2.courses
    assert student2 in course2.students
    assert student2 in course3.students

def test_no_duplicate_association():
    student = Student("Alice Rossi", "MAT123")
    course = Course("Python Programming", "PY101")

    student.add_course(course)
    student.add_course(course)  # Attempt to add the same course again

    assert len(student.courses) == 1
    assert len(course.students) == 1

def test_print_associations(capfd):
    student1 = Student("Alice Rossi", "MAT123")
    student2 = Student("Marco Bianchi", "MAT456")
    course1 = Course("Python Programming", "PY101")
    course2 = Course("Relational Databases", "DB201")

    student1.add_course(course1)
    student1.add_course(course2)
    student2.add_course(course2)

    # Function to print associations
    print(f"{student1.name} is enrolled in the following courses:")
    for course in student1.courses:
        print(f"- {course.title} ({course.code})")

    print(f"\n{course2.title} has the following enrolled students:")
    for student in course2.students:
        print(f"- {student.name} ({student.registration_number})")

    captured = capfd.readouterr()

    assert "Alice Rossi is enrolled in the following courses:" in captured.out
    assert "- Python Programming (PY101)" in captured.out
    assert "- Relational Databases (DB201)" in captured.out
    assert "Relational Databases has the following enrolled students:" in captured.out