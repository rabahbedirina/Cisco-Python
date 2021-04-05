class Stack :
    def __init__(self):
        self.__stack_list=[]
    
    

    def push(self,val):
        self.__stack_list.append(val)
        

    def pop(self):
        val=self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

list_1=Stack()
# 
print(list_1.push(3))
print(list_1.push(2))
print(list_1.push(1))
print(list_1._Stack__stack_list) # how to access to a private instance from outside class
print(list_1.pop())

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum=0
    

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
    
    def pop(self):
        val=Stack.pop(self)
        self.__sum-=val
        return val



stack_object=AddingStack()

for i in range(5):
    stack_object.push(i)

print(stack_object.get_sum())
for i in range(5):
    stack_object.pop()

print(stack_object.get_sum())