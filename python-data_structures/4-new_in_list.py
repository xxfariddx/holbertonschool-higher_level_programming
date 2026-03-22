#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Make a copy of the original list
    new_list = my_list[:]
    # Check for invalid index
    if idx < 0 or idx >= len(my_list):
        return new_list
    # Replace the element at idx
    new_list[idx] = element
    return new_list
