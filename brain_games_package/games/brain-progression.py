from random import randint
from typing import List, Tuple




def do_random_arithmetic_row() -> List[int]:

    step_progression = randint(-15, 15)


    start_position = step_progression * randint(-4, 4)

    progression_row: List[int] = []

    for i in range(10):

        progression_row.append(start_position)

        start_position += step_progression

    return progression_row


def do_question_answer(progression_row: List[int]) -> Tuple[str, str]:

    answer_position = randint(0, len(progression_row) - 1)
    answer = progression_row[answer_position]

    progression_row[answer_position] = '..'
    question = ' '.join(map(str, progression_row))

    return(answer, question)



row = do_random_arithmetic_row()
print(row)
print(do_question_answer(row))