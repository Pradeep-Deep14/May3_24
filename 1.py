class MyClass:
    def __init__(self,x):
        self.x=x
    
    def __call__(self,y):
        return self.x * y

p1=MyClass(2)

print(p1(3))
        