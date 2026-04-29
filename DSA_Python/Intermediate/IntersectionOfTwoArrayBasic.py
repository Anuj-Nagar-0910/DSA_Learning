"""
Problem Description
Given two arrays A and B, write a function to compute their intersection.

Note: Each element in the result should appear as many times as it shows in both arrays. The result needs to be in sorted order.

Input format

First line contains one integer N denoting the number of elements in array A

Next line contains N integers denoting the elements of array A

Next line contains one integer M denoting the number of elements in array B

Next line contains M integers denoting the elements of array B

Output format
Single line containing the intersection elements of the two arrays in sorted order.

Sample Input 1

4

1 2 2 1

2

2 2

Sample Output 1
2 2

Explanation
Since 2 2 are the only elements present in both the arrays.
"""
def intersection_of_two_array_basic(arr1, arr2):
    """
    Returns the sorted intersection of two arrays.

    Each common value appears as many times as it is present in both arrays.
    Example:
    [1, 2, 2, 3] and [2, 2, 4] -> [2, 2]
    """
    arr1.sort()
    arr2.sort()

    i = 0
    j = 0
    intersection = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return intersection



if __name__ == "__main__":
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))
    
    result = intersection_of_two_array_basic(arr1, arr2)
    print(" ".join(map(str, result)))
    intersection_of_two_array_basic(arr1, arr2)
    print(" ".join(map(str, result)))
    print(" ".join(map(str, result)))