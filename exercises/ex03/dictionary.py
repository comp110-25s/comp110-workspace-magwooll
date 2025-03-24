"""An exercise utilizing dictionary functions."""

__author__ = "730472800"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary."""
    inverted_dict = {}
    for key in input:
        if input[key] in inverted_dict:
            raise KeyError(f"Duplicate value '{input[key]}' found during inversion.")
        inverted_dict[input[key]] = key
    return inverted_dict


def count(values: list[str]) -> dict[str, int]:
    """Creates a dictionary from a given list where keys are items in the list and values are the count of the associated items."""
    frequencies = {}
    for item in values:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies


def favorite_color(preferences: dict[str, str]) -> str:
    """Determines which color appears most frequently in a dictionary of names and favorite colors."""
    color_number = {}
    for name in preferences:
        if preferences[name] not in color_number:
            color_number[preferences[name]] = 1
        else:
            color_number[preferences[name]] += 1
    frequent_color = "None"
    total_count = 0
    for key in color_number:
        if color_number[key] > total_count:
            frequent_color = key
            total_count = color_number[key]
    return frequent_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    result = {}
    for item in words:
        length = len(item)
        if length in result:
            result[length].add(item)
        else:
            result[length] = {item}
    return result
