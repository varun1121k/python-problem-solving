# Calculator CLI Project

def get_values():
    n = int(input("Number of values: "))
    values = []
    for _ in range(n):
        value = int(input("Enter value: "))
        values.append(value)
    return values


def addition(values):
    return sum(values)


def subtraction(values):
    result = values[0]
    for v in values[1:]:
        result -= v
    return result


def multiplication(values):
    result = 1
    for v in values:
        result *= v
    return result


while True:
    print("\n---- Calculator ----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage")
    print("6. Power")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        vals = get_values()
        print("Result:", addition(vals))

    elif choice == "2":
        vals = get_values()
        print("Result:", subtraction(vals))

    elif choice == "3":
        vals = get_values()
        print("Result:", multiplication(vals))

    elif choice == "4":
        a = int(input("Dividend: "))
        b = int(input("Divisor: "))
        if b == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Result:", a / b)

    elif choice == "5":
        obtained = int(input("Obtained: "))
        total = int(input("Total: "))
        if total == 0:
            print("Error: Total cannot be zero")
        else:
            print("Result:", (obtained / total) * 100)

    elif choice == "6":
        num = int(input("Number: "))
        p = int(input("Power: "))
        print("Result:", num ** p)

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
