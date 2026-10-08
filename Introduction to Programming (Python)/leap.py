"""Checks if year given in input is leap."""
    
year = int(input('Give year: '))
if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
    print(year,'is a leap year.')
else:
    print(year,'is not a leap year.')
