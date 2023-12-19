import time


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
        self.move()
        
    def move(self):
        # self.requests = sorted(self.requests)
        cache = [] # create a temporary list
        
        if self.currentFloor > self.requests[0]: # if the very next request is less than cureent floor
            for x in range(self.currentFloor-1, self.requests[0], -1):# iterate through all the floor numbers in between current floor and very next request floor
                if x in self.requests[1:]:# if the floor number is in rest of the requests
                    #print(x)
                    cache.append(x)# then add it to the temporary list and 
                    self.requests.remove(x) # delete it from requests
            self.requests = sorted(cache)[::-1] + self.requests # now sort the temporary list backwards and add it from front to the requests
            
        elif self.currentFloor < self.requests[0]: # if the very next request is greater than cureent floor
            for x in range(self.currentFloor+1, self.requests[0]):# iterate through all the floor numbers in between current floor and very next request floor
                if x in self.requests[1:]:# if the floor number is in rest of the requests
                    #print(x)
                    cache.append(x)# then add it to the temporary list and 
                    self.requests.remove(x) # delete it from requests
            self.requests = sorted(cache) + self.requests # now sort the temporary list forwards and add it from front to the requests

        time.sleep(abs(self.requests[0]-self.currentFloor))
        self.currentFloor = self.requests[0]
        del self.requests[0]
        print("currentFloor = ", self.currentFloor)
        if len(self.requests) != 0:
            self.move()

# class Building:
#     def __init__(self) -> None:
#         pass

E = Lift()
E.request(7)
E.request(6)
E.request(9)
E.request(3,2,5)
E.request(1)
E.request(2,6,4)