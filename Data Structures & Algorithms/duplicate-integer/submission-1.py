class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = {}
        for i in nums:
            if i in ans:
                print(i)
                return True
            ans[i] = 1
        return False