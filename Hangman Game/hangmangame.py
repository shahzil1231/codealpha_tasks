import random

# Predefined list of words
words = ["apple", "house", "chair", "table", "phone"]

# Pick a random word
word = random.choice(words)
word_letters = list(word)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman!")
print("Guess the word:", " ".join(guessed))

# Game loop
while attempts > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_letters:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    print("Word:", " ".join(guessed))
    print("Guessed letters:", ", ".join(guessed_letters))

# Final result
if "_" not in guessed:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)
