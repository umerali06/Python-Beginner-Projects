foods = []
prizes = []
total= 0

while True:
  food = input("Enter the Food Item (Press q to exit): ")
  if food.lower() == "q":
    break
  else:
    try:
      prize = int(input("Enter the Prize Money: $"))
      foods.append(food)
      prizes.append(prize)
    except ValueError:
      print("Invalid input. Please enter a number for the prize money.")
  
print("\n-------Your CART-------\n")

for food in foods:
  print(food, end=" ")
for prize in prizes:
  total += prize
  
print()
print(f"Your total prize is ${total}")
  