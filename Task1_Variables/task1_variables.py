# Task 1: Variables

pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))
print("\nNote: 'for' is a reserved keyword in Python and cannot be used as a variable name.")
print("Instead, use a different name, like 'for_value':")
for_value = 4
print("for_value =", for_value)

# Getting user input
try:
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest (%): "))
    time = 3
    simple_interest = (principal * rate * time) / 100
    print(f"Simple Interest for 3 years: {simple_interest}")
except ValueError:
    print("Please enter valid numeric values for principal and rate.")
