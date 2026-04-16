def convert_to_uppercase(input_file):
    f = open(input_file, "r")
    content = f.read()
    f.close()

    content = content.upper()

    out = open("output.txt", "w")
    out.write(content)
    out.close()



convert_to_uppercase("example.txt")