import time
import math

A = [8, 7, 6, 5, 4, 3, 2, 1]
B = []
C = []
moves = 0
def tower_recursive(disk: int, a, c, b):
    global moves, A
    if disk == 1:
        c.append(disk)
        a.remove(disk)
    else:
        tower_recursive(disk - 1, a, b, c)
        c.append(disk)
        a.remove(disk)
        tower_recursive(disk - 1, b, c, a)
    moves += 1
    print(a, "   ", b, "   ", c)
    
    
startTime = time.time()
tower_recursive(len(A), A, C, B)
endTime = time.time()

print("Runtime:", round((endTime - startTime)*10000)/10000, "seconds")

print(moves)
