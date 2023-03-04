# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import unittest
import test_cases
class TestStringMethod (unittest.TestCase):
    def test_care_speed_low(self):
        self.assertEqual('Low', test_cases.car_speed(30))
    def test_care_speed_normal(self):
        self.assertEqual('Normal', test_cases.car_speed(100))

    def test_care_speed_normal(self):
        self.assertEqual('Invalid', test_cases.car_speed(230))

mysuit = unittest.TestSuite()
mysuit.addTest(TestStringMethod())
#-------------------------------------------------------student score-------
class TestScore (unittest.TestCase):
    def test_care_speed_failed(self):
        self.assertEqual('Failed', test_cases.student_score(30))
    def test_care_speed_Passed(self):
        self.assertEqual('Passed', test_cases.student_score(60))
    def test_care_speed_failed(self):
        self.assertEqual('Good', test_cases.student_score(75))


mysuitscore = unittest.TestSuite()
mysuitscore.addTest(TestStringMethod())
#---------------------------------------------------------------------------

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(mysuit)
    runner.run(mysuitscore)

