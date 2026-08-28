from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = defaultdict(int)
        for c in s1:
            mp[c] += 1

        need = len(mp)

        for i in range(len(s2)):
            mp2 = defaultdict(int)
            cur = 0

            for j in range(i, len(s2)):
                ch = s2[j]

                if ch not in mp:
                    break

                mp2[ch] += 1

                if mp2[ch] > mp[ch]:
                    break

                if mp2[ch] == mp[ch]:
                    cur += 1

                if cur == need:
                    return True

        return False