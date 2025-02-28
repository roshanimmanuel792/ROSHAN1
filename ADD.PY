class Adder:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

# Example usage
adder = Adder(3, 5)
print(adder.add())  # Output: 8
