#!/usr/bin/python3
def no_c(my_string):
    ret = ""
    for i in range(len(my_string)):
        if (my_string != 'c' and my_string != 'C'):
            ret += my_string[i]
        return ret
