# 词汇共现关系（eage）

import pandas as pd
import jieba

txt_0 = pd.read_table(r'C:\Users\Administrator\Desktop\Patient Flow Online\2018.txt',
                     names = ['text'],encoding = 'UTF-8-sig')
stop_words = list(pd.read_csv(r'C:\Users\Administrator\Desktop\Patient Flow Online\词库\Patient Flow Online停用词表.txt',
                             names = ['word'],sep = 'aaa',encoding = 'UTF-8-sig').word)
jieba.load_userdict(r'C:\Users\Administrator\Desktop\Patient Flow Online\词库\Patient Flow Online词库.txt')


def m_cut(intxt):
    return [w for w in jieba.lcut(intxt) if w not in stop_words]

txt_0_part = [m_cut(w) for w in txt_0.text]

yaopin = list(pd.read_excel(r'C:\Users\Administrator\Desktop\Gephi药品.xlsx').word)
jibing = list(pd.read_excel(r'C:\Users\Administrator\Desktop\Gephi疾病.xlsx').word)
zhengzhuang = list(pd.read_excel(r'C:\Users\Administrator\Desktop\Gephi症状.xlsx').word)
zong = yaopin + jibing + zhengzhuang

part = []
for sentence in txt_0_part:
    part.append([])


s = -1    
for sentence in txt_0_part:
    s = s + 1
    for word in sentence:
        if word not in zong:
            continue
        else:
            part[s].append(word)

word = []

for sent in part:
    for w1 in sent:
        for w2 in sent:
            if w1 == w2:
                continue
            word.append(w1+','+w2)
            
relati = pd.DataFrame(word,columns = ['word'])

relati['num'] = 1

relati1 = relati.groupby('word').sum()

relati1.to_csv(r'C:\Users\Administrator\Desktop\eage共现关系（边）.csv')



# 词汇共现关系（node）

import pandas as pd
import jieba

txt_0 = pd.read_table(r'C:\Users\Administrator\Desktop\Patient Flow Online\2018.txt',
                     names = ['text'],encoding = 'UTF-8-sig')
stop_words = list(pd.read_csv(r'C:\Users\Administrator\Desktop\Patient Flow Online\词库\Patient Flow Online停用词表.txt',
                             names = ['word'],sep = 'aaa',encoding = 'UTF-8-sig').word)
jieba.load_userdict(r'C:\Users\Administrator\Desktop\Patient Flow Online\词库\Patient Flow Online词库.txt')


def m_cut(intxt):
    return [w for w in jieba.lcut(intxt) if w not in stop_words]

txt_0_part = [m_cut(w) for w in txt_0.text]

yaopin = list(pd.read_excel(r'C:\Users\Administrator\Desktop\Gephi药品.xlsx').word)
jibing = list(pd.read_excel(r'C:\Users\Administrator\Desktop\Gephi疾病.xlsx').word)
zhengzhuang = list(pd.read_excel(r'C:\Users\Administrator\Desktop\Gephi症状.xlsx').word)
zong = yaopin + jibing + zhengzhuang

part = []
for sentence in txt_0_part:
    part.append([])


s = -1    
for sentence in txt_0_part:
    s = s + 1
    for word in sentence:
        if word not in zong:
            continue
        else:
            part[s].append(word)

word = []

for sent in part:
    for w1 in sent:
        for w2 in sent:
            if w1 != w2:
                continue
            word.append(w1+','+w2)
            
relati = pd.DataFrame(word,columns = ['word'])

relati['num'] = 1

relati1 = relati.groupby('word').sum()

relati1.to_csv(r'C:\Users\Administrator\Desktop\node共现关系（节点）.csv')