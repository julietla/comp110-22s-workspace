"""Examples of importing Python."""


from lessons import helpers
#    package        module


from lessons import helpers as hp
# Abbreviation for helpers


from lessons.helpers import powerful
# Import names defined globally in module


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {helpers.THE_ANSWER}")


if __name__ == "__main__":
    main()
else: 
    # It is not idiomatic to have else branch
    print(f"helpers.py was imported: {__name__}")