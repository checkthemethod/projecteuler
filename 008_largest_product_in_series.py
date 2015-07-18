# Problem 8 - Largest product in a series
# Find the thirteen adjacent digits in the 1000-digit number
# that have the greatest product. What is the value of this product?
# NOTE: first program written in Python - Be gentle ^__^

# used python instead of node because
# JavaScript only supports 53 bit integers
# http://www.2ality.com/2012/07/large-integers.html

# set 1000-digit number in longNumber var
longNumber = 73167176531330624919225119674426574742355
349194934969835203127745063262395783180169848018694788
518438586156078911294949545950173795833195285320880551
112540698747158523863050715693290963295227443043557668
966489504452445231617318564030987111217223831136222989
342338030813533627661428280644448664523874930358907296
290491560440772390713810515859307960866701724271218839
987979087922749219016997208880937766572733300105336788
122023542180975125454059475224352584907711670556013604
839586446706324415722155397536978179778461740649551492
908625693219784686224828397224137565705605749026140797
296865241453510047482166370484403199890008895243450658
541227588666881164271714799244429282308634656748139191
231628245861786645835912456652947654568284891288314260
769004224219022671055626321111109370544217506941658960
408071984038509624554443629812309878799272442849091888
458015616609791913387549920052406368991256071760605886
116467109405077541002256983155200055935729725716362695
61882670428252483600823257530420752963450


# split the longNumber var into an array of single digits
digitArray = map(int, str(longNumber))
# set the limit of numbers to multiply at one time
limit = 13


# find the products of a series by passing an array of factors
def find_products_of_series(_factors_array):
    # set answer to default 1
    answer = 1
    # loop through the factors array
    for x in range(0, len(_factors_array)):
        # multiply each number to the previous product until array is empty
        # make sure answers are converted from string to int before multiplying
        answer *= int(_factors_array[x])
    # return the product
    return answer


# traverse through the long number 13 digits at a time
# return highest product
def find_thirteen_digits(_num):
    # set rangeEnd to passed limit
    range_end = _num
    # set default highestProduct var
    highest_product = 0
    # loop through longNumber, 13 digits at a time
    for x in range(0, (len(digitArray) - (_num - 1))):
        # set/reset default array that factors get stored
        factor_array = []
        # loop through the 13 digit sample
        for j in range(x, range_end):
            # push the digits into an array
            factor_array.append(digitArray[j])
        # set the nextProduct var to the value of the next 13 digit product
        next_product = find_products_of_series(factor_array)
        # compare if the current highestProduct is less than the new product
        if highest_product < next_product:
            # if so, set the nextProduct as the highestProduct
            highest_product = next_product

        # increase range by 1 to grab the next 13 in range
        range_end += 1

    # after looping through all 1000 digits, return the highestProduct
    return highest_product


print "Exercise 8 - Largest product in series is:", find_thirteen_digits(limit)
