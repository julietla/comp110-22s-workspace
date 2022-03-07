"""Ex of Function Definitions"""

import sre_compile


def love (name: str) -> str:
    """Given a name as a parameter, return loving string."""
    return f"I love you {name}! "

    #return type has to be same type as specified in the signature

# >>> from lessons.love_functions import love
# >>> love("Holly")
# 'I love you Holly! '

# >>> result: str = love("Kris")
# >>> print(result)
# I love you Kris! 

# >>> player_name = "John"
# >>> love(player_name)
# 'I love you John! '

def spread_love (to: str, n: int) -> str:
    """Generates string that repeats a loving message in times."""
    love_note = str()
    i = 0
    while i < n: 
        love_note += love(to) + "\n"
        i += 1
    return love_note

def mystery(n: int) -> str:
    """A useless function. """
    i: int = 0
    while i < n:
        if i % 2 == 1:
            return "ooh"
        i += 1
    return "ahh"
    