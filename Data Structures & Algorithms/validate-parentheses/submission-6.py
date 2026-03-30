class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in s:
            if(i == '(' or i == "{" or i == "["):
                res.append(i)
            else:
                if(len(res) > 0):
                    if( (i == "]" and res[-1] == "[") or (i == "}" and res[-1] == "{") or (i == ")" and res[-1] == "(")):
                        res.pop()
                        continue
                    else:
                        return False
                else:
                    return False
        return True if len(res) == 0 else False
                    
