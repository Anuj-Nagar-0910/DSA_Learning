"""Problem Description
Given an matrix of dimension n*n. Find the sum of elements present at principal diagonal of the matrix.

Input format
First line contains integer n.

In next n lines each line contains n elements.

Output format
An integer representing the sum of diagonal elements.

Sample Input 1
4

1 2 3 4

1 2 4 5

2 3 3 4

1 1 2 3

Sample Output 1
9

Explanation
elements at diagonal are 1, 2, 3, 3 and their sum is 9.

Constraints
1 <= n <= 100

0 <= element of matrix <= 10^5

Sample Input 2
5

1 2 3 4 5

1 2 3 4 5

1 2 3 4 5

1 2 3 4 5

1 2 3 4 5

Sample Output 2
15
"""

n = int(input())
sum = 0
for i in range(n):
    for j in range(n):
        if i == j:
            sum += int(input())
print(sum)


# Read the matrix
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Calculate diagonal sum
diagonal_sum = 0
for i in range(n):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)



# Alternative solution using list comprehension
def diagonal_sum_alternative(matrix):
    """Calculate diagonal sum using list comprehension"""
    n = len(matrix)
    return sum(matrix[i][i] for i in range(n))

# Test the alternative solution
if __name__ == "__main__":
    # Example usage with the same input format
    test_matrix = [
        [1, 2, 3, 4],
        [1, 2, 4, 5], 
        [2, 3, 3, 4],
        [1, 1, 2, 3]
    ]
    result = diagonal_sum_alternative(test_matrix)
    print(f"Diagonal sum using alternative method: {result}")

    # Example usage with the same input format
    test_matrix = [
        [1, 2, 3, 4],
        [1, 2, 4, 5], 
        [2, 3, 3, 4],
        [1, 1, 2, 3]
    ]
    result = diagonal_sum_alternative(test_matrix)
    print(f"Diagonal sum using alternative method: {result}")   