# Object Oriented Programming
# Class and Object
#Create class and object

class emptyclass: #Example 1
    """This is an empty class"""
    pass


class numberclass:#Example 2
    num=5   

n1=numberclass()
print("The number in the class is ",n1.num)

class withfunction:# Example 3 uses constructor
    num1=200
    num2=100
    def lab(self):
        print("This is lab session")
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

obj1=withfunction(500,1000)
obj1.lab()
#print(withobject.num1)
#print(withobject.num2)
#withobject.num1=2000 #modify the object property
#print(withobject.num1)
#del withobject.num1
#print(withobject.num1)
#withobject.lab()
#print(withobject.num1)
#print(withobject.num2)
