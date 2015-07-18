# Problem 8 - Largest product in a series
# Find the thirteen adjacent digits in the 1000-digit number
# that have the greatest product. What is the value of this product?
# 
# NOTE: first program written in Python - Be gentle ^__^

# used python instead of node because 
# JavaScript only supports 53 bit integers
# http://www.2ality.com/2012/07/large-integers.html

# set 1000-digit number in longNumber var 
longNumber = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

# split the longNumber var into an array of single digits
digitArray = map(int, str(longNumber))
# set the limit of numbers to multiply at one time
limit = 13

# find the products of a series by passing an array of factors
def findProductsOfSeries(_factorsArray):
    # set answer to default 1
    answer = 1
    # loop through the factors array
    for x in range(0, len(_factorsArray)):
        # multiply each number to the previous product until array is empty
        # make sure answers are converted from string to int before multiplying
        answer *= int(_factorsArray[x])
    #return the product
    return answer

# traverse through the long number 13 digits at a time
# return highest product
def findThirteenDigits(_num):
    # set rangeEnd to passed limit
    rangeEnd = _num
    # set default highestProduct var
    highestProduct = 0
    # loop through longNumber, 13 digits at a time
    for x in range(0, (len(digitArray)-(_num-1))):
        # set/reset default array that factors get stored
        factorArray = []
        # loop through the 13 digit sample
        for j in range(x, rangeEnd):
            # push the digits into an array
            factorArray.append(digitArray[j])
        # set the nextProduct var to the value of the next 13 digit product
        nextProduct = findProductsOfSeries(factorArray)
        # compare if the current highestProduct is less than the new product
        if highestProduct < nextProduct:
            # if so, set the nextProduct as the highestProduct
            highestProduct = nextProduct

        # increase range by 1 to grab the next 13 in range
        rangeEnd += 1

    # after looping through all 1000 digits, return the highestProduct
    return highestProduct



print "Exercise 8 - Largest product in series is: %d" % findThirteenDigits(limit)

