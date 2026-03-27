# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        def dfs(node):
            if not node: return
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
            nums.append(node.val)
        dfs(root)

        i = 0
        j = len(nums) - 1
        nums.sort()
        
        while i < j:
            if nums[i] + nums[j] == k:
                return True
                break
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1

        return False