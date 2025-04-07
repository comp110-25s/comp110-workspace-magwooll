"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        surviving_fish = []
        surviving_bears = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.fish = surviving_fish
        self.bears = surviving_bears
        return None

    def bears_eating(self):
        if len(self.fish) >= 5:
            for bear in self.bears:
                bear.eat(3)
            self.remove_fish(3 * len(self.bears))
        return None

    def check_hunger(self):
        surviving_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        num_fish = len(self.fish)
        num_offspring = (num_fish // 2) * 4
        idx = 0
        while idx < num_offspring:
            self.fish.append(Fish())
            idx += 1
        return None

    def repopulate_bears(self):
        num_bears = len(self.bears)
        num_offspring = num_bears // 2
        idx = 0
        while idx < num_offspring:
            self.bears.append(Bear())
            idx += 1
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        days = 0
        while days < 7:
            self.one_river_day()
            days += 1
        return None

    def remove_fish(self, amount: int) -> None:
        if amount >= len(self.fish):
            self.fish = []
        else:
            self.fish = self.fish[amount:]
