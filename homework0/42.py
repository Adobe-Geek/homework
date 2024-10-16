dist = float(input("Enter distance between A and B: "))
v_rab = float(input("Enter speed of rabbit: "))
v_turt = float(input("Enter speed of turtle: "))

t = dist / (v_rab + v_turt)
print("Distance from B: ", t * v_turt)
