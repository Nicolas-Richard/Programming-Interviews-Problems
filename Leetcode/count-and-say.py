class Solution:
    # @return a string
    def countAndSay(self, n):
        
        result='1' 

        for i in range(1,n):
            result=self.CAS1(result)

        return result

    def CAS1(self, stri):
        count=1
        result=''
        for i in range(len(stri)):
            try:    
                if stri[i]==stri[i+1]:
                    count+=1
                else:
                    result += str(count)+stri[i]
                    count=1
            except:
                result += str(count)+stri[i]


        return result



s=Solution()

print s.countAndSay(2)              