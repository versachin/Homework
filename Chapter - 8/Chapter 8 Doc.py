import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    print("tests for reverse")
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")


prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
   if letter == "O" or letter == "Q":
       print (letter + "u" + suffix)
   else:
       print(letter+suffix)

#Problem 3
def count_letters(word,letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count
#Problem 4
def find2(string, char, start=0):
    ix=start
    while ix < len(string):
        if string[ix] == char:
            return ix
        ix+=1
    return -1


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,2021,22,23,24,25,26]

print(count_letters("oooooooooooofbfkdfv","o"))

#Problem 7
def reverse(word):
    s = len(word)
    while s > 0:
        print(word[s-1])
        s-=1
reverse("poof")







test_suite()









