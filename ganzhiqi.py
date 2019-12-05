'''
@Description: 智能算法
@Autor: xiaosi
@Date: 2019-12-05 14:10:39
@LastEditors: xiaosi
@LastEditTime: 2019-12-05 15:11:37
'''
import numpy as np

# 输入0-9数字向量矩阵(最后一列代表的是偏置b)

X = np.array([
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]
]
)
# 输出矩阵Y
Y = np.array([1, -1, 1, -1, 1, -1, 1, -1, 1, -1])

# 输入一共15个维度，输出是一个维度。因此权重向量W+B的应该是16维
# random返回的是[0-1]之间的数 -0.5*2让其在[-1,1]之间
W = (np.random.random(16)-0.5)*2 

#设定学习率
lr = 0.3

def update():
    global  X, Y, W, lr
    # 遍历X中的每一行
    temp_out = []
    for (index, data) in enumerate(X):
        # 先计算结果
        out = np.sign(np.dot(data, W.T))
        temp_out.append(out)
        # 更新权重
        W = W + lr * np.dot((Y[index] - out), data)
    return temp_out
if __name__ == "__main__":
    temp_out = np.random.random(10)
    while not (temp_out == Y).all():
        temp_out = update()
        print(temp_out)
