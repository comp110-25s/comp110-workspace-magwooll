"""A word guessing game."""

__author__ = "730472800"


def contains_char(word: str, character: str) -> bool:
    """Determines if a single character is found at any index of the first string."""
    assert len(character) == 1, f"len('{character}') is not 1"
    index = 0
    while index < len(word):
        if word[index] == character:
            return True
        index += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Creates a string of emojis in response to a guess and secret string of equal lengths which represents how each character in the guess matches the secret word."""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    result = ""
    index = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


def input_guess(expected_length: int) -> str:
    """Prompts the user of the program to provide a guess of an expected length. The function continues prompting for a guess until it is of the expecting length."""
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns_left = 6
    turn_number = 1
    won = False
    while turn_number <= turns_left and not won:
        print(f"===Turn {turn_number}/{turns_left} ===")
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)
        if guess == secret:
            won = True
        else:
            turn_number += 1
    if won:
        print(f"You won in {turn_number-1}/{turns_left} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
