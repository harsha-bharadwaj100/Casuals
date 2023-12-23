import time
import threading as Th
from tkinter import simpledialog

class Lift:
    def __init__(self, currentFloor=0, requests=[]) -> None:
        self.currentFloor = currentFloor
        self.requests = requests
        print("currentFloor = ", self.currentFloor)
    
    def request(self, *floor):
        floors = list(floor)
        for f in floors:
            if f not in self.requests:
                self.requests.append(f)
        # Th.Thread(target=self.move).start()
        if len(Th.enumerate()) > 2:
            print(f"waiting...{Th.current_thread()}")
            time.sleep(1)
        self.move()
        
    def move(self):
        # self.requests = sorted(self.requests)
        cache = [] # create a temporary list
        try:
            if self.currentFloor > self.requests[0]: # if the very next request is less than cureent floor
                for x in range(self.currentFloor-1, self.requests[0], -1):# iterate through all the floor numbers in between current floor and very next request floor
                    if x in self.requests[1:]:# if the floor number is in rest of the requests
                        print(x, "1")
                        cache.append(x)# then add it to the temporary list and 
                        self.requests.remove(x) # delete it from requests
                self.requests = sorted(cache)[::-1] + self.requests # now sort the temporary list backwards and add it from front to the requests
                print(self.requests)
                
            elif self.currentFloor < self.requests[0]: # if the very next request is greater than cureent floor
                for x in range(self.currentFloor+1, self.requests[0]):# iterate through all the floor numbers in between current floor and very next request floor
                    if x in self.requests[1:]:# if the floor number is in rest of the requests
                        print(x, "2")
                        cache.append(x)# then add it to the temporary list and 
                        self.requests.remove(x) # delete it from requests
                self.requests = sorted(cache) + self.requests # now sort the temporary list forwards and add it from front to the requests
                print(self.requests)
        except TypeError:
            exit()
        
        if self.requests[0]>self.currentFloor:
            for x in range(abs(self.requests[0]-self.currentFloor)):
                time.sleep(1)
                self.currentFloor += 1
                print(self.requests)
                print("test currentFloor = ",self.currentFloor)
                if len(Th.enumerate()) > 2:
                    print(f"exiting...{Th.current_thread()}")
                    exit()
        elif self.requests[0]<self.currentFloor:
            for x in range(abs(self.requests[0]-self.currentFloor)):
                time.sleep(1)
                self.currentFloor -= 1
                print(self.requests)
                print("test currentFloor = ",self.currentFloor)
                if len(Th.enumerate()) > 2:
                    print(f"exiting...{Th.current_thread()}")
                    exit()
                
        self.currentFloor = self.requests[0]
        del self.requests[0]
        print("currentFloor = ", self.currentFloor)
        print(self.requests)
        while True:
            if self.requests == None:
                exit()
            if len(self.requests) != 0:
                self.move()
            else:
                print("Waiting in this damn thing...")
                time.sleep(0.5)
                print(Th.enumerate())

# class Building:
#     def __init__(self) -> None:
#         pass

E = Lift()
# E.request(7)
# E.request(6)
# E.request(9)
# E.request(3,2,5)
# E.request(1)
# E.request(2,6,4)


def listener():
    ExitVar = 0
    while True:
        req = simpledialog.askinteger("Title", "Floor: ")
        print(f"Floor {req} requested")
        if req == None:
            E.requests == None
            time.sleep(0.1)
            ExitVar += 1
        if ExitVar == 3:
            exit()
        Th.Thread(target=E.request, args=(req,)).start()
        print(Th.enumerate())
listener()
# runListener = Thread(target=listener)
