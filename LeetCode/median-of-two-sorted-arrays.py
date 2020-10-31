"""
Runtime: 88 ms, faster than 84.24% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.4 MB, less than 11.15% of Python3 online submissions for Median of Two Sorted Arrays.
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
"""
#SOLUTION
for _ in range(int(input())):
    nums1 = list(map(int, input().split(' ')))
    nums2 = list(map(int, input().split(' ')))
    for j in range(len(nums2)):
        nums1.append(nums2[j])
    nums = sorted(nums1)
    med = int(len(nums)/2)
    print(nums)
    if len(nums)%2!=0:
        print(nums[med])
    else:
        med = (nums[med]+nums[med-1])/2
        print(med)
"""
SUBMITTED
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for j in range(len(nums2)):
            nums1.append(nums2[j])
        nums = sorted(nums1)          
        med = int(len(nums)/2)                
        if len(nums)%2!=0:
            return nums[med]
        else:
            med = (nums[med]+nums[med-1])/2     
            return med
"""
