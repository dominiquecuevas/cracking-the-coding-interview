from graph import GNode, Graph

def graph_dfs(node, visited=set()):
    """"""
    if not node:
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for child in node.children:
            graph_dfs(child, visited)

def graph_bfs(node):
    if not node:
        return
    queue = [node]
    queued = set([node,])
    while queue:
        current = queue.pop(0)
        print(current)
        queued.add(current)
        for child in current.children:
            if child not in queued:
                queue.append(child)
                queued.add(child)

zero = GNode(0)
one = GNode(1)
two = GNode(2)
three = GNode(3)
four = GNode(4)
five = GNode(5)

zero.children.add(one)
zero.children.add(four)
zero.children.add(five)
one.children.add(three)
one.children.add(four)
two.children.add(one)
three.children.add(two)
three.children.add(four)

graph_dfs(zero)
print()
graph_bfs(zero)