"""
Problem Description
Given a linked list and an element X, find if there exists a node in the linked list with data equal to X.


Note that input and output are being handled by a main() method behind the scenes, so you do NOT have to implement the main() method or any I/O here.


You’d have to implement the function defined in the stub, using the arguments, and returning the answer based on the return type of the function.


The structure of the linked list is given as a reference for you while writing the code. Do not make any modifications to it, or any of the rest of the already given stub.


Input format
There are three lines of input.

First line contains N, the size of the linked list.

Next line contains N space separated integers describing the linked list.

Next line contains a single integer X.

Output format
Print "true" if the element is present in the linked list else print "false".

Sample Input 1
5

1 2 3 4 5

2

Sample Output 1
true

Constraints
1 <= N <= 200
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search(head, x):
    current = head
    while current:
        if current.data == x:
            return True
        current = current.next
    return False

def main():
    n = int(input())
    values = list(map(int, input().split()))
    x = int(input())

    head = None
    tail = None
    for val in values:
        new_node = Node(val)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    result = search(head, x)
    print("true" if result else "false")

if __name__ == "__main__":
    main()