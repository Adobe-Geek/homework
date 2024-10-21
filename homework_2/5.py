class Bracket:
    def __init__(self, line):
        self.line = line

    def validity(self):
        temp = []
        for el in self.line:
            if el == "(":
                temp.append(el)
                if ")" in self.line[self.line.index("(") :]:
                    temp.remove("(")
            elif el == "{":
                temp.append(el)
                if "}" in self.line[self.line.index("{") :]:
                    temp.remove("{")
            elif el == "[":
                temp.append(el)
                if "]" in self.line[self.line.index("[") :]:
                    temp.remove("[")
        if len(temp) == 0:
            return "Valid"
        else:
            return "Invalid"


bracket = Bracket("()[]{}")
print(bracket.validity())
