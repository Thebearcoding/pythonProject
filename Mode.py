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

# 计算众数
for i in range(200):
    List = data[10 * i:10 * i + 10]
    Dic = {}
    Max = 0
    count = 0
    Sum = 0
    for j in range(10):
        if List[j] not in Dic.keys():
            Dic[List[j]] = 1
        else:
            Dic[List[j]] = Dic[List[j]] + 1
    Max = max(Dic.values())
    for key in Dic.keys():
        if Dic[key] == Max:
            count += 1
            Sum += key
    ans = float(Sum) / count

    Ans.append(ans)
Preview_num = sum(Ans) / 200 * TotalArea / Square2 / 10000
print(Preview_num)
S = 0
for num in Ans:
    S += (num * TotalArea / Square2 / 10000 - Total_num) * (num * TotalArea / Square2 / 10000 - Total_num)
S /= 200
S = math.sqrt(S)
print(S)
print(Preview_num-1145.2156)
