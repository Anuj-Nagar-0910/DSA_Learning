"""Problem Description
Given the array of integers nums of size n, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Input format
First line contains n, the number of distinct integers.

Second line contains n space separated integers.

Output format
Print the maximum product.

Sample Input 1
4

3 4 5 2

Sample Output 1
12

Explanation
If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)(nums[2]-1) = (4-1)(5-1) = 3*4 = 12.

Sample Input 2
4

1 5 4 5

Sample Output 2
16

Explanation
Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

Constraints
2 <= n <= 500

1 <= nums[i] <= 10^3

Use the heap data structure to find the maximum product of two numbers in the array. We can maintain a max heap to keep track of the largest two numbers in the array. When we insert a number, we can compare it with the current maximum and second maximum to update them accordingly. Finally, we can calculate the product using the two largest numbers.
"""
import heapq as h
def maxProduct(nums):
    max_heap = []
    for num in nums:
        h.heappush(max_heap, -num)
    first_max = -h.heappop(max_heap)
    second_max = -h.heappop(max_heap)
    return (first_max - 1) * (second_max - 1)

