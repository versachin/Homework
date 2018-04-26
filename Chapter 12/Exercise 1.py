
#Question 1
import calendar
cal = calendar.TextCalendar()
cal.pryear(2012)

#Question 1B
cal = calendar.TextCalendar(3)
cal.pryear(2018)

#Question 1C
cal = calendar.TextCalendar(6)
cal.prmonth(2018, 8)

#Question 1D
d = calendar.LocalTextCalendar(6,"CHINESE")
d.pryear(2012)

#Question 1E
print(calendar.isleap(8))
#it expects year
#Returns true or false
#Boolean function

