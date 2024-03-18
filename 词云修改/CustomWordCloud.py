# -*- encoding:utf-8 -*-
import jieba
import wordcloud as wc
import numpy
from PIL import Image
def GenerateFile(pic_path,file_path,mask_path,stop_words,width=250,height=200):
    f=open(file_path,encoding='GBK')
    s=f.read()
    f.close()
    ls1=jieba.lcut(s)
    ls2=[]

    for v in ls1:
        if len(v)==1 or v in stop_words:
            continue
        else:
            ls2.append(v)
    words=' '.join(ls2)
    mask = numpy.array(Image.open(mask_path))
    w=wc.WordCloud(width=width,
                   height=height,
                   background_color='white',
                   mask=mask,
                   max_words=50,
                   max_font_size=96,
                   font_path='simsun.ttc')
    w.generate(words)
    w.recolor(color_func=wc.ImageColorGenerator(mask))

    w.to_file(pic_path)




