"""Checking an attribute's existence"""
# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1


# example_object = ExampleClass(2)
# print(example_object.a)

# try:
#     print(example_object.b)
# except AttributeError:
#     pass


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
