height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)
print(f"Your BMI: {bmi:.2f}")
if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")

countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}
city = input("\nEnter a city name: ")
country_found = None
for country, cities in countries.items():
    if city in cities:
        country_found = country
        break
if country_found:
    print(f"{city} is in {country_found}")
else:
    print(f"{city} is not in the given list")

city1 = input("\nEnter the first city: ")
city2 = input("Enter the second city: ")
country1, country2 = None, None
for country, cities in countries.items():
    if city1 in cities:
        country1 = country
    if city2 in cities:
        country2 = country
if country1 and country2 and country1 == country2:
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to the same country")
