'''

http://www.geeksforgeeks.org/median-of-two-sorted-arrays/

http://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
'''


class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):

        if len(A) != len(B):
            return 'stop, doesn\'t work with array of unequal sizes'
         
        if not A:
            return self.findMedianSortedArrays(B,B)
        if not B:
            return self.findMedianSortedArrays(A,A)

        #print A,B

        m1 = self.median(A)
        m2 = self.median(B)

        #print m1,m2

        if m1 == m2:
            return m1

        elif len(A) == 1 and len(B) == 1:
            return (A[0] + B[0])/2.       

        elif len(A) == 2 and len(B) == 2:
            return (max(A[0],B[0]) + min(A[1],B[1]))/2.

        elif m1 < m2:
            if len(A) % 2 == 0:
                return self.findMedianSortedArrays(A[len(A)/2:], B[:len(B)/2])
            else:
                return self.findMedianSortedArrays(A[len(A)/2:], B[:len(B)/2+1])  

        elif m1 > m2:
            if len(A) % 2 == 0:
                return self.findMedianSortedArrays(A[:len(A)/2], B[len(B)/2:])
            else:
                return self.findMedianSortedArrays(A[:len(A)/2+1], B[len(B)/2:])    

  
    
    def median(self, A):
        if len(A)%2 == 0:
            return (A[len(A)/2-1] + A[len(A)/2])/2.
        else:
            return A[len(A)/2]            


s = Solution()


'''
# testing the median is the mean of the two middle values

from random import randint

for j in range(10):

    n = randint(1,10)
    A = []
    for i in range(n):
        A.append(randint(1,1000))
    A.sort()    

    B=[]
    for i in range(n):
        B.append(randint(1,1000))
    B.sort()

    real_result = A+B
    real_result.sort()
    real_result = s.median(real_result)
    print 'length of the arrays: %d' %(n)
    if not real_result == s.findMedianSortedArrays(A,B):
        print A
        print B
    else:
        print True    '''


'''

A comment I posted on why the test sometimes return false

Hey Everyone,

In Method 2, it's not clear to me what definition of the median is used in the case where the median is not unique.

"If there is an even number of observations, then there is no single middle value;" from http://en.wikipedia.org/wiki/M...

Method 2 sometimes returns a value that is a correct median but which is not the the mean of the two middle values.

Anyone is aware of this ? It's not necessarily a big deal, I'm just wondering if it's true of if i'm missing something.

An example :

[371, 470, 750, 873] [70, 491, 535, 746]

m1 = 610.0 m2= 513.0

[371, 470] [535, 746]

Then we pick our median (470 + 535)/2 = 502.5

Which is a correct choice for the median as the full array is:

[70, 371, 470, 491, 535, 746, 750, 873]

which is correctly divided in two halves by 502.5

However the the mean of the two middle values is (491 + 535)/2 = 513.0

Thanks for your help.

Nicolas


'''


# testing if the median is a good pick in the sense that it divides properly the array

from random import randint

for j in range(10):

    n = randint(1,100)
    A = []
    for i in range(n):
        A.append(randint(1,1000))
    A.sort()    

    B=[]
    for i in range(n):
        B.append(randint(1,1000))
    B.sort()

    C = A+B
    C.sort()

    my_median = s.findMedianSortedArrays(A,B)

    print 'length of the arrays: %d' %(n)
    if not C[n-1] <= my_median and my_median <= C[n]:
        print A
        print B

'''

I found out, that it's not always a good pick either !

One example :

A = [8, 52, 86, 93, 112, 139, 139, 153, 155, 164, 190, 195, 250, 259, 275, 276, 301, 304, 344, 349, 357, 369, 374, 375, 381, 383, 388, 389, 403, 405, 452, 494, 554, 582, 584, 630, 661, 688, 706, 711, 712, 727, 736, 744, 753, 758, 760, 763, 783, 816, 834, 847, 857, 862, 867, 895, 896, 913, 924, 929, 936, 939, 947, 975, 976, 979, 981, 987]

B = [18, 23, 32, 38, 72, 95, 132, 206, 216, 216, 222, 234, 236, 241, 266, 274, 286, 312, 329, 361, 364, 372, 396, 461, 476, 515, 527, 532, 545, 552, 560, 569, 573, 575, 600, 603, 607, 612, 615, 619, 623, 624, 643, 663, 694, 710, 720, 720, 738, 746, 756, 787, 792, 799, 806, 811, 836, 874, 877, 885, 902, 903, 906, 909, 918, 931, 970, 992]

my code returns : 579.5

But the actual median is 583.0

C[n-3:n+3] : [573, 575, 582, 584, 600, 603]

At this point I can only conclude that my code is wrong :D

'''

