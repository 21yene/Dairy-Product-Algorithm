def fermentation(milk, milk_to_yogurt, yogurt_to_butter, butter_to_milk):
    yogurt = milk * milk_to_yogurt
    butter = yogurt / yogurt_to_butter
    return butter * butter_to_milk

milk = float(input("Enter the quantity of milk (in liters): "))
milk_to_yogurt = float(input("Enter the conversion rate from milk to yogurt: "))
yogurt_to_butter = float(input("Enter the conversion rate from yogurt to butter: "))
butter_to_yogurt = 1 / yogurt_to_butter
butter_to_milk = float(input("Enter the conversion rate from butter to milk: "))
days = int(input("Enter the number of days: "))

for day in range(1, days + 1):
    milk = fermentation(milk, milk_to_yogurt, yogurt_to_butter, butter_to_milk)

print(f"Total liters of milk fermented: {milk}")
