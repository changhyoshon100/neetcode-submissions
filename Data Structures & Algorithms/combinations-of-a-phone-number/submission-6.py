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
                res.append(''.join(ch))
                return

            for nei in mp[digits[i]]: # def
                ch.append(nei)
                dfs(i+1)
                ch.pop()
        
        dfs(0)
        return res

