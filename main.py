'''
@Description: 智能算法
@Autor: xiaosi
@Date: 2019-11-13 16:31:56
@LastEditors: xiaosi
@LastEditTime: 2019-11-13 18:02:19
'''
g = [
    [-1, 3, 1, 5, 8],
    [3, -1, 6, 7, 9],
    [1, 6, -1, 4, 2],
    [5, 7, 4, -1, 3],
    [8, 9, 2, 3, -1]
]
# g = [
#     [-1, 1, -1, -1, -1],
#     [1, -1, -1, 1, -1],
#     [-1, -1, -1, 1, 1],
#     [-1, 1, 1, -1, -1],
#     [-1, -1, 1, -1, -1]
# ]

# print(g)

def get_routes():
    '''
    通过深度优先遍历暴力求解TSP问题
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
                routes.append(route)
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
    return routes


if __name__ == "__main__":

    routes = get_routes()
    min_len = 99999999999
    min_route = []
    # 遍历所有回路求出最短路径
    for route in routes:
        lengh = 0
        for i in range(len(route)):
            lengh += g[route[i]][route[(i+1)%len(g)]]
        print(lengh)
        print(route)
        if lengh < min_len:
            min_len = lengh
            min_route = route
    print("最短长度为:" + str(min_len))
    print("最短路径为:"),
    min_route = [i+1 for i in min_route]
    print(min_route)