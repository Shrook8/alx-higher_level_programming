#!/usr/bin/python3
for i in rang(ord('a'), ord('z') + 1):
    if i != ord('q') and i != ord('e'):
        print("{:c}".format(i), end=" ")
