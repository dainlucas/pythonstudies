#Variables exercise:
pacient_name = "John Smith"
pacient_age = 20
new_patient = False

#Type Conversion exercise:
first_number = float(input("First Number: "))
second_number = float(input("Second Number: "))
sum = first_number + second_number
print("Sum is: " + str(sum))

#Unit Conversion exercise:
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
