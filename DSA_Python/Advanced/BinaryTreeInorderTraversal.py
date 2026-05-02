"""
Problem Description
Given a binary tree, return the inorder traversal of its nodes' values.

For the tree given shown here

image

Inorder Traversal would result in - Process (Left, Root, Right) : 4 2 5 1 3

Input format
First line contains T, denoting the number of test cases given.

For each test case, we follow the following format:

First line contains N, denoting the number of nodes the tree has.

The next N lines contain the binary tree structure ( format is explained at the end of this page).

Output format
For each test case, print on a new line, n space separated integers denoting the inorder traversal of the nodes.

Constraints
1<= T <= 1000

1<= Number of nodes in a Tree <=10000

0 <= Value of the nodes <= 10^9

It's guaranteed that the sum of the number of tree nodes across all test cases will be less than 500000.

Sample Input 1
1

5

5 1 4 3 6

1 2 3

2 -1 -1

3 4 5

4 -1 -1

5 -1 -1

Sample Output 1
1 5 3 4 6

Explanation 1
The tree can be represented as :

image

The inorder is hence 1 , 5 , 3 , 4 , 6.

Sample Input 2
1

3

2 1 3

1 2 3

2 -1 -1

3 -1 -1

Sample Output 2
1 2 3

Explanation 2
The tree can be represented as :

image

The inorder is hence 1 , 2 , 3.
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(nodes):
    if not nodes:
        return None
    
    node_dict = {}
    
    for value, left, right in nodes:
        if value not in node_dict:
            node_dict[value] = TreeNode(value)
        node = node_dict[value]
        
        if left != -1:
            if left not in node_dict:
                node_dict[left] = TreeNode(left)
            node.left = node_dict[left]
        
        if right != -1:
            if right not in node_dict:
                node_dict[right] = TreeNode(right)
            node.right = node_dict[right]
    
    return node_dict[nodes[0][0]]  # Return the root of the tree    
def inorder_traversal(root):
    if root is None:
        return []
    
    # Traverse left subtree, visit root, and then traverse right subtree
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        
        nodes = []
        for _ in range(n):
            value, left, right = map(int, data[index].split())
            nodes.append((value, left, right))
            index += 1
        
        root = build_tree(nodes)
        result = inorder_traversal(root)
        print(' '.join(map(str, result)))   
if __name__ == "__main__":
    main()