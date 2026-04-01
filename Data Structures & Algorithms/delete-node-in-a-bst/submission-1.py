# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
        return root
        """
        ``` Pseudocode
            bstDelete(t, v):
                Input: tree t, value v
                Output: t with v deleted

                if t is empty:
                    return empty tree
                else if v < t->item:
                    t->left = bstDelete(t->left, v)
                else if v > t->item:
                    t->right = bstDelete(t->right, v)
                else:
                    if t->left is empty:
                        new = t->right
                    else if t->right is empty:
                        new = t->left
                    else:
                        new = bstJoin(t->left, t->right)

                    free(t)
                    t = new
                return t

        ```
        """