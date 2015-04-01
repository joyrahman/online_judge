# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        stack = []
        temp = root
        while True:
            while temp is not None:
                if temp.right is not None:
                    stack.append(temp.right)
                stack.append(temp)
                temp = temp.left

            temp = stack.pop()
            if temp.right and self.top(stack) == temp.right:
                stack.pop()
                stack.append(temp)
                temp =temp.right
            else:
                print(temp.val)
                temp = None

            if len(stack)== 0:
                break
    def top(self,stack):
        a = stack.pop()
        stack.append(a)
        return a






def create_binary_tree():
    head = TreeNode(1)
    runner = head

    temp_l = TreeNode(2)
    temp_r = TreeNode(3)
    runner.left = temp_l
    runner.right = temp_r

    runner_l = runner.left
    runner_r = runner.right

    temp_l = TreeNode(4)
    temp_r = TreeNode(5)
    runner_l.left = temp_l
    runner_l.right = temp_r

    temp_l = TreeNode(6)
    temp_r = TreeNode(7)
    runner_r.left = temp_l
    runner_r.right = temp_r

    runner = runner_l.right
    temp_l = TreeNode(10)
    temp_r = TreeNode(11)
    runner.left = temp_l
    runner.right = temp_r

    return head

def main():

    s = Solution()
    head = create_binary_tree()
    s.postorderTraversal(head)


if __name__ == "__main__":
    main()