#!/usr/bin/env python3

def main():
    with open('day8.sample', 'r') as file:
        lines = file.readlines()

    matrix = [list(line.strip()) for line in lines]
    print(matrix)
    last_column = len(matrix[0]) -1
    last_row = len(matrix) -1
    print(last_column, last_row)
    visible = 0
    for row_index, row in enumerate(matrix):
        for column_index, column in enumerate(row):
            try:
                if (column > matrix[row_index + 1][column_index] or
                   column > matrix[row_index - 1][column_index] or
                   column > matrix[row_index][column_index + 1] or
                   column > matrix[row_index][column_index - 1]):
                       visible += 1
                elif (row_index == 0 or column_index == 0 or
                      row_index == last_row or column_index == last_column):
                    visible += 1
                else:
                    print(f'not visible {column_index}x{row_index}', column)
            except IndexError:
                visible += 1
    print(visible)



if __name__ == '__main__':
    main()
