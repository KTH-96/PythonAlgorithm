from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaximumDepthOfBinaryTree104:
    def dfs(self, root: 'TreeNode', depth: int) -> int:
        if not root:
            return depth - 1

        left_depth = self.dfs(root.left, depth + 1)
        right_depth = self.dfs(root.right, depth + 1)

        return max(left_depth, right_depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 1)


tree = MaximumDepthOfBinaryTree104()

# 직접 트리를 생성
node7 = TreeNode(7)
node15 = TreeNode(15)
node20 = TreeNode(20, node15, node7)
node9 = TreeNode(9)
root = TreeNode(3, node9, node20)

print(tree.maxDepth(root))
