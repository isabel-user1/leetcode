# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# traversing order is from top to down
# for level order, if level is odd, traversing from right to left
# if level is even, traversing order is as default (from left to right)

# 		go through the queue if the queue is not empty
#           get levelSize
#           declare levelItems to store current level items
#           iterating current level
#               get dequeue node
#               if level is even: 
#                   append the value to levelItems
#               if level is odd
#                   insert value into the first index of levelItems
#               store left child to queue if node has left child
#               store right child to queue if node has right child
#           finish current level iteration, append levelItems into result
# 			reverse evenLevel
#       finish visiting all node, return result


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if (not root): return []
        result = []
        q = [root]
        evenLevel = True
        
        while (q):
            levelSize = len(q)
            levelItems = []
            for _ in range(levelSize):
                node = q.pop(0)
                if (evenLevel):
                    levelItems.append(node.val)
                else:
                    levelItems.insert(0, node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(levelItems)
            evenLevel = not evenLevel;
        return result


