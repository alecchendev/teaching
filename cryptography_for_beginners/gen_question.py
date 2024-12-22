import argparse
from dataclasses import dataclass
from typing import List
import random

@dataclass
class Choice:
    choice: str
    correct: bool

class Question:
    def __init__(self, question: str, choices: List[Choice]):
        assert sum([choice.correct for choice in choices]) == 1, "There must be exactly one correct choice."
        self.question = question
        self.choices = choices

    def __str__(self):
        choices_str = "\n".join([f"{choice.choice}" for choice in self.choices])
        correct_choice = [choice.choice for choice in self.choices if choice.correct][0]
        return f"{self.question}\n\n{choices_str}\n\nCorrect: {correct_choice}"

def binary_to_decimal() -> Question:
    number = random.randint(10, 32)
    binary = bin(number)[2:]
    question = f"What is ${binary}_2$ in decimal (base 10)?"

    skew = random.random() * 2
    wrong_choices = []
    while len(wrong_choices) < 3:
        offset = random.random() - 1
        choice_number = int(number * skew + offset * number)
        if choice_number < 0 or choice_number == number or choice_number in [choice for choice in wrong_choices]:
            continue
        wrong_choices.append(choice_number)
    choices = [Choice(str(number), True)] + [Choice(str(choice), False) for choice in wrong_choices]
    random.shuffle(choices)

    return Question(question, choices)

def main():
    parser = argparse.ArgumentParser(description="CLI to generate questions.")
    parser.add_argument("question", type=str, help="The question type to generate.")
    
    args = parser.parse_args()
    question = args.question

    commands = {
        "bin_to_dec": binary_to_decimal(),
    }

    if question in commands:
        print(commands[question])
    else:
        print(f"Unknown command: {question}")
        print("Available commands:", ", ".join(commands.keys()))

if __name__ == "__main__":
    main()
