from typing import NamedTuple, List, Tuple
from collections import Counter

import re

with open("data.txt", "r") as f:
    OBSERVATIONS = f.read().splitlines()

time_rgx = r"\[([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})\]"
guard_rgx = r"(.*) Guard #([0-9]+) begins shift"


class Nap(NamedTuple):
    guard_id: int
    sleep: int
    wake: int


def find_naps(observations: List[str]) -> List[Nap]:
    naps = []
    observations = sorted(observations)

    guard_id = sleep = wake = None

    for observation in observations:
        time = re.match(time_rgx, observation).groups()
        guard = re.match(guard_rgx, observation)

        if guard:
            guard_id = int(guard.groups()[1])
        elif "falls asleep" in observation:
            sleep = int(time[4])
        elif "wakes up" in observation:
            wake = int(time[4])

        if guard_id is not None and sleep is not None and wake is not None:
            naps.append(Nap(guard_id, sleep, wake))
            sleep = wake = None

    return naps


def find_laziest_guard(naps: List[Nap]) -> int:

    laziness = Counter()
    for nap in naps:
        laziness[nap.guard_id] += nap.wake - nap.sleep

    return laziness.most_common(1)[0][0]


def find_guards_laziest_minute(naps: List[Nap], laziest_guard_id: int) -> int:

    lazy_minutes = Counter()
    for nap in naps:
        if nap.guard_id == laziest_guard_id:
            for minute in range(nap.sleep, nap.wake):
                lazy_minutes[minute] += 1

    return lazy_minutes.most_common(1)[0][0]


def find_overall_laziest_minutes(naps: List[Nap]) -> Tuple[int, int]:
    lazy_minutes = Counter()
    for nap in naps:
        for minute in range(nap.sleep, nap.wake):
            lazy_minutes[(nap.guard_id, minute)] += 1

    return lazy_minutes.most_common(1)[0][0]


if __name__ == "__main__":
    naps = find_naps(OBSERVATIONS)

    # Part 1
    laziest_guard = find_laziest_guard(naps)
    print(f"Guard #{laziest_guard} is the laziest guard")
    laziest_guard_minute = find_guards_laziest_minute(naps, laziest_guard)
    print(f"He a sleeps the most on minute {laziest_guard_minute}")
    print(f"Solution {laziest_guard * laziest_guard_minute}")

    # Part 2
    guard, minute = find_overall_laziest_minutes(naps)
    print(f"Guard #{guard} is most frequently asleep on the same minute {minute}")
    print(f"Solution {guard * minute}")
