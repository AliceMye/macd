# MACD ewm 指数的窗口 带权重的窗口（即分窗口）
import pandas as pd


def cal_macd(close, long, short, mid):
    if __name__ == '__main__':
        diff = close.ewm(span=short).mean() - close.ewm(span=mid).mean()
        dea = diff.ewm(span=mid).mean()
        macd = (diff-dea)*2
        return (diff,dea,macd)

