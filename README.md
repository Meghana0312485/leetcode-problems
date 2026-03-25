problem 55
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
        return True





problem 92
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        result = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return result
        

problem 1

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        for i in range(len(nums)):
           for j in range(i+1,len(nums)):
              if((nums[i]+nums[j]) ==target):
                  return [i,j]
        return       
                          
problem 2

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

                                       problem 3
          

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mx,start,chars=0,0,{}
        for i in range (len(s)):
            if s[i]in chars and start<=chars[s[i]]:
                start=chars[s[i]]+1
            else:
                mx=max(mx,i-start+1)
            chars[s[i]]=i
        return mx

                                  problem 15

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

                            **problem 30**

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            right = i
            curr_count = Counter()
            window_count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    curr_count[word] += 1
                    window_count += 1

                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                        window_count -= 1

                    if window_count == len(words):
                        result.append(left)
                else:
                    curr_count.clear()
                    window_count = 0
                    left = right

        return result
        
        problem 42

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        right = [0]*n
        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        water_trapped = 0
        for i in range(0, n):
            water_trapped += max(0, min(left[i], right[i]) - height[i])
        return water_trapped
       
        
        problem 41:first missing poostive
        
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsset=set(nums)
        smallestpositive = 1
        while smallestpositive in numsset :
            smallestpositive += 1
        return smallestpositive 

        problem 4
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=sorted(nums1+nums2)
        n= len(arr)
        if(n%2==0):
            mid1=arr[n//2-1]
            mid2=arr[n//2]
            return(mid1+mid2)/2
        else:
            return(arr[n//2])
        
        return
    problem 7 
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        sign = -1 if x < 0 else 1
        x *= sign
        reversed_num = int(str(x)[::-1])
        result = sign * reversed_num
        if result < -2**31 or result > 2**31 - 1:
           return 0
        return result
        
    problem 268 
  class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        return n*(n+1)//2-sum(nums)

problems 3731
   class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        nums.sort()
        for i in range(nums[0],nums[-1]):
            if i not in nums:
                res.append(i)
        return res   
        
problem 58
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[-1]) if words else 0

problem number 78
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        n=len(nums)
        for i in range (1<<n):
            s=[]
            for j in range (n):
                if i&(1<<j):
                    s.append(nums[j])
            res.append(s)
        return res
        
problem number 76
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if not s or not t:
            return ""

        t_count = Counter(t)
        required = len(t_count)
        formed = 0

        window_counts = {}
        min_len = float('inf')
        min_window = (0, 0)
        left = 0

        for right in range(len(s)):
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in t_count and window_counts[character] == t_count[character]:
                formed += 1

            while formed == required and left <= right:
                character = s[left]
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = (left, right)

                window_counts[character] -= 1
                if character in t_count and window_counts[character] < t_count[character]:
                    formed -= 1
                left += 1

        left, right = min_window
        return "" if min_len == float('inf') else s[left:right + 1]

problem number 115
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        
        for i in range(m + 1):
            dp[i][0] = 1
        
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        
        return dp[m][n]

problem number 179
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        c=""
        arr=nums[::-1]
        for i in arr:
            c=c+str(i)
        return c
problem 181
# Write your MySQL query statement below
SELECT e1.name AS Employee
FROM Employee e1
JOIN Employee e2
ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;

        
