print("Welcome ot the tip calculator.\n")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give?"))
total_bill = bill + float(bill * tip_percent) / 100
splits = int(input("How many people to split the bill?"))
ind_bill = round((total_bill / splits),2)
print(f"Each person should pay: {ind_bill}")

