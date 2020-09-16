"""
pennies weigh 2.50 grams
nickels weigh 5.000 grams
dimes weigh 2.268 grams 
a quarter weighs 5.670 grams

"""

# Allows to count their coins by weighing them and arriving at a total

penny_amount = float(input("Enter the weight of your pennies in (G)rams: "))
nickel_amount = float(input("Enter the weight of your nickels in (G)rams: "))
dime_amount = float(input("Enter the weight of your dimes in (G)rams: "))
quarter_amount = float(input("Enter the weight of your quarters in (G)rams: "))

one_penny = 2.50
one_nickel = 5.00
one_dime = 2.2268
one_quarter = 5.670

total = (penny_amount / one_penny) + (nickel_amount / one_nickel) + (dime_amount / one_dime) + (quarter_amount / one_quarter)


print(f"""

	With {penny_amount} grams of pennies, {nickel_amount} grams of nickels, {dime_amount} grams of dimes and {quarter_amount} grams of quarters, you total is approx ${round(total, 2)} 

	""")