#!/usr/bin/env python3

def main():
    with open('day1', 'r') as file:
        lines = file.readlines()

    floor = 0
    position = 0
    for line in lines:
        for char in line:
            if char == '(':
                position += 1
                floor += 1
            elif char == ')':
                position += 1
                floor -= 1
                if floor == -1:
                    print(f'{position = }')

    print(f'{floor = }')
                

if __name__ == '__main__':
    main()
