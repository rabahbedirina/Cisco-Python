class Stack:
    def __init__(self):
        self.__stk=[]
    def push(self,val):
        self.__stk.append(val)

    def pop(self):
        del self.__stk[-1]

class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count=0

    def get_count(self):
        return self.__count

    def pop(self):
        self.__count+=1
        Stack.pop(self)

    def push(self,val):
        # self.__count+=1
        Stack.push(self,val)


stk=CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_count())

