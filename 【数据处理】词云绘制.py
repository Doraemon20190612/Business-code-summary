# 词云绘制（色系模仿）

# 导入模块包
import numpy as np
import pandas as pd
import wordcloud
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import get_single_color_func


# 读取词频文件
wc = pd.read_excel('C:\\Users\\sb\\Desktop\\新词云.xlsx',sheetname = 2)

# 将DataFrame转换为字典
wc1 = wc.set_index('word').T.to_dict('int')['num']

# 绘制并修改轮廓（尺寸美化：修改轮廓后，尺寸不可变）
wc2 = wordcloud.WordCloud(font_path = 'C:\\Windows\\Fonts\\msyh.ttc',
                          relative_scaling = 0.2,
                          prefer_horizontal = 0.9,
                          width = 5600,
                          height = 2800,
                          mode = 'RGB',
                          background_color = 'white',mask = imread('C:\\Users\\sb\\Desktop\\新词云3.jpg')).fit_words(wc1)

# 美化色系（色系模仿）
imgarray = np.array(imread('C:\\Users\\sb\\Desktop\\新词云3.jpg'))
imgcolors = wordcloud.ImageColorGenerator(imgarray)
wc2.recolor(color_func = imgcolors)

#指定单词组颜色(官网自定义函数)
class GroupedColorFunc(object):
    def __init__(self,color_to_words,default_color):
        self.color_func_to_words = [
            (get_single_color_func(color),set(words))
            for (color,words) in color_to_words.items()]
        self.defalt_color_func = get_single_color_func(default_color)
    def get_color_func(self,word):
        try:
            color_func = next(color_func for (color_func,words) in self.color_func_to_words
                              if word in words)
        except StopIteration:
            color_func = self.defalt_color_func
        return color_func
    def __call__(self,word,**kwargs):
        return self.get_color_func(word)(word,**kwargs)

'''# 指定单词组颜色
color_to_words = {'green':['奥沙利铂','卡培他滨','希罗达','替吉奥','氟尿嘧啶','伊立替康','PD1','瑞戈非尼','雷替曲塞','PD-1','帕尼',
                          '西妥昔','呋喹替尼','丝裂霉素']}
default_color = 'gray'
grouped_color_func = GroupedColorFunc(color_to_words,default_color)
wc2.recolor(color_func = grouped_color_func)'''

# 输出词云
plt.imshow(wc2)
plt.axis('off')
plt.show()

# 导出图片
wc2.to_file('C:\\Users\\sb\\Desktop\\sheet.png')






# 词云绘制（自定义单词组颜色）

# 导入模块包
import numpy as np
import pandas as pd
import wordcloud
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import get_single_color_func


# 读取词频文件
wc = pd.read_excel(r'C:\Users\Administrator\Desktop\Python GUI\词云测试文件\症状词云.xlsx')

# 将DataFrame转换为字典
wc1 = wc.set_index('word').T.to_dict('int')['num']

# 绘制并修改轮廓（尺寸美化：修改轮廓后，尺寸不可变）
wc2 = wordcloud.WordCloud(font_path = 'C:\\Windows\\Fonts\\msyh.ttc',
                          relative_scaling = 0.2,
                          prefer_horizontal = 0.9,
                          width = 5600,
                          height = 2800,
                          mode = 'RGB',
                          background_color = 'white',mask = imread(r'C:\Users\Administrator\Desktop\Python GUI\词云测试文件\症状词云模板.png')).fit_words(wc1)

# 美化色系（色系模仿）
#imgarray = np.array(imread(r'C:\Users\Administrator\Desktop\Python GUI\词云测试文件\症状词云模板.png'))
#imgcolors = wordcloud.ImageColorGenerator(imgarray)
#wc2.recolor(color_func = imgcolors)

#指定单词组颜色(官网自定义函数)
class GroupedColorFunc(object):
    def __init__(self,color_to_words,default_color):
        self.color_func_to_words = [
            (get_single_color_func(color),set(words))
            for (color,words) in color_to_words.items()]
        self.defalt_color_func = get_single_color_func(default_color)
    def get_color_func(self,word):
        try:
            color_func = next(color_func for (color_func,words) in self.color_func_to_words
                              if word in words)
        except StopIteration:
            color_func = self.defalt_color_func
        return color_func
    def __call__(self,word,**kwargs):
        return self.get_color_func(word)(word,**kwargs)

# 指定单词组颜色
dic = {'#CCFFFF':['便血','腹痛','便秘','腹胀','腹泻','消化','放屁','贫血','恶心','消瘦']}
st = 'gray'

color_to_words = dic
default_color = st
grouped_color_func = GroupedColorFunc(color_to_words,default_color)
wc2.recolor(color_func = grouped_color_func)

# 输出词云
plt.imshow(wc2)
plt.axis('off')
plt.show()

# 导出图片
wc2.to_file('C:\\Users\\sb\\Desktop\\sheet.png')