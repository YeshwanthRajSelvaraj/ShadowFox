import random

# Simulate 20 dice rolls
rolls = [random.randint(1, 6) for _ in range(20)]
count_6 = rolls.count(6)
count_1 = rolls.count(1)
count_two_6s = sum(1 for i in range(len(rolls) - 1) if rolls[i] == 6 and rolls[i + 1] == 6)

print("Dice rolls:", rolls)
print(f"Number of 6s: {count_6}")
print(f"Number of 1s: {count_1}")
print(f"Number of two 6s in a row: {count_two_6s}")

# Jumping jacks simulation
total_jacks = 0
for i in range(10):
    total_jacks += 10
    print(f"\nCompleted {total_jacks} jumping jacks")
    
    if total_jacks == 100:
        print("Congratulations! You completed the workout")
        break

    tired = input("Are you tired? (yes/y or no/n): ").lower()
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {total_jacks} jumping jacks")
            break
    else:
        remaining = 100 - total_jacks
        print(f"{remaining} jumping jacks remaining")
