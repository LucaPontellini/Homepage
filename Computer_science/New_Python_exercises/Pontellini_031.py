class NaturalPark:
    def __init__(self, title: str, description: str, instructor: str, enrolled_students: list[Student], quiz: Quiz):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.enrolled_students = enrolled_students
        self.quiz = quiz
    
    def enroll_student(student: Student):
        self.enrolled_students.append(student)

    def add_quiz(quiz: Quiz):
        self.quiz = quiz

class Student:


if __name__ == "__main__":
    # Create a course
    python_course = Course("Python Course", "Introduction to Python", "Prof. Rossi")

    # Create a quiz
    quiz = Quiz("Basic Python Quiz", minimum_score=1)

    # Add questions to the quiz
    question1 = Question("What is Python?", ["A snake", "A programming language", "A game"], 1)
    quiz.questions.append(question1)

    # Set the quiz for the course
    python_course.set_quiz(quiz)

    # Create a student
    student = Student("Mario", "Rossi", "mario.rossi@email.com")

    # Enroll the student in the course
    python_course.enroll_student(student)

    # Create a quiz attempt
    attempt_1 = QuizAttempt(quiz, student)

    # Submit answers
    attempt_1.submit_answers([0])  # Correct answer

    # Print the results
    print(f"Score: {attempt_1.score}")
    print(f"Passed: {attempt_1.passed}")

    # Create a quiz attempt
    attempt_2 = QuizAttempt(quiz, student)

    # Submit answers
    attempt_2.submit_answers([1])  # Correct answer

    # Print the results
    print(f"Score: {attempt_2.score}")
    print(f"Passed: {attempt_2.passed}")