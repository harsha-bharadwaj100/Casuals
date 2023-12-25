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
        
        if Th.active_count() > 2:
            print(f"waiting...{Th.current_thread()}")
            print(Th.enumerate())
            [t.join() for t in Th.enumerate()[1:-1]]
        print(f"resuming...{Th.current_thread()}")
        self.move()
        
    def move(self):
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
            print(f"Exiting Final Lift Thread{Th.current_thread()}")
            exit()
        
        if self.requests[0]>self.currentFloor:
            for x in range(abs(self.requests[0]-self.currentFloor)):
                time.sleep(1)
                self.currentFloor += 1
                print(self.requests)
                print("test currentFloor = ",self.currentFloor)
                if Th.active_count() > 2:
                    print(f"exiting...{Th.current_thread()}")
                    exit()
        elif self.requests[0]<self.currentFloor:
            for x in range(abs(self.requests[0]-self.currentFloor)):
                time.sleep(1)
                self.currentFloor -= 1
                print(self.requests)
                print("test currentFloor = ",self.currentFloor)
                if Th.active_count() > 2:
                    print(f"exiting...{Th.current_thread()}")
                    exit()
                
        self.currentFloor = self.requests[0]
        del self.requests[0]
        print("currentFloor = ", self.currentFloor)
        print(self.requests)
        if len(self.requests) != 0:
            self.move()
        else:
            print("Waiting for new requests...")
            print(Th.enumerate())
            print(f"exiting {Th.current_thread()}")
            exit()

E = Lift()

def listener():
    while True:
        req = simpledialog.askinteger("Title", "Floor: ")
        print(f"Floor {req} requested")
        if req == None:
            E.request(None)
            [t.join() for t in Th.enumerate()[1:]]
            exit()
        Th.Thread(target=E.request, args=(req,)).start()
        print(Th.enumerate())
listener()