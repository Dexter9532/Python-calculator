# Calculator program

from functions import add

def main():

    while True:
        print("Calculator Program")
        function = input("Enter one of the operations (+, -, *, /): ")
        if function == "+":
            a = float(input("a: "))
            b = float(input("b: "))
            result = add(a, b)
            print(f"= {result}")
        elif function not in ["+", "-", "*", "/"]:
            print("Invalid operation. Please enter one of the operations (+, -, *, /).")


if __name__ == "__main__":
    main()