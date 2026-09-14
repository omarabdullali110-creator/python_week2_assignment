# Simple Bill Calculator
# Ask the user for inputs
price_input = input("Enter the price of one item: ")
quantity_input = input("Enter the quantity: ")

#Convert raw strings to float and int
price = float(price_input)
quantity = int(quantity_input)

#Calculate total
total = price * quantity

#Print summary using f-string formatting
print(f"\n{quantity} items at {price:.2f} each = {total:.2f}")