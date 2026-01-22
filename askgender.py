print("Hello, my lovely teacher!")

def check_hemo(sex, hemo):
    sex = sex.lower()

    if sex == "males":
        if 134 <= hemo <= 167:
            print("So great")
        else:
            print("Need to pay more attention to our health.")
    elif sex == "females":
        if 117 <= hemo <= 155:
            print("So great")
        else:
            print("Need to pay more attention to our health.")
    else:
        print("Invalid input.")

sex = input("Are you Males/Females: ")
hemo = float(input("Enter hemoglobin value (g/l): "))

check_hemo(sex, hemo)

