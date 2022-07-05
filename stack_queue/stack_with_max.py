"""
EPI 8.1- Implement Stack with MAX api
    Stack that has getMax() api which returns the max value present in stack.

Approach 1:

    While doing push set max value.
    While doing pop() if the popped value is == current_max value then re-calculate the new max.

                        [2,     10,     5,  20,   4,  8,    25,     6]
   stack.push(2)        max
   stack.push(10)               max
   stack.push(5)                max
   stack.push(20)                           max
   stack.push(4)                            max
   stack.push(8)                            max
   stack.push(25)                                           max


   stack.pop()#6                                             max        value popped is less than current max so no need to do anything
   stack.pop()#25                           max                         value popped is equal to current max so need to recalculate what is the new max
   stack.pop()#8                            max
   stack.pop()#4                            max
   stack.pop()#20               max


Approach 2:
    keep history of all max values.

                    [2, 10, 5, 20, 4, 8, 25, 6]

    stack.push(2)       max_history = [2]               => max= 2
    stack.push(10)      max_history = [2, 10]           => max= 10
    stack.push(5)       max_history = [2, 10]           => max= 10
    stack.push(20)      max_history = [2, 10, 20]       => max= 20
    stack.push(4)       max_history = [2, 10, 20]       => max= 20
    stack.push(8)       max_history = [2, 10, 20]       => max= 20
    stack.push(25)      max_history = [2, 10, 20, 25]   => max= 25

    stack.pop()#6       max_history = [2,10,20,25]      => max= 25
    stack.pop()#25      max_history = [2,10,20]         => max= 20
    stack.pop()#8       max_history = [2,10,20]         => max= 20
    stack.pop()#4       max_history = [2,10,20]         => max= 20
    stack.pop()#20      max_history = [2,10]            => max= 10




"""

class MyStack1(object):
    def __init__(self):
        self.data = []
        self.max = None

    def push(self, val):
        if val > self.max:
            self.max = val
        self.data.append(val)

    def pop(self):
        if not self.data:
            return -1
        val = self.data.pop()
        if val == self.max:
            new_max = float('-inf')
            for i in range(len(self.data)):
                if self.data[i] > new_max:
                    new_max = self.data[i]
            self.max = new_max

    def getMax(self):
        return self.max if self.data else None

    def print_elem(self):
        return [i for i in self.data]


class MyStack2(object):
    def __init__(self):
        self.data = []
        self.max = None
        self.max_history = []

    def push(self, val):
        if val > self.max:
            self.max = val
            self.max_history.append(val)
        self.data.append(val)

    def pop(self):
        if not self.data:
            return -1
        val = self.data.pop()
        if val == self.max:
            self.max_history.pop()
            self.max = self.max_history[-1]

    def getMax(self):
        return self.max if self.data else None

    def print_elem(self):
        return [i for i in self.data]

if __name__=="__main__":
    # stack = MyStack1()
    # stack.push(2)
    # stack.push(10)
    # print "max: {}, stack {}".format(stack.getMax(), stack.print_elem())
    # stack.push(20)
    # print "max: {}, stack {}".format(stack.getMax(), stack.print_elem())
    # stack.push(4)
    # stack.push(5)
    # print "max: {}, stack {}".format(stack.getMax(), stack.print_elem())
    # stack.push(25)
    # print "max: {}, stack {}".format(stack.getMax(), stack.print_elem())
    # stack.push(6)
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # print "max: {}, stack {}".format(stack.getMax(), stack.print_elem())
    # stack.pop()
    # stack.pop()
    # print "max: {}, stack {}".format(stack.getMax(), stack.print_elem())


    stack = MyStack2()
    stack.push(2)
    stack.push(10)
    print "max: {}, stack {}".format(stack.getMax(), stack.print_elem())
    stack.push(20)
    print "max: {}, stack {}".format(stack.getMax(), stack.print_elem())
    stack.push(4)
    stack.push(5)
    print "max: {}, stack {}".format(stack.getMax(), stack.print_elem())
    stack.push(25)
    print "max: {}, stack {}".format(stack.getMax(), stack.print_elem())
    stack.push(6)
    stack.pop()
    stack.pop()
    stack.pop()
    print "max: {}, stack {}".format(stack.getMax(), stack.print_elem())
    stack.pop()
    stack.pop()
    print "max: {}, stack {}".format(stack.getMax(), stack.print_elem())
