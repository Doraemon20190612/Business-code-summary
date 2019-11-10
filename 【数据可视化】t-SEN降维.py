# 进行t-SNE降维
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE


x2 = np.array(x1_df)
tsne = TSNE(n_components = 2)
tsne.fit_transform(x1)
print(tsne.embedding_)

# 将聚类结果与降维结果合并
tsne_df = pd.DataFrame(tsne.embedding_,columns = ['x','y'])
tsne_df['cluster'] = clf.labels_
tsne_df



tsne_df_0 = tsne_df[(tsne_df.cluster==0)]
tsne_df_1 = tsne_df[(tsne_df.cluster==1)]


writer=pd.ExcelWriter(r'C:\Users\Administrator\Desktop\t-SNE KM聚类降维1.xlsx')
tsne_df_0.to_excel(writer,sheet_name = 'sheet0')
tsne_df_1.to_excel(writer,sheet_name = 'sheet1')

cluster0 = pd.read_excel(r'C:\Users\Administrator\Desktop\t-SNE KM聚类降维.xlsx',sheetname = 0)
cluster1 = pd.read_excel(r'C:\Users\Administrator\Desktop\t-SNE KM聚类降维.xlsx',sheetname = 1)
cluster2 = pd.read_excel(r'C:\Users\Administrator\Desktop\t-SNE KM聚类降维.xlsx',sheetname = 2)

from pyecharts import Scatter

data_0 = cluster0.values
data_1 = cluster1.values
data_2 = cluster2.values

scatter = Scatter('晚期咨询聚类结果','t-SNE降维结果')

data_0x = data_0[:,0]
data_0y = data_0[:,1]

data_1x = data_1[:,0]
data_1y = data_1[:,1]

data_2x = data_2[:,0]
data_2y = data_2[:,1]

scatter.add('晚期中药咨询',data_0x,data_0y,xaxis_name = 'x',yaxis_name = 'y',yaxis_name_gap = 40)
scatter.add('晚期手术咨询',data_1x,data_1y,xaxis_name = 'x',yaxis_name = 'y',yaxis_name_gap = 40)
scatter.add('晚期靶向咨询',data_2x,data_2y,xaxis_name = 'x',yaxis_name = 'y',yaxis_name_gap = 40)

scatter
