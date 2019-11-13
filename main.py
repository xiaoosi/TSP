g = [
    [-1, 3, 1, 5, 8],
    [3, -1, 6, 7, 9],
    [1, 6, -1, 4, 2],
    [5, 7, 4, -1, 3],
    [8, 9, 2, 3, -1]
]
# g = [
#     [-1, -1, 1, 5, -1],
#     [-1, -1, -1, -1, 9],
#     [1, -1, -1, 4, -1],
#     [5, -1, -1, -1, -1],
#     [-1, 9, 9, 3, -1]
# ]
print(g)

def get_max_limit():
    # 通过构造一个随机的回路求上限
    g_len = len(g)
    # 从第0个节点开始深度优先遍历求得一个环路
    visited_list = []
    visited_list.append(0)
    stack = [[0, 0]] #代表从第0个节点的第一个子节点遍历 
    while(stack):
        node_num, this_cnum = stack[-1]
        print(visited_list)
        # 判断是否遍历到头，没到就入栈，到了就出栈
        if (this_cnum <= g_len-1) and (g[node_num][this_cnum] != -1) and(this_cnum not in visited_list):
            stack.append([this_cnum, 0])
            visited_list.append(this_cnum)
        elif (this_cnum <= g_len-1) and ((g[node_num][this_cnum] == -1) or (this_cnum in visited_list)):
            stack[-1][-1] += 1
        elif (this_cnum > g_len-1):
            # 如果此时所有的点都在list中且最后一个点与第一点相同，则得到结果
            if(len(visited_list) == g_len and g[node_num][visited_list[0]] != -1):
                print(visited_list)
                break
            else:
                visited_list.pop()
                stack.pop()
        return reduce(add, )
    


if __name__ == "__main__":
    # 求出下限
    min_limit = 0
    # 遍历每行求出每行最小的两个值
    for row in g:
        sort_row = sorted(row)
        min_limit += (sort_row[0] + sort_row[1])/2
    print(min_limit)

    # 求出上限
    get_max_limit()
    