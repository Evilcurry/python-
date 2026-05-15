class Node:
    def __init__(self, value, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree:
    def __init__(self):
        self.root = None
        self.queue = [] # 辅助队列
    def build_tree(self, node: Node):
        if self.root is None:
            self.root = node
            self.queue.append(node)
        else:
            self.queue.append(node)
            if self.queue[0].lchild is None: #如果当前节点的左孩子为空
                self.queue[0].lchild = node # put lift child
            else:
                self.queue[0].rchild = node # put right child
                self.queue.pop(0)


    def preorder(self, node: Node):
        if node is not None:
            print(node.value,end=' ')
            self.preorder(node.lchild)
            self.preorder(node.rchild)

    def leve_lorder(self):
        queue = []
        queue.append(self.root)
        while queue:
            out_node:Node = queue.pop(0)
            print(out_node.value,end=' ')
            if out_node.lchild:
                queue.append(out_node.lchild)
            if out_node.rchild:
                queue.append(out_node.rchild)

if __name__ == '__main__':
    btree = BinaryTree()
    for i in range(1,11):
        new_node = Node(i)
        btree.build_tree(new_node)
    btree.preorder(btree.root)
    print()
    btree.leve_lorder()