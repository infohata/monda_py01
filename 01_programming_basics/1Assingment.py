fst_number = int(input("Give me the first number: "))
scnd_number = int(input("Give me the second number: "))
print(f"Alright, so we're working with {fst_number} & {scnd_number}")
operation = (input("""What type of equation are we going for?
+, -, *, or /: """))
if operation == "+":
    result = fst_number + scnd_number
    print(f"{fst_number} + {scnd_number} is  = {result}")
elif operation == "-":
    result = fst_number - scnd_number
    print(f"{fst_number} - {scnd_number} is = {result}")
elif operation == "*":
    result = fst_number * scnd_number
    print(f"{fst_number} * {scnd_number} is = {result}")
elif operation == "/":
    result = fst_number // scnd_number
    print(f"{fst_number} / {scnd_number} is = {result}")
else:
    print("Something went wrong, please try again!")