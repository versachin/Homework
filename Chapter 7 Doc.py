mylist = {0, 2, 3, 7, 11, 12}

mymixedlist = {0, -2, -4, 7, 9, -1}
 
def count_odd(numlist):
    count = 0
    for i in numlist:
        if i%2 != 0:
            count = count+1
    return count
             
def sum_even(numlist):
    sum = 0
    for i in numlist:
        if i%2 == 0:
            sum = sum + i
    return sum

def sum_neg(numlist):
    negsum = 0
    for i in numlist:
        if i<1:
            negsum =  negsum+i
    return negsum

