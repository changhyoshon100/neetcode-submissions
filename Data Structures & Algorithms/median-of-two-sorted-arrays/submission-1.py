class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = (total + 1) // 2

        left, right = 0, len(nums1)

        while left <= right:
            partitionA = left + (right - left) // 2
            partitionB = half - partitionA

            Aleft = nums1[partitionA - 1] if partitionA > 0 else float("-inf")
            Aright = nums1[partitionA] if partitionA < len(nums1) else float("inf")

            Bleft = nums2[partitionB - 1] if partitionB > 0 else float("-inf")
            Bright = nums2[partitionB] if partitionB < len(nums2) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return max(Aleft, Bleft)

                return (
                    max(Aleft, Bleft) +
                    min(Aright, Bright)
                ) / 2

            elif Aleft > Bright:
                right = partitionA - 1

            else:
                left = partitionA + 1