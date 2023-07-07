#!/usr/bin/env python3

def compute_result_one(opp, my_play):
    match opp:
        case 'A':
            match my_play:
                case 'X':
                    result = 3
                case 'Y':
                    result = 6
                case 'Z':
                    result = 0 
        case 'B':
            match my_play:
                case 'X':
                    result = 0
                case 'Y':
                    result = 3
                case 'Z':
                    result = 6 
        case 'C':
            match my_play:
                case 'X':
                    result = 6
                case 'Y':
                    result = 0
                case 'Z':
                    result = 3 
    return result


def compute_result_two(opp, my_play):
    match opp:
        case 'A':
            match my_play:
                case 'X':
                    result = 3
                case 'Y':
                    result = 4
                case 'Z':
                    result = 8 
        case 'B':
            match my_play:
                case 'X':
                    result = 1
                case 'Y':
                    result = 5
                case 'Z':
                    result = 9 
        case 'C':
            match my_play:
                case 'X':
                    result = 2
                case 'Y':
                    result = 6
                case 'Z':
                    result = 7 
    return result


def main():
    me = {
            'X': 1, # Rock
            'Y': 2, # Paper
            'Z': 3 # Scissors 
         }

    score = 0
    with open('day2', 'r') as file:
        lines = file.readlines()
        for line in lines:
            opp, my_play = line.split()
            score += me[my_play]
            result = compute_result_one(opp, my_play)
            score += result
    print(score)

    score = 0
    with open('day2', 'r') as file:
        lines = file.readlines()
        for line in lines:
            opp, my_play = line.split()
            result = compute_result_two(opp, my_play)
            score += result
    print(score)

if __name__ == '__main__':
    main()
