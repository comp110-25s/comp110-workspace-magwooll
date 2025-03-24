"""An exercise utilizing dictionary functions."""

__author__ = "730472800"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary."""
    inverted_dict = {}
    for key, value in input:
        if value in inverted_dict:
            raise KeyError(f"Duplicate value '{value}' found during inversion.")
        inverted_dict[value] = key
    return inverted_dict


def count(values: list[str]) -> dict[str, int]:
    frequencies = {}
    for item in values:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies


def favorite_color(preferences: dict[str, str]) -> str:
    """Determines which color appears most frequently in a dictionary of favorite colors."""
    color_number = count(list(preferences))
    frequent_color = None
    max_count = 0
    for color in preferences:
        if color_number[color] > max_count:
            frequent_color = color
            max_count = color_number[color]
    return frequent_color


def bin_len(words: list[str]) -> dict[int, set]:
    result = {}
    for string in words:
        length = len(string)
        if length not in result:
            result[length] = {string}
        else:
            result[length].append(string)
    return result
