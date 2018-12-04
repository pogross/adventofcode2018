import unittest
from inventory_management import checksum, differ_by_one_character


class InventoryManagementCheckusmTest(unittest.TestCase):
    def test(self):
        self.assertEqual(checksum(["abcdef"]), 0 * 0)
        self.assertEqual(checksum(["bababc"]), 1 * 1)
        self.assertEqual(checksum(["abbcde"]), 1 * 0)
        self.assertEqual(checksum(["abcccd"]), 0 * 1)
        self.assertEqual(checksum(["aabcdd"]), 1 * 0)
        self.assertEqual(checksum(["abcdee"]), 1 * 0)
        self.assertEqual(checksum(["ababab"]), 0 * 1)


class InventoryManagementCharacterDifference(unittest.TestCase):
    def test(self):
        self.assertEqual(
            differ_by_one_character(["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]), "fgij"
        )


if __name__ == "__main__":
    unittest.main()
