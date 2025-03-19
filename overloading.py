#operator overloading

class Myclass():
    def __init__(self,a):
        self.a =a
        print(self.a)

    def __add__(self,other):
        return self.a + other.a    

x= Myclass(10)        
y= Myclass(20)

print(x + y)
print("")

class Employees():
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def __mul__(self,other):
        return self.salary*other.days    
        
         
class pay():
    def __init__(self,days):
        self.days=days       


obj1 =Employees("madhan",2500)
obj2=pay(25)

print(obj1*obj2)
print("")


#method overloading

class addition():
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a
result=addition()

print(result.add(10)) 
print(result.add(10,20))     
print(result.add(10,20,30))            
print("")



class easy():
    def addition(self,*args):
        sum = 1
        for i in args:
            sum *=i
        return sum


result1=easy()
print(result1.addition(10,20,30))
print(result1.addition(1,2,3,4,5))
print(result1.addition(100,50,200,300))
