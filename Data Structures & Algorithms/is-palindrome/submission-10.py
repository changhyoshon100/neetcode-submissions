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
        sentence = ""

        for i in range(len(s)):
            if s[i] in mp:
                sentence += mp[s[i]]
            elif s[i] >= 'a' and s[i] <= 'z' or s[i] >= '0' and s[i] <= '9':
                sentence += s[i]
            else:
                continue
        
        for i in range(len(sentence) // 2):
            # print(sentence[i], sentence[len(sentence) - i - 1])
            if sentence[i] != sentence[len(sentence) - i - 1]:
                return False
        return True







