def phone_protect():
    while True :
        sdt = input(" Pls enteer your phone number: ")
        if sdt.startswith("+84") or sdt.startswith("0"):
            anonymous = "#" * (len(sdt)-3) + sdt[7:] 
            return anonymous


print(phone_protect())
