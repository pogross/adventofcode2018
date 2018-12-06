import unittest

from alchemical_reduction import is_opposite_polarity, is_same_type, polymer_reaction, best_polymer_modification


class AlchemicalReductionTest(unittest.TestCase):
    def test(self):

        self.assertEqual(is_opposite_polarity("a", "B"), True)
        self.assertEqual(is_opposite_polarity("a", "a"), False)

        self.assertEqual(is_same_type("a", "A"), True)
        self.assertEqual(is_same_type("a", "B"), False)

        TEST_DATA = "dabAcCaCBAcCcaDA"
        self.assertEqual(polymer_reaction(TEST_DATA), "dabCBAcaDA")
        self.assertEqual(len(polymer_reaction(TEST_DATA)), 10)

        self.assertEqual(best_polymer_modification(TEST_DATA), ("c", 4))


if __name__ == "__main__":
    unittest.main()
