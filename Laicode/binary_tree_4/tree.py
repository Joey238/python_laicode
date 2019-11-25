class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right =None
        
    
def isBST(root, min, max):
    if not root:
        return True
    elif root.value <= min or root.value >= max:
        return False
    
    return isBST(root.left, min, root.value) and isBST(root.right, root.value, max)
    
    
def bstRange(root, lower, higher):
    if root == None:
        return True

    
    if root.value > lower:
        bstRange(root.left, lower, higher)
    elif root.value >= lower and root.value <= higher: #
        print(root.value)
    elif root.value < righer:
        bstRange(root.right, lower, higher)