"""
Problem Description
In this problem, you’ll learn to implement functions to insert a node at the beginning and end of a linked list.


Note that input and output are being handled by a main() method behind the scenes, so you do NOT have to implement the main() method or any I/O here.


You’d have to implement the insertAtEnd and insertAtBeginning functions defined in the stub, using the arguments, and returning the answer based on the return type of the functions.


The structure of the linked list is given as a reference for you while writing the code. Do not make any modifications to it.


Input format
There are Q+1 lines of input.

First line contains Q, number of queries.

Each of the next Q lines contains 2 integers, representing the type of query and the data.

A query 1 3 means to insert 3 at the beginning of the LL.

A query 2 6 means to insert 6 at the end of the LL

Output format
After each query print the linked list where each node's data is printed separated by space.

Sample Input 1
5

1 2

1 3

2 7

1 9

2 11

Sample Output 1
2

3 2

3 2 7

9 3 2 7

9 3 2 7 11

Constraints
1 <= Q <= 20
"""
class Node:
    """A node in a singly linked list."""

    def __init__(self, data):
        """Initialize a node with the given data and no next node.

        Args:
            data: The value stored in this node.
        """

        self.data = data
        self.next = None


def insertAtEnd(head, data):
    """Insert a node with the given data at the end of the linked list.

    Args:
        head: The head node of the linked list, or None for an empty list.
        data: The value to add to the end of the list.

    Returns:
        The head node of the updated linked list.
    """
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head


def insertAtBeginning(head, data):
    """Insert a node with the given data at the beginning of the linked list.

    Args:
        head: The head node of the linked list, or None for an empty list.
        data: The value to add to the beginning of the list.

    Returns:
        The new head node of the updated linked list.
    """
    new_node = Node(data)
    new_node.next = head
    return new_node


def print_list(head):
    """Print the values stored in the linked list from head to tail.

    Args:
        head: The head node of the linked list.
    """
    result = []
    current = head
    while current:
        result.append(str(current.data))
        current = current.next
    print(' '.join(result))


def main():
    """Read queries and perform linked list insert operations."""
    q = int(input())
    head = None
    for _ in range(q):
        query_type, data = map(int, input().split())
        if query_type == 1:
            head = insertAtBeginning(head, data)
        elif query_type == 2:
            head = insertAtEnd(head, data)
        print_list(head)

if __name__ == "__main__":
    main()