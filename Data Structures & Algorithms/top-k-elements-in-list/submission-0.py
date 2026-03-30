class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans=[]
        for i in nums:
            count[i] = 1 + count.get(i,0)

        for i in sorted(count.items(), key=lambda items:items[1], reverse=True):
            if k==0:
                break
            else:
                ans.append(i[0])
                k+=-1

        return ans