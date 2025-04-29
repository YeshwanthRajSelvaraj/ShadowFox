# Task 2 (Intermediate): Hangman
import random

words = [
    ("python", "A popular programming language"),
    ("coding", "The act of writing computer programs"),
    ("shadowfox", "Your internship organization"),
    ("internship", "A temporary position for gaining experience"),
    ("github", "A platform for version control")
]

word, hint = random.choice(words)
word_letters = set(word)
guessed_letters = set()
max_attempts = 10
attempts_left = max_attempts

stages = [
    "  _____\n  |   |\n      |\n      |\n      |\n=========",
    "  _____\n  |   |\n  O   |\n      |\n      |\n=========",
    "  _____\n  |   |\n  O   |\n  |   |\n      |\n=========",
    "  _____\n  |   |\n  O   |\n /|   |\n      |\n=========",
    "  _____\n  |   |\n  O   |\n /|\\  |\n      |\n=========",
    "  _____\n  |   |\n  O   |\n /|\\  |\n /    |\n=========",
    "  _____\n  |   |\n  O   |\n /|\\  |\n / \\  |\n========="
]

print("Welcome to Hangman!")
print(f"Hint: {hint}")
while attempts_left > 0 and word_letters != guessed_letters:

    print("\nAttempts left:", attempts_left)
    print(stages[max_attempts - attempts_left])
    display = "".join(letter if letter in guessed_letters else "_" for letter in word)
    print("Word:", " ".join(display))
    
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.add(guess)
    if guess in word_letters:
        print("Good guess!")
    else:
        print("Wrong guess!")
        attempts_left -= 1
      
if word_letters == guessed_letters:
    print("\nCongratulations! You guessed the word:", word)
else:
    print(stages[-1])
    print("\nGame Over! The word was:", word)
