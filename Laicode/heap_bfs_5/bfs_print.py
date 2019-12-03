
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None

def bfs_print_layer(root):
    '''
             1   expand(1) → generate(3) and generate(2)
          /    \ 
        3	    2  
      /  \     /  \
     5    4	  7   null
    /  \ 
   9   11
   
  [1]   queue.size = 1   1    [3,2]
  [3 2] queue.size = 2   3    [2, 5, 4]
                         2    [5, 4, 7]
  [5,4,7] queue.size=3   5    [4,7, 9, 11] 
                         4    [7, 9, 11]  
                         7    [9 ,11]
  [9 ,11] queue.size =2  9    [11]
                         11   []
    '''
    if root == None:
        return
    
    queue = [] # FIFO
    queue.append(root)
    while queue:
        current_layer_size = len(queue)
        for i in range(current_layer_size): 
            node = queue.pop(0)
            if node.leftNode:
                queue.append(node.leftNode)
            if node.rightNode:
                queue.append(node.rightNode)
            print(node.value, end= ' ')
        print()


def is_complete_tree(root):
    if not root:
        return 
    
    queue = []
    queue.append(root)
    flag = False
    while len(queue) > 0:
        current = queue.pop(0)
        # if any of thd child is not preset, set the flag to true
        if flag and current.leftNode: 
            return False
        elif not current.leftNode: #if flag is set true but still having a child, Fasle complete tree
            flag = True
        else:
            queue.append(current.leftNode)
            
        if flag and current.rightNode:
            return False
        if not current.rightNode:
            flag = True
        else:
            queue.append(current.rightNode)
    return True

def barpartite(root):
    

if __name__ == "__main__":
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2)
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node7 = TreeNode(7)
    node9 = TreeNode(9)
    node11 = TreeNode(11)
    # node2.rightNode = TreeNode(23)
    
    node1.leftNode = node3
    node1.rightNode = node2
    node2.leftNode = node7
    node3.leftNode = node5
    node3.rightNode = node4
    node5.leftNode = node9
    node5.rightNode = node11
    
    # bfs_print_layer(node1)
    result = is_complete_tree(node1)
    print(result)