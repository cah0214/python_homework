def make_hangman(secret_word):
    guesses = []  # this is the "memory" the closure keeps

    def hangman_closure(letter):
        # add guess
        letter = letter.lower()
        guesses.append(letter)

        # build display word
        display = []
        for ch in secret_word.lower():
            if ch in guesses:
                display.append(ch)
            else:
                display.append("_")

        print("".join(display))

        # return True if all letters guessed
        return "_" not in display

    return hangman_closure


# ---------------- MAIN GAME ----------------
secret = input("Enter the secret word: ").strip()
game = make_hangman(secret)

while True:
    guess = input("Guess a letter: ").strip()
    if not guess:
        continue

    # if they type more than 1 letter, use the first one
    done = game(guess[0])

    if done:
        print("You got it!")
        break