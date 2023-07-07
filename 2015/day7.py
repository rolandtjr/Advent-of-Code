#!/usr/bin/env python3

def parse_line(line, identifiers):
    elements = line.split()
    length = len(elements)
    match length:
        case 3: # Assignment
            return int(elements[0]), elements[2].strip()
        case 4: # NOT
            return ~identifiers[elements[1]], elements[3].strip()
        case 5: # AND OR LSHIFT RSHIFT
            match elements[1]:
                case 'AND':
                    return identifiers[elements[0]] & identifiers[elements[2]], elements[4].strip()
                case 'OR':
                    return identifiers[elements[0]] | identifiers[elements[2]], elements[4].strip()
                case 'LSHIFT':
                    return identifiers[elements[0]] << int(elements[2]), elements[4].strip()
                case 'RSHIFT':
                    return identifiers[elements[0]] >> int(elements[2]), elements[4].strip()


def main():
    with open('day7.sample', 'r') as file:
        lines = file.readlines()

    identifiers = {}
    for line in lines:
        value, identifier = parse_line(line, identifiers)
        identifiers[identifier] = value

    print(identifiers)


if __name__ == '__main__':
    main()
