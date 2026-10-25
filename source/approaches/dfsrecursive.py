"""🌳 Reconstruct a binary tree using recursive DFS."""
from typing import Dict, List, Optional
from treenode import TreeNode

class DFSRecursive:
    """🧩 Build a tree using preorder and inorder traversals."""

    def __init__(self, preorder: List[int], inorder: List[int]) -> None:
        # 📥 Store preorder for root-first traversal.
        self.__preorder: List[int] = preorder

        # ⚡ Map each inorder value to its index for constant-time lookup.
        self.__inorder_map: Dict[int, int] = {
            value: index for index, value in enumerate(inorder)
        }

    def buildTree(
        self,
        preorder_start: int,
        preorder_end: int,
        inorder_start: int,
        inorder_end: int,
    ) -> Optional[TreeNode]:

        # 🛑 An empty range represents an empty subtree.
        if preorder_start > preorder_end or inorder_start > inorder_end:
            return None

        # 🌱 Preorder's first value is the current subtree's root.
        root_val: int = self.__preorder[preorder_start]
        root: TreeNode = TreeNode(root_val)

        # ⚡ Find the root's position in inorder without scanning.
        index: int = self.__inorder_map[root_val]

        # 📏 Determine how many nodes belong to the left subtree.
        elements_left: int = index - inorder_start

        # 🌿 Build the left subtree from the ranges before the root.
        root.left = self.buildTree(
            preorder_start + 1,
            preorder_start + elements_left,
            inorder_start,
            index - 1,
        )

        # 🌳 Build the right subtree from the ranges after the root.
        root.right = self.buildTree(
            preorder_start + elements_left + 1,
            preorder_end,
            index + 1,
            inorder_end,
        )

        # ✅ Return the reconstructed subtree.
        return root
