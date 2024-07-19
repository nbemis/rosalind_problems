'''
This script is meant to solve the following

Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a
through b, inclusively.
'''
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Allow user to pass in int range.')

# Add arguments
parser.add_argument('first_int', type=int, help='Low int')
parser.add_argument('second_int', type=int, help='Top int')


# Parse the arguments
args = parser.parse_args()

low = args.first_int
high = args.second_int

def sum_odd_int(a, b):

    odd_int_sum = 0

    for num in range(a, b+1):

        if num % 2 != 0:
            odd_int_sum += num

    return odd_int_sum

print(sum_odd_int(low, high))
