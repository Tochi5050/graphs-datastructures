from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def __init__(self):
        self.ans = []

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()
        temp_q = []
        q.append(root)

        while q:
            node = q.popleft()

            if len(q) == 0 and node is not None:
                node.next = None
                self.ans.append(node.val)
                self.ans.append(node.next)
                temp_q.append(node.left)
                temp_q.append(node.right)

            elif len(q) > 0 and q[0] is not None and node is not None:
                node.next = q[0]
                self.ans.append(node.val)
                self.ans.append(node.next.val)
                temp_q.append(node.left)
                temp_q.append(node.right)

            # print(temp_q)
            if len(q) == 0:
                for value in temp_q:
                    q.append(value)
                    temp_q = []

        return root










result = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(result.connect(root))
