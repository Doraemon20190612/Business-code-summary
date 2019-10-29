import numpy as np
import pandas as pd
from scipy.stats import pearsonr

data_tj = pd.read_excel(r'C:\Users\Administrator\Desktop\相关性分析数据处理.xlsx',sheetname = 0)
data_yd = pd.read_excel(r'C:\Users\Administrator\Desktop\相关性分析数据处理.xlsx',sheetname = 1)
data_ydts = pd.read_excel(r'C:\Users\Administrator\Desktop\相关性分析数据处理.xlsx',sheetname = 2)
data_dhjt = pd.read_excel(r'C:\Users\Administrator\Desktop\相关性分析数据处理.xlsx',sheetname = 3)
data_dhyq = pd.read_excel(r'C:\Users\Administrator\Desktop\相关性分析数据处理.xlsx',sheetname = 4)
data_cjhy = pd.read_excel(r'C:\Users\Administrator\Desktop\相关性分析数据处理.xlsx',sheetname = 5)


lst1 = []


for i in range(len(data_tj)):
    x = data_tj.loc[i,['3月','4月','5月','6月']].tolist()
    y = data_cjhy.loc[i,['3月','4月','5月','6月']].tolist()
    lst1.append(pearsonr(x, y))