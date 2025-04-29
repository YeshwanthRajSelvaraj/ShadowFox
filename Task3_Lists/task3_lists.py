justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)

print("Number of members:", len(justice_league))

justice_league.extend(["Batgirl", "Nightwing"])
print("After adding Batgirl and Nightwing:", justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman leader:", justice_league)

aquaman_idx = justice_league.index("Aquaman")
flash_idx = justice_league.index("Flash")
if abs(aquaman_idx - flash_idx) == 1:
    justice_league.remove("Green Lantern")
    justice_league.insert(flash_idx, "Green Lantern")
print("After separating Aquaman and Flash:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team assembled by Superman:", justice_league)

justice_league.sort()
print("Sorted Justice League:", justice_league)
print("New leader (at index 0):", justice_league[0])
print("Bonus Prediction: The new leader is Cyborg, as 'C' comes first alphabetically.")
