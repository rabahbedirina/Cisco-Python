"""Class Variable"""

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5
example_object_3.fourth = 6

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

# As you know, such an addition makes the instance variable private - it becomes inaccessible from the outer world.

# The actual behavior of these names is a bit more complicated, so let's run the program. This is the output:


class ExampleClass1:
    # counter=0 you can access to the this variable from outside the class
    __counter=0  # private variable
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass1.__counter+=1
        # ExampleClass1.counter+=1
    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass1()
example_object_2 = ExampleClass1(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass1(4)
example_object_3.__third = 5
example_object_3.fourth = 6


print(example_object_1.__dict__,example_object_1._ExampleClass1__counter)
# print(example_object_1.__dict__,example_object_1.counter)
print(example_object_1.__dict__,example_object_1._ExampleClass1__counter)
# print(example_object_2.__dict__,example_object_2.counter)
print(example_object_1.__dict__,example_object_1._ExampleClass1__counter)
# print(example_object_3.__dict__,example_object_3.counter)

