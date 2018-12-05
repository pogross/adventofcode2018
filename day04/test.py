import unittest

from response_record import find_laziest_guard, find_naps, find_guards_laziest_minute, find_overall_laziest_minutes


class SleepyGuardTest(unittest.TestCase):
    def test(self):
        with open("test_data.txt", "r") as f:
            TEST_DATA = f.read().splitlines()

        naps = find_naps(TEST_DATA)
        laziest_guard = find_laziest_guard(naps)
        self.assertEqual(laziest_guard, 10)
        laziest_minute = find_guards_laziest_minute(naps, laziest_guard)
        self.assertEqual(laziest_minute, 24)
        solution1 = laziest_minute * laziest_guard
        self.assertEqual(solution1, 240)
        self.assertEqual(find_overall_laziest_minutes(naps), (99, 45))


if __name__ == "__main__":
    unittest.main()
