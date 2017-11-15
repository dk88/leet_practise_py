# encoding:utf-8
import sys

__author__ = 'zhaoxiaojun'

reload(sys)
sys.setdefaultencoding('utf-8')


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pre_order_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            res.append(root.val)
            res += self.pre_order_traversal(root.left)
            res += self.pre_order_traversal(root.right)
        return res

    def mid_order_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            res += self.mid_order_traversal(root.left)
            res.append(root.val)
            res += self.mid_order_traversal(root.right)
        return res

    def post_order_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            res += self.post_order_traversal(root.left)
            res += self.post_order_traversal(root.right)
            res.append(root.val)
        return res

    def pre_order_traversal_literal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            res.append(root.val)
            res += self.pre_order_traversal(root.left)
            res += self.pre_order_traversal(root.right)
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.left.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    so = Solution()
    print so.pre_order_traversal(root)
    print so.mid_order_traversal(root)
    print so.post_order_traversal(root)
