#!/usr/bin/env python3

def main():
    with open("day3.sample", "r") as file:
        lines = file.readlines()

    for line in lines:
        print(int(line.strip(), 2))


if __name__ == "__main__":
    main()
