class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        L,R = 0, len(people) - 1
        ans = 0
        while L <= R:
            remain = limit - people[R]
            ans += 1
            R -= 1

            if L <= R and remain >= people[L]:
                L += 1
        return ans
