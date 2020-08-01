"""This module contains a tree structure and its corresponding methods."""


class Node:
    """Basic structure for a Tree"""
    def __init__(self, data=None):
        """Create the basics elements from the Node
        :param data: Value to store in the Node"""
        self.left_child = None
        self.right_child = None
        self.data = data


class Tree:
    """Class to create the object tree and being able to manipulate as it."""

    def __init__(self):
        """
        Create the root node
        """
        self.root = None

    def insert(self, data):
        """
        Returns True or False depending if there are no more space to add a value in the tree
        :param data: Any type value to be stored in the tree
        :return Boolean that says if the operation was possible or not.
        """
        temp_node = Node()
        temp_node.data = data
        temp_node.left_child = None
        temp_node.right_child = None

        if self.root is None:
            self.root = temp_node
            return True

        current_node = self.root

        while True:
            parent_node = current_node

            # Go to left of the Tree
            if data < parent_node.data:
                current_node = parent_node.left_child  # Assign the next position
                if current_node is None:
                    parent_node.left_child = temp_node  # Insert new node
                    return True
            # Go to right of the Tree
            else:
                current_node = parent_node.right_child
                if current_node is None:
                    parent_node.right_child = temp_node
                    return True

    def search(self, data):
        """
        Search of an element at the given index or value.
        :param data: Any type value to be searched

        :return the Node that has that data
        """
        if self.root:
            current_node = self.root
            while current_node.data != data:
                # Go to left tree
                if data < current_node.data:
                    current_node = current_node.left_child
                # Go to right tree
                else:
                    current_node = current_node.right_child

                if current_node is None:
                    return None
            return current_node

    def traversal(self, root):
        """"""
        if root:
            print('\t{}\n  {} - {}\n'.format(root.data,
                                             root.left_child.data if root.left_child else '_',
                                             root.right_child.data if root.right_child else '_'))
            self.traversal(root.left_child)
            self.traversal(root.right_child)
        # print("Branch completed.")

    def traverse(self):
        """
        Print all the tree elements one by one.
        """
        print("\n")
        self.traversal(self.root)


if __name__ == "__main__":
    tree = Tree()
    tree.insert('H')
    tree.insert('e')
    tree.insert('l')
    tree.insert('l')
    tree.insert('o')
    tree.traverse()
    searched_node = tree.search('e')
    print(searched_node.data)
