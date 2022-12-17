print("Hello World!")

# a short real program
num = 5
print(num)
num = "five"
print(num)

# identity function
x = 10
y = 100

print("When x = 10, y = 100")
print(id(x))
print(id(y))

y = x
print("When x = 10, y = x")
print(id(x))
print(id(y))