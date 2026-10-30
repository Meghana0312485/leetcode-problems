# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        mid=(count/2)+1
        temp=head
        for i in range(mid-1):
            temp=temp.next
        return temp


        