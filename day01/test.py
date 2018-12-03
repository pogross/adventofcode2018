import unittest
from chronal_calibration import find_frequency_repetition


class ChronalCalibrationTest(unittest.TestCase):
    def test(self):
        self.assertEqual(find_frequency_repetition([1, -1]), 0)
        self.assertEqual(find_frequency_repetition([3, 3, 4, -2, -4]), 10)
        self.assertEqual(find_frequency_repetition([-6, 3, 8, 5, -6]), 5)
        self.assertEqual(find_frequency_repetition([+7, +7, -2, -7, -4]), 14)


if __name__ == "__main__":
    unittest.main()
