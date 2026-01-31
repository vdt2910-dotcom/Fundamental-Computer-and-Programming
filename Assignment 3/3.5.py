def get_middle_char(text):
    mid = len(text) // 2

    if len(text) % 2 == 0:
        return text[mid - 1: mid + 1]
    else:
        return text[mid]

print("Middle of 'Python':", get_middle_char("Python"))
print("Middle of 'Rules':", get_middle_char("Rules"))