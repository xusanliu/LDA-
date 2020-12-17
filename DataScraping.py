#!/usr/bin/env python
# coding: utf-8

# In[1]:


#导入所需的库
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import pymysql


# In[2]:


#可以走循环啦
URLs=[]
titles=[]
SavedNum=0
URLNum=1
CurrentURL='http://sousuo.gov.cn/column/30611/0.htm'


#先爬20页吧
while(URLNum<20):
    response=urllib.request.urlopen(CurrentURL)
    HTMLText=response.read()
    #选择基于BeautifulSoup解析整个页面
    BSobj = BeautifulSoup(HTMLText, "html.parser")
    ArticleLists=BSobj.find("ul",{"class":"listTxt"})
    
    #提取出所有的URL和标题
    for a in ArticleLists.findAll("a", href=True):
        #if re.findall("",a['href']):
        URLs.append(a['href'])
        titles.append(a.get_text())
    dict={
        'title':titles,
        'url':URLs
         }
    Next=BSobj.find("a",{"class":"next"})
    NextPageURL=Next['href']

    if NextPageURL is None:
        print("已经爬到了最后一页！")
        break
    else:
        CurrentURL=NextPageURL
        URLNum+=1

data=pd.DataFrame(dict)

for title,link in data.iterrows():
    try:
        ContentResponse=urllib.request.urlopen(link[1])
        ContentHTMLText=ContentResponse.read()
        ContentBSobj=BeautifulSoup(ContentHTMLText,"html.parser")
        ArticleTime=ContentBSobj.find("div",{"class":"pages-date"})
        #print(ArticleTime.get_text()[0:16])
        Content=ContentBSobj.find("div",{"class":"pages_content"})
        #print(Content.get_text())
        Source=ContentBSobj.find("span",{"class":"font"})
        #print(Source.get_text())
        newssource=Source.get_text()[4:]
        newstitle=link[0]
        newslink=link[1]
        newstime=ArticleTime.get_text()[0:16]
        newscontent=Content.get_text()
        #1.Connection Open
        conn = pymysql.connect(user='root', password='12345678', database='login', charset='utf8')
        # 2.Cursor Creating:
        cursor = conn.cursor()
        # 3.SQL Execution
        # 执行SQL语句，循环插入记录:
        sqlstr = "REPLACE INTO GOV_NEWS(GOV_NEWS_TITLE,GOV_NEWS_DATE,GOV_NEWS_SOURCE,GOV_NEWS_URL,GOV_NEWS_CONTENT) VALUES('" + newstitle + "','" + newstime + "','" + newssource + "','" + newslink + "','" + newscontent + "')"
        # 4.Cursor Moving
        # 执行, 游标移至当前位置
        cursor.execute(sqlstr)
        # 提交事务:
        conn.commit()
        # 5.Connection Close
        # 关闭Cursor:Connection:
        cursor.close()
        conn.close() 
        SavedNum =1
        print(newstitle + " " + newstime + "   " + newslink)
    except:
        print("Error:"+ newstitle + " " + newslink)
    finally:
        print(str(SavedNum) + " News Saved")
        SavedNum = 0#SavedNum复位为0


# In[ ]:




