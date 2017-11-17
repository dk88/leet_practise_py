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
        stack = []
        res = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res

    def mid_order_traversal_literal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def post_order_traversal_literal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        flag_list = []
        while stack or root:
            while root:
                stack.append(root)
                flag_list.append(0)
                root = root.left
            root = stack.pop()
            flag = flag_list.pop()
            if flag == 0:
                stack.append(root)
                flag_list.append(1)
                root = root.right
            else:
                res.append(root.val)
                root = None
        return res

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        if not t1 and not t2:
            return t2
        if t1 and not t2:
            return t1
        if t1 and t2:
            t3 = TreeNode(t1.val if t1 else 0 + t2.val if t2 else 0)
            t3.left = self.mergeTrees(t1.left, t2.left)
            t3.right = self.mergeTrees(t1.right, t2.right)
            return t3

    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.val > R:
            return self.trimBST(root.left, L, R)
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root


if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(6)
    # root.left.left.right = TreeNode(5)
    # root.left.right.left = TreeNode(7)
    # so = Solution()
    # print so.pre_order_traversal(root)
    # print so.pre_order_traversal_literal(root)
    # print so.mid_order_traversal(root)
    # print so.mid_order_traversal_literal(root)
    # print so.post_order_traversal(root)
    # print so.post_order_traversal_literal(root)

    so = Solution()

    # root1 = TreeNode(1)
    # root1.left = TreeNode(3)
    # root1.left.left = TreeNode(5)
    # root1.right = TreeNode(2)
    #
    # root2 = TreeNode(2)
    # root2.left = TreeNode(1)
    # root2.left.right = TreeNode(4)
    # root2.right = TreeNode(3)
    # root2.right.right = TreeNode(7)
    # print so.mergeTrees(root1, root2)
    root = TreeNode(3)
    root.left = TreeNode(0)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(1)
    new_root = so.trimBST(root, 1, 3)
    print so.mid_order_traversal(new_root)


