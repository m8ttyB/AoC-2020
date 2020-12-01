#!/usr/bin/env python
# 2020 Advent of Code, Day 01 solution
import os

def get_list_of_ints(filename):
    '''convert txt file to ordered list of ints'''
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        num_list = [int(i) for i in lines]
        num_list.sort()

        return num_list


def find_sum_two_numbers(value, nums):
    '''
    In a list of integers, find two numbers that 
    when summed, equal the `value`.
    '''
    i = 0
    j = len(nums) - 1
    while(i < j):
        sum = nums[i] + nums[j]
        if sum == value: # if solution found, yay!
            answer = (nums[i], nums[j])
            return answer
        elif sum < value:
            i += 1
        else: # sum > value:
            j -= 1
    # if a match isn't found, return -1
    return -1


def find_sum_three_numbers(value, nums):
    '''
    In a list of integers, find three numbers that 
    when summed equal the `value`.
    '''
    list_length = len(nums)
    for i in range(list_length - 2):
        j = i + 1
        k = list_length - 1
        while(j < k):
            sum = nums[i] + nums[j] + nums[k]
            if sum == value: # if solution found, yay!
                return (nums[i], nums[j], nums[k])
            elif sum < value:
                j += 1
            else:
                k -= 1
    # if a match isn't found, return -1
    return -1
    

if __name__ == '__main__':
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = os.path.join(location, "day_01_input.txt")
    
    # readlines into a list   
    num_list = get_list_of_ints(file)

    # find the sum of 2 numbers
    print("Find the sum of two numbers")
    values = find_sum_two_numbers(2020, num_list)
    
    # multiply the values and return the answer
    print("The solution is %s: %s \n\n" % (values, values[0] * values[1]))

    # find the sum of 3 numbers
    print("Find the sum of three numbers")
    values = find_sum_three_numbers(2020, num_list)

    # multiply the values and return the answer
    print("The solution is %s: %s" % (values, values[0] * values[1] * values[2]))
