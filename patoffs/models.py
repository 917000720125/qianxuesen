from django.db import models

# Create your models here.
class paper_summary(models.Model):#论文总表
    id = models.IntegerField(primary_key=True)
    s_id = models.CharField(max_length=255)#学号
    s_name= models.CharField(max_length=255)#学生姓名
    college= models.CharField(max_length=255)#学院
    major= models.CharField(max_length=255)#专业
    s_type=models.CharField(max_length=255)#学生类型
    title=models.CharField(max_length=255)#论文名
    journal=models.CharField(max_length=255)#期刊名
    rank=models.CharField(max_length=255)#论文排名
    publish=models.CharField(max_length=255)#发表情况
    included=models.CharField(max_length=255)#收录情况
    year=models.CharField(max_length=255)#刊出日期-年
class patent_summary(models.Model):#专利总表python manage.py makemigrations polls
    id = models.IntegerField(primary_key=True)
    s_id = models.CharField(max_length=255)#学号
    s_name= models.CharField(max_length=255)#学生姓名
    college= models.CharField(max_length=255)#学院
    major= models.CharField(max_length=255)#专业
    s_type=models.CharField(max_length=255)#学生类型
    title=models.CharField(max_length=255)#专利名称
    pat_id=models.CharField(max_length=255)#专利号
    rank=models.CharField(max_length=255)#专利排名
    p_type=models.CharField(max_length=255)#专利类型
    year=models.CharField(max_length=255)#公示日期-年
class achievement_summary(models.Model):#科研成果总表
    id = models.IntegerField(primary_key=True)
    s_id = models.CharField(max_length=255)#学号
    s_name= models.CharField(max_length=255)#学生姓名
    college= models.CharField(max_length=255)#学院
    major= models.CharField(max_length=255)#专业
    s_type=models.CharField(max_length=255)#学生类型
    title=models.CharField(max_length=255)#获奖成果名称
    year=models.CharField(max_length=255)#获奖日期-年
    rank=models.CharField(max_length=255)#获奖排名
    type=models.CharField(max_length=255)#成果级别
    achievement=models.CharField(max_length=255)#获奖情况
class project_summary(models.Model):#科研项目总表
    id = models.IntegerField(primary_key=True)
    s_id = models.CharField(max_length=255)#学号
    s_name= models.CharField(max_length=255)#学生姓名
    college= models.CharField(max_length=255)#学院
    major= models.CharField(max_length=255)#专业
    s_type=models.CharField(max_length=255)#学生类型
    project=models.CharField(max_length=255)#项目名称
    p_id=models.CharField(max_length=255)#项目编号
    source=models.CharField(max_length=255)#项目来源
    fund=models.CharField(max_length=255)#项目经费
    principal=models.CharField(max_length=255)#项目负责人


