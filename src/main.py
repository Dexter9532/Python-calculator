from lib.functions import add, buffer

print("Calculator Program")

def main():

    while True:
        
        state = input("Press Enter to continue or 'q' to quit: ")

        if state == "q":
            print("Goodbye!")
            break
        if state == "":
            value = buffer()
            if function == "+":
                result = float(add(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z))
                print(f"= {result}")

if __name__ == "__main__":
    main()