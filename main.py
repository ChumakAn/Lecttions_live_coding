class Tree:
    def __init__(self):
        self.root = None

    def search(self, value: int):
        found_node = self._search(self.root, value)
        if found_node is None:
            return False
        else:
            return True

    def _search(self, node_to_check, value):
        # no more nodes, parent is a leaf
        if (node_to_check is None) or (node_to_check.value == value):
            return node_to_check

        if node_to_check.root.value == value:
            return True

        elif value > node_to_check.root.value:
            # go right

            return self._search(node_to_check.right, value)
        else:
            # go left
            return self._search(node_to_check.left, value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        self._insert(self.root, value)

    # def _insert_with_search(self, value):
    # found_node = self._search(self.root, value)

    # 2 scenarios
    # scenario 1 - no such value
    # found_node.parent

    def _insert(self, current_node, value):
        # go to right
        if value > current_node.value:
            # add to the rigth if absent
            if current_node.right is None:
                current_node.right = Node(value, current_node)
                return
                # search for a proper position in right branch
            return self._insert(current_node.right, value)

        if value < current_node.value:
            # add to left leaf if absent
            if current_node.left is None:
                current_node.left = Node(value, current_node)
                # search for a proper position in left branch
                return

            return self._insert(current_node.left, value)
        return

    def delete(self, value):
        pass

    def max_value(self):
        pass

    def min_value(self):
        pass

    def print_tree(self):
        self.print_current(self.root)

    def print_current(self, current):
        print(current.value)
        if current.left:
            self.print_current(current.left)
        if current.right:
            self.print_current(current.right)


class Node:
    def __init__(self, value, parent=None):
        self.right = None
        self.left = None
        self.parent = None
        self.value = value


tree = Tree()
tree.insert(15)
tree.insert(1)
tree.insert(11)
tree.insert(20)
tree.insert(2)

tree.print_tree()
