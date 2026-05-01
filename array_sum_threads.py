import threading

arr = [10, 20, 30, 40, 50, 60]

def sum_part(part, name):
    print(name, "sum =", sum(part))

mid = len(arr) // 2

t1 = threading.Thread(target=sum_part, args=(arr[:mid], "Thread 1"))
t2 = threading.Thread(target=sum_part, args=(arr[mid:], "Thread 2"))

t1.start()
t2.start()

t1.join()
t2.join()
