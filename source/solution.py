"""🌳 Construct a binary tree from preorder and inorder traversals."""
from typing import List, Optional
from treenode import TreeNode
from .approaches import DFSRecursive, DFSIterative

class Solution:
    """🧩 Provide the interface for binary tree construction."""

    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int],
    ) -> Optional[TreeNode]:
        """Reconstruct a binary tree from its traversal sequences.

        Args:
            preorder: Node values visited in root-left-right order.
            inorder: Node values visited in left-root-right order.

        Returns:
            The root of the reconstructed binary tree, or None if empty.
        """
        dfsrecursive: DFSRecursive = DFSRecursive(preorder=preorder, inorder=inorder)
        dfsiterative: DFSIterative = DFSIterative()
        return dfsiterative.buildTree(preorder=preorder, inorder=inorder)
