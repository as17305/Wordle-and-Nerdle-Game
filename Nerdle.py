import random
first = random.randint(1, 9)
functions = ["+", "-", "*", "/"]
function = random.randint(0, 3)
second = random.randint(1, first)
if function == 0:
  result = first + second
elif function == 1:
  result = first - second
elif function == 2:
  result = first * second
elif function == 3:
  result = first // second
first = str(first)
second = str(second)
result = str(result)
secretCalculation = first + functions[function] + second + "=" + result
print("Round the result of the numbers down")
print("The result is greater than or equal to zero")
print(f"The calculation length is {len(secretCalculation)}")
print("Guess it in six tries.")
for i in range(6):
	guess = input(f"Guess #{i + 1} the equation. Do not put spaces between characters.\n")
	if guess == secretCalculation:
		print("You Win")
		break
	x = guess
	if "+" in x:
		x = x.split("+")
	elif "-" in x:
		x = x.split("-")
	elif "/" in x:
		x = x.split("/")
	elif "*" in x:
		x = x.split("*")
	z = str(x[1])
	y = z.split("=")
	split = x + y
	split.pop(1)
	if not(int(split[0]) + int(split[1]) == int(split[-1])) and not(int(split[0]) - int(split[1]) == int(split[-1])) and not(int(split[0]) * int(split[1]) == int(split[-1])) and not(int(split[0]) // int(split[1]) == int(split[-1])):
		print("It is not a true equation")
	elif  "=" not in guess:
		print("It is not a true equation")
	elif not(len(guess) == len(secretCalculation)):
		print("The length of your guess do not match the length of the answer.")
	else:
		for j in range(len(secretCalculation)):
			check = list(secretCalculation)
			guess = list(guess)
			if guess[j] == check[j]:
				print(f"{guess[j]} is in the equation and is in the right spot")
			elif guess[j] in check:
				print(f"{guess[j]} is in the equation but is in the wrong spot")
			else:
				print(f"{guess[j]} is not in the equation")
	if i == 5:
		print(f"Here's the (not so) secret equation you are trying to guess: {secretCalculation}")
		print("You Lose")