"""EX05 List Utility Functions."""


__author__ = 730238845


def only_evens(original_list: list[int]) -> list[int]:
    """A list of even ints."""
    result: list[int] = []
    for number in original_list:
        if number % 2 == 0:
            result.append(number)
    return result


def sub(original_list: list[int], start: int, end: int) -> list[int]:
    """A function for a subset list between the start and end index of a given list."""
    sub_result: list[int] = []
    if start < 0:
        start = 0
    i: int = start
    if end > len(original_list):
        end = len(original_list)
    elif len(original_list) == 0 or start > len(original_list) or end <= 0:
        return sub_result
    while i < end:
        sub_result.append(original_list[i])
        i += 1
    return sub_result


def concat(list1: list[int], list2: list[int]) -> list[int]: 
    """Combining all elements of the first followed by all elements of second list."""
    combined_list: list[int] = []
    list1_i: int = 0
    list2_i: int = 0
    while list1_i < len(list1): 
        combined_list.append(list1[list1_i])
        list1_i += 1
    while list2_i < len(list2):
        combined_list.append(list2[list2_i])
        list2_i += 1
    return combined_list