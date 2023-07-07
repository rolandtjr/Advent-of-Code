#!/usr/bin/env python3

def get_max_coords(points):
    max_x = 0
    max_y = 0
    for x, y in points:
        if int(x) > max_x:
            max_x = int(x)
        if int(y) > max_y:
            max_y = int(y)
    return max_x, max_y


def print_coords(points, max_x, max_y):
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if [f'{x}',f'{y}'] in points:
                print('#', end='')
            else:
                print('.', end='')
        print()


def fold_y(points, temp_points, line):
    for x, y in points:
        x = int(x)
        y = int(y)
        if y > line:
            new_y = line - (y - line)
            temp_points.append([f'{x}', f'{new_y}'])
        else:
            temp_points.append([f'{x}', f'{y}'])


def fold_x(points, temp_points, line):
    for x, y in points:
        x = int(x)
        y = int(y)
        if x > line:
            new_x = line - (x - line)
            temp_points.append([f'{new_x}', f'{y}'])
        else:
            temp_points.append([f'{x}' ,f'{y}'])


def do_instructions(instructions, points):
    first = True
    for axis, line in instructions:
        line = int(line)
        temp_points = []
        match axis:
            case 'y':
                fold_y(points, temp_points, line)
            case 'x':
                fold_x(points, temp_points, line)
        if first:
            get_uniq = [tuple(point) for point in temp_points]
            print(len(set(tuple(get_uniq))))
            first = False
        points = temp_points
    return points


def main():
    with open('day13', 'r') as file:
        lines = file.readlines()

    instructions = []
    points = []
    for line in lines:
        line = line.strip().split(',')
        if len(line) == 2:
            points.append(line)
        elif line[0] == '':
            pass
        else:
            line = line[0].split()
            instructions.append(line[2].split('='))

    points = do_instructions(instructions, points)
    max_x, max_y = get_max_coords(points)
    print_coords(points, max_x, max_y)


if __name__ == '__main__':
    main()
