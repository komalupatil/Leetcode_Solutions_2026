# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        queue = deque()
        queue.append(root)
        parent[root] = None
        while queue:
            node = queue.popleft()
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
        
        level = 0
        queue = deque()
        queue.append(target)
        visited = {target}
        while queue:
            if level == k:
                return [node.val for node in queue]
            for _ in range(len(queue)):
                node = queue.popleft()
                for nbr in (node.left, node.right, parent[node]):
                    if nbr is not None and nbr not in visited:
                        queue.append(nbr)
                        visited.add(nbr)
            level += 1
        return []


            
