#The four compass points can be abbreviated by single-letter
#strings as “N”, “E”, “S”, and “W”.
#Write a function turn_clockwise that takes one
#of these four compass points as its parameter,
#and returns the next compass point in the clockwise direction.
#Here are some tests that should pass:

        return "E"
    elif d == "E":
        return "S"
    elif d == "S":
        return "W"
    elif d == "W":
        return "N"
    else:
        return "none"
