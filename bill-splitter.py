print("Bill Split Calculator")
bill = float(input("Enter Bill Amount: $"))
tip = float(input("what percentage tip would you like to give?: "))
tip_amount = (tip / 100) * bill
bill_amount = bill + tip_amount
print(f"Total (including tip): ${bill_amount:.2f}")
answer = input("Would you like to split the bill? (yes/no): ")
if answer.lower() == "yes":
    amount_per_person = int(input("How many people are splitting the bill?: "))
    split = bill_amount / amount_per_person
    print(f"Each person pays: ${split:.2f}")