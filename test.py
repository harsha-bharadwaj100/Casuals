# # # from threading import Thread
# # # from time import sleep

# # # def fun():
# # #     sleep(5)
# # #     print("fun woke up!")

# # # t1 = Thread(target=fun)
# # # t1.start()
# # # t1.join()
# # # t1.start()
# # # print("Done!")

# # from tkinter import simpledialog

# # res = simpledialog.askstring("Titler", " Enterr: \t\t\t")
# # print(res)

# import threading as th
# import time

# def foo():
#     print("Running t1 - foo")
#     time.sleep(5)

# def fun():
#     print("Running t2 - fun")
#     t1.join()

# t1 = th.Thread(target=foo)
# t2 = th.Thread(target=fun)
# t1.start()
# t2.start()
# print(th.enumerate())
ls = [4, 2, 7, 9, 0]
print(ls[1:-1])