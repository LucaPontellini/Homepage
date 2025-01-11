import unittest
from Pontellini_018 import Coach, Members, Course, Training_Schedule

class TestE18(unittest.TestCase):
    def setUp(self):
        self.coach1 = Coach("Giovanni", "Rossi", "Fitness")
        self.coach2 = Coach("Luca", "Bianchi", "Yoga")
        self.member1 = Members("Anna", "Verdi")
        self.member2 = Members("Marco", "Neri")
        self.course1 = Course("Pilates", 3, self.coach1)
        self.course2 = Course("HIIT", 6, self.coach1)
        self.course3 = Course("Advanced Yoga", 4, self.coach2)
        self.training_schedule1 = Training_Schedule(
            self.member1, ["Squat", "Push-up"], ["Exercise 1: Squat", "Exercise 2: Push-up"]
        )
        self.training_schedule2 = Training_Schedule(
            self.member2, ["Plank", "Burpee"], ["Exercise 1: Plank", "Exercise 2: Burpee"]
        )

    def test_set_coach(self):
        self.member1.set_coach(self.coach1)
        self.assertEqual(self.member1.coach, self.coach1)
        self.assertIn(self.member1, self.coach1.members)

    def test_enroll_course(self):
        self.member1.enroll_course(self.course1)
        self.assertIn(self.course1, self.member1.courses)
        self.assertIn(self.member1, self.course1.members)

    def test_set_training_schedule(self):
        self.member1.set_training_schedule(self.training_schedule1)
        self.assertEqual(self.member1.training_schedule, self.training_schedule1)
        self.assertEqual(self.training_schedule1.member, self.member1)

    def test_course_coach_relationship(self):
        self.assertIn(self.course1, self.coach1.courses)
        self.assertEqual(self.course1.coach, self.coach1)

if __name__ == "__main__":
    unittest.main()