# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s = 1
        l = n
        
        while s <= l:
            m = (s+l)//2
            # guess is higher
            if guess(m) == -1:
                l = m - 1
            elif guess(m) == 1:
                s = m + 1
            else:
                return m