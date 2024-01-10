print("The Love Calculator is calculating your score...")
name1 = input("Enter your name: ") # What is your name?
name2 = input("Enter their name: ") # What is their name?

# combine names
combined_names = name1 + name2
# convert into lowercase
lower_names = combined_names.lower()

# first digit
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

# second digit
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

# concatenation
score = int(str(first_digit) + str(second_digit))

# if statements
if (score < 10)  or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
