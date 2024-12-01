#!/usr/bin/env python

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_first_and_last(line):
    for letter in line:
        if letter.isdigit():
            first = letter
            break
    for letter in line[::-1]:
        if letter.isdigit():
            last = letter
            break
    return first, last


def find_first(line):
    first_position = len(line) + 1
    result = "0"
    for number in numbers:
        index = line.find(number)
        if index >= 0 and index < first_position:
            first_position = index
            result = numbers[number]
    for number in "123456789":
        index = line.find(number)
        if index >= 0 and index < first_position:
            first_position = index
            result = number
    return result


def find_last(line):
    last_position = -1
    result = "0"
    for number in numbers:
        index = line.rfind(number)
        if index >= 0 and index > last_position:
            last_position = index
            result = numbers[number]
    for number in "123456789":
        index = line.rfind(number)
        if index >= 0 and index > last_position:
            last_position = index
            result = number
    return result


def main():
    with open("day1", "r") as file:
        lines = file.readlines()
    total = 0
    for line in lines:
        first, last = get_first_and_last(line)
        total += int(first + last)

    print(total)

    new_total = 0
    for line in lines:
        first, last = find_first(line), find_last(line)
        new_total += int(first + last)

    print(new_total)


if __name__ == "__main__":
    main()
