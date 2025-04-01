#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    stack = []
    max_stack = []
    res = []

    for operation in operations:
        op = operation.split()
        
        if op[0] == '1':  # Push operation
            num = int(op[1])
            stack.append(num)
            if not max_stack or num >= max_stack[-1]:
                max_stack.append(num)
        
        elif op[0] == '2':  # Pop operation
            if stack:
                popped = stack.pop()
                if popped == max_stack[-1]:
                    max_stack.pop()
        
        elif op[0] == '3':  # Print max
            if max_stack:
                res.append(max_stack[-1])
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
