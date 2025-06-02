from lib.calculate import calc_std, calc_dec_to_bin

def std():
    try:
        a = float(input("a: "))
        operation = input("Op ")
        b = float(input("b: "))
        result = calc_std(a, b, operation)
        print(f"= {result}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values for a and b.")
    
def dec_to_bin():
    dec = int(input("Decimal: "))
    bin_result = calc_dec_to_bin(dec)
    print(f"ob{bin_result}")