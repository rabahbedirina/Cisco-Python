"""Checking an attribute's existence"""
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(2)
print(example_object.a)

try:
    print(example_object.b)
except AttributeError:
    pass


class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
if hasattr(example_object,'a'):
    print(example_object.a)

if hasattr(example_object, 'b'):
    print(example_object.b)



"""hasattr() function can operate on classes, too. 
You can use it to find out if a class variable is available"""
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))