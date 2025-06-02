def man():
    modes = ["man", "dec to bin", "std"]
    print("Available modes:")  
    for m in modes:
        print(f"- {m}")
    man_for = input("Enter mode for manual: ")

    if man_for == "std":
        print("Standard mode: Performs basic arithmetic operations (+, -, *, /). Can only peform one operation at a time with a and b.")
    
    elif man_for == "dec_to_bin":
        print("Decimal to Binary mode: Converts a decimal number to binary. Enter a decimal number to get its binary representation.")

    elif man_for == "man":
        print("Manual mode: Allows you to see available modes and their descriptions.")

    elif man_for == "exit":
        print("Exit. Allows you to exit the program.")
