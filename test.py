import unittest
from main import cel_to_fah

class TestTemperatureConversion(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(cel_to_fah(0), 32)

    def test_boiling(self):
        self.assertEqual(cel_to_fah(100), 212)

    def test_negative(self):
        self.assertEqual(cel_to_fah(-40), -40)


if __name__ == "__main__":
    unittest.main()
