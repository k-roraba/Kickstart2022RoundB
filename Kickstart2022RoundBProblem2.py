#Google Kickstart Round B 2022 Problem 2
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acee89


# this produced a runtime error.  
# I plan to reread and redo.


import math
from pickle import FALSE, TRUE

case = int(input())
output = []

def isPalin(num):
    if(len(str(num)) == 1):
        return True
    
    if(len(str(num)) == 2  or len(str(num)) == 3):
        if(str(num)[0] != str(num)[len(str(num))-1]):
            return False

    for j in range(0, len(str(num))//2 - 1):
        if(str(num)[j] != str(num)[len(str(num)) - j]):
            return False
    
    return TRUE


for i in range(case):
    a = int(input())
    count = 1 #1 is always a palindrome
    if(isPalin(a)):
        count += 1
    x = 2 
    while(x <= math.sqrt(a)):
        if(a % x == 0):
            #x is a factor, so check if palindrome (and check other factor)
            #need to not double-count pf sq factors
            if(isPalin(x)):
                count += 1
            
            if(isPalin(a//x) and a//x != x):
                count += 1
        x += 1
    
    output.append(str(count))

for i in range(case):
    print("Case #{}:".format(i+1), output[i])




