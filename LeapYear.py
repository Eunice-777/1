#A leap year is perfectly divisible by 4 except for century years (ending with 00) which are perfectly divisible by 400.
year=int(input("Please input year to be checked: "))
if(year%4==0 or year%400==0):
    print("The year you entered is a leap year")
else:
    print("The year you entered is not a leap year")
