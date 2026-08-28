class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        L,R = 0, len(people) - 1
        ans = 0
        people.sort()
        while L <= R:
            if people[L] + people[R] <= limit:
                L += 1
            ans += 1
            R -= 1
        return ans