import random

words = ["apple", "banana", "grape", "orange", "melon"]
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6
display_word = ["_"] * len(word)

while incorrect_guesses < max_incorrect and "_" in display_word:
    print("\nWord: " + " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Guess a letter: ").lower()
    
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                display_word[i] = guess
        print("Correct!")
    else:
        incorrect_guesses += 1
        print(f"Incorrect! You have {max_incorrect - incorrect_guesses} guesses left.")

if "_" not in display_word:
    print(f"\nCongratulations! You guessed the word: {word}")
else:
    print(f"\nGame over! The word was: {word}")
