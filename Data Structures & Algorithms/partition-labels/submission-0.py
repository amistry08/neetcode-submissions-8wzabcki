class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashT = {}
        res = []
        for c in s:
            hashT[c] = 1 + hashT.get(c, 0) 
        
        curr = set()
        i = 0
        j = 0
        while i < len(s):
            j += 1
            curr.add(s[i])
            hashT[s[i]] -= 1
            if hashT[s[i]] == 0:
                curr.remove(s[i])
                if len(curr) == 0:
                    res.append(j)
                    j = 0
            i += 1
    
        return res

