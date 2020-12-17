CREATE TABLE GOV_NEWS
(
 GOV_NEWS_ID             INT(10)           PRIMARY KEY AUTO_INCREMENT,
 GOV_NEWS_TITLE          VARCHAR(300)      NOT NULL,
 GOV_NEWS_DATE           DATETIME          NOT NULL,
 GOV_NEWS_SOURCE           VARCHAR(100)      NOT NULL,
 GOV_NEWS_URL            VARCHAR(500)      NOT NULL UNIQUE,
 GOV_NEWS_CONTENT        TEXT,
 GOV_NEWS_CONTENT_SEG    TEXT
);