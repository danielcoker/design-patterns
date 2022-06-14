from abc import ABC, abstractmethod


class Calculate(ABC):
    """
    Calculate abstract class with an abstract method other strategies implement.
    """

    @abstractmethod
    def execute(self, a: int, b: int) -> int:
        pass


class CalculateAdd(Calculate):
    """
    Calculate concrete add strategy.
    """

    def execute(self, a: int, b: int) -> int:
        return a + b


class CalculateSubtract(Calculate):
    """
    Calculate concrete subtract strategy.
    """

    def execute(self, a: int, b: int) -> int:
        return a - b


class CalculateMultiply(Calculate):
    """
    Calculate concrete multiply strategy.
    """

    def execute(self, a: int, b: int) -> int:
        return a * b


class CalculateDivide(Calculate):
    """
    Calculate concrete divide strategy.
    """

    def execute(self, a: int, b: int) -> int:
        return a / b


class Calculator:
    def set_calculate(self, calculate: Calculate) -> None:
        """
        Set the calculate strategy to use.
        """
        self.calculate = calculate

    def result(self, a: int, b: int) -> int:
        """
        Compute result using the appropriate calculate strategy.
        """
        return self.calculate.execute(a, b)


if __name__ == "__main__":
    calculator = Calculator()

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    action = input("Enter action: [add, subtract, multiply, divide] ")

    if action == "add":
        calculator.set_calculate(CalculateAdd())

    if action == "subtract":
        calculator.set_calculate(CalculateSubtract())

    if action == "multiply":
        calculator.set_calculate(CalculateMultiply())

    if action == "divide":
        calculator.set_calculate(CalculateDivide())

    result = calculator.result(a, b)

    print("RESULT", result)
