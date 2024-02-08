"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)       # Traverse left subtree
            result.append(node.val)  # Visit the node
            inorder(node.right)      # Traverse right subtree

        inorder(root)
        return result

# testCase
# Manually creating the binary tree structure [1, None, 2, 3]
root = TreeNode(1)             # Root node with value 1
root.right = TreeNode(2)       # Right child of root with value 2
root.right.left = TreeNode(3)  # Left child of node 2 with value 3

test = Solution()

print(test.inorderTraversal(root))  # Output: [1,3,2]
