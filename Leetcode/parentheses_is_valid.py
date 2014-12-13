class Solution:
    # @return a boolean
    def isValid(self, s):
        
        stack = []
       
        for letter in s:
            if letter in ')]}':
                if len(stack) == 0:
                   return False

                if self.is_matched(stack[len(stack)-1], letter):
                    stack.pop()
            else:
                stack.append(letter)
         
            #print stack

        if len(stack) == 0:
            return True
        else: 
            return False
          
    def is_matched(self, a, b):
        if a == '(' and b == ')': return True
        elif a == '[' and b == ']': return True
        elif a == '{' and b == '}': return True
        else:
            return False
            
s = Solution()
