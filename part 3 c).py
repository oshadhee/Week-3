meal_cost = float(input("Enter the cost of the meal: $"))

satisfaction = int(input("Rate your satisfaction (1 = Totally satisfied, 2 = Satisfied, 3 = Dissatisfied): "))

if satisfaction == 1:
    tip_percent = 20
elif satisfaction == 2:
    tip_percent = 15
elif satisfaction == 3:
    tip_percent = 10
else:
    print("Invalid satisfaction rating. Please enter 1, 2, or 3.")
    tip_percent = 0

tip_amount = (tip_percent / 100) * meal_cost

if tip_percent > 0:
    print(f"Satisfaction: {satisfaction}")
    print(f"Tip: ${tip_amount:.2f}")