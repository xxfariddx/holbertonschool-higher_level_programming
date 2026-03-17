#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number > 0:
    ld = number % 10
    if ld > 5:
        print(f"Last digit of {number} is {ld} "
              f"and is greater than 5")
    elif ld == 0:
        print(f"Last digit of {number} is {ld} "
              f"and is 0")
    else:
        print(f"Last digit of {number} is {ld} "
              f"and is less than 6 and not 0")

elif number == 0:
    ld = 0
    print(f"Last digit of {number} is {ld} "
          f"and is 0")

else:
    ld = -(-number % 10)
    if ld > 5:
        print(f"Last digit of {number} is {ld} "
              f"and is greater than 5")
    elif ld == 0:
        print(f"Last digit of {number} is {ld} "
              f"and is 0")
    else:
        print(f"Last digit of {number} is {ld} "
              f"and is less than 6 and not 0")
