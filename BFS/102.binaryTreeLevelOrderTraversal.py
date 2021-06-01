# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# declare a result array
# if root doesn't exists, return []
# declare a queue to store nodes
# iterating queue if queue is not empty
#   create a levelItems array
#   create a levelSize to store current level size
#
#   iterating current level
#     get the dequeue node
#     push the dequeue node into levelItems
#     if dequeue node has left child, store left child into queue
#     if dequeue node has right child, store right child into queue
#   after iterating current level, push levelItems into result
# after iterating queue, return result
    
# time: O(N), space: O(N)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        q = [root]
    
        while q:
            levelSize = len(q)
            levelItems = []
            for _ in range(levelSize):
                node = q.pop(0)
                levelItems.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(levelItems)
        return res
        
