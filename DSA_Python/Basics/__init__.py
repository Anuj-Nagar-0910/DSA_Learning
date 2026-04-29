"""
Line-by-line breakdown:
new_node = Node(value)

Creates a new Node object with the provided value
The new node's next property is automatically set to None by the Node constructor
if self.head is None:

Checks if the linked list is empty (no head node exists)
self.head = new_node

If the list is empty, makes the new node the first (head) node of the list
else:

If the list is not empty, we need to find the last node to attach our new node
current = self.head

Starts traversing from the head of the list
while current.next is not None:

Continues traversing until we find a node whose next is None (the last node)
current = current.next

Moves to the next node in the traversal
current.next = new_node

Once we find the last node, we set its next property to point to our new node
self.length += 1

Increments the length counter to reflect the addition of the new node
Example:
If you have a list [1, 2, 3] and call append(4), the method will traverse to node 3 (which has next = None) and set 3.next = new_node(4), resulting in [1, 2, 3, 4].

The time complexity is O(n) because in the worst case, you need to traverse the entire list to find the last node.
"""