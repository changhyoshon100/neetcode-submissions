class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        # mp[digits[i]] -> def , ghi
        # for ch in mp[digits[i]]:
        
        def dfs(i, ch):
            if i == len(digits):
                res.append(ch)
                return 

            for c in mp[digits[i]]:
                dfs(i+1, ch + c)
            
            return res
        
        return dfs(0, "")
        