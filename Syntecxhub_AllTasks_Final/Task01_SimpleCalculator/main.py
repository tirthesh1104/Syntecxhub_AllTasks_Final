def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def main():
    print("=== Simple Calculator ===")

    try:
        a = float(input("A: "))
    except ValueError:
        print("Invalid number! Please enter digits only.")
        return

    op = input("Op (+ - * /): ").strip()
    ops = {'+': add, '-': sub, '*': mul, '/': div}

    if op not in ops:
        print("Invalid operator!")
        return

    try:
        b = float(input("B: "))
    except ValueError:
        print("Invalid number! Please enter digits only.")
        return

    result = ops[op](a, b)
    print("Result:", result)


if __name__ == "__main__":
    main()
