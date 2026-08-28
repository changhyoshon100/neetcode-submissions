class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        
        s_strim = ''
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
        for i in range(len(s)):
            if 'a' <= s[i] <= 'z' or '0' <= s[i] <= '9':
                s_strim += s[i]
            elif 'A' <= s[i] <= 'Z':
                s_strim += mp[s[i]]
            else:
                continue
        print(s_strim)
        R = len(s_strim) - 1
        while L < R:
            if s_strim[L] != s_strim[R]:
                return False
            L += 1
            R -= 1
        return True

