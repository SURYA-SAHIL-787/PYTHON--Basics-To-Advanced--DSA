import threading

stack = []
lock = threading.Lock()

def push_item(item):
    with lock:
        stack.append(item)
        print("Pushed:", item)

def pop_item():
    with lock:
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty")

t1 = threading.Thread(target=push_item, args=(10,))
t2 = threading.Thread(target=push_item, args=(20,))
t3 = threading.Thread(target=pop_item)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
