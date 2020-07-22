import pandas as pd
file = "津市河道水文报表汇总.xlsx"
# 自行替换文件
data = pd.read_excel(file)
data["时间"] = pd.to_datetime(data["时间"])
# 将“时间”改成pandas能够识别的Datetime类型
test = data.groupby(data["时间"].dt.date).mean()
# 利用.dt.date将Datetime类型转换为Day类型数据，再用groupby汇总求取平均值
print(test)
