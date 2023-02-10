import treelib as treelib

class fileNode(treelib.Node): 
    def __init__(self, name, size): 
        self.size = size
        self.name = name