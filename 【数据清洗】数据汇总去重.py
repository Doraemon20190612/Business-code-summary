# 数据表汇总并去重

# 导入模块
import pandas as pd

# 导入文本
data_201801 = pd.read_excel(r'C:\Users\Administrator\Desktop\Patient Flow Online\数据源\keywords\2018-01.xlsx')
data_201802 = pd.read_excel(r'C:\Users\Administrator\Desktop\Patient Flow Online\数据源\keywords\2018-02.xlsx')
data_201803 = pd.read_excel(r'C:\Users\Administrator\Desktop\Patient Flow Online\数据源\keywords\2018-03.xlsx')
data_201804 = pd.read_excel(r'C:\Users\Administrator\Desktop\Patient Flow Online\数据源\keywords\2018-04.xlsx')
data_201805 = pd.read_excel(r'C:\Users\Administrator\Desktop\Patient Flow Online\数据源\keywords\2018-05.xlsx')
data_201806 = pd.read_excel(r'C:\Users\Administrator\Desktop\Patient Flow Online\数据源\keywords\2018-06.xlsx')
data_201807 = pd.read_excel(r'C:\Users\Administrator\Desktop\Patient Flow Online\数据源\keywords\2018-07.xlsx')
data_201808 = pd.read_excel(r'C:\Users\Administrator\Desktop\Patient Flow Online\数据源\keywords\2018-08.xlsx')
data_201809 = pd.read_excel(r'C:\Users\Administrator\Desktop\Patient Flow Online\数据源\keywords\2018-09.xlsx')
data_201810 = pd.read_excel(r'C:\Users\Administrator\Desktop\Patient Flow Online\数据源\keywords\2018-10.xlsx')
data_201811 = pd.read_excel(r'C:\Users\Administrator\Desktop\Patient Flow Online\数据源\keywords\2018-11.xlsx')
data_201812 = pd.read_excel(r'C:\Users\Administrator\Desktop\Patient Flow Online\数据源\keywords\2018-12.xlsx')

# 文本合并
data_2018_repeat = pd.concat([data_201801,data_201802,data_201803,data_201804,data_201805,data_201806,
                              data_201807,data_201808,data_201809,data_201810,data_201811,data_201812],
                             axis = 0,ignore_index = True)

# 文本去重
data_2018 = data_2018_repeat.drop_duplicates()

# 导出文本
data_2018.to_csv(r'C:\Users\Administrator\Desktop\2018.csv')

