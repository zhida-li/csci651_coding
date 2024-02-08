"""
145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def postorder(node):
            if not node:
                return
            postorder(node.left)     # Traverse left subtree
            postorder(node.right)    # Traverse right subtree
            result.append(node.val)  # Visit the node

        postorder(root)
        return result

# testCase
# Manually creating the binary tree structure [1, None, 2, 3]
root = TreeNode(1)             # Root node with value 1
root.right = TreeNode(2)       # Right child of root with value 2
root.right.left = TreeNode(3)  # Left child of node 2 with value 3

test = Solution()

print(test.postorderTraversal(root))  # Output: [3,2,1]
