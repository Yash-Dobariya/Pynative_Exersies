
class Linked_list:

    
    
    def connect(self,head):
        b=head
        slow=fast=head

        while fast and next(b):
           slow =  next(b)
           fast = next(b)
            
        if fast==slow:
            print(" True")
        print("False")

a=Linked_list()
head = [3,2,0,-4]
print(a.connect(head))




class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(1)
b = ListNode(2)

a.next = b
b.next = a

class Solution:
    def hasCycle(self, head:bool [ListNode]) -> bool:

        slow=head
        fast=head
        head = [3,2,0,-4]

        while(fast  and  next(fast)):
            slow=next(slow)
            fast=next(fast) 
            
            if slow == fast:
                return True
        return False

soulution1 = Solution()

soulution1.hasCycle(a)


# def asd(a: int,b: int,c: int) -> int:

