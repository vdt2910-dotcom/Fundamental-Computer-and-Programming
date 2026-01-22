def year():
    y = int(input("Enter a year: "))

    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        print("This is a leap year.")
    else:
        print("This is not a leap year.")

year()