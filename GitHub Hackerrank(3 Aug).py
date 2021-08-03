#!/usr/bin/env python
# coding: utf-8

# **HackerRank---> DataStructure --->Stack--->Maximum Element ---> Python**
# 
# 
# **Problem:** You have an empty sequence, and you will be given **N** queries. Each query is one of these three type
# 1   -Push the element x into the stack.
# 2    -Delete the element present at the top of the stack.
# 3    -Print the maximum element in the stack.

# In[ ]:


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
    stack = [0]
    ans = []
    #for _ in range(int(input())):
        #a= list(map(int,input().split()))
    for a in operations:
        a= a.split()
        
        if a[0]== '1':
            stack.append(max(stack[-1],int(a[1])))
        elif a[0]=='2':
            stack.pop() 
        else:
            ans.append(stack[-1])
    return ans
                
                
    
                
    


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

