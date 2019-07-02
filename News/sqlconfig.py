deletetable = '''DROP TABLE {0}'''
newssql1 = '''CREATE TABLE IF NOT EXISTS {0}_news \
            (newid INT NOT NULL AUTO_INCREMENT, \
             news_name VARCHAR(100) NOT NULL, \
             news_content TEXT NOT NULL, \
             time DATE, \
             PRIMARY KEY ( newid ) \
            )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'''
newssql2 = '''CREATE TABLE IF NOT EXISTS {0}_news_associated_organization \
            (newid INT, \
             ono VARCHAR(4), \
             newtopic TEXT, \
             emotional_words TEXT, \
             emotional_plus_or_minus INT, \
             probability FLOAT, \
             PRIMARY KEY ( newid,ono ), \
             FOREIGN KEY (newid) REFERENCES {0}_news(newid), \
             FOREIGN KEY (ono) REFERENCES emotion_organization(ono) \
            )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'''
newssql3 = '''CREATE TABLE IF NOT EXISTS {0}_news_associated \
            (newid INT, \
             cno VARCHAR(4), \
             newtopic TEXT, \
             emotional_words TEXT, \
             emotional_plus_or_minus INT, \
             probability FLOAT, \
             PRIMARY KEY ( newid,cno ), \
             FOREIGN KEY (newid) REFERENCES {0}_news(newid), \
             FOREIGN KEY (cno) REFERENCES emotion_basic_information(cno) \
            )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'''

commentssql1 = '''CREATE TABLE IF NOT EXISTS {0}_comment \
            (comment_id INT NOT NULL AUTO_INCREMENT, \
             comment_content TEXT NOT NULL, \
             time DATE, \
             PRIMARY KEY ( comment_id ) \
            )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'''
commentssql2 = '''CREATE TABLE IF NOT EXISTS {0}_comment_associated_organization \
            (comment_id INT, \
             ono VARCHAR(4), \
             comment_topic VARCHAR(255), \
             emotional_words TEXT, \
             emotional_plus_or_minus INT, \
             probability FLOAT, \
             PRIMARY KEY ( comment_id,ono ), \
             FOREIGN KEY (comment_id) REFERENCES {0}_comment(comment_id), \
             FOREIGN KEY (ono) REFERENCES emotion_organization(ono) \
            )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'''
commentssql3 = '''CREATE TABLE IF NOT EXISTS {0}_comment_associated \
            (comment_id INT, \
             cno VARCHAR(4), \
             comment_topic VARCHAR(255), \
             emotional_words TEXT, \
             emotional_plus_or_minus INT, \
             probability FLOAT, \
             PRIMARY KEY ( comment_id,cno ), \
             FOREIGN KEY (comment_id) REFERENCES {0}_comment(comment_id), \
             FOREIGN KEY (cno) REFERENCES emotion_basic_information(cno) \
            )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'''
