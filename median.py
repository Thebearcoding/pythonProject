import math
data = []
Ans = []
TotalArea = 45470000
Square2 = 100
Total_num = 1145.2156
# 输入数据
x = input().split()
for item in x:
    data.append(int(item))
# 计算中位数
for i in range(200):
    List = data[10 * i:10 * i + 10]
    ans = (sorted(List)[4]+sorted(List)[5])/2
    Ans.append(ans)
    print(ans)
Preview_num = sum(Ans) / 200*TotalArea/Square2/10000
print(Preview_num)
S = 0
for num in Ans:
    S += (num * TotalArea / Square2 / 10000 - Total_num) * (num * TotalArea / Square2 / 10000 - Total_num)
S /= 200
S = math.sqrt(S)
print(S)
print(Preview_num-1145.2156)