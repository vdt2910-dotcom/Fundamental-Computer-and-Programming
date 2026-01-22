def cabin():
    cabin_class = input("Nhập hạng cabin (Lux/A/B/C): ")

    if cabin_class.lower() == "lux":
        print("LUX: cabin ở tầng trên, có ban công.")
    elif cabin_class.lower() == "a":
        print("A: cabin ở trên boong xe, có cửa sổ.")
    elif cabin_class.lower() == "b":
        print("B: cabin không có cửa sổ, ở trên boong xe.")
    elif cabin_class.lower() == "c":
        print("C: cabin không có cửa sổ, ở dưới boong xe.")
    else:
        print("Hạng cabin không hợp lệ.")

cabin()