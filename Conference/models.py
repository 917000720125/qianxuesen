from django.db import models

# Create your models here.
#2019国际会议第一批统计
class cf_summary19(models.Model):#2019会议总表
  id=models.IntegerField(primary_key=True)
  s_id=models.CharField(max_length=255)#学号
  name=models.CharField(max_length=255)
  college=models.CharField(max_length=255)#学院
  major=models.CharField(max_length=255)#专业
  mentor=models.CharField(max_length=255)#导师
  cfname=models.CharField(max_length=255)#会议名称
  cfcategory=models.CharField(max_length=255)#会议类别
  title=models.CharField(max_length=255)#论文题目
  condition=models.CharField(max_length=255)#论文状态（拟投/在投/录用）
  form=models.CharField(max_length=255)#汇报形式
  country=models.CharField(max_length=255)#会议国家
  subsidy=models.IntegerField()#补助金
  approved=models.CharField(max_length=2, default='未过')#审核是否通过
class cf_college_declare_19(models.Model):#申报人数/学院
    college=models.CharField(primary_key=True,max_length=20)
    declare=models.IntegerField()
    successful= models.IntegerField()
class cf_major_declare_19(models.Model):  # 申报人数/专业
  major = models.CharField(primary_key=True, max_length=20)
  declare = models.IntegerField()
  successful = models.IntegerField()
class cf_category_declare_19(models.Model):  # 申报人数/会议类别
  category = models.CharField(primary_key=True, max_length=20)
  declare = models.IntegerField()
  successful = models.IntegerField()
class cf_cfname_declare_19(models.Model):  # 申报人数/会议名称
  cfname = models.CharField(primary_key=True, max_length=20)
  declare = models.IntegerField()
  successful = models.IntegerField()
class cf_form_declare_19(models.Model):  # 申报人数/会议名称
  form = models.CharField(primary_key=True, max_length=20)
  declare = models.IntegerField()
  successful = models.IntegerField()
class cf_condition_declare_19(models.Model):  # 申报人数/论文状态
  condition = models.CharField(primary_key=True, max_length=20)
  declare = models.IntegerField()
  successful = models.IntegerField()
class cf_mentor_declare_19(models.Model):  # 申报人数/论文状态
  mentor = models.CharField(primary_key=True, max_length=20)
  declare = models.IntegerField()
  successful = models.IntegerField()
class cf_country_declare_19(models.Model):  # 申报人数/会议国家
  country = models.CharField(primary_key=True, max_length=20)
  declare = models.IntegerField()
  successful = models.IntegerField()