class Course:
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
    def __init__(self, name: str, surname: str, email: str, class_: str, year: int, enrolled_courses: list[Course], quiz_attempts: list[QuizAttempt]):
        self.name = name
        self.surname = surname
        self.email = email
        self.class_ = class_
        self.year = year
        self.enrolled_courses = enrolled_courses
        self.quiz_attempts = quiz_attempts

    def enroll_in_course(course: Course):
        self.enrolled_courses.append(course)

    def attempt_quiz(course: Course):
        quiz = course.quiz
        quiz_attempt = QuizAttempt(quiz, self)
        self.quiz_attempts.append(quiz_attempt)
        return quiz_attempt

class Quiz:
    def __init__(questions: list[Question]):
        self.questions = questions

    def grade_answers(answers: list[str]):
        score = 0
        for i in range(len(answers)):
            if answers[i] == questions[i].correct_answer:
                score += 1
        return score

    def check_passing(score: int, passing_score: int):
        if score >= passing_score:
            return True
        else: return False

class Question:
    def __init__(text: str, options: list[str], correct_answer: str):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def is_correct_answer(answer: str):
        if answer == correct_answer:
            return True
        else: return False
    
class QuizAttempt:
    def __init__(quiz: Quiz, student: Student, answers: list[str], score: int, passed: bool):
        self.quiz = quiz
        self.student = student
        self.answers = answers
        self.score = score
        self.passed = passed

    def submit_answers(answers: list[str]):
        self.answers = answers
        self.score = quiz.grade_answers(answers)
        self.passed = quiz.check_passing(self.score, quiz.passing_score)

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