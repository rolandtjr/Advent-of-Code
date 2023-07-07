#!/usr/bin/env python3
from collections import Counter


def create_semi_memo(tenth, pair_insertion):
    for key in pair_insertion.keys():
        key_l = [ x for x in key ]
        p_t, elements = do_insert(key_l, pair_insertion, 10)
        tenth[key] = [p_t[1:-1], elements]


def do_final_insert(polymer_template, tenth, final_elements, iterations):
    for count in range(1,iterations + 1):
        length_pt = len(polymer_template)
        for index in range(1, length_pt + 1):
            if(index == length_pt):
                break
            p_t = f'{polymer_template[-index*2]}{polymer_template[-index*2+1]}'
            for zindex in range(len(tenth[p_t][0])):
                polymer_template.insert(-index*2+1+zindex, tenth[p_t][0][zindex])
            final_elements = Counter(final_elements) + Counter(tenth[p_t][1])

    return final_elements


def do_insert(polymer_template, pair_insertion, iterations):
    elements = dict()
    for count in range(1,iterations + 1):
        length_pt = len(polymer_template)
        for index in range(1, length_pt + 1):
            if(index == length_pt):
                break
            p_t = f'{polymer_template[-index*2]}{polymer_template[-index*2+1]}'
            polymer_template.insert(-index*2+1, pair_insertion[p_t])
            try:
                elements[pair_insertion[p_t]] += 1
            except KeyError:
                elements[pair_insertion[p_t]] = 1
        print(count)

    return polymer_template, elements


def main():
    with open('day14', 'r') as file:
        lines = file.readlines()

    polymer_template = lines[0].strip()
    pair_insertion = dict()
    final_elements = dict()
    tenth = dict()

    for line in lines[2:]:
        line = line.strip().split()
        pair_insertion[line[0]] = line[2]

    for polymer in polymer_template:
        try:
            final_elements[polymer] += 1
        except KeyError:
            final_elements[polymer] = 1

    polymer_template = [ x for x in polymer_template ]

    polymer_template, elements = do_insert(polymer_template, pair_insertion, 40)

    maxi = max(list(elements.values()))
    mixi = min(list(elements.values()))


    print(maxi-mixi)
    

if __name__ == '__main__':
    main()
