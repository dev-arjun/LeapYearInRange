def LeapYear():
    list_of_years_beg = int(input("Enter the year to begin: "))
    list_of_years_end = int(input("Enter the year to end: "))+1
    for x in range(list_of_years_beg,list_of_years_end):
        if x % 4 == 0:
            print("{} is a leap year".format(x))
        #else:
            #print("{}, is not a leap year".format(x)) #Optional One if you need to print non-leap years
LeapYear()