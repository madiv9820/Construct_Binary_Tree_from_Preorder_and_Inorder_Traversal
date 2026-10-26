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

### 🌳 Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversals of a binary tree with unique node values, reconstruct and return the original tree.

- #### 🌿 1. Recursive DFS — `DFSRecursive`

    - **💡 Intuition :** Preorder identifies the root because it visits nodes in **Root → Left → Right** order. Inorder locates that root and separates the left and right subtrees. Recursion reconstructs each subtree independently.

    - **⚙️ Approach :**
        1. Build a hashmap mapping each inorder value to its index for constant-time root lookups.
        2. Select the first value in the current preorder range as the root.
        3. Find the root's inorder index and calculate the number of nodes in its left subtree.
        4. Recursively construct the left and right subtrees using their respective traversal boundaries.
        5. Return the root once both subtrees are constructed.

    - **📝 Pseudocode :**
        ```text
        BUILD(preStart, preEnd, inStart, inEnd):
            if either range is empty:
                return null

            rootValue = preorder[preStart]
            root = new Node(rootValue)
            rootIndex = inorderMap[rootValue]
            leftSize = rootIndex - inStart

            root.left = BUILD(
                preStart + 1,
                preStart + leftSize,
                inStart,
                rootIndex - 1
            )

            root.right = BUILD(
                preStart + leftSize + 1,
                preEnd,
                rootIndex + 1,
                inEnd
            )

            return root
        ```

    - **⏱️ Complexity**
        - **Time:** `O(n)` — Each node is constructed once, with O(1) hashmap lookups.
        - **Auxiliary Space:** `O(n)` — The hashmap and recursion stack require linear space.

- #### 📚 2. Iterative DFS — `DFSIterative`

    - **💡 Intuition :** Simulate recursive construction with an explicit stack. Preorder reveals the next node to create, while inorder indicates when a node's left subtree is complete and construction should move to a right child.

    - **⚙️ Approach**
        1. Create the root from the first preorder value and push it onto a stack.
        2. Process the remaining preorder values in order.
        3. If the stack's top does not match the current inorder value, attach the new node as its left child and push it.
        4. Otherwise, pop all completed ancestors matching consecutive inorder values, advancing the inorder pointer each time.
        5. Attach the new node as the right child of the last popped ancestor, then push it.
        6. Return the root after processing all preorder values.

    - **📝 Pseudocode**
        ```text
        if preorder is empty:
            return null

        root = new Node(preorder[0])
        stack = [root]
        preIndex = 1
        inIndex = 0

        while preIndex < n:
            node = new Node(preorder[preIndex])

            if stack.top.value != inorder[inIndex]:
                stack.top.left = node
                push node onto stack
            else:
                while stack is not empty
                    and inIndex < n
                    and stack.top.value == inorder[inIndex]:
                    parent = pop stack
                    inIndex += 1

                parent.right = node
                push node onto stack

            preIndex += 1

        return root
        ```

    - **⏱️ Complexity**
        - **Time:** `O(n)` — Each node is pushed and popped at most once.
        - **Auxiliary Space:** `O(n)` — The explicit stack can hold up to n nodes.

- #### 🚦 3. Iterative BFS — `BFSIterative`

    - **💡 Intuition :** Construct the tree level by level using a queue. Each queued entry represents a subtree and carries its node alongside the corresponding preorder and inorder boundaries.

    - **⚙️ Approach**
        1. Return `None` if preorder is empty; otherwise, create the root.
        2. Build a hashmap of inorder values and their indices.
        3. Enqueue the root with the full traversal ranges.
        4. Dequeue a subtree, locate its root in inorder, and calculate its left subtree size.
        5. If a left subtree exists, create its root from the next preorder position and enqueue it with the left subtree's boundaries.
        6. If a right subtree exists, create its root from the position after the root and left subtree in preorder, then enqueue its boundaries.
        7. Continue until the queue is empty and return the root.

    - **📝 Pseudocode :**
        ```text
        if preorder is empty:
            return null

        root = new Node(preorder[0])
        queue = [(root, full preorder range, full inorder range)]

        while queue is not empty:
            node, preRange, inRange = dequeue()
            rootIndex = inorderMap[node.value]
            leftSize = rootIndex - inRange.start

            if left subtree exists:
                create left child from preorder[preRange.start + 1]
                enqueue left child with left subtree ranges

            if right subtree exists:
                create right child from preorder[preRange.start + leftSize + 1]
                enqueue right child with right subtree ranges

        return root
        ```

    - **⏱️ Complexity**
        - **Time:** `O(n)` — Each node is processed once, with constant-time hashmap lookups.
        - **Auxiliary Space:** `O(n)` — The hashmap and queue require linear space.

#### 📊 Approach Comparison

| Feature | 🌿 Recursive DFS | 📚 Iterative DFS | 🚦 Iterative BFS |
|---|---|---|---|
| Main structure | Call stack | Explicit stack | Queue |
| Processing order | Depth-first | Depth-first | Level-order |
| Subtree boundaries | Recursive arguments | Inorder synchronization | Queued range metadata |
| Recursion used | Yes | No | No |
| Time | `O(n)` | `O(n)` | `O(n)` |
| Auxiliary space | `O(n)` | `O(n)` | `O(n)` |
| Main advantage | Natural, easy to follow | Avoids recursion | Demonstrates level-order processing |

**🏁 Takeaway:** All three approaches reconstruct the same tree in `O(n)` time. Recursive DFS is straightforward and natural for subtree decomposition; iterative DFS avoids recursion; iterative BFS demonstrates queue-based construction, though it requires more bookkeeping for traversal boundaries.

---
