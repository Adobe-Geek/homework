def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        print(abs(num))
    else:
        print("Nope")


distance_from_zero(-5.6)
distance_from_zero("What?")
