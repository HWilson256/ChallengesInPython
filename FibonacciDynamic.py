from ctypes.wintypes import LONG
import time
import math
import sys

sys.setrecursionlimit(7000)

foundNums = []
corresponding_nums = []
nCalls = 0
def F(x):
    if foundNums.count(x) == 0:
        global nCalls
        nCalls += 1
        
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            num = (F(x-1) + F(x-2))
            foundNums.append(x)
            corresponding_nums.append(num)
            return num
    else:
        this_num = foundNums.index(x)
        return corresponding_nums[this_num]

number_to_find = 2673
print("Finding Number", number_to_find)
startTime = time.time()
print("Fibonacci Number =", str(F(number_to_find)))
endTime = time.time()

#print(corresponding_nums, "\n")
#print(foundNums)
print("Runtime:", round((endTime - startTime)*10000)/10000, "seconds")