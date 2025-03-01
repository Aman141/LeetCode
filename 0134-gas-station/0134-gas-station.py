class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        gas_left = 0
        start = 0
        for i in range(len(gas)):
            gas_left += gas[i] - cost[i] 
            if gas_left<0:
                gas_left = 0
                start = i+1

        return start        
        