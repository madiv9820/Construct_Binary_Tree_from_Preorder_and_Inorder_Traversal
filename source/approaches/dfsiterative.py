"""🌳 Reconstruct a binary tree using iterative depth-first search."""
from typing import List, Optional
from treenode import TreeNode

class DFSIterative:
    """🧩 Build a binary tree using preorder and inorder traversals."""

    @staticmethod
    def buildTree(
        preorder: List[int],
        inorder: List[int],
    ) -> Optional[TreeNode]:
        # 📏 Track the number of nodes and initialize the root reference.
        n: int = len(preorder)
        root: Optional[TreeNode] = None

        if n:
            # 🌱 Preorder's first element is the root of the tree.
            root = TreeNode(preorder[0])

            # 👉 Track the next preorder node and inorder position to process.
            preorder_index: int = 1
            inorder_index: int = 0

            # 📚 Keep ancestors whose subtree construction is still in progress.
            treeStack: List[TreeNode] = [root]

            while preorder_index < n:
                # 🌿 Create the next node in preorder (Root → Left → Right).
                node: TreeNode = TreeNode(preorder[preorder_index])
                preorder_index += 1

                # 🔍 If the stack top hasn't appeared at the current inorder
                # position, its left subtree is still being constructed.
                if treeStack[-1].val != inorder[inorder_index]:
                    treeStack[-1].left = node
                    treeStack.append(node)

                else:
                    # ✅ Pop completed nodes whose values match inorder.
                    # The last popped node is the parent of the next right child.
                    while (
                        treeStack
                        and inorder_index < n
                        and treeStack[-1].val == inorder[inorder_index]
                    ):
                        currentNode = treeStack.pop()
                        inorder_index += 1

                    # 🌳 The next preorder node starts the right subtree
                    # of the last completed node.
                    currentNode.right = node
                    treeStack.append(node)

        # 🏁 Return the root of the reconstructed binary tree.
        return root
