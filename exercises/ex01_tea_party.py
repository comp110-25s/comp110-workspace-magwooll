"""An exercise to plan a cozy tea party."""

__author__: str = "730472800"


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed for the amount of people."""
    return 2 * people


def treats(people: int) -> int:
    """Calculates the number of treats needed for the amount of people."""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of the tea bags and treats combined as a result of the number of people attending."""
    return 0.50 * tea_count + 0.75 * treat_count
