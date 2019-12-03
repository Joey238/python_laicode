class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right =None
        
    
def bstRange(root, lower, higher):
    if root == None:
        return True

    
    if root.value > lower:
        bstRange(root.left, lower, higher)
    elif root.value >= lower and root.value <= higher: #
        print(root.value)
    elif root.value < righer:
        bstRange(root.right, lower, higher)
        

def isBST(root):
    if not root:
        return True
    min = float('-inf')
    max = float('inf')
    return  isBST_helper(root, min, max)

def isBST_helper(root, min, max):
    if not root:
        return True
    elif root.value <= min or root.value >= max:
        return False
    # float('-inf')
    # float('inf')
    return isBST_helper(root.left, min, root.value) and isBST_helper(root.right, root.value, max)



class TreeNode2:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None


class BinarySearchTree:
    '''1:21
        -design a contianer that use binary search tree to organize the key -value pairs. 
        -当value is a objcet , so we maintain a key
    '''
    def __init__(self, root):
         self.__root = root
    
    def __query(self, root, key):      
        if not root: # base case
            return None
        if root.key == key:
            print(root.value)  
            return root.value # return value (here is key-value pair)
        elif root.key < key:
            self.__query(root.right, key)
        else:
            self.__query(root.left, key)
    
    def __insert(self, root, key, value):
        if not root:
            return TreeNode2(key, value)
        elif root.key < key:
            root.right = self.__insert(root.right, key, value)
            print(root.right.value)
        elif root.key < key:
            root.left = self.__insert(root.left, key, value)
            print(root.left.value)
        else:
            root.value = value # update is same keys  
            print(f'root: {root.value}')
        return root 
        
    def query(self, key): 
        '''用户使用的api和我们实现的api分开
        '''
        return self.__query(self.__root, key)
    
    def insert(self, key, value):
        # if empty tree, then create a node
        if not self.__root:
            return TreeNode2(key, value)
        if not self.query(key): # update or 
            self.__insert(self.__root, key, value)
         

if __name__ == "__main__":
    node1 = TreeNode2(1, '1')
    node3 = TreeNode2(3, '3')
    node2 = TreeNode2(2, '2')
    root = TreeNode2(5, '5')
    node4 = TreeNode2(6, '6')
    node7 = TreeNode2(7, '7')
    node9 = TreeNode2(9, '9')
    node11 = TreeNode2(11, '11')

    root.left = node3
    root.right = node4
    node3.left = node2
    node4.left = node7
    node4.right= node9
    node9.right = node11

    
    bst = BinarySearchTree(root)
    # print(bst.query(9))
    node = bst.insert(8,8)
    print(node)