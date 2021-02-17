"""
Our first Python test program.
Team members: August Wadlington, Bruce Tang, Danny Little
"""


def main():
    my_cool_variable = 'Hello world!'[::-1]
    my_cool_variable_to_list = list(my_cool_variable)
    my_cool_variable_to_list.reverse()
    print(''.join(my_cool_variable_to_list))


if __name__ == "__main__":
    main()
