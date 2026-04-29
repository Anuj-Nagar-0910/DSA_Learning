"""
Problem Description
Given a sorted array of N distinct integers and a target value X, return the index if the target is found. If not found then return -1.

Note - Try implementing with O(logN) runtime complexity.

Input format
First line contains N, the number of distinct integers. Second line contains N space separated integers.

Output format
Print the index of target element if found else return -1.

Sample Input 1
5 7

1 3 5 7 13

Sample Output 1
3

Explanation
Target integer 7 is at index 3.

Sample Input 2
5 8

1 3 5 7 13

Sample Output 2
-1

Explanation
Target integer 8 is not present.

Constraints
1 <= N <= 10^3 1 <= A[i] <= 10^9
"""
def searchTarget(n,array,target):
    #identify the index range to look into
    # arr = [1,2,3,4,5,6,7]
    #serach range at initial = 0, 6
    # print(N,A,X)
    l_index, r_index = 0, n-1
    X = array
    A = target

    while l_index <= r_index:#loop throught the array untill the l <= r
        #find the mid and dive the list into two halves
        # search the target 2 for left
        # search the target 6 for right
        #arr = [1,2,3,4,5,6,7]
        mid =(l_index+r_index)//2#mid=3
        #find the element and retun the index
        #if the element is identified return the index value 'mid'
        if(X[mid] == A):
            return mid
        #else target value is greater then mid that is target is in right half
        #change the left_index to mid+1
        #if target A = 6, 4 < 6
        elif(X[mid] < A):
            #change left index to right side of the half
            l_index = mid +1 #l_index = 3+1 = 4 
            #now the search range becomes from 4, 6
        #else target value is less then the mid that is target is in left half
        #change the right_index to mid-1
        #if target A = 2, 4 > 2
        elif(X[mid] > A):
            #change the right index to left side of the half
            r_index = mid - 1 #r_index = 3-1 = 2
            #now the search region becomes 0, 2
    #if we have not identified the value anywhere return None or -1
    return -1


def main():
    n,target = map(int,input().split())
    array = list(map(int,input().split()))
    res = searchTarget(n,array,target)
    print(res)

if __name__=="__main__":
    main()