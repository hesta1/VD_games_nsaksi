import random


ROUNDS_COUNT = 3


def is_even(number: int) -> bool:
    return number % 2 == 0


def main() -> None:
    print("Welcome to the VD-games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0

    while correct_answers < ROUNDS_COUNT:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ")

        correct_answer = "yes" if is_even(number) else "no"

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")
        correct_answers += 1

    print(f"Congratulations, {name}!")

