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
        ch = []
        def dfs(i):
            if i == len(digits):
                a = ch.copy()
                concat = ''.join(a)
                if len(concat) == len(digits):
                    res.append(concat)
                return

            for j in range(i, len(digits)):
                for nei in mp[digits[j]]: # def
                    ch.append(nei)
                    dfs(j+1)
                    ch.pop()
        
        dfs(0)
        return res






