import unittest
from how_to_slice_it import Claim, count_overlaps, non_overlapping_claims, total_overlaps, find_non_overlapping


class ClaimCoverageTest(unittest.TestCase):
    def test(self):

        claim1 = Claim(1, 1, 3, 4, 4)
        claim2 = Claim(2, 3, 1, 4, 4)
        claim3 = Claim(3, 5, 5, 2, 2)
        claims = [claim1, claim2, claim3]

        cell_overlaps = count_overlaps(claims)
        self.assertEqual(total_overlaps(cell_overlaps), 4)

        non_overlapping_cells = find_non_overlapping(cell_overlaps)
        self.assertEqual(len(non_overlapping_claims(claims, non_overlapping_cells)), 1)
        self.assertEqual(non_overlapping_claims(claims, non_overlapping_cells)[0], 3)


if __name__ == "__main__":
    unittest.main()
