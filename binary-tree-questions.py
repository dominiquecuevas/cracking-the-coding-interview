from linkedlists import LLNode, LinkedList
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

def levels_linked_list_of_nodes(node):
    """pg 109 List of Depths:
    Given a binary tree, design an algorithm which creats a linked list
    of all the nodes at each depth"""
    if not node:
        return
    queue = [(node, 1)]
    linked_lists = {}
    while queue:
        current, depth = queue.pop(0)
        linked_lists[depth] = linked_lists.get(depth, LinkedList())
        linked_lists[depth].append(current)
        if current.left:
            queue.append((current.left, depth+1))
        if current.right:
            queue.append((current.right, depth+1))
    return linked_lists

linked_lists = levels_linked_list_of_nodes(ten)

for depth in linked_lists:
    current = linked_lists[depth].head
    while current:
        print(current)
        current = current.next
    print()