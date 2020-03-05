class GNode:
    def __init__(self, data, children=None):
        self.data = data
        if not children:
            self.children = set()
    def __repr__(self):
        return f"<Gnode data={self.data}>"

class Graph:
    def __init__(self, nodes=set()):
        self.nodes = nodes
    def __repr__(self):
        return f"<Graph nodes={self.nodes}>"