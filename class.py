#Classes and Objects

class car:
    def my_car(self, name):
        return f"Hello {name},Lets Drive a car!"

x= car()
print(x.my_car("Madhan"))


print("")

#using constructor

class calculator():
    def __init__(self, a, b):
        self.a =a
        self.b =b


    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
        


y=calculator(400,50)
z= calculator(2,4)
k=calculator(10,5)

print(y.a)
print(y.b)

print(z.a)

print(y.add())
print(z.add())
print(k.sub())
print(y.sub())
