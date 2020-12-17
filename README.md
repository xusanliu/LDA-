# LDA-
Chinese news data scraping    LDA topic model.  

This project first crawls new data from Chinese government website and the store the data into the mysql database.These are showed in the file 'DataScraping.py'.  

In the file 'LDA.py' , I first fetch the stored data from the mysql database and using the LDA topic model to identify the topic of the news data. 

The file 'CreateTable.sql' is created to create the table in mysql to store the news data.  

The file'中文停用词表.txt' is the stopwords in Chinese and has been adapted based on the feature of the news data in this project.  


