"""🌳 Define a binary tree node and its child references."""
from typing import Optional

class TreeNode:
    """🌱 Represent a node in a binary tree."""

    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ) -> None:
        """
        Initialize a node with a value and optional child nodes.

        Args:
            val: Integer value stored in the node.
            left: Reference to the left child, if present.
            right: Reference to the right child, if present.
        """
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right
