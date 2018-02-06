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




print(count_letters("oooooooooooofbfkdfv","o"))

#Problem 7
def reverse(word):
    reversed = ""
    for i in range(len(word) -1, -1, -1):
        reversed += word[i]
    return reversed

reverse("poof")










test_suite()









