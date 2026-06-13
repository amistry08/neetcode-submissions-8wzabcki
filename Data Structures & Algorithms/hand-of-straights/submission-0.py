class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        n = len(hand) / groupSize

        if len(hand) % groupSize > 0:
            return False

        while n > 0:
            curr = hand[0]
            for i in range(groupSize):
                if curr in hand:
                    hand.remove(curr)
                    curr += 1
                else:
                    return False
            n -= 1
        
        return True
        
