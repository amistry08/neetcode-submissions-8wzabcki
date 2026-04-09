class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i,cur):
            print(cur)
            if len(cur) == len(nums):
                res.append(cur.copy())

            for n in nums:
                if n in cur:
                    continue
                cur.append(n)
                dfs(i+1, cur)
                cur.pop()

        dfs(0, [])
        return res
