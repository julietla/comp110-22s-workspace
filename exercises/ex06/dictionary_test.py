"""Dictionary test!"""


__author__ = "730238845"


from dictionary import invert, favorite_color, count


# invert
def test_invert_empty() -> None:
    """Edge: testing invert function with empty dictionary."""
    dictionary: dict[str, str] = {}
    assert invert(dictionary) == {}


def test_invert_use_1() -> None:
    """Use: testing invert with a dictionary."""
    dictionary: dict[str, str] = {'pig': 'pink', 'goat': 'gray', 'cow': 'black and white', 'horse': 'brown'}
    assert invert(dictionary) == {'pink': 'pig', 'gray': 'goat', 'black and white': 'cow', 'brown': 'horse'}


def test_invert_use_2() -> None:
    """Use: testing invert with a dictionary."""
    dictionary: dict[str, str] = {'wet': 'rainy', 'dry': 'sun', 'in-the-middle': 'cloudy'}
    assert invert(dictionary) == {'rainy': 'wet', 'sun': 'dry', 'cloudy': 'in-the-middle'}


# fav color
def test_favorite_color_empty() -> None:
    """Edge: testing invert function with empty dictionary."""
    color_dict: dict[str, str] = {}
    assert favorite_color(color_dict) == ""


def test_favorite_color_use_1() -> None:
    """Use: testing favorite_color with a dictionary."""
    color_dict: dict[str, str] = {'John': 'pink', 'Amy': 'purple', 'Craig': 'orange'}
    assert favorite_color(color_dict) == "pink"


def test_favorite_color_use_2() -> None:
    """Use: testing favorite_color with a dictionary when the most frequent value is shared by two keys."""
    color_dict: dict[str, str] = {'Jack': 'green', 'Alex': 'green', 'Mary': 'yellow', 'Jane': 'yellow'}
    assert favorite_color(color_dict) == "green"


def test_favorite_color_use_3() -> None:
    """Use: testing favorite_color with a dictionary when one appears to be most frequent but followed by a more frequent color."""
    color_dict: dict[str, str] = {'Jackie': 'yellow', 'Alan': 'yellow', 'Marie': 'green', 'James': 'green', 'Amanda': 'green'}
    assert favorite_color(color_dict) == "green"


def test_favorite_color_use_3_2() -> None:
    """Use: testing favorite_color with a dictionary when one appears to be most frequent but followed by a more frequent color."""
    color_dict: dict[str, str] = {'Jackie': 'green', 'Alan': 'green', 'Marie': 'green', 'James': 'yellow', 'Amanda': 'yellow'}
    assert favorite_color(color_dict) == "green"


def test_favorite_color_use_4() -> None:
    """Use: testing favorite_color with a dictionary when none of the values are the most frequent."""
    color_dict: dict[str, str] = {'Cullen': 'yellow', 'Zachary': 'green', 'Grace': 'pink'}
    assert favorite_color(color_dict) == "yellow"


# count
def test_count_empty() -> None:
    """Edge: testing count function with empty list."""
    count_list: list[str] = []
    assert count(count_list) == {}


def test_count_use_1() -> None:
    """Use: testing count function making a list into a dictionary."""
    count_list: list[str] = ['a', 'a', 'b', 'c', 'c', 'c']
    assert count(count_list) == {'a': 2, 'b': 1, 'c': 3}


def test_count_use_2() -> None:
    """Use: testing count function making a list into a dictionary."""
    count_list: list[str] = ['hi', 'hi', 'hi', 'hey', 'hello']
    assert count(count_list) == {'hi': 3, 'hey': 1, 'hello': 1}