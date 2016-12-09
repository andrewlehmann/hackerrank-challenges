"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    cur_node = head
    result = []
    while cur_node is not None:
        result.append(cur_node.data)
        cur_node = cur_node.next
    result.reverse()
    for num in range(0, len(result)):
        print result[num]

  