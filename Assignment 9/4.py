def average_score(filename):
    total = 0
    count = 0

    f = open(filename, "r")

    for line in f:
        parts = line.strip().split(",")  
        score = int(parts[1])            
        total += score
        count += 1

    f.close()

    return total / count

print(average_score("example.txt"))
