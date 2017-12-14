import sys
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(sum_to_even(mylist)==10)
    
    test(sam(samlist)== 1)
    

samlist = {"molly", "sam"}
mylist = {3, 7, 2, 11, 12}

listletters = {"hello", "my", "name"}

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

def five_letters(letterlist):
    w= 0
    for i in letterlist:
        if len(i) == 5:
            words = words+1
    return words


def sum_to_even(nlist):
    sum = 0
    for i in nlist:
        if i % 2 == 0:
            break
        else:
            sum+=i
    return sum
def sam(namelist):
    count = 0
    for i in namelist:
        if i == "sam":
            count = count+1
            break
        
        count = count+1
    return count
        


test_suite() 