def format_number(num, fmt):
    return format(num, fmt)

result = format_number(145, 'o')
print("Formatted result (145, 'o'):", result)
print("Explanation: 'o' format converts the number to octal, so 145 becomes 221.")

radius = 84
pi = 3.14
area = pi * (radius ** 2)
print(f"Area of the pond: {area} square meters")

water_per_sqm = 1.4
total_water = int(area * water_per_sqm)
print(f"Total water in the pond: {total_water} liters")
