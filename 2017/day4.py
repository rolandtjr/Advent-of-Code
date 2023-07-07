#!/usr/bin/env python3


lis = []
for line in open("day4.sample"):
    print(line)
    for word in line.split():
        lis.append(word)



print([word for line in open("day4.sample") for word in line.split()])



print(lis, type(lis))
