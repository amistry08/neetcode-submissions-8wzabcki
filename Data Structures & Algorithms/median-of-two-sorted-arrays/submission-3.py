class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        print(nums)
        
        if len(nums) <= 0:
            return nums[0]

        m = len(nums) // 2
        if len(nums) % 2 == 1:
            return nums[m]
        else:
            return (nums[m] + nums[m-1]) / 2