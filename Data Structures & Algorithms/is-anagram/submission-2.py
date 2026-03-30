class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictA = {}
        dictB = {}
        for c in s:
            if c in dictA:
                print("here," ,dictA[c])
                dictA[c] = 1 + dictA[c]
            else:
                dictA[c] = 1
        for c in t:
            if c in dictB:
                dictB[c] = 1 + dictB[c]
            else:
                dictB[c] = 1
        print(dictA, dictB)
        if dictA == dictB:
            return True
        else:
            return False
        