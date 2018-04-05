#1
"""What is the Python interpreter’s response to the following? >>> list(range(10, 0, -2))
The three arguments to the range function are start, stop, and step, respectively. In this
example, start is greater than stop. What happens if start < stop and step < 0? Write a
rule for the relationships among start, stop, and step."""

"""
[start+(step), start+(2*step), start+(3*step) ... ] until ((|start - stop| / step)*step) = start 
and (start-stop)/step is a positive integer
"""
# 2
#Consider this fragment of code:
import turtle
tess = turtle.Turtle()
alex = tess
alex.color("hotpink")
"""Does this fragment create one or two turtle instances? Does setting the
color of alex also change the color of tess? Explain in detail."""
#Since you are assigning Alex to Tess, they are considered the same. So when you change one you also change the other. Also, since they are the same, you only make one turtle.
