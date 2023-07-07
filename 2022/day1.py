#!/usr/bin/env python3

def main():
    with open('day1', 'r') as file:
        lines = file.readlines()

        list_calories = []
        current_calories = 0
        max_calories = 0
        for line in lines:
            if line == '\n':
                list_calories.append(current_calories)
                if current_calories > max_calories:
                    max_calories = current_calories
                current_calories = 0
                continue
            current_calories += int(line)

    list_calories = sorted(list_calories, reverse=True)
    top_three = sum(list_calories[:3])
    print(list_calories[0])
    print(top_three)

if __name__ == '__main__':
    main()
