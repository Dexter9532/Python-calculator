# Calculator program

from functions import add

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
            function = input("Op ")
            b = float(input("b: "))
            result = add(a, b)
            print(f"= {result}")
            last_mode = mode
        elif state == "q":
            print("Exiting the calculator program.")
            running = False
            break

if __name__ == "__main__":
    main()