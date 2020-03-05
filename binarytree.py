class BTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __repr__(self):
        return f"<BTNode data={self.data}>"

class BinaryTree:
    def __init__(self, root):
        self.root = root
    def __repr__(self):
        return f"<BinaryTree root={self.root}>"