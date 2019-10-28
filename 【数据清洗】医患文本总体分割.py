# 医患文本总体分割

# 导入模块
import pandas as pd

# 导入文本
txtdata_df = pd.read_table(r'C:\Users\Administrator\Desktop\Patient Flow Online\2018.txt',
                           names = ['text'],engine = 'python',encoding = 'UTF-8-sig')

# 文本分割准备
txtdata = '|||'.join(str(i) for i in txtdata_df['text'])
txt_new = txtdata.split('|||')

# 文本分割
p = []
d = []
for i in txt_new:
    if i[0:2] == 'p:':
        p.append(i)
    else:
        d.append(i)

# 导出文本
try:
    p_df = pd.DataFrame(p,columns = ['text'])
    d_df = pd.DataFrame(d,columns = ['text'])
    p_df.to_csv(r'C:\Users\Administrator\Desktop\患者文本.csv')
    d_df.to_csv(r'C:\Users\Administrator\Desktop\医生文本.csv')
    print('导入成功')
except:
    print('导入失败')