import math
data = []
Ans = []
TotalArea = 45470000
Square2 = 100
Total_num = 1145.2156
x = input().split()
for item in x:
    data.append(int(item))
for i in range(200):
    List = data[10 * i:10 * i + 10]
    ans = sum(List)/10
    Ans.append(ans)
Preview_num = sum(Ans) / 200*TotalArea/Square2/10000
print(Preview_num)
S = 0
for num in Ans:
    S += (num * TotalArea / Square2 / 10000 - Total_num) * (num * TotalArea / Square2 / 10000 - Total_num)
S /= 200
S = math.sqrt(S)
print(S)
print(Preview_num-1145.2156)