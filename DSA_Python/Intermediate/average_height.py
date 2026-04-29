"""
Problem Description
There are n students in a class. You are given the heights of the students, you have to calculate the average height of students in the class. Your answer should be accurate upto 5 decimal places.

Input format
First line contains an integer n - Number of students. Second line contains n space-separated real numbers - The heights array.

Output format
Print the average height.

Sample Input 1
6 2.2 1 3 1.9 2.4 1.7

Sample Output 1
2.033333

Explanation
(2.2+1+3+1.9+2.4+1.7) / 6 = 12.2/6 = 2.03333

Constraints
0 < n < 100 0 < height < 100
"""
## Create tests in .cpp
import sys


def average_height(heights):
    return sum(heights) / len(heights)


def solve():
    values = sys.stdin.read().split()
    n = int(values[0])
    heights = list(map(float, values[1:1 + n]))
    print(f"{average_height(heights):.6f}")


if __name__ == "__main__":
    solve()
