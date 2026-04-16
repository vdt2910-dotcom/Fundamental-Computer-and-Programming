def get_lines_with_keyword(file_name, word):
    result = []
    with open(file_name, "r") as f:
        line_num = 1
        for line in f:
            if word in line:
                result.append(line_num)
            line_num += 1
        return result
print(get_lines_with_keyword("example.txt", "apple"))