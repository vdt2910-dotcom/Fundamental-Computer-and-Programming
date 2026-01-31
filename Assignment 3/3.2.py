INCH_TO_CM = 2.54

inch = float(input("Enter inches: "))

if inch < 0:
    print("Program finished")
else:
    cm = inch * INCH_TO_CM
    print("Centimeters:", cm)