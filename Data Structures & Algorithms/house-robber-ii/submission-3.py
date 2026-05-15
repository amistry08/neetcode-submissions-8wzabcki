class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for n in range(0, len(nums)-1):
            temp = max(one + nums[n], two)
            one = two
            two = temp
        three, four = 0, 0
        for n in range(1, len(nums)):
            temp = max(three + nums[n], four)
            three = four
            four = temp
        
        return max(nums[0], two, four)