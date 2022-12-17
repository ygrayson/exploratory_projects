def wrapper(fn):
    def wrapped():
        print("start")
        fn()
        print("end")
    return wrapped

@wrapper
def f():
    print("Hello")

f()