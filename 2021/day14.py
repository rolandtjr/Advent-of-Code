#!/usr/bin/env python3

from collections import Counter

def get_final_element_count(pair_count, pair_insertion, final_element_count, iterations):
    for _ in range(iterations):
        temp_pair_count = Counter()
        for key, value in pair_count.items():
            if value:
                temp_pair_count[f"{key[0]}{pair_insertion[key]}"] += value
                temp_pair_count[f"{pair_insertion[key]}{key[1]}"] += value
                final_element_count[pair_insertion[key]] += value
        pair_count = temp_pair_count


def build_dicts(polymer_template):
    final_element_count = Counter()
    pair_count = Counter()

    for polymer in polymer_template:
        final_element_count[polymer] += 1

    for index in range(len(polymer_template) - 1):
        p_t = f'{polymer_template[index]}{polymer_template[index+1]}'
        pair_count[p_t] += 1

    return pair_count, final_element_count


def get_pair_insertion(lines):
    pair_insertion = {}
    for line in lines[2:]:
        line = line.strip().split()
        pair_insertion[line[0]] = line[2]
    return pair_insertion


def print_difference(final_element_count):
    maxi = max(list(final_element_count.values()))
    mini = min(list(final_element_count.values()))
    print(maxi - mini)


def main():
    with open('day14', 'r') as file:
        lines = file.readlines()

    polymer_template = list(lines[0].strip())
    pair_insertion = get_pair_insertion(lines)

    # Part1
    pair_count, final_element_count = build_dicts(polymer_template)
    get_final_element_count(pair_count, pair_insertion, final_element_count, 10)
    print_difference(final_element_count)

    # Part2
    pair_count, final_element_count = build_dicts(polymer_template)
    get_final_element_count(pair_count, pair_insertion, final_element_count, 40)
    print_difference(final_element_count)


if __name__ == '__main__':
    main()
