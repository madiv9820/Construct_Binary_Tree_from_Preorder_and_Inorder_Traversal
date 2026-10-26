"""🌳 Reconstruct a binary tree using iterative BFS and traversal boundaries."""
from collections import deque
from typing import Optional, List, Deque, Dict, Tuple
from treenode import TreeNode

class BFSIterative:
    @staticmethod
    def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 📏 Get the number of nodes; an empty traversal represents an empty tree.
        n: int = len(preorder)
        root: Optional[TreeNode] = None

        if n:
            # 🗺️ Map each inorder value to its index for O(1) root lookups.
            inorder_map: Dict[int, int] = {
                val: index for index, val in enumerate(inorder)
            }

            # 🌱 Preorder visits the root first, making its first value the tree root.
            root = TreeNode(preorder[0])

            # 🚦 Queue each subtree with its node and preorder/inorder boundaries.
            # Format: (node, preorder_start, preorder_end, inorder_start, inorder_end)
            treeQ: Deque[Tuple[TreeNode, int, int, int, int]] = deque([
                (root, 0, n - 1, 0, n - 1)
            ])

            while treeQ:
                # 📤 Process the next subtree in level-order (FIFO).
                currentNode, preStart, preEnd, inStart, inEnd = treeQ.popleft()

                # ✂️ Find the root in inorder and calculate the left subtree's size.
                rootIndex = inorder_map[currentNode.val]
                leftSize = rootIndex - inStart

                # ◀️ Create the left subtree if inorder contains nodes before the root.
                if inStart < rootIndex:
                    # 📐 Derive the left subtree's boundaries in both traversals.
                    leftPreStart = preStart + 1
                    leftPreEnd = preStart + leftSize
                    leftInStart = inStart
                    leftInEnd = rootIndex - 1

                    # 🌿 The first value in this preorder range becomes the left child.
                    currentNode.left = TreeNode(preorder[leftPreStart])

                    # ➕ Queue the left subtree for subsequent BFS processing.
                    treeQ.append((
                        currentNode.left,
                        leftPreStart, leftPreEnd,
                        leftInStart, leftInEnd
                    ))

                # ▶️ Create the right subtree if inorder contains nodes after the root.
                if rootIndex < inEnd:
                    # 📐 Skip the root and all left-subtree nodes in preorder.
                    rightPreStart = preStart + leftSize + 1
                    rightPreEnd = preEnd
                    rightInStart = rootIndex + 1
                    rightInEnd = inEnd

                    # 🌿 The first value in this preorder range becomes the right child.
                    currentNode.right = TreeNode(preorder[rightPreStart])

                    # ➕ Queue the right subtree for subsequent BFS processing.
                    treeQ.append((
                        currentNode.right,
                        rightPreStart, rightPreEnd,
                        rightInStart, rightInEnd
                    ))

        # 🏁 Return the fully reconstructed binary tree.
        return root
