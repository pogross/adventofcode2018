from itertools import cycle


def load_frequency_changes():
    with open("data.txt", "r") as data:
        frequency_changes = [int(line.strip()) for line in data]
    return frequency_changes


def find_frequency_repetition(frequency_changes):
    seen_frequencies = {0}
    while True:
        current_frequency = 0
        frequency_changes_cycle = cycle(frequency_changes)
        for frequency_change in frequency_changes_cycle:
            current_frequency += frequency_change
            if current_frequency in seen_frequencies:
                return current_frequency
            else:
                seen_frequencies.add(current_frequency)


if __name__ == "__main__":

    frequency_changes = load_frequency_changes()

    # Calibrate device for first use
    print(f"First use frequency is : {sum(frequency_changes)}")

    # Identify a first frequency repetition
    print(f"Frequency {find_frequency_repetition(frequency_changes)} is the first repeated frequency.")
