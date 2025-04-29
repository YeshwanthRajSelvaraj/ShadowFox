# Task 1: Variables

pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

try:
    for = 4  # This will cause a SyntaxError because 'for' is a reserved keyword
except SyntaxError:
    print("'for' is a reserved keyword in Python. Using it as a variable name will cause a SyntaxError.")
    print("Instead, use a different name, like 'for_value':")
    for_value = 4
    print("for_value =", for_value)

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (%): "))
time = 3
simple_interest = (principal * rate * time) / 100
print(f"Simple Interest for 3 years: {simple_interest}")
