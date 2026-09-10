# import threading
# def myfunc():
#     print("Hello from Thread,",threading.current_thread.name())
#     thread=threading.Thread(target=myfunc)
#     thread.start()
#     thread.join()





import threading

def task(name):
    print(f"Thread {name} running")

# Method 1: Pass a function
t = threading.Thread(target=task, args=("A",))
t.start()
t.join()  # Wait for thread to finish

# Method 2: Subclass Thread
class MyThread(threading.Thread):
    def run(self):
        print(f"Running {self.name}")

t = MyThread()
t.start()
t.join()

# t=threading.Thread(target=task,daemon=True)
# t.start()