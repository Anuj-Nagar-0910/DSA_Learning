'''
create a basic Linked list.
where we create a node and add a value, and read the properties of the Linked list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self.length -= 1
                return
            current = current.next

    def print_list(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements))

    def get_length(self):
        return self.length


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    ll.print_list()
    print("Length:", ll.get_length())
    ll.delete(2)
    ll.print_list()
    print("Length:", ll.get_length())
'''

class Node:
    """
    This is a node class that has a value and a next property.
    """
    def __init__(self, value):
        """
        This is a node class that has a value and a next property.
        """
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        """
        The user has selected __init__, which refers to the constructor methods in the Python code. There are two __init__ methods in this linked list implementation - one for the Node class and one for the LinkedList class. Let me explain both:

        Node Class __init__ Method
        def __init__(self, value):
            self.value = value
            self.next = None
        Purpose: This is the constructor for the Node class that initializes a new node.

        Parameters:

        value: The data/value that this node will store

        What it does:

        self.value = value: Stores the provided value in the node

        self.next = None: Initializes the pointer to the next node as None (indicating this node doesn't point to anything yet)

        Example usage:

        node = Node(5)  # Creates a node with value 5 and next = None
        LinkedList Class __init__ Method
        def __init__(self):
            self.head = None
            self.length = 0
        Purpose: This is the constructor for the LinkedList class that initializes an empty linked list.

        Parameters: None (besides self)

        What it does:

        self.head = None: Sets the head pointer to None, indicating the list is empty (no first node)
        self.length = 0: Initializes the length counter to 0, tracking how many nodes are in the list
        Example usage:

        ll = LinkedList()  # Creates an empty linked list

        Key Concepts:
        1. *__init__* is Python's special method for object initialization (constructor)
        2. Node initialization creates individual building blocks of the linked list
        3. .LinkedList initialization creates the container that manages the collection of nodes
        4. Both constructors set up the initial state needed for their respective classes to function properly

        The __init__ methods ensure that every new object starts in a well-defined, predictable state before any other operations are performed on them.
        """
        self.head = None
        self.length = 0

    def append(self, value):
        """
        This method appends a node to the end of the linked list.
        Add information about the method. What each line does
        The append method adds a new node with the given value to the end of the linked list. Here's what each line does:

        Line-by-line breakdown:
        new_node = Node(value)

        Create a new Node object with the provided value
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
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def prepend(self, value):
        """
        The prepend method adds a new node with the given value to the beginning of the linked list, making it the new head node.

        Line-by-line breakdown:
        new_node = Node(value)

        Creates a new Node object with the provided value
        The new node's next property is automatically set to None by the Node constructor
        new_node.next = self.head

        Sets the new node's next property to point to the current head of the list
        If the list is empty (self.head is None), the new node's next will be None
        If the list has existing nodes, the new node will point to the previous first node
        self.head = new_node

        Updates the linked list's head to point to the new node
        This makes the new node the first node in the list
        self.length += 1

        Increments the length counter to reflect the addition of the new node
        Example:
        If you have a list [2, 3, 4] and call prepend(1):

        Before: head -> [2] -> [3] -> [4] -> None
        Create new node: [1] -> None
        Point new node to current head: [1] -> [2] -> [3] -> [4] -> None
        Update head: head -> [1] -> [2] -> [3] -> [4] -> None
        Result: [1, 2, 3, 4]
        Time Complexity:
        O(1) - Constant time, because we only need to update a few pointers regardless of the list size. This is much more efficient than append() which is O(n).
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def delete(self, value):
        """
        Line-by-line breakdown:
        1. if self.head is None:

        Checks if the linked list is empty (no nodes exist)
        If empty, there's nothing to delete, so the method returns early
        2. if self.head.value == value:

        Checks if the first node (head) contains the value we want to delete
        This is a special case because deleting the head requires updating the head pointer
        3. self.head = self.head.next

        If the head node needs to be deleted, we update the head to point to the second node
        This effectively removes the first node from the list
        If there was only one node, self.head.next would be None, making the list empty
        4. self.length -= 1 and return

        Decrements the length counter and exits the method since we found and deleted the target
        5. current = self.head

        If we reach this point, the head doesn't contain our target value
        We start traversing from the head to find the target node
        6. while current.next is not None:

        Continues traversing until we reach the last node
        We check current.next because we need to maintain a reference to the node before the one we want to delete
        7. if current.next.value == value:

        Checks if the next node contains the value we want to delete
        8. current.next = current.next.next

        This is the key deletion step: we "skip over" the target node by pointing the current node directly to the node after the target
        The target node becomes unreachable and will be garbage collected
        9. Final self.length -= 1 and return

        Updates the length and exits since we found and deleted the target
        10. current = current.next

        If the next node wasn't our target, we move forward in the traversal
        Example:
        If you have a list [1, 2, 3, 4] and call delete(3):

        Before: [1] -> [2] -> [3] -> [4] -> None
                        ↑      ↑      ↑
                    current  target  next

        After:  [1] -> [2] ---------> [4] -> None
        The method finds node 2, sees that current.next (node 3) matches our target, then sets current.next = current.next.next (pointing to node 4), effectively removing node 3.

        Time Complexity:
        O(n) in the worst case, where n is the number of nodes
        We might need to traverse the entire list if the target is at the end or doesn't exist

        Note:
        This implementation only deletes the first occurrence of the value. If there are multiple nodes with the same value, only the first one encountered will be removed.
        """
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self.length -= 1
                return
            current = current.next

    def print_list(self):
        """
        Line-by-line breakdown:
        elements = []

        Creates an empty list to store the string representations of all node values
        This will be used to collect all values before printing them
        current = self.head

        Starts the traversal from the head (first node) of the linked list
        current is a pointer that will move through each node
        while current is not None:

        Continues the loop as long as there are more nodes to visit
        When current becomes None, we've reached the end of the linked list
        elements.append(str(current.value))

        Converts the current node's value to a string and adds it to the elements list
        Using str() ensures that values of any data type can be displayed properly
        current = current.next

        Moves the pointer to the next node in the linked list
        This is how we traverse through the entire list
        print(" -> ".join(elements))

        Joins all the collected string values with " -> " as a separator
        Prints the result, creating a visual representation of the linked list
        Example:
        If your linked list contains the values [0, 1, 2, 3], the method will output:

        0 -> 1 -> 2 -> 3
        Time Complexity:
        O(n) where n is the number of nodes in the linked list
        We must visit every node once to collect all values
        Space Complexity:
        O(n) for storing all the string values in the elements list
        This method provides a clean, visual way to see the structure and contents of your linked list, making it very useful for debugging and understanding the current state of your data structure.
        """
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements))

    def get_length(self):
        return self.length


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    ll.print_list()
    print("Length:", ll.get_length())
    ll.delete(2)
    ll.print_list()
    print("Length:", ll.get_length())

