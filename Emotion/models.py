from django.db import models


# Create your models here.
class User(models.Model):
    userid = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)
    permissions = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1)
    national = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
class gp_summary(models.Model):#留学总表
  id=models.IntegerField(primary_key=True)
  csc=models.CharField(max_length=10)#csc录取结果（基金委录取,无则没有录取）
  college=models.CharField(max_length=255)
  name=models.CharField(max_length=255)
  s_id=models.CharField(max_length=255)#学号
  teacher=models.CharField(max_length=255)
  major=models.CharField(max_length=255)
  grade=models.CharField(max_length=255)#在读年级
  type=models.CharField(max_length=255)#联培/学位
  m_or_d=models.CharField(max_length=255)#硕士/博士
  country=models.CharField(max_length=255)#拟留学国家
  university=models.CharField(max_length=255)#大学中文名
  QS=models.CharField(max_length=10)#QS排名
  US_NEWS=models.CharField(max_length=10)
  time_mon=models.IntegerField()#留学时间（月）
class college_declare(models.Model):#申报人数/学院
    college=models.CharField(primary_key=True,max_length=10)
    declare=models.IntegerField()
    successful= models.IntegerField()
class grade_declare(models.Model):#申报人数/在读年级
    grade=models.CharField(primary_key=True,max_length=10)
    declare=models.IntegerField()
    successful= models.IntegerField()
class type_declare(models.Model):#申报人数/联培/学位
    type=models.CharField(primary_key=True,max_length=10)
    declare=models.IntegerField()
    successful= models.IntegerField()
class time_declare(models.Model):#申报人数/留学期限
    time=models.IntegerField(primary_key=True)
    declare=models.IntegerField()
    successful= models.IntegerField()
class QS_declare(models.Model):#申报人数/QS
    QS=models.CharField(primary_key=True,max_length=255)
    declare=models.IntegerField()
    successful= models.IntegerField()
class major_declare(models.Model):#申报人数/专业
    major=models.CharField(primary_key=True,max_length=255)
    college=models.CharField(max_length=255)
    declare=models.IntegerField()
    successful= models.IntegerField()
#2020留学申请统计
class gp_summary20(models.Model):#2020留学总表
  id=models.IntegerField(primary_key=True)
  projects=models.CharField(max_length=10)#申请项目
  college=models.CharField(max_length=255)
  name=models.CharField(max_length=255)
  s_id=models.CharField(max_length=255)#学号
  teacher=models.CharField(max_length=255)
  major=models.CharField(max_length=255)
  grade=models.CharField(max_length=255)#在读年级
  type=models.CharField(max_length=255)#联培/学位
  m_or_d=models.CharField(max_length=255)#硕士/博士
  country=models.CharField(max_length=255)#拟留学国家
  university=models.CharField(max_length=255)#大学中文名
  QS=models.CharField(max_length=10)#QS排名
  time_mon=models.IntegerField()#留学时间（月）
class time_declare20(models.Model):#申报人数/留学期限
    time=models.IntegerField(primary_key=True)
    declare=models.IntegerField()
class QS_declare20(models.Model):#申报人数/QS
    QS=models.CharField(primary_key=True,max_length=255)
    declare=models.IntegerField()
class college_declare20(models.Model):#申报人数/学院
    college=models.CharField(primary_key=True,max_length=10)
    declare=models.IntegerField()
class project_declare20(models.Model):#申报人数/申报项目
    project=models.CharField(primary_key=True,max_length=10)
    declare=models.IntegerField()
#2020留学报送统计
class gp_summary20_1(models.Model):#2020留学总表
  id=models.IntegerField(primary_key=True)
  projects=models.CharField(max_length=10)#申请项目
  college=models.CharField(max_length=255)
  name=models.CharField(max_length=255)
  s_id=models.CharField(max_length=255)#学号
  teacher=models.CharField(max_length=255)
  major=models.CharField(max_length=255)
  grade=models.CharField(max_length=255)#在读年级
  type=models.CharField(max_length=255)#联培/学位
  m_or_d=models.CharField(max_length=255)#硕士/博士
  country=models.CharField(max_length=255)#拟留学国家
  university=models.CharField(max_length=255)#大学中文名
  QS=models.CharField(max_length=10)#QS排名
  time_mon=models.IntegerField()#留学时间（月）
class time_declare20_1(models.Model):#申报人数/留学期限
    time=models.IntegerField(primary_key=True)
    declare=models.IntegerField()
class QS_declare20_1(models.Model):#申报人数/QS
    QS=models.CharField(primary_key=True,max_length=255)
    declare=models.IntegerField()
class college_declare20_1(models.Model):#申报人数/学院
    college=models.CharField(primary_key=True,max_length=10)
    declare=models.IntegerField()
class project_declare20_1(models.Model):#申报人数/申报项目
    project=models.CharField(primary_key=True,max_length=10)
    declare=models.IntegerField()
#高数成绩统计
class cj_college(models.Model):
    college = models.CharField(primary_key=True, max_length=10)
    fail = models.IntegerField()
    average= models.FloatField()
class cj_summary(models.Model):
    s_id=models.CharField(primary_key=True,max_length=255)
    s_name=models.CharField(max_length=10)
    college = models.CharField(max_length=10)
    major= models.CharField(max_length=20)
    c_id = models.CharField(max_length=20)
    c_name = models.CharField(max_length=20)
    score= models.IntegerField()
#课程统计
class course_summary(models.Model):
    c_id=models.CharField(primary_key=True,max_length=255)
    c_name=models.CharField(max_length=10)#课程名称
    college = models.CharField(max_length=10)
    cl_name=models.CharField(max_length=10)#班级名称
    t_name=models.CharField(max_length=10)#教师名称
    t_title=models.CharField(max_length=10)#教师职称
    Shuodao=models.CharField(max_length=1)#是否是硕导
    Doctoral_advisor=models.CharField(max_length=1)#是否是博导
    number=models.IntegerField()
    place=models.CharField(max_length=10)#上课地点
class course_coll(models.Model):
    college=models.CharField(primary_key=True,max_length=10)
    coursenum=models.IntegerField()
    classnum= models.IntegerField()
class course_place(models.Model):
    id=models.IntegerField(primary_key=True)
    college = models.CharField( max_length=10)
    place=models.CharField( max_length=10)
    classnum = models.IntegerField()

