# Calculator program

from lib.functions import std

def main():
    running = False
    while True:
        if running == False:
            state = input("Calculator Program. Enter To continue: ")        
            if state == "":
                running = True
        mode = input("Mode: ")
        if mode == "std" or mode == "" and last_mode == "std":
            a = float(input("a: "))
            operation = input("Op ")
            b = float(input("b: "))
            result = std(a, b, operation)
            print(f"= {result}")
            last_mode = mode
        elif state == "q":
            print("Exiting the calculator program.")
            running = False
        elif mode == "exit" or mode == "quit":
            print("Exiting the calculator program.")
            running = False
if __name__ == "__main__":
    main()