weight = float(input("Weight: "))
units = input("(K)g or (L)bs: ")
if units == "K" or units == "k":
    weight *= 2.20462
    print("Your weight is: " + str(weight) + " Lbs")
    exit()
else:
    weight *= 0.453592
    print("Your weight is: " + str(weight) + "Kg")
    exit()

