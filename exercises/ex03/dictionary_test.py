"""An exercise utilizing unit test functions."""

__author__ = "730472800"

import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_use_1() -> None:
    """Tests use case for invert function using unique keys and values of a dictionary."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_2() -> None:
    """Tests another use case for invert function using different unique keys and values."""
    assert invert({"apple": "cat", "orange": "dog"}) == {
        "cat": "apple",
        "dog": "orange",
    }


def test_invert_edge_1() -> None:
    """Tests edge case for invert function with an empty dictionary."""
    assert invert({}) == {}


with pytest.raises(KeyError):
    input = {"kris": "jordan", "michael": "jordan"}
    invert(input)


def test_count_use_1() -> None:
    """Tests a use case for count function using a list where items are repeated."""
    assert count(["dog", "rabbit", "cat", "dog", "dog"]) == {
        "cat": 1,
        "rabbit": 1,
        "dog": 3,
    }


def test_count_use_2() -> None:
    """Tests another use case for count function using list of all different items."""
    assert count(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}


def test_count_edge() -> None:
    """Tests edge case for count function using an empty list."""
    assert count([]) == {}


def test_favorite_color_use_1() -> None:
    """Tests use case for favorite_color using a dictionary including one most frequent color."""
    assert (
        favorite_color({"Maggie": "blue", "Blair": "red", "Sophie": "blue"}) == "blue"
    )


def test_favorite_color_use_2() -> None:
    """Tests another use case for favorite_color using a dictionary including two most frequent colors."""
    assert favorite_color({"Maggie": "blue", "Sophie": "red"}) == "blue"


def test_favorite_color_edge() -> None:
    """Tests an edge case for favorite_color using an empty dictionary"""
    assert favorite_color({}) == "None"


def test_bin_len_use_1() -> None:
    """Tests a use case for bin_len using strings with different lengths."""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_2() -> None:
    """Tests a use case for bin_len using strings of all unique lengths."""
    assert bin_len(["Maggie", "ice", "tree"]) == {
        3: {"ice"},
        4: {"tree"},
        6: {"Maggie"},
    }


def test_bin_len_edge() -> None:
    """Tests an edge case for bin_len using an empty list."""
    assert bin_len([]) == {}
