def count_lines(filename):
    count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() != "":
                count += 1
                return count
file_name = "example.txt"
print(count_lines(file_name))