# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""
from __future__ import division
from __future__ import print_function


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    list_numbers = []
    while start < stop:
        list_numbers.append(start)
        start += step
    return list_numbers


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    if start <= stop:
        step = abs(step)
        list_numbers = range(start, stop, step)
    else:
        step = -abs(step)
        list_numbers = range(start, stop, step)
    return list_numbers


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    list_numbers_2 = range(start, stop, 2)
    return list_numbers_2


def gene_krupa_range(start, stop, even_step, odd_step):
    """Make a range that has two step sizes.

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """
    i = 0
    list_numbers = [start]
    while start < stop:
        if i % 2 == 0 and (stop - start) >= even_step:
            start += even_step
            list_numbers.append(start)
        elif i % 2 != 0 and (stop - start) >= odd_step:
            start += odd_step
            list_numbers.append(start)
        else:
            break
        i += 1
    return list_numbers


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    while True:
        my_input = raw_input('Enter a number between {} and {} '.
                             format(low, high))
        if low < int(my_input) < high:
            return my_input
            break


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    while True:
        my_input = str(raw_input('Enter a number: '))
        if my_input.isdigit():
            return int(my_input)
            break


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    print ('Enter a number between {} and {}'.format(low, high))
    while True:
        my_input = not_number_rejector('Super')
        if int(my_input) < low or int(my_input) > high:
            continue
        else:
            break
    return my_input


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    # inside Atom, you need to run them from the terminal. E.g.:
    # ben@um:~/projects/git/code1161base$ python week3/exercise1.py

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector('Dare')
    print("\nsuper_asker")
    super_asker(33, 42)
