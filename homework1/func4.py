def shut_down(s):
    if s == "yes":
        print("Shutting down")
    elif s == "no":
        print("Shutdown aborted")
    else:
        print("Sorry")


shut_down("yes")
shut_down("no")
shut_down("else")
