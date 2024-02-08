"""
144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def preorder(node):
            if not node:
                return
            result.append(node.val)  # Visit the node
            preorder(node.left)     # Traverse left subtree
            preorder(node.right)    # Traverse right subtree

        preorder(root)
        return result

# testCase
# Manually creating the binary tree structure [1, None, 2, 3]
root = TreeNode(1)             # Root node with value 1
root.right = TreeNode(2)       # Right child of root with value 2
root.right.left = TreeNode(3)  # Left child of node 2 with value 3

test = Solution()

print(test.preorderTraversal(root))  # Output: [1,2,3]
