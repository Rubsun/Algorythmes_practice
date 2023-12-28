class Node:
   def __init__(self, x):
       self.val = x
       self.next = None

#Заяц и черепаха
def hasCycle(head: Node):
    if head is None:
        return False

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        if fast.next == fast:
            return False
        if slow == fast:
            return True
        
        slow = slow.next
        fast = fast.next.next

    return False