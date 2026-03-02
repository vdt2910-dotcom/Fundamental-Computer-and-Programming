def course_codes():
    clss = input("Enter your course code: ")

    if clss[:2].isupper():
        return True
    else:
        return False

print(course_codes())