from collections.abc import Sequence
from random import randint, choice


# task 9-13 dice
class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll_die(self):
        rand_number = randint(1, self.num_sides)
        return rand_number

    def show_roll_die(self):
        print(f"The dice showed the number: {self.roll_die()}")

    def show_dice_info(self):
        print(f"\nThis dice has {self.num_sides} sides")


die_0 = Die()
die_0.show_dice_info()
die_0.show_roll_die()

die_1 = Die(10)
die_1.show_dice_info()
die_1.show_roll_die()

dice_rolls_number = 10

die_2 = Die(20)
die_2.show_dice_info()

for i in range(0, dice_rolls_number):
    die_2.show_roll_die()


# task 9-14 lottery
class Lottery:
    """Implementing a simple lottery"""

    DEFAULT_POOL = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e")

    def __init__(
        self,
        draw_count=4,
        pool: Sequence | None = None,
    ):
        if draw_count <= 0:
            raise ValueError("draw_count must be positive")

        self.draw_count = draw_count
        self.pool = pool if pool is not None else self.DEFAULT_POOL

        if not self.pool:
            raise ValueError("pool cannot be empty")

    def run_lottery(self):
        return [choice(self.pool) for _ in range(self.draw_count)]

    def show_result(self):
        result = self.run_lottery()
        result_str = " ".join(map(str, result))
        return f"Winning combination: {result_str}"


lotto_0 = Lottery()
print(lotto_0.show_result())

lotto_1 = Lottery(6)
print(lotto_1.show_result())


# task 9-15 lottery analysis
def lottery_analysis(ticket):
    loto = Lottery()
    count = 0
    active = True

    while active:
        result_str = "".join(map(str, loto.run_lottery()))
        count += 1

        if result_str == ticket:
            active = False

    return f"\nIt took {count} tries to win."


my_ticket = "87e3"
how_many = lottery_analysis(my_ticket)
print(how_many)
