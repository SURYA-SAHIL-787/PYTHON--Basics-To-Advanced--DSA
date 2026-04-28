class ArrayDivision:
    def __init__(self, numbers):
        self.numbers = numbers

    def divide_elements(self, divisor):
        result = []

        for num in self.numbers:
            result.append(num / divisor)

        return result


try:
    arr = [10, 20, 30, 40]

    divisor = int(input("Enter divisor: "))

    obj = ArrayDivision(arr)

    print("Original Array:", arr)
    print("Result Array:", obj.divide_elements(divisor))

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Enter only integer value")
