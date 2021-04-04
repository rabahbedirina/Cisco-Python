"""
LAB

Estimated time
20-45 minutes

Level of difficulty
Easy/Medium

Objectives
improving the student's skills in defining classes from scratch;
implementing standard data structures as classes.
Scenario
As you already know, a stack is a data structure realizing the so-called LIFO (Last In - First Out) model. It's easy and you've already grown perfectly accustomed to it.

Let's taste something new now. A queue is a data model characterized by the term FIFO: First In - Fist Out. Note: a regular queue (line) you know from shops or post offices works exactly in the same way - a customer who came first is served first too.

Your task is to implement the Queue class with two basic operations:

put(element), which puts an element at end of the queue;
get(), which takes an element from the front of the queue and returns it as the result (the queue cannot be empty to successfully perform it.)
Follow the hints:

use a list as your storage (just like we did in stack)
put() should append elements to the beginning of the list, while get() should remove the elements from the list's end;
define a new exception named QueueError (choose an exception to derive it from) and raise it when get() tries to operate on an empty list.
Complete the code we've provided in the editor. Run it to check whether its output is similar to ours.

Expected output
1
dog
False
Queue error


"""


class Queue:
    def __init__(self):
        self.__lis = []

    def put(self, elem):
        self.__lis.append(elem)

    def get(self):
        val = self.__lis[-1]
        del self.__lis[-1]
        return val


class QueueError(Queue):  # Choose base class for the new exception.
    def __init__(self):
        Queue.__init__(self)

    def get(self):
        try:
            Queue.get(self)
            raise IndexError("Index error ")
        # except:
        #     print("Queue error")

    def put(self, val):
        Queue.put(self, val)


que = QueueError()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    print(que.get())
