def Reverse(head):
    cur_node = head
    prev = head
    while cur_node is not None:
        prev = cur_node
        cur_node = cur_node.next
        prev.next = head
        head = prev
        if head.next == head:
            head.next = None            
    return head
        

  