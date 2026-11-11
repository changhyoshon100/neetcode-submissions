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
        subsets = []

        def dfs(i):
            if i == len(digits):
                cp = subsets.copy()
                st = ''.join(cp)
                res.append(st)
                return
            
            for ch in mp[digits[i]]:
                subsets.append(ch)
                dfs(i+1)
                subsets.pop()
        dfs(0)
        return res


            