# 分词
import pandas as pd
import jieba


txt_0 = pd.DataFrame(pd.read_excel(r'C:\Users\Administrator\Desktop\Patient Flow Online\2018Topic.xlsx',sheetname = 8)['text'])

stop_words = list(pd.read_csv(r'C:\Users\Administrator\Desktop\Patient Flow Online\词库\Patient Flow Online停用词表.txt',
                             names = ['word'],sep = 'aaa',encoding = 'UTF-8-sig').word)
jieba.load_userdict = r'C:\Users\sb\Desktop\Patient Flow Online\词库\Patient Flow Online词库.txt'

def m_cut(intxt):
    return [w for w in jieba.lcut(intxt) if w not in stop_words and len(w) > 1]

txt_0_part = [' '.join(m_cut(w)) for w in txt_0.text]

txt_0_part_df = pd.DataFrame(txt_0_part,columns = ['part'])

# 构建向量
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

countvec = CountVectorizer(min_df = 10)
x = countvec.fit_transform(txt_0_part)

transformer = TfidfTransformer()
tfidf = transformer.fit_transform(x)

# 将向量转array格式

import numpy as np
import scipy.sparse
x1 = x.A
x1_df = pd.DataFrame(x1)
x1_df

# 进行KM聚类
from sklearn.cluster import KMeans

clf = KMeans(n_clusters = 2,n_jobs = -1)
s = clf.fit(tfidf)

clf.cluster_centers_ # 输出每类的类中心

# 聚类中心的形状
clf.cluster_centers_.shape

# 展示文档聚类结果
clf.labels_
txt_0['cluster'] = clf.labels_
print(txt_0.head())
txt_0.sort_values('cluster').cluster

txt_0.to_excel(r'C:\Users\Administrator\Desktop\晚期咨询聚类结果.xlsx')

# 将聚类结果文本合并
txt_0_groupby = txt_0.groupby('cluster')
txt_0_cluster = txt_0_groupby.agg(sum)
txt_0_cluster

# 将聚类文本空格分隔分词
txt_0_newpart = [' '.join(m_cut(w)) for w in txt_0_cluster.text]
txt_0_newpart_df = pd.DataFrame(txt_0_newpart,columns = ['part'])
txt_0_newpart_df

txt_0_newpart_se = pd.Series(txt_0_newpart_df['part'].values)
txt_0_newpart_se

# 列出每个聚类的关键词
import jieba.analyse
jieba.analyse.set_stop_words(r'C:\Users\Administrator\Desktop\Patient Flow Online\词库\Patient Flow Online停用词表.txt')

for item in txt_0_newpart_se:
    print(jieba.analyse.extract_tags(item,topK = 10))
