from typing import Tuple
from collections import Counter

with open("data.txt") as f:
    POLYMER = f.readline()


def polymer_reaction(polymer: str) -> str:
    remaining_units = list(polymer)
    processed_units = []

    # pairwise check the last processed unit with the first remaining unit
    while True:
        # if there are no processed units no reaction can occur
        if len(processed_units) == 0:
            processed_units.append(remaining_units.pop(0))
        else:
            first_unit = processed_units[-1]
            second_unit = remaining_units.pop(0)

            # if of same type and of opposite polarity they cancle each other out
            if is_same_type(first_unit, second_unit) and is_opposite_polarity(first_unit, second_unit):
                processed_units.pop()
            else:
                processed_units.append(second_unit)

            if len(remaining_units) == 0:  # continue if units remain in queue
                break

    return "".join(processed_units)


def is_opposite_polarity(first_unit: str, second_unit: str) -> bool:
    both_lower = first_unit.islower() and second_unit.islower()
    both_upper = first_unit.isupper() and second_unit.isupper()
    if both_lower or both_upper:
        return False
    else:
        return True


def is_same_type(first_unit: str, second_unit: str) -> bool:
    if first_unit.lower() == second_unit.lower():
        return True
    else:
        return False


def best_polymer_modification(polymer: str) -> (str, int):
    unique_units = set(polymer.lower())
    removal_ranking = Counter()

    for unit in unique_units:
        lower_case = unit
        upper_case = unit.upper()

        polymer_candidate = polymer.replace(lower_case, "").replace(upper_case, "")
        processed_polymer = polymer_reaction(polymer_candidate)
        removal_ranking[unit] = len(processed_polymer)

    best_unit = removal_ranking.most_common()[-1][0]
    shortest_polymer_length = removal_ranking.most_common()[-1][1]
    return best_unit, shortest_polymer_length


if __name__ == "__main__":

    # Part 1
    processed_polymer = polymer_reaction(POLYMER)
    print(f"After all reactions the polymer has a length of {len(processed_polymer)}")

    # Part 2
    best_unit, shortest_lenght = best_polymer_modification(POLYMER)
    print(f'Removing "{best_unit}" produces the shortest polymer with a length of {shortest_lenght}')
