try:
    numbers = [10, 20, 30, 40]

    index = int(input("Enter index: "))
    print("Value:", numbers[index])

except IndexError:
    print("Error: Invalid index.")

except ValueError:
    print("Error: Index must be a number.")

finally:
    print("Program finished.")
