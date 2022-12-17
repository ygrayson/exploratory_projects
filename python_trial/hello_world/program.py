# my big program in Python
# Grayson Yin

def func1():
    print("This is function 1")

def func2():
    print("This is function 2")

def add(num1, num2):
    return num1 + num2

class Complex:
    """This is a good class"""
    #class vaiable real and complex
    name = "complex"

    def __init__(self, realpart = 0, imagpart = 0):
        self.r = realpart
        self.i = imagpart
        self.b = 10

    def conjugate(self):
        self.i = -self.i

    def print(self):
        print("The complex number is ", self.r, " + ", self.i, "i\n")

    def print_b_and_name(self):
        print(self.b)
        print(self.name)

# main function
def main():
    z1 = Complex()
    z2 = Complex(1, 2)

    #change z1 and z2
    z1.b = 99
    z1.name = "new_name"

    z1.print_b_and_name()
    z2.print_b_and_name()

if __name__ == "__main__":
    main()