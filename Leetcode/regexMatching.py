'''
https://oj.leetcode.com/problems/regular-expression-matching/

More explanation on the iterative vs recursive solution: 
http://leetcode.com/2011/09/regular-expression-matching.html 

This recursive solution works but gets TLE on leetcode

'''

class Solution:
    # @return a boolean
    def isMatch(self, s, p):

        s = self.no_star(s)
        p = self.no_star(p)

        return self.helper(s,p)

    def helper(self, s, p):

        if len(p) == 0:
            return len(s) == 0

        if len(s) == 0:
            if len(p) != 0: # need to check if the remainings of p are full of stars                    
                for letter in p:
                    if '*' not in letter:
                        return False
                return True

        elif '*' in p[0]:
            if s[0] in p[0] or '.' in p[0]:
                for i in range(len(s)):
                    if self.helper(s[1:],[p[0]]*i + p[1:]) == True:
                        return True
                return False
            else:
                return self.helper(s,p[1:])            
        
        else:
            if p[0] == s[0] or p[0] == '.':
                return self.helper(s[1:], p[1:])
            else:
                return False    


    def no_star(self, p):
        i = 0
        no_star_p = []
        while i < len(p):
            if i+1 < len(p) and p[i+1]=='*':
                no_star_p.append(p[i]+p[i+1])
                i += 2
            else: 
                no_star_p.append(p[i])
                i += 1    
        return no_star_p

s = Solution()

# Unit tests
print 1,s.isMatch('a','a*') == True
print 2,s.isMatch('a','.*') == True
print 3,s.isMatch('a','b*') == False
print 4,s.isMatch('a','a') == True
print 5,s.isMatch('a','.') == True
print 6,s.isMatch('a','b') == False

print 7,s.isMatch('a','aa') == False
print 8,s.isMatch('aa','a') == False

print 9,s.isMatch('aaa','a*a') == True
print 10,s.isMatch('aaa','.*..a*') == True
print 11,s.isMatch("aaa", "ab*a*c*a") == True


'''
class Solution:
    """ My attempt at writing an iterative solution. 
    Turns out it's very difficult and I didn't foresee all the possible edge cases
    """
    # @return a boolean

    def isMatch(self, s, p):

        i = 0
        j = 0


        s = self.no_star(s)
        s = self.cleaner(s)
        p = self.no_star(p)
        p = self.cleaner(p)

        while len(s) > 0 and len(p) > 0:

            if '*' in p[0]:
                if s[0] == p[0][0]:     #(a,a*)
                    s.remove(s[0])

                elif p[0][0] == '.':    #(a,.*)
                    s.remove(s[0])
                else:                   #(a,b*)
                    p.remove(p[0])    
            else:
                if s[0] == p[0]:        #(a,a)
                    s.remove(s[0])
                    p.remove(p[0])
                elif p[0] == '.':       #(a,.)
                    s.remove(s[0])
                    p.remove(p[0])
                else:                   #(a,b)
                    return False

        # at this point either p or s is empty.
            # if s is empty / p not empty

        print s, p

        if len(s) == 0:
            if len(p) == 0:
                return True
            else: # need to check if the remainings of p are full of stars    
                for letter in p:
                    if '*' not in letter:
                        return False
                return True
        else: # len(p) == 0        
            return False


    def no_star(self, p):
        i = 0
        no_star_p = []
        while i < len(p):
            if i+1 < len(p) and p[i+1]=='*':
                no_star_p.append(p[i]+p[i+1])
                i += 2
            else: 
                no_star_p.append(p[i])
                i += 1    
        return no_star_p

    def cleaner(self,p): # p as a list
        i = 0
        while i < (len(p)-1):
            if '*' in p[i] and '*' not in p[i+1] and p[i][0] == p[i+1]:
                        p.remove(p[i+1])
            else:
                i += 1            
        return p                

s = Solution()

# Unit tests
print s.isMatch('a','a*') == True
print s.isMatch('a','.*') == True
print s.isMatch('a','b*') == False
print s.isMatch('a','a') == True
print s.isMatch('a','.') == True
print s.isMatch('a','b') == False

print s.isMatch('a','aa') == False
print s.isMatch('aa','a') == False

print s.isMatch('aaa','a*a') == True
print s.isMatch('aaa','.*..a*') == True

# FAIL !
print s.isMatch("aaa", "ab*a*c*a") == True
'''

