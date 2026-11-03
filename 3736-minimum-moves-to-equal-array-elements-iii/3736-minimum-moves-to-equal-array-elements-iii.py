class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxum=max(nums)
        ans=0
        for i in nums:
            ans+=maxum-i
        return ans
       
        