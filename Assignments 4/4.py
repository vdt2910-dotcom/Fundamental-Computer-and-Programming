phone_number_list = []

while True:
    phone = input("Type your phone number here: ")

    if phone.startswith("0") or phone.startswith("+84"):
        phone_number_list.append(phone)
        
        anonymous = "#" * (len(phone) - 3) + phone[-3:]
        print("Your phone number is anonymized:", anonymous)
        break
    else:
        print("Try again")
        