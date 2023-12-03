#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolean_List = []
    for i in my_list:
        if i % 2 == 0:
            boolean_List.append(True)
        else:
            boolean_List.append(False)
    return boolean_List
