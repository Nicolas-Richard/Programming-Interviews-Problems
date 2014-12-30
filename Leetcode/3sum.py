
'''
https://oj.leetcode.com/problems/3sum/

My first attempt relied on dictionnaries and was not fast enough

Then I looked at these two pages and figured it out

1. Always very helpful to understand the theory: http://en.wikipedia.org/wiki/3SUM
2. How to handle duplicates : http://www.programcreek.com/2012/12/leetcode-3sum/
'''


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        
        result = []

        num.sort()
        #print num

        for i in range(len(num)):
            if (i == 0 or num[i] > num[i-1]):
                a = num[i]
                start = i + 1
                end = len(num) - 1

                while start < end:
                    b = num[start]
                    c = num[end]
                    #print [a,b,c]
                    if (a+b+c) == 0:
                        result.append([a,b,c])
                        start +=1
                        end -=1
                        while start < end and num[start-1] == num[start]:
                            start += 1
                        while start < end and num[end+1] == num[end]:
                            end -= 1
                    elif (a+b+c) > 0:
                        end -=1
                    else:    
                        start += 1

        return result

s = Solution()

test1 = [-1, 0, 1, 2, -1, -4]
test2 = [-2,0,1,1,2]
testTLE = [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
testTLE2 = [-3,-12,-3,-9,14,4,8,-4,11,4,7,-8,-5,4,7,-12,2,9,6,-12,8,-5,-14,5,3,11,14,-6,-5,10,-8,0,6,5,6,5,-6,-9,-13,12,2,1,-10,13,13,4,-14,0,-2,0,-5,13,10,-12,-5,-9,-15,-13,-8,-13,12,-1,-6,3,11,7,-14,-9,14,10,10,-7,-4,-15,-9,-6,4,-15,2,10,-8,12,0,9,-14,11,-15,8,13,14,10,2,-9,-10,13,-13,12,14,-15,3,1,11,12,12,11,10]
'''
Solution using dictionnaries, not fast enough even after I spent sometime optimizing whiel measuring the execution time with %timeit

        dict_single = {}
        dict_pair = {}
        result = []

        num.sort()

        # this loop has a O(n^2) run time
        for i in range(len(num)):
            dict_single[num[i]] = 0
            for j in range(i+1,len(num)):
                dict_pair[(num[i],num[j])] = num[i] + num [j]

        for i in range(len(num)):
            dict_single[num[i]] += 1

        for key in dict_pair.keys(): #O(n^2)
            #if - dict_pair[key] in dict_single.keys(): # this O(n) for sure
            #if dict_single.has_key(-dict_pair[key]):    # is this O(n) I believe it shoudl be O(1)
            #if  - dict_pair[key] in dict_single: # O(1) ?
            if - dict_pair[key] in dict_single:
                triplet = [key[0], key[1], - dict_pair[key]]
                #triplet_sorted = [key[0], key[1], - dict_pair[key]]
                #triplet_sorted.sort()
                #if triplet == triplet.sort():
                if triplet[0] <= triplet[1] and triplet[1] <= triplet[2]:
                    if key[0] == triplet[2] or key[1] == triplet[2]:
                        # there there are two identical elements in the solution, need to check if it can acutally be built 
                            # find which is the one that appears twice, then check if it's there twice in the array via dict_single
                        if key[0] == triplet[2]:
                            appears_twice = key[0]
                        elif key[1] == triplet[2]:
                            appears_twice = key[1]
                        if dict_single[appears_twice] > 1:
                            result.append(triplet)                        
                    else:
                        result.append(triplet) 
'''                        


