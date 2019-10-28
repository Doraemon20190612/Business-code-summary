# 导入模块
import numpy as np
import pandas as pd
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import matplotlib.pyplot as plt
import pyLDAvis
import pyLDAvis.sklearn


# 读取文本
txt_0 = pd.DataFrame(pd.read_excel(r'C:\Users\Administrator\Desktop\Patient Flow Online\2018Topic.xlsx',sheetname = 0)['text'])
stop_words = list(pd.read_csv(r'C:\Users\Administrator\Desktop\Patient Flow Online\词库\Patient Flow Online停用词表lda.txt',
                              names = ['word'],sep = 'aaa',encoding = 'UTF-8').word)
jieba.load_userdict('C:\\Users\\Administrator\\Desktop\\Patient Flow Online\\词库\\Patient Flow Online词库.txt')

# 去除文本分隔符
lst = list(txt_0['text'])
lst1 = []
for i in range(len(lst)):
    s = lst[i].replace('|||','')
    lst1.append(s)
txt = pd.DataFrame(lst1,columns = ['text'])

# 自定义分词函数
def m_cut(intxt):
    return [ w for w in jieba.cut(intxt)
            if w not in stop_words and len(w) > 1]

# term-doc矩阵的文本处理
txt_part = [' '.join(m_cut(w)) for w in txt.text]

countvec = CountVectorizer(min_df = 5)
x = countvec.fit_transform(txt_part)

'''# 基于x文档词条矩阵计算TFIDF值(可用于LDA模型训练的备选算法)
from sklearn.feature_extraction.text import TfidfTransformer

transformer = TfidfTransformer()
tfidf = transformer.fit_transform(x)
tfidf'''

columns = []
data = []
for i in range(1,10):
    columns.append(i)
    ldamodel = LatentDirichletAllocation(n_topics = i,max_iter = 1,random_state = 111)
    ldamodel.fit(x)
    data1 = ldamodel.perplexity(x)
    data.append(data1)

# n_topic参数选择
data_df = pd.DataFrame(columns,columns = ['x'])
data_df['y'] = data
plt.plot(data_df['x'],data_df['y'],c = 'b')
plt.xlabel('n_topics')
plt.ylabel('perplexity')
plt.show()

# LDA模型拟合
ldamodel = LatentDirichletAllocation(n_topics = 7,max_iter = 50,random_state = 111)
ldamodel.fit(x)

# 输出LDA模型(topics-word形状)
print('-------------------------输出LDA模型(topics-word形状)-------------------------')
print(ldamodel.components_.shape)

# 输出LDA模型(topics-word top15)
print('-------------------------输出LDA模型(topics-word top15)-------------------------')
print(ldamodel.components_[:5])

# 输出LDA模型(perplexity)
print('-------------------------输出LDA模型(perplexity)-------------------------')
print(ldamodel.perplexity(x))

# 自定义Topics打印函数
def print_top_words(model,feature_names,n_top_words):
    for topic_idx,topic in enumerate(model.components_):
        print('Topic #%d:' % topic_idx)
        print(' '.join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()

# 打印Topics
print('-------------------------打印Topics-------------------------')
n_top_words = 12
tf_feature_names = countvec.get_feature_names()
print_top_words(ldamodel,tf_feature_names,n_top_words)

# LDA主题文本分布
lda_topics = ldamodel.fit_transform(x)

# 输出LDA模型(doc-topics)
print('-------------------------输出LDA模型(doc-topics)-------------------------')
print(lda_topics)

# 输出LDA模型(导出doc-topics)
print('-------------------------输出LDA模型(导出doc-topics)-------------------------')
lda_topics_df = pd.DataFrame(lda_topics)
lda_topics_df.to_csv(r'C:\Users\Administrator\Desktop\lda_doc-topics.csv')

# 生成训练集LDAvis聚类图
pyLDAvis.enable_notebook()
data = pyLDAvis.sklearn.prepare(ldamodel,x,countvec)
pyLDAvis.show(data)