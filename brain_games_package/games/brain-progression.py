from random import randint
from typing import List




def do_random_arithmetic_row() -> List[int]:

    step_progression = randint(-15, 15)


    start_position = step_progression * randint(-4, 4)

    progression_row: List[int] = []

    for i in range(10):

        progression_row.append(start_position)

        start_position += step_progression

    return progression_row