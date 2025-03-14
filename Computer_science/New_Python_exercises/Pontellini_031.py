class Course:
    def __init__(self, title: str, description: str, instructor: str, enrolled_students: list, quiz: 'Quiz'):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.enrolled_students = enrolled_students
        self.quiz = quiz
    
    def enroll_student(self, student: 'Student'):
        self.enrolled_students.append(student)

    def add_quiz(self, quiz: 'Quiz'):
        self.quiz = quiz

class Student:
    def __init__(self, name: str, surname: str, email: str, class_: str, year: int, enrolled_courses: list, quiz_attempts: list):
        self.name = name
        self.surname = surname
        self.email = email
        self.class_ = class_
        self.year = year
        self.enrolled_courses = enrolled_courses
        self.quiz_attempts = quiz_attempts

    def enroll_in_course(self, course: Course):
        self.enrolled_courses.append(course)

    def attempt_quiz(self, course: Course):
        quiz = course.quiz
        quiz_attempt = QuizAttempt(quiz, self)
        self.quiz_attempts.append(quiz_attempt)
        return quiz_attempt

class Quiz:
    def __init__(self, questions: list):
        self.questions = questions

    def grade_answers(self, answers: list):
        score = 0
        for i in range(len(answers)):
            if answers[i] == self.questions[i].correct_answer:
                score += 1
        return score

    def check_passing(self, score: int, passing_score: int):
        return score >= passing_score

class Question:
    def __init__(self, text: str, options: list, correct_answer: str):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def is_correct_answer(self, answer: str):
        return answer == self.correct_answer
    
class QuizAttempt:
    def __init__(self, quiz: Quiz, student: Student):
        self.quiz = quiz
        self.student = student
        self.answers = []
        self.score = 0
        self.passed = False

    def submit_answers(self, answers: list):
        self.answers = answers
        self.score = self.quiz.grade_answers(answers)
        self.passed = self.quiz.check_passing(self.score, 1)

if __name__ == "__main__":
    # Create a course
    python_course = Course("Python Course", "Introduction to Python", "Prof. Rossi", [], None)

    # Create a quiz
    quiz = Quiz([])

    # Add questions to the quiz
    question1 = Question("What is Python?", ["A snake", "A programming language", "A game"], "A programming language")
    quiz.questions.append(question1)

    # Set the quiz for the course
    python_course.add_quiz(quiz)

    # Create a student
    student = Student("Mario", "Rossi", "mario.rossi@email.com", "Class A", 2023, [], [])

    # Enroll the student in the course
    python_course.enroll_student(student)

    # Create a quiz attempt
    attempt_1 = QuizAttempt(quiz, student)

    # Submit answers
    attempt_1.submit_answers(["A programming language"])  # Correct answer

    # Print the results
    print(f"Score: {attempt_1.score}")
    print(f"Passed: {attempt_1.passed}")

    # Create a quiz attempt
    attempt_2 = QuizAttempt(quiz, student)

    # Submit answers
    attempt_2.submit_answers(["A snake"])  # Incorrect answer

    # Print the results
    print(f"Score: {attempt_2.score}")
    print(f"Passed: {attempt_2.passed}")