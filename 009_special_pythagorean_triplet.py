# Problem 9 - Special Pythagorean triplet
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math   # This will import math module, for math.floor

def findNumbersEqualThousand(_limit):
    #this need a better range but assumed number can't be larger than totalNum/3
    # or else it will be greater than b or c
    rangeA = int(math.floor(_limit/3))
    rangeB = int(math.floor(_limit/2))
    for a in range(0, rangeA): 
        # in current loop, b can't be larger than _limit/2, or won't add up
        for b in range(a+1, rangeB):
            # in current loop, b can't be larger than 1000-(b-a), or won't add up
            for c in range(b+1, _limit-(b-a)):
                #if asquared + bsquared = csquared AND a+b+c=1000, then tell me what it is
                if ((a*a) + (b*b) == (c*c) and (a+b+c) == _limit):
                    print "a: %d || b: %d || c: %d" % (a,b,c)
                    #return product of abc
                    return a*b*c

#print answer
print "Exercise 9 - product of abc is: %d" % findNumbersEqualThousand(1000)