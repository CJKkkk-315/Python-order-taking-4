import jieba.posseg
import jieba
from collections import Counter
jieba.setLogLevel(jieba.logging.INFO)
table = [
'''n 名词
nr 人名
nr1 汉语姓氏
nr2 汉语名字
nrj 日语人名
nrf 音译人名
ns 地名
nsf 音译地名
nt 机构团体名
nz 其它专名
nl 名词性惯用语
ng 名词性语素
t 时间词
tg 时间词性语素
s 处所词
f 方位词
v 动词
vd 副动词
vn 名动词
vshi 动词“是”
vyou 动词“有”
vf 趋向动词
vx 形式动词
vi 不及物动词（内动词）
vl 动词性惯用语
vg 动词性语素
a 形容词
ad 副形词
an 名形词
ag 形容词性语素
al 形容词性惯用语
b 区别词
bl 区别词性惯用语
z 状态词
r 代词
rr 人称代词
rz 指示代词
rzt 时间指示代词
rzs 处所指示代词
rzv 谓词性指示代词
ry 疑问代词
ryt 时间疑问代词
rys 处所疑问代词
ryv 谓词性疑问代词
rg 代词性语素
m 数词
mq 数量词
q 量词
qv 动量词
qt 时量词
d 副词
p 介词
pba 介词“把”
pbei 介词“被”
c 连词
cc 并列连词
u 助词
uzhe 着
x 其他'''
]
table = [i.split(' ') for i in table[0].split('\n') if i]
dic = {i[0]:i[1] for i in table}
content = ''.join([j for j in [i.replace('\n','') for i in open('歌词.txt',encoding='utf8').readlines()] if j])
cipin = Counter(list(jieba.cut(content)))
for i,j in cipin.items():
    print(i,j)
while True:
    try:
        word,tag = input('请输入自定义词和词性，以空格分割，输入0结束自定义').split()
        jieba.add_word(word,tag=tag)
    except:
        break
content = content.replace(' ','')
res = jieba.posseg.cut(content)
ipt = input('请输入词性:')
for i in res:
    if str(i).split('/')[1] in dic and ipt == dic[str(i).split('/')[1]]:
        print(i)
