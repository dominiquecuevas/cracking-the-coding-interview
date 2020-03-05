from binarytree import BTNode, BinaryTree

ten = BTNode(10)
five = BTNode(5)
three = BTNode(3)
seven = BTNode(7)
fifteen = BTNode(15)
twenty = BTNode(20)

ten.left = five
ten.right = twenty
five.left = three
five.right = seven
twenty.left = fifteen

tree = BinaryTree(ten)

def in_order_traversal(node):
    if node != None:
        in_order_traversal(node.left)
        print(node)
        in_order_traversal(node.right)


def pre_order_traversal(node):
    """depth-first"""
    if node != None:
        print(node)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_oder_traversal(node):
    if node != None:
        post_oder_traversal(node.left)
        post_oder_traversal(node.right)
        print(node)

in_order_traversal(ten)
print()
pre_order_traversal(ten)
print()
post_oder_traversal(ten)