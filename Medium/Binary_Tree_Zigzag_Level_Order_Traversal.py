# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# bfs, queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque()
        queue.append(root)
        zigzag = False
        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize):
                currentNode = queue.popleft()
                if not zigzag:
                    currentLevel.append(currentNode.val)
                else:
                    currentLevel.insert(0, currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            zigzag = not zigzag
            result.append(currentLevel)
        return result
