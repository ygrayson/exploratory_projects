from threading import Thread

def thread_body():
    print("This is in the thread")
    print("2")
    print("3")

t = Thread(target=thread_body)
t.start()
print("Main Thread")
t.join()