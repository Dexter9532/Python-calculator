# This file contains basic arithmetic functions
    

# standard calc function with basic arithmetic operations
def calc_std(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation" 

# converting decimal to binary
def calc_dec_to_bin(dec):
    bin = "" 
    while dec > 0:
        bin = str(dec % 2) + bin
        dec = dec // 2
    return bin

#def calc_bin_to_bin(bin):


