class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, value):
        if self.leftChild == None:
            self.leftChild = BinaryTree(value)
        else:
            newNode = BinaryTree(value)
            newNode.leftChild = self.leftChild
            self.leftChild = newNode
        return self.leftChild

    def insertRight(self, value):
        if self.rightChild == None:
            self.rightChild = BinaryTree(value)
        else:
            newNode = BinaryTree(value)
            newNode.rightChild = self.rightChild
            self.rightChild = newNode
        return self.rightChild

    def preOrder(self):
        print(self.value)
        if self.leftChild:
            self.leftChild.preOrder()
        if self.rightChild:
            self.rightChild.preOrder()

###
a = BinaryTree('a')
    ###
b = a.insertLeft('b')
        ###
d = b.insertLeft('d')
            ###
h = d.insertLeft('h')
            ###
i = d.insertRight('i')
        ###
e = b.insertRight('e')
            ###
j = e.insertLeft('j')
            ###
k = e.insertRight('k')
    ###
c = a.insertRight('c')
        ###
f = c.insertLeft('f')
            ###
l = f.insertLeft('l')
            ###
m = f.insertRight('m')
        ###
g = c.insertRight('g')
            ###
n = g.insertLeft('n')
            ###
o = g.insertRight('o')

a.preOrder()
