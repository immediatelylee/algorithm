# https://leetcode.com/problems/merge-two-binary-trees/

# root1 = [1, 3, 2, 5]
# root2 = [2, 1, 3, None, 4, None, 7]
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TestCase
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.left = TreeNode(None)
root2.left.right = TreeNode(4)
root2.right.left = TreeNode(None)
root2.right.right = TreeNode(7)


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)

            return node
        else:
            return root1 or root2


test = Solution()
print(test.mergeTrees(root1, root2))
