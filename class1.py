class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        # Functionality to calculate the costs from the area of the house
house = House()
print(house.num_rooms)
print(House.num_rooms)

house.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

value = 7
class A:
    value = 5
a = A()
a.value = 3
print(value)


bravo = 3
b = B()
class B:
    bravo = 5
    print("Inside class B")
c = B()
print(b.bravo)