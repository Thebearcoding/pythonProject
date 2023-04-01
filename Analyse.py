import math
import numpy as np
import matplotlib.pyplot as plt

List = []
data = []
Dic = {}
x = input().split()
for item in x:
    data.append(int(item))
# 拟合正态分布模型

# 绘制数据的直方图和拟合的正态分布曲线


for each in x:
    if int(each) not in Dic.keys():
        Dic[int(each)] = 1
    else:
        Dic[int(each)] = 1 + Dic[int(each)]
x = list(sorted(Dic.keys()))
for i in x:
    plt.bar(i, float(Dic[i]) / 2000)
plt.xlabel("Animal Count")
plt.ylabel("Probability distribution")
u = 24.759  # 均值μ
sig = 8.350204728  # 标准差δ
x = np.linspace(u - 3 * sig, u + 3 * sig, 50)  # 定义域
y = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)  # 定义曲线函数
plt.plot(x, y, "g", linewidth=2)  # 加载曲线
plt.grid(True)  # 网格线
plt.show()
print(Dic)
