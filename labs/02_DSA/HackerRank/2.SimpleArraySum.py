import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    # for i in ar:
    #     sum = int(0)
    #     sum += i
    # return sum
    return sum(ar)
        

if __name__ == '__main__':

    ar_count = int(input('Digite um numero ai pra eu testa').strip())

    ar = list(map(int, input('fitia mais').rstrip().split()))

    result = simpleArraySum(ar)

    print(result)


