from django.db import connection
from django.db import models

from News.sqlconfig import *


# Create your models here.
# 两个总表
# 每建立一行会建立三个对应的子表
class News(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    sourse = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    news_table = models.CharField(max_length=255)
    # 主hno;news_name,news_content,time
    news_associated_table = models.CharField(max_length=255)
    # 外hno,ono;newstopic,emotional_words,emotional_plus_or_minus,probability
    news_associated_organization_table = models.CharField(max_length=255)

    # 外hno,ono;newstopic,emotional_words,emotional_plus_or_minus,probability
    def save(self, *args, **kwargs):
        try:
            self.news_table = self.name + '_news'
            self.news_associated_table = self.name + '_news_associated'
            self.news_associated_organization_table = self.name + '_news_associated_organization'
            super(News, self).save(*args, **kwargs)
            with connection.cursor() as cursor:
                cursor.execute(newssql1.format(self.name))
                cursor.execute(newssql2.format(self.name))
                cursor.execute(newssql3.format(self.name))
        except Exception as e:
            raise e

    def delete(self, *args, **kwargs):
        try:
            with connection.cursor() as cursor:
                cursor.execute(deletetable.format(self.news_associated_organization_table))
                cursor.execute(deletetable.format(self.news_associated_table))
                cursor.execute(deletetable.format(self.news_table))
                super(News, self).delete(*args, **kwargs)
        except Exception as e:
            raise e


class Comments(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    sourse = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    conment_table = models.CharField(max_length=255)
    # 主comment_cno;content,time
    conment_associated_table = models.CharField(max_length=255)
    # 外comment_cno,cno;comment_topic,emotional_words,emotional_plus_or_minus,probability
    conment_associated_organization_table = models.CharField(max_length=255)

    # 外comment_cno,ono;comment_topic,emotional_words,emotional_plus_or_minus,probability
    def save(self, *args, **kwargs):
        try:
            self.conment_table = self.name + '_comment'
            self.conment_associated_table = self.name + '_comment_associated'
            self.conment_associated_organization_table = self.name + '_comment_associated_organization'
            super(Comments, self).save(*args, **kwargs)
            with connection.cursor() as cursor:
                cursor.execute(commentssql1.format(self.name))
                cursor.execute(commentssql2.format(self.name))
                cursor.execute(commentssql3.format(self.name))
        except Exception as e:
            raise e

    def delete(self, *args, **kwargs):
        try:
            with connection.cursor() as cursor:
                cursor.execute(deletetable.format(self.conment_associated_organization_table))
                cursor.execute(deletetable.format(self.conment_associated_table))
                cursor.execute(deletetable.format(self.conment_table))
                super(Comments, self).delete(*args, **kwargs)
        except Exception as e:
            raise e
