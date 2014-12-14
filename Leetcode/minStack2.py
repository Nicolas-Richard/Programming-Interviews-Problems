'''
Not an accepted solution either. Time Limit Exceeded.
https://oj.leetcode.com/problems/min-stack/
This solution was accepted : http://www.cnblogs.com/zuoyuan/p/4091870.html
But pop, getMin and top method are not executed in constant time, because they use negative slices [-1], which actually requires making a all pass through the stack.
'''


class MinStack:
    # @param x, an integer
    # @return an integer

    def __init__(self):
        self.val_stack = []
        self.min_stack = []

    def push(self, x):
        self.val_stack.insert(0,x)

        if self.min_stack == []:
            self.min_stack.append(x)
        elif x > self.min_stack[0]:
            self.min_stack.insert(0,self.min_stack[0])
        else:  
            self.min_stack.insert(0,x)
    
    # @return nothing
    def pop(self):
        self.val_stack = self.val_stack[1:]
        self.min_stack = self.min_stack[1:]        

    # @return an integer
    def top(self):
        return self.val_stack[0]
        

    # @return an integer
    def getMin(self):
        return self.min_stack[0]
        