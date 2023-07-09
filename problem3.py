from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_nodes_at_level(root, target_level):
    if root is None:
        return 0

    queue = deque([(root, 0)])
    count = 0

    while queue:
        node, level = queue.popleft()

        if level == target_level:
            count += 1

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return count


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

target_level = 2
count = count_nodes_at_level(root, target_level)
print(f"Number of nodes at level {target_level}: {count}")