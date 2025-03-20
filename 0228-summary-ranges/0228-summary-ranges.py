class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        ans = []
        s = str(nums[0])
        count = 0
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1]>1 and count !=0:
                s += f"->{nums[i-1]}"
                ans.append(s)
                s = str(nums[i])
                count = 0
            elif nums[i]-nums[i-1]>1 and count == 0:
                ans.append(s)
                s = str(nums[i])
            else:
                count += 1 
                continue        
                
        if count == 0:
            ans.append(s)
        else:
            ans.append(s + f"->{nums[-1]}")    

        return ans        
