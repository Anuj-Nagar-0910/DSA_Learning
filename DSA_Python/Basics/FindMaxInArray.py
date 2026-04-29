"""
Problem Description
You are given Q queries. Each query can be of two types -

Insert an element in an array.

Remove the maximum element of the array,and return it.


Note that you will first have to choose the data structure you’re going to use and define it as a class variable before you write the logic for the methods. This data structure should then be accessible to all methods of the class.


You’ll then have to implement the insert() and getMax() methods using the data structure you defined.


You do not have to write the main method, or worry about input output - that is handled behind the scenes. You have to ensure that you use the arguments to the functions and return the output based on the return type of the functions.

Input format
There are Q+1 lines of input

First line contains Q, the number of queries.

Next Q lines will contain any of these two formats :

1 3 - Meaning - insert element 3 in the array

2 - Meaning remove the maximum element in the array and return it.

Output format
For each query of the second type print the maximum element inside the array.

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

Explanation
Note that there will be no output for query type 1, thus, we get outputs for only the two queries of type 2.

In the first query, the array will be [3, 2] and thus, the largest element in the array will be 3, which is removed and returned. In the second query, the array will be [2, 1], and thus, the largest element is 2, which is removed and returned.

Constraints
1 <= Q <= 10^5

-10^9 <= X <= 10^9
"""
import heapq as h
max_heap = []
def insert(num: int) -> None:
      h.heappush(max_heap, -num)

def getMax() -> int:
      if not max_heap:
            return -1
      return -h.heappop(max_heap)

insert(3)
insert(2)
insert(1)
insert(4)
insert(5)
print(max_heap)
print(getMax())
print(max_heap)