# Calculator program

from lib.calculate import calc_std
from lib.manuals import man
from lib.mode import std

def main():
    running = False
    last_mode = "std"
    while True:
        if not running:
            state = input("Calculator Program. Enter To continue: ")      

            if state == "":
                running = True
        
            elif state == "exit":
                print("Exiting the calculator program.")
                break
        mode = input("Mode: ")

        # Standard Mode
        if mode == "std" or (mode == "" and last_mode == "std"):
            std()
            last_mode = "std"

        # Manual
        elif mode == "man" or (mode == "" and last_mode == "man"):
            man()
            last_mode = "man"

        # Exit
        elif mode == "exit":
            print("Exiting the calculator program.")
            break
        
if __name__ == "__main__":
    main()