import threading

arr = [5, 10, 15, 20, 25, 30]
target = 20

def search(part, name):
    if target in part:
        print(name, "found", target)
    else:
        print(name, "did not find", target)

mid = len(arr) // 2

t1 = threading.Thread(target=search, args=(arr[:mid], "Thread 1"))
t2 = threading.Thread(target=search, args=(arr[mid:], "Thread 2"))

t1.start()
t2.start()

t1.join()
t2.join()
