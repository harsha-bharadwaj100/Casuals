class Lift:
    def __init__(self, currentFloor=0, requests=[]) -> None:
        self.currentFloor = currentFloor
        self.requests = requests
        print("currentFloor = ", self.currentFloor)
    
    def request(self, *floor):
        self.requests += list(floor)
        self.move()
        
    def move(self):
        self.requests = sorted(self.requests)
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