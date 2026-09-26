class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idxm = m - 1
        idxn = n - 1
        idxl = m + n - 1

        for i in range(idxl, -1, -1):
            if idxm >= 0 and idxn >= 0:
                if nums1[idxm] > nums2[idxn] and idxm >= 0 and idxn >= 0:
                    nums1[i] = nums1[idxm]
                    idxm -= 1
                else:
                    nums1[i] = nums2[idxn]
                    idxn -= 1
            elif idxm < 0:
                nums1[i] = nums2[idxn]
                idxn -= 1
            else:
                nums1[i] = nums1[idxm]
                idxm -= 1
        