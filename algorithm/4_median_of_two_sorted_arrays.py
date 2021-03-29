from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
         m = len(nums1)
         n = len(nums2)
         sum = m + n
         if sum % 2 ==0:
            need No. sum/2 and sum/2 + 1, need to search sum // 2 + 1
         else:
            need No. (sum + 1) / 2, need to search sum // 2 + 1
        '''

        len_nums1, len_nums2 = len(nums1), len(nums2)
        sum = len_nums1 + len_nums2
        left, right = 0, 0
        index_nums1, index_nums2 = 0, 0

        for i in range(0, sum // 2 + 1):
            left = right
            if index_nums1 < len_nums1 and (index_nums2 >= len_nums2 or nums1[index_nums1] <= nums2[index_nums2]):
                right = nums1[index_nums1]
                index_nums1 = index_nums1 + 1
            else:
                right = nums2[index_nums2]
                index_nums2 = index_nums2 + 1
        if sum % 2 == 0:
            return (left + right) / 2
        else:
            return right


if __name__ == "__main__":
    solution = Solution()
    res = solution.findMedianSortedArrays([1, 2], [3, 4])
    print(res)
