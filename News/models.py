from django.db import models


class Event(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    agname = models.CharField(max_length=255)


class Source(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)


# 新闻
class News(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    time = models.DateField()
    source = models.CharField(max_length=255)
    emotional_words = models.CharField(max_length=255)
    emotional_express = models.CharField(max_length=255)
    emotional_express_class = models.CharField(max_length=255)
    emotional_event = models.CharField(max_length=255)
    emotional_plus_or_minus = models.IntegerField()
    probability = models.FloatField()
    language = models.CharField(max_length=255)


class South_sea_news(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    time = models.DateField()
    source = models.CharField(max_length=255)
    emotional_words = models.CharField(max_length=255)
    emotional_express = models.CharField(max_length=255)
    emotional_express_class = models.CharField(max_length=255)
    emotional_event = models.CharField(max_length=255)
    emotional_plus_or_minus = models.IntegerField()
    probability = models.FloatField()
    language = models.CharField(max_length=255)


class Huanqiu_news(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    time = models.DateField()
    source = models.CharField(max_length=255)
    emotional_words = models.CharField(max_length=255)
    emotional_express = models.CharField(max_length=255)
    emotional_express_class = models.CharField(max_length=255)
    emotional_event = models.CharField(max_length=255)
    emotional_plus_or_minus = models.IntegerField()
    probability = models.FloatField()
    language = models.CharField(max_length=255)


# 评论
class Comments(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    content = models.TextField()
    time = models.DateField()
    source = models.CharField(max_length=255)
    emotional_words = models.CharField(max_length=255)
    emotional_express = models.CharField(max_length=255)
    emotional_express_class = models.CharField(max_length=255)
    emotional_event = models.CharField(max_length=255)
    emotional_plus_or_minus = models.IntegerField()
    probability = models.FloatField()
    language = models.CharField(max_length=255)


class South_sea_comments(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    content = models.TextField()
    time = models.DateField()
    source = models.CharField(max_length=255)
    emotional_words = models.CharField(max_length=255)
    emotional_express = models.CharField(max_length=255)
    emotional_express_class = models.CharField(max_length=255)
    emotional_event = models.CharField(max_length=255)
    emotional_plus_or_minus = models.IntegerField()
    probability = models.FloatField()
    language = models.CharField(max_length=255)


class Twitter_comments(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    content = models.TextField()
    time = models.DateField()
    emotional_words = models.CharField(max_length=255)
    emotional_express = models.CharField(max_length=255)
    emotional_express_class = models.CharField(max_length=255)
    emotional_event = models.CharField(max_length=255)
    emotional_plus_or_minus = models.IntegerField()
    probability = models.FloatField()
    language = models.CharField(max_length=255)
