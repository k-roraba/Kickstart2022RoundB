# Google KickStart Round B 2022 Problem 1
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acf079
# find the total area of the circles generated.

case = int(input())
output = []

PI = 3.14159265358979323

for i in range(case):

    area = 0
    r, a, b = [int(x) for x in input().split()]

    #first one is strange
    area += r*r

    #after that, there is a chance of termination
    while(r != 0):
        #change radius to big, add area of big
        r *= a
        area += r*r

        #change radius to small, add area of small
        r //= b
        area += r*r
    
    area *= PI

    output.append(str(area))

for i in range(case):
    print("Case #{}:".format(i+1), output[i])


