'''
This script is meant to solve the following

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
'''
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Allow user to pass a file containing at most 1000 lines')

# Add arguments
parser.add_argument('-d','--dataset', type=argparse.FileType('r'), help='Dataset to parse')

# Parse the arguments
args = parser.parse_args()

# Collect data
dataset = args.dataset

#Read file and print even lines
line_count = 1
for line in dataset.readlines():
    
    if line_count % 2 == 0:

        #edit: print with newlines removed
        print(line.strip())
    line_count += 1
        
    
