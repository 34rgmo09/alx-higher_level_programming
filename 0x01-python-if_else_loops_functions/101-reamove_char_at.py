#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""

    i = 0
    for j in str:
        if i != n:
             new = new + j
        i += 1
    return (new)
