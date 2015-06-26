# On CodeEval, test cases are read in from a file which is the first argument to your program
# Open the file and read in line by line. Each line represents a different test case
# (unless given different instructions in the challenge description)

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()

# to execute the file do: python file_name.py file_name_In.txt > file_name_Out.txt
