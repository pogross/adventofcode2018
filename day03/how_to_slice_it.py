from typing import List
import re

from collections import Counter

rgx_pattern = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"


class Claim:
    def __init__(self, id: int, margin_left: int, margin_top: int, width, height: int):
        self.id = id
        self.margin_left = margin_left
        self.margin_top = margin_top
        self.width = width
        self.height = height

        # Generate a set of all coordinates that are covered by the claim
        self.coverage = set()

        start_x = self.margin_left + 1
        start_y = self.margin_top + 1

        for x in range(start_x, start_x + self.width):
            for y in range(start_y, start_y + self.height):
                self.coverage.add((x, y))

    @staticmethod
    def read_claims(input_file: str) -> List["Claim"]:
        claims = []
        with open(input_file) as f:
            for line in f:
                curr_claim = Claim(*[int(x) for x in re.match(rgx_pattern, line).groups()])
                claims.append(curr_claim)

        return claims


def count_overlaps(claims: list("Claim")) -> Counter:
    """
    Returns a counter of overlaps for every cell
    """
    overlap_count = Counter()
    for claim in claims:
        overlap_count.update(claim.coverage)
    return overlap_count


def total_overlaps(overlap_count: Counter) -> int:
    """
    Returns the total number of overlaps
    """
    return sum(1 for i in overlap_count.values() if i > 1)


def find_non_overlapping(overlap_count: Counter) -> set:
    """
    Finds all cells that have no overlap and
    returns a set of these cells
    """
    non_overlapping_cells = set()
    for cell, occurences in overlap_count.most_common():
        if occurences == 1:
            non_overlapping_cells.add(cell)

    return non_overlapping_cells


def non_overlapping_claims(claims: list("Claim"), non_overlapping_cells) -> List[int]:
    """
    Returns the ids of all claims that have no
    overlap with other claims
    """
    ids = []
    for claim in claims:
        if claim.coverage.issubset(non_overlapping_cells):
            ids.append(claim.id)

    return ids


if __name__ == "__main__":

    # Part 1
    claims = Claim.read_claims("data.txt")
    cell_overlaps = count_overlaps(claims)
    print(f"{total_overlaps(cell_overlaps)} square inches are covered by two or more claims")

    # Part 2
    non_overlapping_cells = find_non_overlapping(cell_overlaps)
    ids = non_overlapping_claims(claims, non_overlapping_cells)
    print(f"The claims {ids} do not overlap with anything")
