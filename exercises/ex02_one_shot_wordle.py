"""EX 02 - One Shot Wordle."""

__author__ = "730238845"

# python -m exercises.ex02_one_shot_wordle

secret_word = str("python")
guess: str = input(f"What is your {len(secret_word)} letter guess? ")


while len(guess) != len(secret_word):
    guess = (str(input(f"That was not {len(secret_word)} letters! Try again: ")))

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
emoji: str = ("")

while i < len(secret_word):
    if guess[i] == secret_word[i]:
        emoji = emoji + GREEN_BOX
        i += 1
    else:
        alt_index: int = 0
        match: bool = False
        while alt_index < len(secret_word) and not match:
            if guess[i] == secret_word[alt_index]:
                match = True
            else:
                alt_index += 1
        if match is True:
            emoji = emoji + YELLOW_BOX
        else: 
            emoji = emoji + WHITE_BOX
        i += 1
print(emoji)

if len(guess) == len(secret_word):
    if guess == secret_word:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")