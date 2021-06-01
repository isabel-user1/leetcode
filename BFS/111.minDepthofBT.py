# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# if no root, return 0
# create a queue to store root
# set minDepth as 0
# iterating queue
#     increasing the depth
#     get level size
#     iterating current level
#         get the dequeue node
#         if node doesn't have any children, return depth
#         if node has left child, store it to queue
#         if node has right child, store it to queue
        

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        q = [root]
        minDepth = 0
        
        while (q):
            minDepth += 1
            levelSize = len(q)
            for _ in range(levelSize):
                node = q.pop(0)
                if (not node.left and not node.right):      # hit the end, get the minDepth
                    return minDepth             
                if (node.left): q.append(node.left)
                if (node.right): q.append(node.right)
            

# recursion
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if (not root): return 0
        minDepth = 1
        return self.search(root, minDepth)

    
    def search(self, root, depth):
        # base case: node doesn't hava any children, return depth
        if (not root.left and not root.right):
            return depth;
        
        if (not root.left):
            return self.search(root.right, depth + 1)
        
        if (not root.right):
            return self.search(root.left, depth + 1)
        
        if (root.left and root.right):
            return min(self.search(root.left, depth + 1), self.search(root.right, depth + 1))