print("Welcome to the Tip Calculator!")
print("What was the total bill?")
bill = float(input())
tip = 0

while  tip not in [10, 12, 15]:
    print("What percentage tip would you like to give? 10, 12, or 15? ")
    tip = int(input())
    if tip not in [10, 12, 15]:
        print("❌ Please choose only 10, 12, or 15.")

print("How many people to split the bill?")
split = int(input())
total = bill + tip / 100 * bill
print(f'Your total bill with {tip}% tip is {total}')
print("<<<<<====================== ================= =======================>>>>")
splited_bill = total / split
print(f"Each person should pay: {round(splited_bill,2)}")
