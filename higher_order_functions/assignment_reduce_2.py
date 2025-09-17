from functools import reduce


class Node:
    def __init__(self, value, is_transformator=False):
        self.value = value
        self.is_transformator = is_transformator
        self.children = []

    def add_child(self, child):
        self.children.append(child)



def sum_transformator_values(node: Node, children: list[Node]) -> int:
    # TODO implement using reduce that takes this function as argument. Hint the initial value is 0 or node.value
    pass



root = Node(10, is_transformator=True)
child1 = Node(5)
child2 = Node(15, is_transformator=True)
child3 = Node(20)
child4 = Node(25, is_transformator=True)
child5 = Node(8)
child6 = Node(12)
child7 = Node(3, is_transformator=True)
child8 = Node(30)

# Build the tree structure
root.add_child(child1)
root.add_child(child2)
child1.add_child(child3)
child1.add_child(child5)
child2.add_child(child4)
child2.add_child(child6)
child3.add_child(child7)
child4.add_child(child8)

# Test the sum_transformator_values function
total_value = sum_transformator_values(root, root.children)
assert total_value == 53, "10 + 15 + 25 + 3"
