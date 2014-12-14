'''Not accepted by leetcode, seems like using my own objects was a bad idea.
See minStack2.py for a solution that relies on Python lists and that is accepted
'''

class MinStack:
    # @param x, an integer
    # @return an integer
    def push(self, x):
        
        if self.val == None:
            self.val = x
            self.min = x
            self.under = None
        else:
            # Making a deep copy of self manually (because leetcode don't allow 'import copy') (using tmp = self creates a shallow copy that won't work as I want it)
            tmp_val = self.val
            tmp_min = self.min
            tmp_under = self.under

            self.val = x
            if x > tmp_min:
                self.min = tmp_min
            else:
                self.min = x 

            self.under = MinStack()
            self.under.val = tmp_val
            self.under.min = tmp_min
            self.under.under = tmp_under

                     
    # @return nothing
    def pop(self):
        if self.under == None:
            self.val = None
            self.min = None
            self.under = None
        else:
            self.val = self.under.val
            self.min = self.under.min
            self.under = self.under.under

    # @return an integer
    def top(self):
        return self.val

    # @return an integer
    def getMin(self):
        return self.min

    def __init__(self):
        self.val = None
        self.min = None
        self.under = None

test1 = MinStack()

test1.push(1)
test1.push(-4)
test1.push(5)

print test1.top()
print test1.getMin()
print ''
print test1.under.top()
print test1.under.getMin()
print ''
print test1.under.under.top()
print test1.under.under.getMin()
print ''

test1.pop()
print test1.top()
print test1.getMin()
print ''
print test1.under.top()
print test1.under.getMin()
print ''

