# Excercise 2: Shopping cart program

item = input("What would you like to purchase?: ")
price = float(input("How much does the item cost?: "))
quantity = int(input("How many items would you like to purchase?: "))
total_cost = price * quantity

print (f"You have purchased {quantity} {item}(s) for a total of ${total_cost: .2f}!")
# .2f is used to format the total cost to 2 decimal places with automatic rounding, which is common for currency.
