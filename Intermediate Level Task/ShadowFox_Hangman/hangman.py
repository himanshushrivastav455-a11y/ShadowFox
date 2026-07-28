import random

# Words with hints
words = {
    "PYTHON": "Programming Language",
    "ELEPHANT": "Largest land animal",
    "TAJMAHAL": "Famous monument in India",
    "JAVASCRIPT": "Web Programming Language",
    "COMPUTER": "Electronic Machine",
    "KEYBOARD": "Used for typing",
    "MOUNTAIN": "Very high landform",
    "FOOTBALL": "Popular outdoor sport",
    "NOTEBOOK": "Used for writing notes",
    "INTERNET": "Global network"
}

# Hangman stages
hangman = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
'''
]


def play_game():
    word = random.choice(list(words.keys()))
    hint = words[word]

    guessed = []
    wrong = 0
    max_wrong = len(hangman) - 1

    print("=" * 45)
    print("🎮 WELCOME TO HANGMAN GAME 🎮")
    print("=" * 45)
    print(f"💡 Hint: {hint}")

    while True:

        # Display guessed word
        display = ""
        complete = True

        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "
                complete = False

        print("\nWord:", display)
        print(hangman[wrong])

        if complete:
            print("🎉 Congratulations! You guessed the word:", word)
            break

        guess = input("Enter a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Enter only one alphabet.")
            continue

        if guess in guessed:
            print("⚠ You already guessed that letter.")
            continue

        guessed.append(guess)

        if guess in word:
            print("✅ Correct Guess!")
        else:
            wrong += 1
            print("❌ Wrong Guess!")

        print("Guessed Letters:", " ".join(guessed))

        if wrong == max_wrong:
            print(hangman[wrong])
            print("💀 Game Over!")
            print("The correct word was:", word)
            break


# Main Program
while True:
    play_game()

    choice = input("\nDo you want to play again? (Y/N): ").upper()
    if choice != "Y":
        print("👋 Thanks for playing Hangman!")
        break