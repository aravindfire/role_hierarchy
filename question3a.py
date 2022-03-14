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
        return;
    # Standard level order traversal code
    # using queue
    q = []  # Create a queue
    q.append(root); # Enqueue root
    output =[] # to store output
    while (len(q) != 0):
        n = len(q)
  
        # If this node has children
        while (n > 0):
         
            # Dequeue an item from queue and print it
            p = q[0]
            q.pop(0)
            output.append(p.key)
   
            # Enqueue all children of the dequeued item
            for i in range(len(p.child)):
             
                q.append(p.child[i]);
            n -= 1
    print(','.join(output))
    
def insert(root,subrole,report):
    if root.key == report:
            root.child.append(newNode(subrole))
    else :
            level = []
            level.append(root)
            while (len(level) != 0):
                n = len(level)
                while (n > 0):
                    # Dequeue an item from queue and print it
                    p = level[0]
                    level.pop(0)
                    if p.key== report :
                        p.child.append(newNode(subrole))
                    # Enqueue all children of the dequeued item
                    for i in range(len(p.child)):
                            level.append(p.child[i]);
                    n -= 1
    print("\n")
    
   
# Driver program
if __name__=='__main__':

    rootkey=input("Enter the root role name : ")
    root = newNode(rootkey)
    op = 0 
    while op!=2:
        print("Operations : \n\t 1. Add Sub Role. \n\t 2. Display Roles.")
        op = int(input("\nOperation to be performed : "))
        if op==1 :
            subrole = input("Enter sub role name : ")
            report = input("Enter reporting to role name : ")
            insert(root,subrole,report)

    LevelOrderTraversal(root)
    