#!/usr/bin/env python3
from string import ascii_letters

priority = {letter:index+1 for index,letter in enumerate(ascii_letters)}

def main():
    with open('day3', 'r') as file:
        lines = file.readlines()

    priorities = 0
    for line in lines:
        length_compartments = int(len(line) / 2)
        first = line[:length_compartments]
        second = line[length_compartments:]


        for item in first:
            if item in second:
                priorities += priority[item]
                break
    print(priorities)

    priorities = 0
    for index, line in enumerate(lines):
        mod_index = (index + 1) % 3
        match mod_index:
            case 1:
                first = line
            case 2:
                second = line
            case 0:
                third = line

                for item in first:
                    if (item in second) and (item in third):
                        priorities += priority[item]
                        break
    print(priorities)

if __name__ == '__main__':
    main()
