import threading
import time

stack = []

def push_items():
    for i in range(1, 6):
        stack.append(i)
        print("Pushed:", i)
        time.sleep(1)

def pop_items():
    time.sleep(2)
    while stack:
        item = stack.pop()
        print("Popped:", item)
        time.sleep(1)

t1 = threading.Thread(target=push_items)
t2 = threading.Thread(target=pop_items)

t1.start()
t2.start()

t1.join()
t2.join()
