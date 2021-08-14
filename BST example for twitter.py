""Find the top 10 trending hashtags in twitter using python.

Assumptions & notes :  

1) A tweet is a text being input by tweeters.  

2) A main method in a python class to be implemented which takes the tweet as an input.  

3) You need to extract hashtag from a tweet text (Ex: Dhoni is hashtag in the tweet -> " Worlds best cricketer is #Dhoni")  

4) Maintain a data structure that keeps tracking of the count of each hashtag that is coming to your main method  

5) print the list of top 10 hashtags at the end of main method execution""


import threading
class node:
    def __init__(self,key,name):
        self.name=name
        self.right=None
        self.left=None
        self.key=key
class hashtagclass():
    hashtagdict={}
    hashtag=[]
    mainroot=None
    hashtagdicts={}
    no_of_tweets=0
    def __init__(self,tags):
        self.tags=tags
        self.top10tags=[]
        self.keylock=threading.Lock()
    def postorder(self,root):
        elements=[]
        if root is not None:
            elements+=self.postorder(root.right)
            elements.append(root.name)
            elements+=self.postorder(root.left)
        return elements
    def insert(self,nodee, key, name):
        #if the tree is empty it will return a new node
        if nodee is None:
            return node(key, name)
        #otherwise recurrsive  down the tree
        if key <= nodee.key:
            nodee.left = self.insert(nodee.left, key, name)
        else:
            nodee.right = self.insert(nodee.right, key, name)

        # return the (unchanged) node pointer
        return nodee

    def minValueNode(self,node):
        present = node
        #loop down to find the leftmost leaf
        while (present.left is not None):
            current = present.left
        return present
    def deleteNode(self,root, key, name):
        # Base Case
        if root is None:
            return root
        # If the node to be deleted
        # its count smaller than the root's
        # node then it lies in  left subtree
        #otherwise node lies in left subtree
        if key <= root.key and root.name != name:
            root.left = self.deleteNode(root.left, key, name)
        elif (key > root.key) and root.name != name:
            root.right = self.deleteNode(root.right, key, name)
        else:
            if name == root.name and root.key == key:
                #deleting node having one child
                if root.left is None:
                    temp = root.right
                    root = None
                    return temp

                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp
                #deleting node having one child
                #get the inorder successor
                temp = self.minValueNode(root.right)
                #copy the inorder successors
                #content to this node
                root.key = temp.key
                root.name = temp.name
            #delete the inorder successor
                #print("yp yp")
                root.right = self.deleteNode(root.right, temp.key, temp.name)
        return root
    def add_node(self,node,rootnode):
        if node.key<=rootnode.key:
                if rootnode.left:
                    rootnode=self.add_node(node,rootnode.left)
                else:
                    rootnode.left=node
        else:
            if rootnode.right:
                for k in range(0,20):
                    rootnode=self.add_node(node,rootnode.right)
            else:
                for i in range(0,len(s)):
                    if rootnode.data>=20:


                        rootnode.right=node

    def adjust_bst(self,nodee, key, name):
        #accepts the root node, count,#tag
        #delete the node and update the tree
        m=self.deleteNode(nodee,key, name)
        node1 = node(key+1,name)
        mm=self.add_node(node1,m)
        return m

    def find_toptags(self):
        self.tags = self.tags.split(" ")
        self.keylock.acquire()
        hashtagclass.no_of_tweets += 1
        for i in self.tags:
            if i[0] == '#':
                tag = i[1:len(i)]
                #get rootnode from the static variable
                #get the #tag from the input
                #if rootnode is None then call insert() method which creates BST and update rootnode,
                    # update dictionary containing #tag and count as key value pair
                #otherwise get the count from the dictionary and call method adjust_bst
                    #and update rootnode and dictionary
                if hashtagclass.mainroot != None:
                    if tag in hashtagclass.hashtag:
                        c = hashtagclass.hashtagdicts[tag]
                        hashtagclass.mainroot = self.adjust_bst(hashtagclass.mainroot, c, tag)
                        hashtagclass.hashtagdicts[tag] = c + 1
                    else:
                        hashtagclass.mainroot = self.insert(hashtagclass.mainroot, 1, tag)
                        hashtagclass.hashtagdicts[tag] = 1
                        hashtagclass.hashtag.append(tag)
                else:
                    hashtagclass.hashtagdicts[tag] = 1
                    hashtagclass.mainroot = self.insert(hashtagclass.mainroot, 1, tag)
                    hashtagclass.hashtag.append(tag)


        print("\nTop trending #tags after ",hashtagclass.no_of_tweets,"tweets")
        count=0
        #get the list of trending tags by calling postorder method
        top=(self.postorder(hashtagclass.mainroot))

        if len(top)<11:
            print(top)
        else:
            print(top[0:10])
        self.keylock.release()
def executionmain(text):
    obj = hashtagclass(text)
    obj.find_toptags()
t1=threading.Thread(target=executionmain,args=(input(), ))
t2=threading.Thread(target=executionmain,args=(input(), ))
t3=threading.Thread(target=executionmain,args=(input(), ))
t1.start()
t2.start()
t3.start()



