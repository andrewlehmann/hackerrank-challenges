#Body
"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def equalityCheck(first, other):
    var = 1
    if first is None:
        if other is not None:
            var = 0
    elif other is None:
        if first is not None:
            var = 0
    else:
        var = first.data == other.data
    return var

def notEqual(first, other):
    return not equalityCheck(first, other)

def CompareLists(headA, headB):
    cur_nodeA = headA
    cur_nodeB = headB
    while cur_nodeA is not None and cur_nodeB is not None:
        if cur_nodeA.data != cur_nodeB.data:
            return 0
        cur_nodeA = cur_nodeA.next
        cur_nodeB = cur_nodeB.next
    return int(cur_nodeA == None and cur_nodeB == None)
        