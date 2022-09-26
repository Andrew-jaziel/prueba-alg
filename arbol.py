
class Node:  
    def __init__(self,value=None,left=None,right=None):  
         self.value=value  
         self.left = left #left subtree
         self.right = right #right subárbol
def preTraverse(root):  
    '''
         Recorrido previo al pedido
    '''
    if root==None:  
        return  
    print(root.value)  
    preTraverse(root.left)  
    preTraverse(root.right)  
 
def midTraverse(root): 
    '''
         Recorrido en orden
    '''
    if root==None:  
        return  
    midTraverse(root.left)  
    print(root.value)  
    midTraverse(root.right)  
  
def afterTraverse(root):  
    '''
         Recorrido posterior al pedido
    '''
    if root==None:  
        return  
    afterTraverse(root.left)  
    afterTraverse(root.right)  
    print(root.value)
    
if __name__=='__main__':
    root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    print ('Preorden traversal:')
    preTraverse(root)
    print('\n')
    print ('Recorrido en orden:')
    midTraverse(root)
    print('\n')
    print ('Recorrido posterior al pedido:')
    afterTraverse(root)
    print('\n')
