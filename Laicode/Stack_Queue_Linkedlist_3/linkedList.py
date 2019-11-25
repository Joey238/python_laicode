

class Node:  #ListNode
    
    def __init__(self, value):
        self.value =  value
        self.next = None
        

def reverse_linkedList(head):
    if not head or not head.next:
        return 
    
    pre = None
    current = head
    while current:
        next = current.next #first: never lose control of next
        current.next = pre
        pre = current
        current = next
        
    return pre  #最后头是pre

        
def reverse_linkedList_rec(head):
    if not head.next:
        return head
    
    new_head = reverse_linkedList(head.next)
    head.next.next = head
    head.next = None

    return new_head


if __name__ == '__main__':
    
    node1 = Node(1)
    node1.next = Node(2)
    node2 = node1.next
    node2.next = Node(3)
    node3 = node2.next
    node3.next = Node(4) 
    
    
    new_head = reverse_linkedList(node1)
    print(new_head.value)    
    
    