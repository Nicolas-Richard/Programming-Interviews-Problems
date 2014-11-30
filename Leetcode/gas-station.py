

# The O(n) solution was hard to understand, need to convince yourself that the best place to start is the station after the one you will reach with the minimum level of fuel. See : https://oj.leetcode.com/discuss/5776/got-tle-on-python-solution-is-there-a-faster-one?show=6065#a6065
# The brute force method doesn't pass Leetcode's tests, I get a Time Limit Exceeded error, not surprising given a O(n^2) complexity.
# https://oj.leetcode.com/problems/gas-station/


class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer


    def canCompleteCircuit(self, gas, cost):

        tank = 0
        min_level = 0
        min_index = 0 

        for i in range(len(gas)):
            tank += gas[i]
            tank -= cost[i]

            if tank <= min_level:
                min_level = tank
                min_index = i

        if tank <0:
            return -1
        else : 
            return (min_index +1)%len(gas)





    def canCompleteCircuit_brute_force(self, gas, cost):
        tank = 0
        N = len(gas)
        gas = gas + gas
        cost = cost + cost

        for j in range(0,N): # length of the circuit
            tank = 0

            #print '-'*10
            #print 'attempt starting at station %d' %(j)
            #print 'circuit'
            #print cost[j:len(gas)/2+j]
            #print 'gas'
            #print gas[j:len(gas)/2+j]

            for i in range(0,N): 
                tank = self.canGoToNextStation(gas[j:len(gas)/2+j],cost[j:len(gas)/2+j],tank,i)
                if tank < 0:
                    break
                #else:   
                    #print tank

            if tank >0:               
                #print j
                return j 
                break        
        
    def canGoToNextStation(self, gas, cost, tank=0, current_station=0):

        tank += gas[current_station]
        if cost[current_station]> tank:
            return -1
        elif cost[current_station]<= tank:
            tank -= cost[current_station]
            return tank
            



s=Solution()       
 
gas = [1,2,1]
cost = [2,1,1]   

#print s.canGoToNextStation(gas,cost,0,0)
#print s.canGoToNextStation(gas,cost,0,1)

s.canCompleteCircuit_brute_force(gas,cost)

    