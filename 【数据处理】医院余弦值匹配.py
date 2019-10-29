# 导入相关库
import math
import jieba
import pandas as pd


# 自定义求余弦值函数
def compute_cosine(sentence_a, sentence_b):
    # 分词
    words_a = jieba.lcut(sentence_a,cut_all = True)  
    words_b = jieba.lcut(sentence_b,cut_all = True)  

    # 统计词频，输出字典
    words_a_dict = {}
    words_b_dict = {}
    for word in words_a:
        if word != '' and word in words_a_dict:
            num = words_a_dict[word]
            words_a_dict[word] = num + 1
        elif word != '':
            words_a_dict[word] = 1
        else:
            continue
    for word in words_b:
        if word != '' and word in words_b_dict:
            num = words_b_dict[word]
            words_b_dict[word] = num + 1
        elif word != '':
            words_b_dict[word] = 1
        else:
            continue

    # 排序并输出列表格式
    dic1 = sorted(words_a_dict.items(), key=lambda asd: asd[1], reverse=True)
    dic2 = sorted(words_b_dict.items(), key=lambda asd: asd[1], reverse=True)

    
    # 将词加入到列表中
    words_key = []
    for i in range(len(dic1)):
        words_key.append(dic1[i][0])
    for i in range(len(dic2)):
        if dic2[i][0] in words_key:
            pass
        else:  
            words_key.append(dic2[i][0])
            
    
    # 将列表中的词，按照之前的词频，输出词向量
    vector_a = []
    vector_b = []
    for word in words_key:
        if word in words_a_dict:
            vector_a.append(words_a_dict[word])
        else:
            vector_a.append(0)
        if word in words_b_dict:
            vector_b.append(words_b_dict[word])
        else:
            vector_b.append(0)

    # 计算余弦相似度
    sum = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(vector_a)):
        sum += vector_a[i] * vector_b[i]
        sq1 += pow(vector_a[i], 2)
        sq2 += pow(vector_b[i], 2)
    try:
        result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
    except ZeroDivisionError:
        result = 0.0
    return result



# 自定义匹配函数
def return_result(text1, text2):
    if compute_cosine(text1,text2) > 0.64:
        return 'Match'
    else:
        return 'Mismatch'
    
    
# 导入待匹配数据    
data_qz = pd.read_excel(r'C:\Users\Administrator\Desktop\奇正医院匹配实验数据.xlsx',sheetname = 4)
data_cy = pd.read_excel(r'C:\Users\Administrator\Desktop\奇正医院匹配实验数据.xlsx',sheetname = 5)


# 创建匹配列表
lsti = []
lstj = []
lstr = []
for i in range(len(data_qz)):
    data_qz_part = data_qz.text[i]
    for j in range(len(data_cy)):
        data_cy_part = data_cy.text[j]
        if __name__ == '__main__':
            lsti.append(i)
            lstj.append(j)
            lstr.append(return_result(data_qz_part,data_cy_part))

            
# 将结果导出为excel
dic = {'lsti':lsti,'lstj':lstj,'lstr':lstr}
new = pd.DataFrame(dic)
new.to_excel(r'C:\Users\Administrator\Desktop\医院匹配实验数据结果.xlsx')