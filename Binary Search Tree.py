# -*- coding: utf-8 -*-

class Node():

    def __init__(self, rootObj):
        self.parent = None
        self.key = rootObj
        self.rightChild = None
        self.leftChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = Node(newNode)

        else:
            t= Node(newNode)
            t.leftChild = self.leftChild
            t.parent = self
            self.leftChild = t
            self.leftChild.parent = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = Node(newNode)
        else:
            t = Node(newNode)
            t.rightChild = self.rightChild
            t.parent = self
            self.rightChild = t
            self.rightChild.parent = t

    def getRightChild(self):

        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setLeftChild(self, leftchild):
        self.leftChild = leftchild

    def setRightChild(self, rightChild):
        self.rightChild = rightChild

    def getRootVal(self):
        if self is None:
            return None
        else:
            return self.key

    def setRootVal(self, key):
        self.key = key

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent


class BinaryTree():
    def __init__(self, root):
        self.root = root

    def set_root(self, root):
        self.root

    def get_root(self):
        return self.root

    def __getattr__(self, item):
        try:
            r = object.__getattribute__(self, item)
        except:
            r = None
        return r

    def tree_insert(self, node):
        # tree是树本身,node是叶子
        if self.get_root() is None:
            # node为根
            self.set_root(node)
        else:
            current_node = self.get_root()
            while True:
                if node.getRootVal() <= current_node.getRootVal():
                    if current_node.getLeftChild() is None:
                        # 设置其左子树
                        node.setParent(current_node)
                        current_node.setLeftChild(node)
                        break
                    else:
                        current_node = current_node.getLeftChild()
                else:
                    if current_node.getRightChild() is None:
                        node.setParent(current_node)
                        current_node.setRightChild(node)
                        break
                    else:
                        current_node = current_node.getRightChild()

    def tree_max(self, tree):
        # 最大关键元素
        current_node = tree.get_root()
        while True:
            if current_node.getRightChild() is not None:
                current_node = current_node.getRightChild()
            else:
                return current_node

    def tree_min(self, tree):
        # 最小关键元素
        def get_current_node(tree):
            if isinstance(tree, BinaryTree):
                current_node = tree.get_root()
            else:
                current_node = tree
            return current_node

        current_node = get_current_node(tree)
        while True:
            if current_node.getLeftChild() is not None:
                current_node = current_node.getLeftChild()
            else:
                return current_node

    def iterative_tree_search(self, tree, node):
        # 查找二叉树
        current_node = tree.get_root()
        while True:
            if current_node is None:
                return None
            else:
                if node.getRootVal() < current_node.getRootVal():
                    current_node = current_node.getLeftChild()
                elif node.getRootVal() == current_node.getRootVal():
                    return current_node
                else:
                    current_node = current_node.getRightChild()

    def tree_successor(self, x):
        # 假设能狗获取到父节点
        if x.getRightChild() is not None:
            return self.tree_min(x.getRightChild())

        else:
            while True:
                if x.getParent().getRightChild() == x:
                    return x.getParent()
                else:
                    x = x.getParent()

    def inorder_tree_walk(self, tree):
        # 中序遍历
        def get_current_node(tree):
            if isinstance(tree, BinaryTree):
                current_node = tree.get_root()
            else:
                current_node = tree
            return current_node

        current_node = get_current_node(tree)

        if current_node is not None:
            self.inorder_tree_walk(current_node.getLeftChild())
            # 打印根元素
            print current_node.getRootVal()
            self.inorder_tree_walk(current_node.getRightChild())

    def tree_delete(self, tree, z):
        # 删除
        def has_one_child(z):
            if (z.getLeftChild() is not None and z.getRightChild() is None) or \
                    (z.getLeftChild() is None and z.getRightChild() is not None):
                return True
            else:
                return False

        def has_two_child(z):
            if z.getLeftChild() is not None and z.getRightChild() is not None:
                return True
            else:
                return False

        def has_no_child(z):
            if (z.getLeftChild() is None and z.getRightChild() is None):
                return True
            else:
                return False

        def is_parent_rightchild(z):
            if z.getParent().getRightChild() == z:
                return True
            else:
                return False

        def get_z_child(z):
            if z.getLeftChild() is not None:
                return z.getLeftChild()
            else:
                return z.getRightChild()

        def put_to_z_location(successor):
            successor.setParent(z_parent)
            z_parent.setLeftChild(successor)
            successor.setRightChild(z_right_child)
            z_right_child.setParent(successor)
            successor.setLeftChild(z_left_child)
            z_left_child.setParent(successor)

        if has_no_child(z):
            if is_parent_rightchild(z):
                z.getParent().setRightChild(None)
            else:
                z.setParent().setLeftChild(None)
        elif has_one_child(z):
            z_child = get_z_child(z)
            if is_parent_rightchild(z):
                z_child.setParent(z.getParent())
                z.getParent().setRightChild(z_child)
            else:
                z_child.setParent(z.getParent())
                z.getParent().setLeftChild(z_child)
        elif has_two_child(z):
            if tree.get_root() is None:
                # 设定节点为根
                tree.set_root(z)
            else:
                successor = self.tree_successor(z)  # 求出后继者
                successor_right_child = successor.getRightChild()
                successor_parent = successor.getParent()
                z_parent = z.getParent()
                z_left_child = z.getLeftChild()
                z_right_child = z.getRightChild()

                if successor_right_child is not None:
                    successor_right_child.setParent(successor.getParent())
                    successor_parent.setLeftChild(successor_right_child)
                else:
                    successor_parent.setRightChild(None)
                put_to_z_location(successor)
        else:
            print 'error'



