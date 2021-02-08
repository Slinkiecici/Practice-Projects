while True:
    year = input("Please supply a year to check: ")
    year = int(year)
    if (year/4).is_integer() and (year/100).is_integer() and (year/400).is_integer():
        print (str(year) +" is a leap year")
    elif (year/4).is_integer() and ((year/100).is_integer())== False:
        print (str(year) +" is a leap year")
    else: print (str(year) + " is not a leap year")

