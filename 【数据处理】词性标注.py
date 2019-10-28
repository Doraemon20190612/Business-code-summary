# 词性标注
import pandas as pd
import jieba
import jieba.posseg as psg

# 导入文本
txtdata_df = pd.read_table(r'C:\Users\Administrator\Desktop\Patient Flow Online\2018.txt',
                         names = ['text'],engine = 'python',encoding = 'UTF-8')
stop_words = list(pd.read_csv(r'C:\Users\Administrator\Desktop\Patient Flow Online\词库\Patient Flow Online停用词表.txt',
                              names = ['word'],engine = 'python',sep = 'aaa',encoding = 'UTF-8').word)
lexicon = r'C:\Users\Administrator\Desktop\Patient Flow Online\词库\Patient Flow Online词库.txt'
jieba.load_userdict(lexicon)

txtdata = ''.join(str(i) for i in txtdata_df['text'])

def m_cut(intxt):
    return [w for w in jieba.cut(intxt) if w not in stop_words]
    
txtdata_part = ''.join(m_cut(txtdata))

txtdata_part_pos = psg.cut(txtdata_part)
    
txt_part_pos1 = []
txt_part_pos2 = []
for i in txtdata_part_pos:
    txt_part_pos1.append(i.word)
    txt_part_pos2.append(i.flag)
txt_part_pos1_df = pd.DataFrame(txt_part_pos1,columns = ['word'])
txt_part_pos2_df = pd.DataFrame(txt_part_pos2,columns = ['flag'])
txt_part_pos_df = txt_part_pos1_df.join(txt_part_pos2_df)

txt_part_pos_df

txt_part_pos_df.to_csv(r'C:\Users\Administrator\Desktop\2018词性.csv')