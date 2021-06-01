# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#         create result array
#         if no root, return []
#         create queue to store nodes
        
#         iterating queue if queue is not empty
#             get current level size
#             create a sum to store level sum
            
#             itearting current level using levelSize
#                 get dequeue node
#                 add up each node value
#                 store left child to queue if left child exists
#                 store right child to queue if right child exists
#             after itearting current level, append current level average into result
        
#         after itearting all nodes, return result

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        if (not root): return result;
        q = [root]
        while (q):
            levelSize = len(q)
            sum = 0
            for _ in range(levelSize):
                node = q.pop(0)
                sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(sum / levelSize)
        return result