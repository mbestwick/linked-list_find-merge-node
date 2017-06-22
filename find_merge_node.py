"""
Given pointers to the head nodes of 2 linked lists that merge together at some
point, find the Node where the two lists merge. It is guaranteed that the two
head Nodes will be different, and neither will be NULL.

In the diagram below, the two lists converge at Node x:

[List #1] a--->b--->c
                     \
                      x--->y--->z--->NULL
                     /
     [List #2] p--->q

Complete the int FindMergeNode(Node* headA, Node* headB) method so that it finds
and returns the data value of the Node where the two lists merge.

Input Format
The FindMergeNode(Node*,Node*) method has two parameters, headA and headB, which
are the non-null head Nodes of two separate linked lists that are guaranteed to
converge.
Do not read any input from stdin/console.

Output Format
Each Node has a data field containing an integer; return the integer data for
the Node where the two lists converge.
Do not write any output to stdout/console.

"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


def FindMergeNode(headA, headB):
    # traverse listA and add all nodes to a set
    setA = set()
    while headA:
        setA.add(headA)
        headA = headA.next
    # traverse listB, and at each node check if it exists in the set
    while headB:
    # if so, return the data of that node
        if headB in setA:
            return headB.data
    # otherwise, keep traversing
        else:
            headB = headB.next
