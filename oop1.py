class Dog:
    def __init__(self,name,age):
       self.name=name
       self.age=age
    def grow(self):
        self.age+=1
    
d1=Dog("Ramu",3)
#print(type(d1))
d2=Dog("Bam",6)
print(d1.name,d1.age)
print(d2.name,d2.age)
d1.age+=30
print(d1.age,d2.age)
d2.grow()
print(d2.age) 