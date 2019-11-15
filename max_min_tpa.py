'''
@Description: 智能算法
@Autor: xiaosi
@Date: 2019-11-13 16:31:56
@LastEditors: xiaosi
@LastEditTime: 2019-11-15 20:38:49
'''
import json

g = [
    [99999, 3, 1, 5, 8],
    [3, 99999, 6, 7, 9],
    [1, 6, 99999, 4, 2],
    [5, 7, 4, 99999, 3],
    [8, 9, 2, 3, 99999]
]

class TspTree(object):
    # 该类存储根节点和子节点列表

    # 建立TspTree
    def __init__(self, node, max_limit):
        self.root = TspNode([node])
        # 定义叶子节点
        self.leaf_node = [self.root]
        # 上限
        self.max_limit = max_limit
    
    # 拓展Tsp节点
    def tuozhan(self):

        # 找出要拓展的点即exc最小的点
        tuozhan_node = self.leaf_node[0]
        min_exc = self.max_limit
        for node in self.leaf_node:
            if node.exc < min_exc:
                min_exc = node.exc
                tuozhan_node = node

        print(tuozhan_node)

        # 当路径中包含所有的点时返回结果
        if len(tuozhan_node.route_list) == len(g):
            return tuozhan_node.exc

        # 父节点移除叶子节点列表
        self.leaf_node.remove(tuozhan_node)
        # 拓展子节点并加入叶子节点列表
        for i in range(len(g)):
            if i not in tuozhan_node.route_list:
                new_list = [j for j in tuozhan_node.route_list]
                new_list.append(i)
                new_node = TspNode(new_list)
                self.leaf_node.append(new_node)
                tuozhan_node.child.append(new_node)
        return -1

# 建立分支树 树中存储路径route_list和该节点的期望值以及子节点列表
class TspNode(object):    

    def __init__(self, route_list):
        self.route_list = [i for i in route_list]
        self.exc = self.get_exc()
        self.child = []

    def __repr__(self):
        return "<节点路径{},期望值{}>".format(json.dumps(self.route_list), self.exc)
    
    # 求解期望值
    def get_exc(self):
        route_list = self.route_list
        exc = 0
        # 如果路径长度为5说明已经扩展到顶点了直接返回回路长度
        if len(route_list) == len(g):
            for i in range(len(route_list)):
                exc += g[route_list[i]][route_list[(i+1)%len(route_list)]]
            return exc
        for i in range(len(g)):
            # i在list里时要算已经确定的边
            if i in route_list:
                num = 0 #num用来计数
                new_list = sorted(g[i]) #取出该行
                i_index = route_list.index(i)
                # 如果此节点左边有值（即此节点左侧有一条路径）则计算这条路径
                if i_index != 0:
                    exc += g[i][route_list[i_index-1]]
                    new_list.remove(g[i][route_list[i_index-1]])
                    num += 1
                # 同理右边有值的话先算右边的路径
                if i_index+1 != len(route_list):
                    exc += g[i][route_list[i_index+1]]
                    new_list.remove(g[i][route_list[i_index+1]])
                    num += 1
                # 没有路径的话用最小值补上
                if num == 0:
                    exc += new_list[0]
                    exc += new_list[1]
                if num == 1:
                    exc += new_list[0]
                
            # 不在list里时直接算两个最小值
            else:
                new_list = sorted(g[i])
                exc += new_list[0]
                exc += new_list[1]
        return exc/2.0

# 通过深度优先遍历到一个回路作为最大的界限
def get_route():
    '''
    通过深度优先遍历到一个回路作为最大的界限
    '''
    routes = []
    g_len = len(g)
    # 从第0个节点开始深度优先遍历求得一个环路
    # visited 保存所有以遍历的节点 防止回路
    visited_list = []
    visited_list.append(0)
    stack = [[0, 0]] #第一个数代表当前状态、第二个数代表要扩展的状态、初始化为第零个节点
    while(stack):
        # 取出栈顶元素
        # print(stack)
        thisn, nextn = stack[-1]
        # 此时该节点上层节点全部拓展完了
        # print(visited_list)
        if( nextn >= g_len):
            # 退栈寻找其他通路
            if(len(visited_list) == 5 and (g[thisn][visited_list[0]] != -1)):
                route = [i for i in visited_list]
                return route
            visited_list.pop()
            stack.pop()
            # 此时下层节点全部遍历完，上层节点横向拓展
            if stack:
                stack[-1][1] += 1
        # 如果要扩展的节点时空节点直接拓展下一个
        elif(g[thisn][nextn] == -1) or (nextn in visited_list):
            stack[-1][1] += 1
        # 查看nextn是否可以拓展
        # 如果nextn和thisn之间有通路且没有被访问过就可以拓展
        elif (g[thisn][nextn] != -1) and (nextn not in visited_list):
            # 拓展时将此节点压入栈并且初始化此节点的nextn为0
            visited_list.append(nextn)
            stack.append([nextn, 0])
    return -1



if __name__ == "__main__":

    # 取得一个回路
    route = get_route()
    # 计算回路的长度
    lengh = 0
    for i in range(len(route)):
        lengh += g[route[i]][route[(i+1)%len(g)]]
    max_limit = lengh

    # 使用第0个节点和上界初始化树
    tree = TspTree(0, max_limit)
    print("拓展节点为：")
    num = -1
    while(num == -1):
        # 当可以拓展时就拓展
        num = tree.tuozhan()
    print("最终路径长度为：{}".format(num))