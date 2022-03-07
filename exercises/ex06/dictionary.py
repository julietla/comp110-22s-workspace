"""Dictionaries!"""


__author__ = "730238845"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Function that inverts the key and value in a dictionary."""
    result: dict[str, str] = {}
    for key in dictionary:
        if dictionary[key] in result:
            raise KeyError("Error!")
        else:
            result[dictionary[key]] = key
    return result


def favorite_color(color_dict: dict[str, str]) -> str:
    """Function that finds the most frequently occuring color in a dictionary."""
    most_freq_color: str = ""
    new_dict: dict[str, int] = {}
    for key in color_dict:
        color = color_dict[key]
        if color in new_dict:
            new_dict[color] += 1
        else:
            new_dict[color] = 1
    i = 0
    for color in new_dict:
        if new_dict[color] > i:
            i = new_dict[color]
            most_freq_color = color
    return most_freq_color


def count(count_list: list[str]) -> dict[str, int]:
    """Function that finds the number of times something is included in a list."""
    count_dict: dict[str, int] = {}
    for key in count_list:
        if key in count_dict:
            count_dict[key] += 1
        else:
            count_dict[key] = 1
    return count_dict