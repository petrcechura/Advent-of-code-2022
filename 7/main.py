# import TreeNode as TN
import treelib as tlib
import TreeNode as fn

def command_ls(file, size):
    global root
    global cur_node
    
    if root.contains(file):
        pass
    elif size == 'dir':
        root.create_node(tag=file,
                             identifier=file,
                             data=fn.fileNode(name=file, size=0),
                             parent=cur_node)
    else:
        root.create_node(tag=file,
                             identifier=file,
                             data=fn.fileNode(name=file, size=size),
                             parent=cur_node)
        root.update_node(cur_node, data=fn.fileNode(name=cur_node, size=5)) # TODO

def command_cd(next_dir):
    global cur_node
    global root
    
    if next_dir == '..': # step back to ancestor
        cur_node = root.ancestor(cur_node)
    elif next_dir == '/': # step into a root
        cur_node = 'root'
    elif next_dir.isascii(): 
        if root.contains(next_dir): # if child already exists, just step into it
            cur_node = next_dir
        else: # if child doesn't exist, create a new one with given name
            root.create_node(tag=next_dir,
                             identifier=next_dir,
                             data=fn.fileNode(name=next_dir, size=0),
                             parent=cur_node)
            cur_node = next_dir
            
    else:
        raise Exception("Invalid argument of cd command")
    
    
# get input
with open("input.txt", 'r') as f:
    lines = f.readlines()

commands = []
ls_files = []
for line in lines:
    com = line.split(sep=' ')
    if line[0] == '$':
        if len(ls_files) > 0: # if files have been gathered from previous lines (due to 'ls' command)
            commands.append(('ls', ls_files.copy()))
            ls_files.clear()
        
        if com[1] == 'cd': # command 'cd' is taken with a argument
            commands.append(('cd', com[2]))
            
    else:
        
        ls_files.append((com[1], com[0])) # filename and size
        

# root
root = tlib.Tree()
root.create_node(tag='root', identifier='root', data=fn.fileNode(name='root', size=0))
cur_node = 'root'
# commands


# run the program
for command in commands:
    if command[0] == 'cd':
        command_cd(command[1])
    elif command[0] == 'ls':
        for file in command[1]:
            command_ls(file[0], file[1])
    else:
        raise Exception("ERROR!")
    
root.show(data_property='size')

