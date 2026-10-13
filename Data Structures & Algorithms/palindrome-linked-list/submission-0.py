# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        def reverseList(reverseHead):
            tmp = reverseHead
            prev = None

            while(tmp):
                temp = tmp.next
                tmp.next = prev
                prev = tmp
                tmp = temp
            return prev
        
        eol = reverseList(slow)

        while(eol != head and head and eol):
            if(head.val != eol.val):
                return False
            eol = eol.next
            head = head.next
        
        return True