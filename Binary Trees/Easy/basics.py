class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution():
    
    #checking depth of the tree
    def maxDepth(self,root):
        if not root:
            return 0
        
        left= self.maxDepth(root.left)
        right= self.maxDepth(root.right)
        return 1+ max(left,right)
    

root=TreeNode()

