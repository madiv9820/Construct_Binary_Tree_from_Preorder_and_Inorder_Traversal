# [🌳 Reconstruct the Binary Tree: Two Traversals, One Tree!]()

### 📖 The Story

Imagine discovering two mysterious maps of a forgotten tree 🌲—one records the nodes in **root-first order**, while the other captures them in **left-root-right order**. Can you combine these clues to bring the original binary tree back to life? 🧩

### 📝 Problem Explanation

Given two integer arrays, `preorder` and `inorder`, representing the preorder and inorder traversals of the same binary tree, **construct and return the original binary tree**.

- **Preorder:** Visits the root, then the left subtree, and finally the right subtree.
- **Inorder:** Visits the left subtree, then the root, and finally the right subtree.

Each node contains a unique value, and both traversals are guaranteed to represent the same valid binary tree.

#### 🧪 Example

- **Rebuilding the Tree**

    **Input:**

    ![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

    ```python
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    ```

    **Output:**
    ```python
    [3, 9, 20, None, None, 15, 7]
    ```

    **Explanation:** 🌱 The root is `3`. Its left child is `9`, while its right subtree is rooted at `20`, with children `15` and `7`.

- **A Single-Node Tree**

    **Input:**
    ```python
    preorder = [-1]
    inorder = [-1]
    ```

    **Output:**
    ```python
    [-1]
    ```

    **Explanation:** 🍃 Both traversals describe the same tree containing just one node, `-1`.

#### ⚙️ Constraints

- $1 \leq \text{preorder.length} \leq 3000$
- `inorder.length == preorder.length`
- $-3000 \leq \text{preorder[i]}, \text{inorder[i]} \leq 3000$
- All values in each traversal are **unique**.
- Every value in `inorder` also appears in `preorder`.
- Both arrays are guaranteed to be valid traversals of the same binary tree.

---