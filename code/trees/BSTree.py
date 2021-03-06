# -*- coding: utf-8 -*-
# 创造BSTree
# 查找BSTree的节点
# 插入BSTree的节点
# 删除BSTree的节点


class BSTreeNode(object):
    def __init__(self, val=None, lnode=None, rnode=None):
        self.val = val
        self.lnode = lnode
        self.rnode = rnode


def insert_bstree(root, val):
    if root is None:
        root = BSTreeNode(val=val)
    current = root
    while current is not None:
        if val < current.val:
            if current.lnode is None:
                current.lnode = BSTreeNode(val=val)
                break
            current = current.lnode
        else:
            if current.rnode is None:
                current.rnode = BSTreeNode(val=val)
                break
            current = current.rnode
    return root

def create_bstree(data=[]):
    if len(data) == 0:
        return None
    root = BSTreeNode(val=data[0])
    for i in data[1:]:
        insert_bstree(root, i)
    return root

# 中序遍历
def in_order(root):
    if root is None:
        return None
    in_order(root.lnode)
    print root.val
    in_order(root.rnode)


def search_bstree(root, val):
    if root is None:
        return None
    ret = []
    while root is not None:
        if val < root.val:
            root = root.lnode
        else:
            if val == root.val:
                ret.append(root.val)
            root = root.rnode
    return ret

def max_bstree(root):
    if root is None:
        return None
    q = root.rnode
    while q is not None:
        root = q
        q = q.rnode
    return root.val


def min_bstree(root):
    if root is None:
        return None
    q = root.lnode
    while q is not None:
        root = q
        q = q.lnode
    return root.val

# 根节点的前继为BSTreeNode()
def pre_node_bstree(root, val):
    if root is None:
        return
    pre_ret = []
    pre = BSTreeNode()
    current = root
    while current is not None:
        if val < current.val:
            pre = current
            current = current.lnode
        else:
            if val == current.val:
                pre_ret.append(pre)
            pre = current
            current = current.rnode
    return pre_ret

# 叶子节点的后继节点为BSTreeNode()
def post_node_bstree(root, val):
    if root is None:
        return
    post_ret = []
    cur = root
    while cur is not None:
        if val < cur.lnode:
            cur = cur.lnode
        else:
            if val == cur.val:
                if cur.rnode is None:
                    cur.rnode = BSTreeNode()
                post_ret.append(cur.rnode)
            cur = cur.rnode
    return post_ret


# 不支持重复节点出现
def delete_bstree(root, val):
    if root is None:
        return
    if root.val == val:
        if not root.lnode and not root.rnode:
            return None
        elif root.lnode and not root.rnode:
            return root.lnode
        elif root.rnode and not root.lnode:
            return root.rnode
        else:
            ppmin = root
            p_cur = root.rnode
            if p_cur.lnode is None:
                ppmin.rnode = p_cur.rnode
                root.val = p_cur.val
                return root
            while p_cur.lnode is not None:
                ppmin = p_cur
                p_cur = p_cur.lnode
            root.val = p_cur.val
            ppmin.lnode = None
            return root
    pre = root
    cur = root
    while cur is not None:
        if val < cur.val:
            pre = cur
            cur = cur.lnode
        else:
            if val == cur.val:
                if not cur.lnode and not cur.rnode:
                    pre.rnode = None
                    pre.lnode = None
                elif cur.lnode and not cur.rnode:
                    pre.rnode = cur.lnode
                elif cur.rnode and not cur.lnode:
                    pre.rnode = cur.rnode
                else:
                    ppmin = cur
                    p_cur = cur.rnode
                    if p_cur.lnode is None:
                        ppmin.rnode = p_cur.rnode
                        cur.val = p_cur.val
                    else:
                        while p_cur.lnode is not None:
                            ppmin = p_cur
                            p_cur = p_cur.lnode
                        cur.val = p_cur.val
                        ppmin.lnode = None
            pre = cur
            cur= cur.rnode
    return root


if __name__ == '__main__':
    data1 = [1, 1, 3, 2, 5, 4, 3, 5]
    root1 = create_bstree(data=data1)
    in_order(root1)
    val1 = 1
    print search_bstree(root1, val1)
    print max_bstree(root1)
    print min_bstree(root1)
    data2 = [1, 2, 3, 4, 5, 3, 3]
    root2 = create_bstree(data=data2)
    val2 = 1
    pres = pre_node_bstree(root2, val2)
    post = post_node_bstree(root2, val2)
    for p in pres:
        print p.val if p and p.val else 'None', p.lnode.val if p and p.lnode else 'None', p.rnode.val if p and p.rnode else 'None'
    for p in post:
        print p.val if p and p.val else 'None', p.lnode.val if p and p.lnode else 'None', p.rnode.val if p and p.rnode else 'None'
    data3 = [3, 1, 4, 13, 2, 7, 8, 9, 6, 5, 10]
    val3 = 7
    root3 = create_bstree(data=data3)
    del_root = delete_bstree(root3, val3)
    in_order(del_root)