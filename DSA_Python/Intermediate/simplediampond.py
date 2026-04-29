"""
Provide the optimum solution for the following problem with 
minimum time and space complexity.
Problem Description
Given a number n, you have to print a diamond-shaped pattern with 2n-1 rows using '*', with the i’th row having i asterisks for i <= n and 2n-i asterisks for i > n. (i starts at 1)

For eg. if n = 5, the pattern will be:

image

Keep in mind that every '*' is followed by a space.

Input format
One line of input, containing an integer - n.

Output format
Print the pattern as described. There should be a space after each '*'.

Sample Input 1
5

Sample Output 1
image
"""
import sys


def simple_diamond(n):
    rows = []

    for stars in range(1, n + 1):
        rows.append("* " * stars)

    for stars in range(n - 1, 0, -1):
        rows.append("* " * stars)

    return "\n".join(rows)


def solve():
    data = input()
    if not data:
        return

    print(simple_diamond(int(data)))
    


if __name__ == "__main__":
    solve()
