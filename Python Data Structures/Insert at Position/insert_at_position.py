"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    cur_node = head
    if position == 0:
        temp = cur_node
        cur_node = cur_node.next
        head = cur_node
    else:
        for num in range(0, position-1):
            cur_node = cur_node.next
        prev = cur_node
        cur_node = cur_node.next
        after = cur_node.next
        prev.next = after
        del cur_node
    return head
  
  
  