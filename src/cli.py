from src.main import addition, subtraction, multiplication, division

def main():
    print("Basic Calculator (add, sub, mul, div)")
    op = input("Operation: ").strip().lower()
    a = float(input("First number: "))
    b = float(input("Second number: "))

    if op == "add":
        print(addition(a, b))
    elif op == "sub":
        print(subtraction(a, b))
    elif op == "mul":
        print(multiplication(a, b))
    elif op == "div":
        try:
            print(division(a, b))
        except ZeroDivisionError as e:
            print(f"Error: {e}")
    else:
        print("Unknown operation.")

if __name__ == "__main__":
    main()
