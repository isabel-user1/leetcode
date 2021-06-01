# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#       if no root, return []
#       create array result
#       create array queue with root
#       go through the queue
#           create levelItems array
#           get current level size
#           go through current level
#               get dequeue node 
#               append node value into levelItems
#               if node has left child, store it in queue
#               if node has right child, store it in queue
#           finish current level iteartion, store the last value in levelItems to result
#       return result


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if (not root): return []
        result = []
        q = [root]
        
        while (q):
            levelItems = []
            levelSize = len(q)
            for _ in range(levelSize):
                node = q.pop(0)
                levelItems.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                    
            result.append(levelItems[levelSize-1])
        return result
