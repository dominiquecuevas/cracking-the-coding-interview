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
    ll = LinkedList()
    linked_lists = [ll]
    while queue:
        current, level = queue.pop(0)
        if len(linked_lists) != level:
            ll = LinkedList()
            linked_lists.append(ll)
        linked_lists[-1].append(current)
        
        if current.left:
            queue.append((current.left, level+1))
        if current.right:
            queue.append((current.right, level+1))
    return linked_lists

linked_lists = levels_linked_list_of_nodes(ten)

for ll in linked_lists:
    current = ll.head
    while current:
        print(current)
        current = current.next
    print()

print()

def level_recursively(node):
    level = 1
    lists = []
    def level_recursively_(node, level, lists):
        if node == None:
            return
        if len(lists) != level:
            ll = LinkedList()
            lists.append(ll)
        lists[level-1].append(node)
        level_recursively_(node.left, level+1, lists)
        level_recursively_(node.right, level+1, lists)
        return lists
    return level_recursively_(node, level, lists)

linked_lists_rec = level_recursively(ten)

for ll in linked_lists_rec:
    current = ll.head
    while current:
        print(current)
        current = current.next
    print()