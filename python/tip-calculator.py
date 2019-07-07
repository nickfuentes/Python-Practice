total_amount = input("Enter total amount: ")
tip_percentage = input("Enter the tip percentage amount: ")

result = round(float(total_amount) * (float(tip_percentage) / 100), 2)

print(f"The total tip for the bill is ${result}!")
