from collections import Counter

with open("data.txt", "r") as f:
    BOX_IDS = [line.strip() for line in f]


def checksum(box_ids):
    """
    Finds the chechsum for the boxes which can be computed by
    count of letters occuring twice times
    count of letters ocurring thrice
    """
    twice = 0
    thrice = 0
    for id in box_ids:
        counts = Counter()
        counts.update(letter.strip().lower() for letter in id)
        # twice and thrice occurence is only counted once for an id
        if 2 in counts.values():
            twice += 1
        if 3 in counts.values():
            thrice += 1
    return twice * thrice


def differ_by_one_character(box_ids):
    """
    Finds the id that differs only by one character
    """
    one_removed_counter = Counter()
    for id in box_ids:
        # Generating all ids with one character removed and couting occurence
        # This is faster than comparing all ids with each other
        for i in range(len(id)):
            one_character_removed = tuple(id[:i] + "-" + id[(i + 1) :])
            one_removed_counter[one_character_removed] += 1
    id_letters, count = one_removed_counter.most_common(1)[0]
    return "".join(id_letters).replace("-", "")


if __name__ == "__main__":

    # Part 1
    print(f"Checksum: {checksum(BOX_IDS)}")

    # Part 2
    print(f"Correct box id: {differ_by_one_character(BOX_IDS)}")
