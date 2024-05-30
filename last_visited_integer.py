class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k = 0
        for val in range(len(nums)):
            if (nums[val] > 0):
                seen.insert(0,nums[val])
                k=0
            elif (nums[val] == -1):
                k+=1
                if (k <= len(seen)):
                    ans.append(seen[k-1])
                else:
                    ans.append(-1)  
        return ans