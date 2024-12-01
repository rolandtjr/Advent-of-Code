#!/usr/bin/env python
from collections import Counter


def part_one(left_list: list, right_list: list) -> int:
    left_list.sort()
    right_list.sort()

    diffs = []
    for left, right in zip(left_list, right_list):
        diffs.append(abs(left - right))

    return sum(diffs)


def part_two(left_list: list, right_list: list) -> int:
    right_counter = Counter(right_list)

    similarity_score = 0
    for left in left_list:
        if left in right_counter:
            similarity_score += left * right_counter[left]

    return similarity_score


def main():
    with open("day1") as file:
        lines = file.readlines()

    left_list = []
    right_list = []
    for line in lines:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

    print(part_one(left_list, right_list))
    print(part_two(left_list, right_list))


if __name__ == "__main__":
    main()
