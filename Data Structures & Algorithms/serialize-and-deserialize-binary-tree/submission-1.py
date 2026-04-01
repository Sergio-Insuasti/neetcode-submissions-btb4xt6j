# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def doSerialize(node):
            if node:
                vals.append(str(node.val))
                doSerialize(node.left)
                doSerialize(node.right)
            else:
                vals.append("_")
        vals = []
        doSerialize(root)
        return ' '.join(vals)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def doDSerialize():
            val = next(vals)
            if val == "_":
                return None
            node = TreeNode(int(val))
            node.left = doDSerialize()
            node.right = doDSerialize()
            return node
        vals = iter(data.split())
        return doDSerialize()

