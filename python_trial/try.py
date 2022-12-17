# This is Python code for trying try-catch block
# Qianbo Yin

def my_function():
    # Get input from user
    x = input("What is your input?\n")
    # Convert input to integer
    try:
        y = int(x)
        print("Convert successfully\n")
        print(y)
    except:
        print("Cannot convert\n")

my_function()
