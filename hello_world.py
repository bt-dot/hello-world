"""
Our first Python test program.
Team members: August Wadlington, Bruce Tang, Danny Little
"""
from random import randint


def main():
    my_cool_variable = ''
    target = 'Hello world!'
    i = 0
    misfires = 0
    while my_cool_variable != 'Hello world!':
        r = randint(32, 128)
        to_add = chr(r)
        if to_add == target[i]:
            my_cool_variable += to_add
            i += 1
        elif to_add != target[i]:
            misfires += 1
    print(my_cool_variable)
    print("Misses: ", misfires)
    if misfires == 12:
        print("Are you cheating?")

if __name__ == "__main__":
    main()
