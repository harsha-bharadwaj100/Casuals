# from threading import Thread
# from time import sleep

# def fun():
#     sleep(5)
#     print("fun woke up!")

# t1 = Thread(target=fun)
# t1.start()
# t1.join()
# t1.start()
# print("Done!")

from tkinter import simpledialog

res = simpledialog.askstring("Titler", "Enterr: ")
print(res)
