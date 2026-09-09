class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        cnt = 0

        while sum(target) > 0:
            in_segment = False

            for i in range(len(target)):
                if target[i] > 0:
                    target[i] -= 1

                    if not in_segment:
                        cnt += 1
                        in_segment = True

                else:
                    in_segment = False

        return cnt