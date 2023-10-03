#!/usr/bin/env python
from sys import argv
from collections import Counter, deque

def attempt_one(line, iterations):
    fishes = [int(fish) for fish in line if fish.isdigit()]

    for days in range(iterations):
        number_zeroes = fishes.count(0)
        fishes = [fish if fish else 7 for fish in fishes]
        if number_zeroes:
            fishes.extend(number_zeroes * [9])
        fishes = [fish-1 for fish in fishes]
    return len(fishes)


def lanternfish(line, iterations):
    fishes = Counter([int(fish) for fish in line if fish.isdigit()])
    fishes_list = [0] * 9
    for fish in fishes:
        fishes_list[fish] = fishes[fish]

    fishes_que = deque(fishes_list)

    for days in range(iterations):
        number_zeroes = fishes_que.popleft()
        fishes_que.append(number_zeroes)
        fishes_que[6] += number_zeroes
    return sum(fishes_que)



def main():
    with open("day6", "r") as file:
        line = file.readline()

    print(lanternfish(line, 80))
    print(lanternfish(line, 256))

if __name__ == "__main__":
    main()
