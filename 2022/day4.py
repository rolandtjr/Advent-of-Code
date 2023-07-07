#!/usr/bin/env python3
def part_one(lines):
    pairs = 0
    for line in lines:
        first, second = line.split(',')
        one, two = first.split('-')
        three, four = second.split('-')
        one = int(one)
        two = int(two)
        three = int(three)
        four = int(four)

        first_section_ids = []
        for index in range(one, two+1):
            index_space = str(index) + ' '
            first_section_ids.append(index_space)

        first_ids = ''.join(first_section_ids)

        second_section_ids = []
        for index in range(three, four+1):
            index_space = str(index) + ' '
            second_section_ids.append(index_space)

        second_ids = ''.join(second_section_ids)

        if len(first_ids) == 2 and not (one in range(three, four)):
            continue
        if len(second_ids) == 2 and not (three in range(one, two)):
            continue

        if (first_ids in second_ids) or (second_ids in first_ids):
            pairs += 1

    print(pairs)


def part_two(lines):
    pairs = 0
    for line in lines:
        first, second = line.split(',')
        one, two = first.split('-')
        three, four = second.split('-')
        one = int(one)
        two = int(two)
        three = int(three)
        four = int(four)

        first_section_ids = []
        for index in range(one, two+1):
            index_space = str(index) + ' '
            first_section_ids.append(index_space)

        second_section_ids = []
        for index in range(three, four+1):
            index_space = str(index) + ' '
            second_section_ids.append(index_space)

        for ids in first_section_ids:
            if ids in second_section_ids:
                pairs += 1
                break

    print(pairs)


def main():
    with open('day4', 'r') as file:
        lines = file.readlines()

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
