import random

ROUNDS = 3

def get_question_answer():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(["+", "-", "*"])

    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2

    question = f"{num1} {operation} {num2}"
    return question, answer

def main():
    print("VD-calc")
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

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

