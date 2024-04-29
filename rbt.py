class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = self.left = self.right = None
        self.color = 'RED'

class RedBlackTree(object):

    def find_grandparent_node(self, node):
        if node is not None and node.parent is not None and node.parent.parent is not None:
            return node.parent.parent
        else:
            return None

    def find_uncle_node(self, node):
        grandparent_node = self.find_grandparent_node(node)
        if grandparent_node is None:
            return None

        if node.parent == grandparent_node.left:
            return grandparent_node.right
        else:
            return grandparent_node.left

    def insert_case1(self, node):
        if node.parent is None:
            node.color = 'BLACK'
        else:
            self.insert_case2(node)

    def insert_case2(self, node):
        if node.parent.color == 'BLACK':
            return
        else:
            self.insert_case3(node)

    def insert_case3(self, node):
        uncle = self.find_uncle_node(node)

        if uncle is not None and uncle.color == 'RED':
            node.parent.color = 'BLACK'
            uncle.color = 'BLACK'
            grandparent = self.find_grandparent_node(node)
            grandparent.color = 'RED'
            self.insert_case1(grandparent)
        else:
            self.insert_case4(node)

    def insert_case4(self, node):

        grandparent = self.find_grandparent_node(node)

        if node == node.parent.right and node.parent == grandparent.left:
            self.rotate_left(node.parent)
            node = node.left
        elif node == node.parent.left and node.parent == grandparent.right:
            self.rotate_right(node.parent)
            node = node.right

        self.insert_case5(node)

    def rotate_left(self, node):
        if node is None or node.right is None:
            return
        c = node.right
        p = node.parent

        if c.left is not None:
            c.left.parent = node

        node.right = c.left
        node.parent = c
        c.left = node
        c.parent = p

        if c.parent is None:
            self.root = c

        if p is not None:
            if p.left == node:
                p.left = c
            else:
                p.right = c

    def rotate_right(self, node):
        if node is None or node.left is None:
            return
        c = node.left
        p = node.parent

        if c.right is not None:
            c.right.parent = node

        node.left = c.right
        node.parent = c
        c.right = node
        c.parent = p

        if c.parent is None:
            self.root = c

        if p is not None:
            if p.right == node:
                p.right = c
            else:
                p.left = c

    def insert_case5(self, node):
        grandparent = self.find_grandparent_node(node)

        node.parent.color = 'BLACK'
        grandparent.color = 'RED'

        if node == node.parent.left:
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)

    def __init__(self):
        self.root = None
        self.inserted_node = None

    def insert(self, data, parent_node):
        if self.root is None:
            self.root = Node(data)
            self.root.color = 'BLACK'
            return

        current_node = self.root
        new_node = Node(data)
        while True:
            if data <= current_node.data:
                if current_node.left is None:
                    current_node.left = new_node
                    new_node.parent = current_node
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    new_node.parent = current_node
                    break
                else:
                    current_node = current_node.right

        self.inserted_node = new_node
        self.insert_case1(new_node)

    def find(self, search_key):
        return self.find_value(self.root, search_key)

    def find_value(self, root, search_key):
        if root is None or root.data == search_key:
            return root
        elif search_key > root.data:
            return self.find_value(root.right, search_key)
        else:
            return self.find_value(root.left, search_key)

    def delete(self, key):
        node = self.find(key)
        if node is None:
            return

        self.delete_node(node)

    def minimum(self, node):
        while node.left:
            node = node.left
        return node

    def delete_node(self, node):
        if node.left is not None and node.right is not None:
            successor = self.minimum(node.right)
            node.data = successor.data
            self.delete_node(successor)
        else:
            child = node.left if node.left else node.right
            self.transplant(node, child)
            if node.color == 'BLACK':
                if child and child.color == 'RED':
                    child.color = 'BLACK'
                else:
                    self.delete_fixup(child, node.parent)

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def delete_fixup(self, node, parent):
        while node != self.root and (node is None or node.color == 'BLACK'):
            if node == parent.left:
                sibling = parent.right

                if sibling is None:
                    break

                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    parent.color = 'RED'
                    self.rotate_left(parent)
                    sibling = parent.right

                if (sibling and (sibling.left is None or sibling.left.color == 'BLACK')) and \
                        (sibling and (sibling.right is None or sibling.right.color == 'BLACK')):
                    if sibling:
                        sibling.color = 'RED'
                    node = parent
                    parent = node.parent
                else:
                    if sibling and (sibling.right is None or sibling.right.color == 'BLACK'):
                        sibling.left.color = 'BLACK'
                        sibling.color = 'RED'
                        self.rotate_right(sibling)
                        sibling = parent.right

                    if sibling:
                        sibling.color = parent.color
                    if parent:
                        parent.color = 'BLACK'
                    if sibling and sibling.right:
                        sibling.right.color = 'BLACK'
                    self.rotate_left(parent)
                    node = self.root
            else:
                sibling = parent.left

                if sibling is None:
                    break

                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    parent.color = 'RED'
                    self.rotate_right(parent)
                    sibling = parent.left

                if (sibling and (sibling.left is None or sibling.left.color == 'BLACK')) and \
                        (sibling and (sibling.right is None or sibling.right.color == 'BLACK')):
                    if sibling:
                        sibling.color = 'RED'
                    node = parent
                    parent = node.parent
                else:
                    if sibling and (sibling.left is None or sibling.left.color == 'BLACK'):
                        sibling.right.color = 'BLACK'
                        sibling.color = 'RED'
                        self.rotate_left(sibling)
                        sibling = parent.left

                    if sibling:
                        sibling.color = parent.color
                    if parent:
                        parent.color = 'BLACK'
                    if sibling and sibling.left:
                        sibling.left.color = 'BLACK'
                    self.rotate_right(parent)
                    node = self.root

        if node:
            node.color = 'BLACK'


def process_input(input_filename):
    operations = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            operation, key = line.strip().split()
            key = int(key)
            operations.append((operation, key))
    return operations


def save_result(operations, output_filename):
    rbt = RedBlackTree()
    with open(output_filename, 'w') as output_file:
        for operation, key in operations:
            if operation == 'i':
                if key >= 0:
                    rbt.insert(key, None)
            elif operation == 'd':
                if key >= 0:
                    rbt.delete(key)
            elif operation == 'c':
                result = rbt.find(key)
                if result:
                    output_file.write('color(%d): %s\n' % (key, result.color))

input_filename = "rbt.inp"
output_filename = "rbt.out"
operations = process_input(input_filename)
save_result(operations, output_filename)
