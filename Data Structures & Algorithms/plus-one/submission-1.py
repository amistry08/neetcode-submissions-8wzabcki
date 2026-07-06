class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for n in digits:
            num += str(n)
        num = 1 + int(num)
        return [int(x) for x in str(num)]