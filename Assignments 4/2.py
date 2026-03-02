color_code = input("Enter your color code here: ")

if color_code[0] == "#" and len(color_code) == 7:
    print("Correct")
else:
    print("Try again")