dist = float(input("Enter distance between A and B: "))
v_fly = float(input("Enter speed of fly: "))
v_cycler = float(input("Enter speed of bicycler: "))

t = dist / v_cycler
print("Fly will cover: ", t * v_fly)
