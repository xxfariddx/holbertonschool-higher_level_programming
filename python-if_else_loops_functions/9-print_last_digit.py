#!/usr/bin/python3
def print_last_digit(number):
    ln = abs(number) % 10
    print(ln, end="")
    return ln
