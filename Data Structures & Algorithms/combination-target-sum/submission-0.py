class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(curr_sum):
            if curr_sum > target:
                return []
            if curr_sum == target:
                res.append(subset.copy())
            
            for i in nums:
                subset.append(i)
                dfs(i+curr_sum)
                subset.pop()

        def remove_duplicates(lst):
            seen = set()
            result = []

            for sublist in lst:
                key = tuple(sorted(sublist))
                if key not in seen:
                    seen.add(key)
                    result.append(sublist)
            
            return result

        dfs(0)
        return remove_duplicates(res)
    

    