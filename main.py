
import pandas as pd
import numpy as np
from pyecharts.charts import Bar
import matplotlib.pyplot as plt
# 用来储存生成的列名
columns = []
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 显示中文字体
for i in range(1, 11):
    columns.append("样本" + str(i))
# 生成随机数
x1 = np.random.normal(25, 8, 2000)
x1 = np.around(x1)
x1 = np.asarray(x1, int)
# 计算总数
total = sum(x1)
dic = {}
data_list = []
# 不符合规则的数据的处理
x1[x1 < 0] = 0
x2 = x1[0:10]
for i in range(200):
    data_list.append(x1[i*10:i*10 + 10])
df2w = pd.DataFrame(data=data_list, columns=columns)
df2w.to_csv('data.csv')
df2w.to_excel('data.xlsx')
# 统计不同数据的频数
for item in x1:
    if item not in dic.keys():
        dic[item] = 1
    else:
        dic[item] = dic[item] + 1
x = list(sorted(dic.keys()))
for i in x:
    plt.bar(i, dic[i])
# 通过plt作图对数据进行统计学分析
plt.title("Animal")
plt.xlabel("Animal Count")
plt.ylabel("Count")
plt.show()
bar = Bar()
bar.add_xaxis(list(sorted(dic.keys())))
bar.add_yaxis('数量', list(dic.values()))
bar.render("sc.html")
