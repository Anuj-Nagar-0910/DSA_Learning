"""
Problem Description
Given a linked list, split it into two lists such that all the nodes with even data are in one list and the ones with odd data are in another list.


Make sure that the nodes appear in the same order in which they are present in the original list. For instance, for 1, 2, 3, 4, 5, odd data nodes have to be 1, 3, 5 and not 1, 5, 3 for the tests to pass.


Note that input and output are being handled by a main() method behind the scenes, so you do NOT have to implement the main() method or any I/O here.


You’d have to implement the function defined in the stub, and return the answer based on the return type of the function.


The structure of the linked list is given as a reference for you while writing the code. Do not make any modifications to it, or any of the rest of the stub, or the tests would fail.


Input format
There are two lines of input.

First line contains the N size of the linked list.

Next line contains N space separated integers describing the linked list.

Output format
Print the list with odd elements in the first line and the list with even elements in the second line.

Sample Input 1
5

1 3 2 4 5

Sample Output 1
1 3 5

2 4
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def split_linked_list(head):
    odd_head = odd_tail = None
    even_head = even_tail = None

    current = head
    while current:
        if current.data % 2 != 0:
            if odd_head is None:
                odd_head = current
                odd_tail = current
            else:
                odd_tail.next = current
                odd_tail = current
        else:
            if even_head is None:
                even_head = current
                even_tail = current
            else:
                even_tail.next = current
                even_tail = current
        current = current.next

    if odd_tail:
        odd_tail.next = None
    if even_tail:
        even_tail.next = None

    return odd_head, even_head


def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(str(current.data))
        current = current.next
    print(" ".join(result))


def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head