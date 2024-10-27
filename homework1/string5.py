def bracket(line):
    if "(" in line and ")" in line[line.index("(") :]:
        print("( and ) are correct")
    if "[" in line and "]" in line[line.index("]") :]:
        print("[ and ] are correct")
    else:
        print("position is incorrect")


lin = input("Please enter sentence: ")
bracket(lin)
