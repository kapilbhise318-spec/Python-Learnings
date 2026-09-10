import threading 
def task():
    for i in range(5):
        print(i)

t1=threading.Thread(target=task)
t2=threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()




