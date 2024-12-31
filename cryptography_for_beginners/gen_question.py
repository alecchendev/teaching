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
        choices_str = "\n\n".join([f"[//]: # (choice{' correct' if choice.correct else ''})\n{choice.choice}" for choice in self.choices])
        return f"[//]: # (question)\n{self.question}\n\n{choices_str}"


def random_numbers(center: int, count: int, skewed: bool) -> List[int]:
    skew = random.random() * 2 if skewed else 1
    nums = set()
    while len(nums) < count:
        offset = random.random() - 0.5
        num = int(center * skew + center * offset)
        if num < 0 or num == center:
            continue
        nums.add(num)
    assert len(nums) == count
    return list(nums)

def hex_to_decimal() -> Question:
    number = random.randint(31, 64)
    hex_num = hex(number)[2:]
    question = f"What is ${hex_num}_{{16}}$ in decimal (base 10)?"

    choice_nums = random_numbers(number, 3, True)
    choices = [Choice(str(choice), False) for choice in choice_nums]
    choices.append(Choice(str(number), True))
    random.shuffle(choices)

    return Question(question, choices)

def decimal_to_hex() -> Question:
    number = random.randint(31, 64)
    question = f"What is ${number}_{{10}}$ in hex (base 16)?"

    choice_nums = random_numbers(number, 3, True)
    choices = [Choice(hex(choice)[2:], False) for choice in choice_nums]
    choices.append(Choice(hex(number)[2:], True))
    random.shuffle(choices)

    return Question(question, choices)


def binary_to_decimal() -> Question:
    number = random.randint(10, 32)
    binary = bin(number)[2:]
    question = f"What is ${binary}_2$ in decimal (base 10)?"

    choice_nums = random_numbers(number, 3, True)
    choices = [Choice(str(choice), False) for choice in choice_nums]
    choices.append(Choice(str(number), True))
    random.shuffle(choices)

    return Question(question, choices)

def decimal_to_binary() -> Question:
    number = random.randint(10, 64)
    question = f"What is ${number}_{{10}}$ in binary (base 2)?"

    choice_nums = random_numbers(number, 3, True)
    choices = [Choice(bin(choice)[2:], False) for choice in choice_nums]
    choices.append(Choice(bin(number)[2:], True))
    random.shuffle(choices)

    return Question(question, choices)

def main():
    parser = argparse.ArgumentParser(description="CLI to generate questions.")
    parser.add_argument("question", type=str, help="The question type to generate.")
    
    args = parser.parse_args()
    question = args.question

    commands = {
        "bin_to_dec": binary_to_decimal(),
        "dec_to_bin": decimal_to_binary(),
        "hex_to_dec": hex_to_decimal(),
        "dec_to_hex": decimal_to_hex(),
    }

    if question in commands:
        print(commands[question])
    else:
        print(f"Unknown command: {question}")
        print("Available commands:", ", ".join(commands.keys()))

if __name__ == "__main__":
    main()
