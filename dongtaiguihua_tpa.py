'''
@Description: 智能算法
@Autor: xiaosi
@Date: 2019-11-24 14:47:48
@LastEditors: xiaosi
@LastEditTime: 2019-11-24 16:16:10
'''
# dong
import copy

g = [
    [99999, 3, 1, 5, 8],
    [3, 99999, 6, 7, 9],
    [1, 6, 99999, 4, 2],
    [5, 7, 4, 99999, 3],
    [8, 9, 2, 3, 99999]
]

map_j = []
map_j.append(set())
# 广度方向扩展map_j
per = 0 #遍历指针
while(per < len(map_j)):
    thisset = map_j[per]
    per += 1
    for i in range(len(g)):
        if i not in thisset:
            newset = copy.deepcopy(thisset)
            newset.add(i)
            if newset not in map_j:
                map_j.append(newset)
# print(map_j)

# 初始化距离矩阵全部设置成-1
d = []
for i in range(len(g)):
    tem = [-1 for j in range(len(map_j))]
    d.append(tem)

# 初始化距离矩阵第一列
for i in range(len(g)):
    d[i][0] = g[i][0]


# 求解d(i,V)
# d(i，V)表示从i点经过点集Ｖ各点一次之后回到出发点的最短距离
# V是一个set集合
def get_d(i, V):
    if V:
        print("求解d({}, {})".format(i ,V))
    j = map_j.index(V)
    # 如果V是空直接返回i点与第0个点之间的距离
    if j == 0:
        return d[i][j]
    else:
        # 先查表
        if d[i][j] != -1:
            return d[i][j]
        # 再计算
        d_list = []
        for point in V:
            new_set = copy.deepcopy(V)
            new_set.remove(point)
            d_list.append(g[i][point] + get_d(point, new_set))
        # d_list = [g[i][point] + get_d(point, copy.deepcopy(V).remove(point)) for point in V]
        # print(d_list)
        min_num = min(d_list)
        d[i][j] = min_num
        return d[i][j]

result = get_d(0, set([1,2,3,4]))
print('距离矩阵为：')
for i in range(len(d)):
    print(d[i])
print('最终结果为：')
print(result)

