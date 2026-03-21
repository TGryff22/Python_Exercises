weight = float(input("Enter your weight: "))

unit = input("Is that in (K)g or (L)bs? ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} was not a valid input")

