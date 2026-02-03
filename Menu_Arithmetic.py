def main():
    print("Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter your choice: "))

    if 1 <= choice <= 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", a + b)
        elif choice == 2:
            print("Result =", a - b)
        elif choice == 3:
            print("Result =", a * b)
        elif choice == 4:
            if b != 0:
                print("Result =", a / b)
            else:
                print("Division by zero not possible")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
