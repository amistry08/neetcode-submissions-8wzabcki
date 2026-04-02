class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * i for i in stones]
        heapq.heapify(heap)

        if len(heap) < 2:
            return -1 * heap[0]

        while len(heap) > 1:
            
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            
            if x and y:
                if x > y:
                    heapq.heappush(heap, y-x)
                if x < y:
                    heapq.heappush(heap, x-y)

        return -1 * heap[0] if len(heap) > 0 else 0
            




        