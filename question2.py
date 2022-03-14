class Node:
     def __init__(self, key):
        self.key = key
        self.child = []
   
# Utility function to create a new tree node
def newNode(key):   
    temp = Node(key)
    return temp
     
# Prints the n-ary tree level wise
def LevelOrderTraversal(root):
 
    if (root == None):
        return
    # Standard level order traversal code
    # using queue
    q = []  # Create a queue
    q.append(root); # Enqueue root
    while (len(q) != 0):
        n = len(q)
  
        # If this node has children
        while (n > 0):
         
            # Dequeue an item from queue and print it
            p = q[0]
            q.pop(0)
            print(p.key, end=' ')
   
            # Enqueue all children of the dequeued item
            for i in range(len(p.child)):
             
                q.append(p.child[i])
            n -= 1
   
# Driver program
if __name__=='__main__':

    rootkey = input("Enter root role name : ")
    root = newNode(rootkey)
    counter =0
    while counter<2:
        print("Operations : \n\t 1. Add Sub Role")
        op = int(input("\nOperation to be performed : "))
        if op==1 :
            subrole = input("Enter sub role name : ")
            report = input("Enter reporting to role name : ")
            if root.key == report:
                root.child.append(newNode(subrole))
        counter+=1
        
    print("\n")
    LevelOrderTraversal(root)