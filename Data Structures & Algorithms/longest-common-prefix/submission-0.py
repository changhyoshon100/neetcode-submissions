class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        L = 0
        minlen = 10000
        for i in range(len(strs)):
            minlen = min(minlen, len(strs[i]))
        
        k = 0
        letter = strs[0]
        for i in range(minlen):
            ch = letter[k]
            
            for j in range(1, len(strs)):
                if ch != strs[j][k]:
                    return res
            res += ch
            k+=1   

        return res

                
            
            

