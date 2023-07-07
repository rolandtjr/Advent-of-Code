#!/usr/bin/env python3

def main():
    with open('day1', 'r') as file:
        lines = file.readlines()

    numbers = []
    for line in lines:
        first = int(line.strip())
        for sec in lines:
            second = int(sec)
            if (first + second) == 2020:
                print(first,second, first * second)
            for thi in lines:
                third = int(thi)
                if (first + second + third) == 2020:
                    print(first, second, third, first * second * third)


if __name__ == '__main__':
    main()
