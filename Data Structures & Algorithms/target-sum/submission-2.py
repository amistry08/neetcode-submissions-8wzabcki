class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        def dfs(i, total):
            if i == len(nums) - 1:
                if total == target:                 
                    nonlocal count
                    count += 1
                    return
                
                if total != target:
                    return

            if i < len(nums):
                dfs(i+1, total + nums[i+1])
                dfs(i+1, total + (-1 * nums[i+1]))
            else:
                return

        dfs(-1,0)
        return count
            
