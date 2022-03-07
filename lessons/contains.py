"""Ex of function that searches through list."""

# Defines function named contains
# 2 parameters:
#   1. needle - strong we are searching for
#   2. haystack - list we are searching through


def contains(needle: str, haystack: list[str]) -> bool: 
    # Algorithm
    # For each item in haystack
    #   Test if it is equal to needle
    #       If so, return True
    for item in haystack:
        if item == needle:
            return True
#   After testing all items, return False, because not found
# Returns true if needle in haystack, false otherwise
    return False


# >>> from lessons.contains import contains
# >>> contains("Kevin Bacon", ["Kanye West", "Kevin Bacon", "Pete Davidson"])
# True


def main() -> None: 
    print(contains("Kevin Bacon", ["Kanye West", "Kevin Bacon", "Pete Davidson"]))


if __name__ == "__main__":
    main()
else:
    print(__name__)