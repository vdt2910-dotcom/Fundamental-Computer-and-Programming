def fish():
    fish_length = float(input("Nhập chiều dài con cá (cm): "))

    limit = 42

    if fish_length >= limit:
        print("Con cá đạt kích thước cho phép.")
    else:
        short = limit - fish_length
        print(f"Khi thả cá về hồ, nó vẫn còn thiếu {short} cm so với kích thước cho phép.")
fish()