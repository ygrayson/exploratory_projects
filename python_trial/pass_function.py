# pass function into another function as a parameter

def func_g():
    print("This is function g")

def func_f():
    print("This is function f")
    def func_k():
        print("This is func_k defined inside func_f")
    return func_k

func_g = 1
print(func_g)
func_g = func_f
print(func_g)
