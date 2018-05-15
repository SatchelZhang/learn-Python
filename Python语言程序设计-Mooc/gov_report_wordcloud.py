import jieba, wordcloud
from scipy.misc import imread
mask = imread("chinamap.jpg")
f = open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", \
                        width = 1000, height=700, background_color="white", \
                        max_words=150, mask = mask)
w.generate(txt)
w.to_file("grwordcloud3.png")