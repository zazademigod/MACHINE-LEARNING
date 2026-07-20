#this is essentially a template for a type of object

class point():
    #this __init__ is a magic method used to reference the method itself
    #self in the input is used to identify the value itself
    def __init__(self, val_1, val_2):
        self.x = val_1
        self.y = val_2

p = point(3, 4)

print(p.x)
print(p.y)

#another example, an airline company that helps to  make sure overbookiing doesn't happen
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passenger)


flight = Flight(4)

people = ['harry', 'tobi', 'wale', 'seun', 'dele']
for person in people:
    if flight.add_passenger(person):
        print(f'added {person} to flight successfully.')
    else:
        print(f'no available seat for {person}.')