import unittest
from src.e18 import Coatch, Member, Course, Training_Schedule
class TestE18(unittest.TestCase):
    def setUp(self):
        self.coach1 = Coatch("Giovanni", "Rossi", "Fitness")
        self.coach2 = Coatch("Luca", "Bianchi", "Yoga")
        self.member1 = Member("Anna", "Verdi")
        self.member2 = Member("Marco", "Neri")
        self.course1 = Course("Pilates", "3 months", self.coach1)
        self.course2 = Course("HIIT", "6 months", self.coach1)
        self.course3 = Course("Advanced Yoga", "4 months", self.coach2)
        self.plan1 = Training_Schedule(
            self.member1, ["Exercise 1: Squat", "Exercise 2: Push-up"]
        )
        self.program2 = Training_Schedule(
            self.member2, ["Exercise 1: Plank", "Exercise 2: Burpee"]
        )

    def test_set_coach(self):
        self.member1.set_coach(self.coach1)
        self.assertEqual(self.member1.coach, self.coach1)
        self.assertIn(self.member1, self.coach1.members)

    def test_enroll_course(self):
        self.member1.enroll_course(self.course1)
        self.assertIn(self.course1, self.member1.courses)
        self.assertIn(self.member1, self.course1.enrolled)

    def test_set_training_program(self):
        self.member1.set_training_schedule(self.plan1)
        self.assertEqual(self.member1.training_schedule, self.plan1)
        self.assertEqual(self.plan1.member, self.member1)

    def test_course_coach_relationship(self):
        self.assertIn(self.course1, self.coach1.courses)
        self.assertEqual(self.course1.coach, self.coach1)

if __name__ == "__main__":
    unittest.main()