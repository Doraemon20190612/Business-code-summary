# 分词及词频统计

# 导入模块
import pandas as pd
import jieba


# 导入文本
txtdata_df = pd.read_table(r'C:\Users\Administrator\Desktop\Patient Flow Online\2018.txt',
                           names = ['text'],engine = 'python',encoding = 'UTF-8')
stop_words = pd.read_csv(r'C:\Users\Administrator\Desktop\Patient Flow Online\词库\Patient Flow Online停用词表.txt',
                         names = ['word'],engine = 'python',sep = 'aaa',encoding = 'UTF-8')
lexicon = r'C:\Users\Administrator\Desktop\Patient Flow Online\词库\Patient Flow Online词库.txt'
jieba.load_userdict(lexicon)


txtdata = ''.join(str(i) for i in txtdata_df['text'])
    
txtdata_part = list(w for w in jieba.cut(txtdata) if w not in list(stop_words.word))
    
txtdata_part_df = pd.DataFrame(txtdata_part,columns = ['word'])
    
freqlist = txtdata_part_df.groupby(['word']).size().sort_values(ascending = False)
freqlist_df = pd.DataFrame(freqlist,columns = ['number'])

freqlist.to_csv(r'C:\Users\Administrator\Desktop\2018词频.csv')