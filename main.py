# Calculator program

from lib.functions import std

def main():
    running = False
    while True:
        if not running:
            state = input("Calculator Program. Enter To continue: ")      

            if state == "":
                running = True
        
            elif state == "exit":
                print("Exiting the calculator program.")
                running = False
        mode = input("Mode: ")

        # Standard Mode
        if mode == "std" or mode == "" and last_mode == "std":
            a = float(input("a: "))
            operation = input("Op ")
            b = float(input("b: "))
            result = std(a, b, operation)
            print(f"= {result}")
            last_mode = mode

        # Manual
        elif mode == "man" or mode == "" and last_mode == "man":
            modes = ["man", "exit", "std"]
            print("Available modes:")  
            last_mode = mode
            for m in modes:
                print(f"- {m}")
            man_for = input("Enter mode for manual: ")

            if man_for == "std":
                print("Standard mode: Performs basic arithmetic operations (+, -, *, /). Can only peform one operation at a time with a and b.")

            elif man_for == "man":
                print("Manual mode: Allows you to see available modes and their descriptions.")

            elif man_for == "exit":
                print("Exit. Allows you to exit the program.")

if __name__ == "__main__":
    main()