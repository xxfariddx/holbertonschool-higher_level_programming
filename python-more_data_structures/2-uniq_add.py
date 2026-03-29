#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in my_list:
        if new_list.count(i) == 0:
            new_list.append(i)
    return sum(new_list)
