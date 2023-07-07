#!/usr/bin/env python3

def turn(direction, facing):
    match facing:
        case 'North':
            if direction == 'R':
                facing = 'East'
            else:
                facing = 'West'
        case 'East':
            if direction == 'R':
                facing = 'South'
            else:
                facing = 'North'
        case 'South':
            if direction == 'R':
                facing = 'West'
            else:
                facing = 'East'
        case 'West':
            if direction == 'R':
                facing = 'North'
            else:
                facing = 'South'
    return facing


def check_locations(blocks, facing, x_coord, y_coord, locations):
    x_coord, y_coord = locations[-1]
    match facing:
        case 'North':
            for block in range(1, blocks + 1):
                if [x_coord + block, y_coord] in locations:
                    return [x_coord + block, y_coord]
                locations.append([x_coord + block, y_coord])
        case 'East':
            for block in range(1, blocks + 1):
                if [x_coord, y_coord + block] in locations:
                    return [x_coord, y_coord + block]
                locations.append([x_coord, y_coord + block])
        case 'South':
            for block in range(1, blocks + 1):
                if [x_coord - block, y_coord] in locations:
                    return [x_coord - block, y_coord]
                locations.append([x_coord - block, y_coord])
        case 'West':
            for block in range(1, blocks + 1):
                if [x_coord, y_coord - block] in locations:
                    return [x_coord, y_coord - block]
                locations.append([x_coord, y_coord - block])


def walk(blocks, facing, x_coord, y_coord):
    match facing:
        case 'North':
            x_coord += blocks
        case 'East':
            y_coord += blocks
        case 'South':
            x_coord -= blocks
        case 'West':
            y_coord -= blocks
    return x_coord, y_coord


def main():
    x_coord = 0
    y_coord = 0
    facing = 'North'

    with open('day1', 'r') as file:
        line = file.readlines()[0][:-1]
    
    sequences = line.split(', ')

    locations = [[0,0]]
    hq_loc = []

    for sequence in sequences:
        direction = sequence[0]
        blocks = int(sequence[1:])
        facing = turn(direction, facing)
        x_coord, y_coord = walk(blocks , facing, x_coord, y_coord)

    for sequence in sequences:
        direction = sequence[0]
        blocks = int(sequence[1:])
        facing = turn(direction, facing)
        hq_loc = check_locations(blocks, facing, x_coord, y_coord, locations)
        if hq_loc:
            break

    print(abs(x_coord) + abs(y_coord))
    print(abs(hq_loc[0]) + abs(hq_loc[1]))


if __name__ == '__main__':
    main()
