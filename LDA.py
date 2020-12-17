#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymysql
import jieba
import jieba.posseg as jp
from gensim import corpora, models
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


#先从数据库中取数据
#连接数据库
conn = pymysql.connect(user='root', password='12345678', database='login', charset='utf8')
#创建cursor
cursor=conn.cursor()
#sql查询语句
sql="select GOV_NEWS_CONTENT from GOV_NEWS"
#执行sql语句
cursor.execute(sql)
result_list=cursor.fetchall()
for i in range(len(result_list)):
    print(result_list[i])
conn.commit()
cursor.close()
conn.close()


# In[4]:


#获取新闻长度
len(result_list)


# In[5]:


#导入停用词表
stopwords=[]
with open('中文停用词表.txt','r') as f:
    for line in f.readlines():
        line=line.strip('\n')
        stopwords.append(line)
    print(stopwords)


# In[6]:


#创建一个存储空间来储存分词的结果
word_list=[]
for text in result_list:
    text=str(text)
    words=[word.word for word in jp.cut(text) if word.word not in stopwords]
    word_list.append(words)
print(word_list)


# In[7]:


print(word_list)


# In[8]:


#构造词典
dict=corpora.Dictionary(word_list)
#构造词袋
corpus=[dict.doc2bow(words) for words in word_list]


# In[9]:


#构建lda模型
lda=models.ldamodel.LdaModel(corpus=corpus,num_topics=3,id2word=dict)
#打印主题，每个主题的主题词为8
for topic in lda.print_topics(num_words=20):
    print(topic)


# In[11]:


#测试一下训练的模型
text='新华社海口12月17日电（记者 罗江、田睿）记者从海南省住建厅获悉，近5年来，海南完成扩建和新建9座生活垃圾焚烧发电厂，全省累计建成垃圾处理设施29座，城乡生活垃圾无害化处理率达95%以上，城市生活垃圾无害化处理率达100%。“十三五”期间，海南积极推行“户分类、村集中、镇转运、县处理”的农村生活垃圾收运处理模式，城乡一体化垃圾清运处理和保洁体系基本实现全覆盖。在此基础上，海南正逐步试点推行生活垃圾分类，并明确到2022年，各市县全面推行生活垃圾分类。海南省住建厅有关负责人介绍，海南正在编制《海南省生活垃圾处理专项规划》，将制定全省生活垃圾处理能力建设2020年至2025的近期目标，以及2026年至2035年的远期目标。相较于“十三五”期间的《海南省生活垃圾无害化处理设施规划》，该规划更侧重于终端设施统筹布局，以及全过程全链条垃圾分类处理。'


# In[12]:


#分词和去除停用词
bow = dict.doc2bow([word.word for word in jp.cut(text) if word.word not in stopwords])
result=lda.inference([bow])[0]
for e, value in enumerate(result[0]):
    print('\t主题%d推断值%.2f' % (e, value))


# In[ ]:




