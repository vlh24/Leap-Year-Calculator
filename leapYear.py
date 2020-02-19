checker = False
while checker == False:
    try:
        year = int(input("Input a year: "))
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 == 0:
                print("That is a leap year!" 
                      + " Enjoy the extra day, " + name + ".")
                checker = True
            elif year % 100 == 0 and year % 400 != 0:
                print("Unfortunately, that isn't a leap year, " 
                      + name + ".")
                checker = True
            else:
                print("That is a leap year!" 
                      + " Enjoy the extra day, " + name + ".")    
                checker = True
        else:
            print("Unfortunately, that isn't a leap year, " 
                      + name + ".")
            checker = True
    except ValueError:
        print("That is not a year! Please input a year, " + name + ".")