node15 = Node(15)
node5 =  Node(5)
node16 = Node(16)
node3 = Node(3)
node12 = Node(12)
node10 = Node(10)
node13 = Node(13)
node6 = Node(6)
node7 = Node(7)

node20 = Node(20)
node18 = Node(18)
node23 = Node(23)

tree = BinaryTree(node15)

# －－－－－－－－－－－测试插入－－－－－－－－－－－－－－－
# 再考虑放到树里面
# 测试树为空,不为空

tree.tree_insert(node5)
tree.tree_insert(node16)
tree.tree_insert(node3)
tree.tree_insert(node12)
tree.tree_insert(node10)
tree.tree_insert(node13)
tree.tree_insert(node6)
tree.tree_insert(node7)
tree.tree_insert(node20)
tree.tree_insert(node18)
tree.tree_insert(node23)


# ------------------查看插入是否成功－－－－－－－－－－－－－
print node6.getRightChild().getRootVal() == 7
print node12.getRightChild().getRootVal() == 13
print node10.getLeftChild().getRootVal() == 6


# ----------------求出树的最大值－－－－－－－－－－－－－－－
print u'最大值: ' +str( tree.tree_max(tree).getRootVal())


# #----------------求出树的最小值－－－－－－－－－－－－－－－－
print u'最小值: ' +str( tree.tree_min(tree).getRootVal())


# # ---------------查找节点－－－－－－－－－－－－－－－－－－－
print u'查出来的节点是: '+ str(tree.iterative_tree_search(tree, node10).getRootVal())


# -----------------删除一个子女都没有的节点－－－－－－－－－－－－－－－－－－
tree.tree_delete(tree, node13)
print u'node12的右子: ' + str(tree.iterative_tree_search(tree, node13))


# -----------------删除有一个子女的节点------------------------------------------
tree.tree_delete(tree, node16)
print u'node15的右子: ' + str(tree.iterative_tree_search(tree, node15).getRightChild().getRootVal())
print u'node20的父亲: ' + str(tree.iterative_tree_search(tree, node20).getParent().getRootVal())


# ------------------- 删除有两个子女的节点－－－－－－－－－－－－－－－－－－－－－－－
tree.tree_delete(tree, node5)
print u'node3的父节点: ' + str(tree.iterative_tree_search(tree, node15).getLeftChild().getRootVal())
print u'node15的左子节点: ' +str(tree.iterative_tree_search(tree, node3).getParent().getRootVal())

# ---------------------中序算法打印----------------------------
tree.inorder_tree_walk(tree)


