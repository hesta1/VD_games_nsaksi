import random
import math

ROUNDS = 3

def get_question_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    answer = math.gcd(num1, num2)
    return question, answer

def main():
    print("VD-gcd")
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    for _ in range(ROUNDS):
        question, correct_answer = get_question_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
