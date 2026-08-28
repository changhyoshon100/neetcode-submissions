class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        mp = {
            'A':'a',
            'B':'b',
            'C':'c',
            'D':'d',
            'E':'e',
            'F':'f',
            'G':'g',
            'H':'h',
            'I':'i',
            'J':'j',
            'K':'k',
            'L':'l',
            'M':'m',
            'N':'n',
            'O':'o',
            'P':'p',
            'Q':'q',
            'R':'r',
            'S':'s',
            'T':'t',
            'U':'u',
            'V':'v',
            'W':'w',
            'X':'x',
            'Y':'y',
            'Z':'z',

        }
        new_s = ""
        for i in range(len(s)):
            
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9') or (s[i] >= 'A' and s[i] <= 'Z'):
                if (s[i] >= 'A' and s[i] <= 'Z'):
                    new_s += mp[s[i]]
                    continue
                new_s += s[i]
            
        L = 0
        R = len(new_s) - 1
        # print(new_s)
        while L < R:
            # print(new_s[L], new_s[R])
            if new_s[L] != new_s[R]:
                return False
            
            L += 1
            R -= 1
            
        return True
                

        
































