"""
Problem Description
A queue is a data structure that follows the First In First Out principle (FIFO). That is, an element inserted into the queue first, can be retrieved first.

In this problem, you will perform some operations on queue.

There are Q queries. Each query can be of two types -

Insert an element into the queue.

Remove the first element of the queue and return it.

Note that you are not expected to create a queue from scratch, but use the queue data structure and its accompanying methods. Also, there will be no scenario to remove from an empty queue.

Input format
There are Q+1 lines of input

First line contains Q, number of queries.

Next Q lines will contain either of the following -

1 X - insert X in the queue.

2 - remove the first element of the queue and return it.

Output format
For each query of the second type print the first element.

Sample Input 1
5
1 3
1 2
2
1 1
2

Sample Output 1
3
2

Constraints
1 <= Q <= 100

-10^5 <= X <= 10^5
"""
from collections import deque


class Solution:
    """Provide queue operations for insert and front-removal queries."""

    def __init__(self):
        """
        Initialize an empty queue.

        We use `collections.deque` because:
        - Insertion at the back is O(1)
        - Removal from the front is O(1)
        """
        self.queue = deque()

    def insert(self, num: int) -> None:
        """
        Insert an element at the back of the queue.

        This models query type `1 X`, where `X` is appended and waits its turn.
        """
        self.queue.append(num)

    def getFirst(self) -> int:
        """
        Remove and return the first element from the queue.

        This models query type `2`, which always pops from the front (FIFO order).
        """
        return self.queue.popleft()
