number_of_quarters = 0
number_of_dimes = 0
number_of_nickels = 0
number_of_pennies = 0
amount = int(input("Enter the amount of change: "))
while amount > 0:
  if amount >= 25:
    amount -= 25
    number_of_quarters += 1
  if amount >= 10:
    amount -= 10
    number_of_dimes += 1
  if amount >= 5:
    amount -= 5
    number_of_nickels += 1
  if amount >= 1:
    amount -= 1
    number_of_pennies += 1

if number_of_quarters > 0:
  if number_of_quarters == 1:
    print(str(number_of_quarters) + " quarter")
  else:
    print(str(number_of_quarters) + " quarters")

if number_of_dimes > 0:
  if number_of_dimes == 1:
    print(str(number_of_dimes) + " dime")
  else:
    print(str(number_of_dimes) + " dimes")
if number_of_nickels > 0:
  if number_of_nickels == 1:
    print(str(number_of_nickels) + " nickel")
  else:
    print(str(number_of_nickels) + " nickels")

if number_of_pennies > 0:
  if number_of_pennies == 1:
    print(str(number_of_pennies) + " penny")
  else:
    print(str(number_of_pennies) + " pennies")
print("Total number of coins: " + str(number_of_quarters + number_of_dimes +
                                      number_of_nickels + number_of_pennies))
