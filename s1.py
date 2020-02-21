import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt


# 601233 桐昆股份
df = ts.get_k_data("601233")
df.index = df.pop("date")
# print(df)
close = df["close"]
#   print(close,type(close))
# 十日均线的数据 每十天移动一个窗口 宽度为10 的均线

ma10 = close.rolling(10).mean()
print(ma10)  # 得到一个序列

# 计算均线工具（以移动平均线为列）
ma10.plot()
plt.show()  # 显示右图

