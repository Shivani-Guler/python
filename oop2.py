class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def grow(self):
        self.age+=1

    # def __str__(self):
    #     return f"{self.name},{self.age}"  #--method overriding--
    
    def __repr__(self):
        return f"{self.name},{self.age}"

def getDogInfo():
    name=input("Enter dog name\n")
    age=int(input("Enter dog age\n"))
    return Dog(name,age)
    
def loadDogs(n):
    return [ getDogInfo() for i in range(n) ]
    
num=int(input("How many dogs\n"))
dogs=loadDogs(num)
maxAgeDog=max(dogs,key=lambda d:d.age)
print(maxAgeDog) 
print(dogs)

class Swimmer:                                     #----multiple inheritace---
    def swim(self):
        print("Swimming")

class GermanShepherd(Dog,Swimmer):                #----inheritance----
    def __init__(self, name, age,food):
        super().__init__(name, age)
        self.food=food 

    def __str__(self):
        return f"{self.food}"
    
g1=GermanShepherd("Bam",5,"bread")
print(g1)     