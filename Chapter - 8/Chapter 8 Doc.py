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
def find(string, char, start=0):
    ix=start
    while ix < len(string):
        if string[ix] == char:
            return ix
        ix+=1
    return -1



print(count_letters("oooooooooooofbfkdfv","o"))

#Problem 7
#def reverse(word):
    #for char in word:
        #new_word = word[len(word)] + word[len(word)-1] + word[len(word)-2] +









