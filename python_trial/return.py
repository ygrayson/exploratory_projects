# Python trial program with function calls and returns

def myFunc(y):
    y[1] = 4
    y = [1, 4, 3]


x = [1, 2, 3]
myFunc(x)
print(x) # print out [1, 4, 3]
