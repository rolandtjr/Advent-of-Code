#!/usr/bin/env python
import re


def do_last(index, lines):
    pattern = r"\d+"
    symbol_pattern = r"[^\d.\n]"
    matches = [
        (match.start(), match.end()) for match in re.finditer(pattern, lines[index])
    ]
    numbers = re.findall(pattern, lines[index])

    symbol_indexes = set()
    for row in range(index-1, index+1):
        for match in re.finditer(symbol_pattern, lines[row]):
            symbol_indexes.add(match.start())

    result = []
    for index, match in enumerate(matches):
        is_symbol_adjacent = False
        for number_index in range(match[0]-1, match[1]+1):
            if number_index in symbol_indexes:
                is_symbol_adjacent = True
        if is_symbol_adjacent:
            result.append(int(numbers[index]))
    return sum(result)


def do_first(index, lines):
    pattern = r"\d+"
    symbol_pattern = r"[^\d.\n]"
    matches = [
        (match.start(), match.end()) for match in re.finditer(pattern, lines[index])
    ]
    numbers = re.findall(pattern, lines[index])

    symbol_indexes = set()
    for row in range(index, index+2):
        for match in re.finditer(symbol_pattern, lines[row]):
            symbol_indexes.add(match.start())

    result = []
    for index, match in enumerate(matches):
        is_symbol_adjacent = False
        for number_index in range(match[0]-1, match[1]+1):
            if number_index in symbol_indexes:
                is_symbol_adjacent = True
        if is_symbol_adjacent:
            result.append(int(numbers[index]))
    return sum(result)


def find_adjacent(index, lines):
    pattern = r"\d+"
    symbol_pattern = r"[^\d.\n]"
    matches = [
        (match.start(), match.end()) for match in re.finditer(pattern, lines[index])
    ]
    numbers = re.findall(pattern, lines[index])

    symbol_indexes = set()
    for row in range(index-1, index+2):
        for match in re.finditer(symbol_pattern, lines[row]):
            symbol_indexes.add(match.start())

    result = []
    for index, match in enumerate(matches):
        is_symbol_adjacent = False
        for number_index in range(match[0]-1, match[1]+1):
            if number_index in symbol_indexes:
                is_symbol_adjacent = True
        if is_symbol_adjacent:
            result.append(int(numbers[index]))

    return sum(result)


def main():
    with open("day3", "r") as file:
        lines = file.readlines()

    total_adjacent = 0
    for index in range(len(lines)):
        if index == 0:
            total_adjacent += do_first(index, lines)
        elif index == len(lines) - 1:
            total_adjacent += do_last(index, lines)
        else:
            total_adjacent += find_adjacent(index, lines)
    print(total_adjacent)


if __name__ == "__main__":
    main()
