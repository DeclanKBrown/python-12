import random
from words import words
import string


def getValidWord(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word


def hangman():
    word = getValidWord(words)
    wordLetters = set(word)
    alphabet = set(string.ascii_lowercase)
    usedLetters = set()

    lives = 6

    while len(wordLetters) > 0 and lives != 0:
        print(f"You have {lives} lives")
        print("You have used these letters: ", " ".join(usedLetters))

        wordList = [letter if letter in usedLetters else "-" for letter in word]
        print("Current word: ", " ".join(wordList))

        userLetter = input("Guess a letter: ").lower()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives -= 1

        elif userLetter in usedLetters:
            print("Letter already used. Try again!")

        else:
            print("Invalid character. Try again")

    if lives == 0:
        print(f"You Lost, The word was {word}")
        return

    print(f"You win! The word was {word}")


hangman()
