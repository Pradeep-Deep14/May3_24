class MyClass:
    def __init__(self,x):
        self.x=x  #2
    
    def __call__(self,y):
        return self.x * y #2*3=6

p1=MyClass(2)

print(p1(3))
        

#6