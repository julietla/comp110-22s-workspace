"""Another take at Wordle."""

__author__ = "730238845"


def contains_char(word: str, character: str) -> bool:
    """Used to find whether it is True/False that the characters match when given two strings."""
    assert len(character) == 1
    i: int = 0
    match: bool = False
    while i < len(word) and match is False:
        if word[i] == character:
            match = True
        i += 1
    return match


def emojified(guess: str, secret: str) -> str:
    """Assigning emojis to the True/False values."""
    assert len(guess) == len(secret)
    i: int = 0
    emoji: str = ("")
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while i < len(guess):
        if contains_char(secret, guess[i]):
            if guess[i] == secret[i]:
                emoji = emoji + GREEN_BOX
            else:
                emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
        i += 1
    return emoji


def input_guess(length: int) -> str:
    """Determining whether the length of guess is the expected length."""
    guess = str(input(f"Enter a {length} character word: "))
    while len(guess) != length:
        guess = (str(input(f"That wasn't {length} chars! Try again: ")))
    return guess


def main() -> None:
    """Putting everything together."""
    secret = str("codes")
    turn: int = 1
    is_game_won = False
    while turn <= 6 and is_game_won is False:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            is_game_won = True
            print(f"You won in {turn}/6 turns! ")
        turn += 1
        if turn > 6:
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()