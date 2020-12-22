# LDA-
Chinese news data scraping    LDA topic model.  

This project first crawls news data from Chinese government website and store the data into the mysql database.The process are showed in the file 'DataScraping.py'.  

In the file 'LDA.py' , I first fetch the stored data from mysql database and use the LDA topic model to identify the topics of the news data. 

The file 'CreateTable.sql' is written to create the table in mysql to store the news data.  

The file'中文停用词表.txt' is the stopwords in Chinese and has been adapted based on the feature of the news data in this project.  


