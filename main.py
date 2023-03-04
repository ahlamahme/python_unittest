# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import unittest
import test_cases
class TestSpeed (unittest.TestCase):
    def test_care_speed_low(self):
        self.assertEqual('Low', test_cases.car_speed(30))
        self.assertEqual('Low', test_cases.car_speed(3))

    def test_care_speed_normal(self):
        self.assertEqual('Normal', test_cases.car_speed(100))
        self.assertEqual('Normal', test_cases.car_speed(99))

    def test_care_speed_invalid(self):
        self.assertEqual('Invalid', test_cases.car_speed(230))
        self.assertEqual('Invalid', test_cases.car_speed(250))
    def test_care_speed_v_high(self):
        self.assertEqual('V.High', test_cases.car_speed(210))
        self.assertEqual('V.High', test_cases.car_speed(215))
    def test_care_speed_high(self):
        self.assertEqual('High', test_cases.car_speed(150))
        self.assertEqual('High', test_cases.car_speed(160))


mysuit = unittest.TestSuite()
mysuit.addTest(TestSpeed())
#-------------------------------------------------------student score-------
class TestScore (unittest.TestCase):
    def test_care_speed_failed(self):
        self.assertEqual('Failed', test_cases.student_score(30))
    def test_care_speed_Passed(self):
        self.assertEqual('Passed', test_cases.student_score(60))
    def test_care_speed_good(self):
        self.assertEqual('Good', test_cases.student_score(75))
        self.assertEqual('Good', test_cases.student_score(80))
    def test_care_speed_Excellent(self):
        self.assertEqual('Excellent', test_cases.student_score(99))
        self.assertEqual('Excellent', test_cases.student_score(86))


mysuitscore = unittest.TestSuite()
mysuitscore.addTest(TestScore())
#---------------------------------------------------------------------------

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(mysuit)
    runner.run(mysuitscore)

