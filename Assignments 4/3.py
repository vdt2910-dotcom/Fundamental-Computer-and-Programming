def number():
    text = input("Type your text here: ")
    
    total = 0
    for word in text.split():
        word = word.strip(".,!?")
        if word.isdigit():
            total += int(word)

    print("Tổng số trong văn bản là:", total)
    return total

number()