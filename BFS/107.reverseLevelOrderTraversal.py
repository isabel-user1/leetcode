# 1: put levelItems into the head of result to achieve the reverse
# 2: traversing tree from top to bottom, store each levelItesm into result
# reverse result finally


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# create result array 
# if no root, return []
# create a queue to store root

# iterating queue
#     create levelItems
#     get level size
#     iterating current level
#         get the dequeue node
#         append node to levelItems
#         if node has left child, store it to queue
#         if node has right child, store it to queue
#     after iterating current level, append levelItems to the head of result
# return result


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        if (not root): return result
        q = [root]
    
        while (q):
            levelItems = []
            levelSize = len(q)
            for _ in range(levelSize):
                node = q.pop(0)
                levelItems.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.insert(0, levelItems)
        return result



class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        if (not root): return result
        q = [root]
    
        while (q):
            levelItems = []
            levelSize = len(q)
            for _ in range(levelSize):
                node = q.pop(0)
                levelItems.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(levelItems)
        return reversed(result)