from abc import ABC, abstractmethod
from typing import List

class Rule(ABC):
    @abstractmethod
    def apply(self, number: int) -> str:
        pass

class FizzRule(Rule):
    def apply(self, number: int) -> str:
        if number % 3 == 0:
            return "Fizz"
        return ""

class BuzzRule(Rule):
    def apply(self, number: int) -> str:
        if number % 5 == 0:
            return "Buzz"
        return ""

class FizzBuzzRule(Rule):
    def apply(self, number: int) -> str:
        if number % 15 == 0:
            return "FizzBuzz"
        return ""

class NumberRule(Rule):
    def apply(self, number: int) -> str:
        return str(number)

class FizzBuzzProcessor:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def process(self, number: int) -> str:
        for rule in self.rules:
            result = rule.apply(number)
            if result:
                return result
        return ""

if __name__ == "__main__":
    processor = FizzBuzzProcessor([
        FizzBuzzRule(),
        FizzRule(),
        BuzzRule(),
        NumberRule()
    ])
    for i in range(1, 101):
        print(processor.process(i))
