#File: three_n_plus_one.py

import numpy as np


def one_iteration_of_3n_plus_one(number):
    """
    Applies the 3n+1 rules to a number:
    If odd multiplies by 3 and adds one
    If even divides by 2

    Input: Any integer.
    Output: Integer after rules have been applied
    """
    
    new_number = number
    if (number%2 == 0):
        new_number //= 2
    else:
        new_number *=3
        new_number +=1
    return new_number

def array_of_3n_plus_one_loop(number, operation_limit):
    """
    Starts from a number and applies the 3n+1 rules to it a given number of times.
    Input: Any integer and a limit to how many times the 3n+1 rules can be applied to it.
    Output: An array with length of the operation_limit that contains all the numbers gone through in the 3n+1 loop.
    """
    i = 0
    list_of_number_loop = [number]
    while i < operation_limit:
        next_number = one_iteration_of_3n_plus_one(list_of_number_loop[i])
        list_of_number_loop.append(next_number)
        i +=1
    return list_of_number_loop

def bounded_3n_plus_one(numbers, operation_limit):
    """
    Is given a list of numbers and determines which of those numbers eventually makes it down to one within the given operation_limit. 
    Input: A list of integers, and a limit to how many times each integer can undergo the 3n+1 rules.
    Output: A 2D list of the loop that each number went through and a 1D list of booleans of True or False if they have a value 1 in the array.
    """
    
    two_d_list_of_loops = [[]]
    for num in numbers:
        loop = array_of_3n_plus_one_loop(num, operation_limit)
        two_d_list_of_loops.append(loop)
        
    list_of_three_n_plus_one_success = []
    
    for sequence in two_d_list_of_loops:
        if 1 in sequence:
            list_of_three_n_plus_one_success.append(True)
        else:
            list_of_three_n_plus_one_success.append(False)
            
    return two_d_list_of_loops, list_of_three_n_plus_one_success
    