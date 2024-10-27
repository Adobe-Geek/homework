def count_lines(name):
    hand = open(name, "r")
    lines = hand.readlines()
    return len(lines)


def count_chars(name):
    hand = open(name, "r")
    chars = hand.read()
    return len(chars)


def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"Lines: {lines}, Characters: {chars}")


if __name__ == "__main__":
    test("mymod.py")
