# Calculator program
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.calculate import calc_std, calc_dec_to_bin
from lib.manuals import man
from lib.mode import std, dec_to_bin

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
        
        elif mode == "dec to bin" or (mode == "" and last_mode == "dec to bin"):
            dec_to_bin()
            last_mode = "dec to bin"
            
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