def find_number():
    Paragraph = input(" Pls enter whaterver you want: ") 
    p1 = Paragraph.split()
    numbers = []
    for i in p1:
        clean = i.strip(".,")
        if clean.isdigit():
            numbers.append(int(clean))
    
    tong = sum(numbers) 
    return tong

print(find_number())
