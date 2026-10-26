class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a//b

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("modulo by zero")
        return a % b

    def power(self, a, b):
        result = 1
        for _ in range(b):
            result = self.multiply(result, a)
        return result
