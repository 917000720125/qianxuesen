from django.db import models

# Create your models here.
class qianxuesen_summary(models.Model):#论文总表
    id = models.IntegerField(primary_key=True)
    s_name= models.CharField(max_length=255)#学生姓名
    sex=models.CharField(max_length=255)#学生性别
    province= models.CharField(max_length=255)#省份
    cescore=models.IntegerField()#高考成绩
    prrank = models.IntegerField() #本省排名
    score1 = models.FloatField()  # 高考折算
    score2= models.FloatField()  # 面试成绩
    score3 = models.FloatField()  # 面试折算
    score4 = models.FloatField()  # 总分
    rank=models.IntegerField()#排名
    major= models.CharField(max_length=255)#拟录取专业
class qianxuesen_class(models.Model):#课程安排
    id = models.IntegerField(primary_key=True)
    banji=models.CharField(max_length=255)  # 班级
    number=models.IntegerField()  # 开课人数
    cl_id = models.CharField(max_length=255)  # 课程编号
    cl_name=models.CharField(max_length=255)  # 课程名
    t_name = models.CharField(max_length=255)  # 教师姓名
    t_college=models.CharField(max_length=255)  # 教师所在院系
    time=models.CharField(max_length=255)  # 开课时间
    place= models.CharField(max_length=255)  # 上课地点
    week = models.CharField(max_length=255)  # 上课周次
    sord= models.CharField(max_length=255)  # 单双周
    type=models.CharField(max_length=255)  #
    semester=models.CharField(max_length=255)  #学期
class qianxuesen_banji(models.Model):#课程安排
    id = models.IntegerField(primary_key=True)
    banji=models.CharField(max_length=255)  # 班级
    number=models.IntegerField()  # 开课人数
    cl_id = models.CharField(max_length=255)  # 课程编号
    cl_name=models.CharField(max_length=255)  # 课程名
    t_name = models.CharField(max_length=255)  # 教师姓名
    t_college=models.CharField(max_length=255)  # 教师所在院系
    time1 = models.CharField(max_length=255)  # 星期
    time2=models.CharField(max_length=255)  # 节次
    place= models.CharField(max_length=255)  # 上课地点
    week = models.CharField(max_length=255)  # 上课周次
    sord= models.CharField(max_length=255)  # 单双周
    type=models.CharField(max_length=255)  #
    semester=models.CharField(max_length=255)  #学期
class qianxuesen_trainingplan(models.Model):#培养计划
    id = models.IntegerField(primary_key=True)
    cl_kind=models.CharField(max_length=255)  # 课程类别
    cl_id = models.CharField(max_length=255)  # 课程编号
    cl_name=models.CharField(max_length=255)  # 课程名(中)
    cl_ename = models.CharField(max_length=255)  # 课程名(英)
    languange=models.CharField(max_length=255)#授课语言
    college=models.CharField(max_length=255)  # 开课单位
    credit=models.FloatField()  # 学分

class qianxuesen_xuanke(models.Model):#全校选课大表
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name=models.CharField(max_length=30)    #课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_cailiao(models.Model):#材料
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_dianguang(models.Model):#电光
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_gongwu(models.Model):#公务
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_huagong(models.Model):#化工
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_huansheng(models.Model):#环生
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_jixie(models.Model):#机械
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_jisuanji(models.Model):#计算机
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit = models.FloatField()  # 学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_jingguan(models.Model):#经管
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_lixueyuan(models.Model):#理学院
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_nengdong(models.Model):#能动
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit = models.FloatField()  # 学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_shechuan(models.Model):#设传
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_waiyuan(models.Model):#外国语
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit = models.FloatField()  # 学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_wangan(models.Model):#网络安全
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_xinnengyuan(models.Model):#新能源
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_zhichan(models.Model):#知识产权
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_zhinengzhizao(models.Model):#智能制造
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_zidonghua(models.Model):#自动化
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

class qianxuesen_qianxuesen(models.Model):#钱学森
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=20)   #学生学号
    st_name=models.CharField(max_length=20) #学生姓名
    st_school=models.CharField(max_length=20)   #所属院系
    st_class=models.CharField(max_length=20)    #所属班级
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_credit=models.FloatField()     #学分
    cl_id=models.CharField(max_length=20)   #课序号
    teacher=models.CharField(max_length=20)  # 授课教师

#钱院所有学生
class qianxuesen_qianxuesenst(models.Model):#钱学森
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=200)   #学生学号
    st_name=models.CharField(max_length=200) #学生姓名
    st_major=models.CharField(max_length=200) #学生姓名
    major_2=models.CharField(max_length=200) #学生姓名
    st_grade=models.CharField(max_length=200) #学生姓名
    st_school=models.CharField(max_length=200)   #所属院系
    st_class=models.CharField(max_length=200)    #所属班级
    total_credit=models.FloatField()     #学分


class qianxuesen_chake(models.Model):
    id = models.IntegerField(primary_key=True)
    cl_name = models.CharField(max_length=30)  # 课程名称
    cl_cid = models.CharField(max_length=30)  # 课程编号
    teacher = models.CharField(max_length=20)  # 授课教师
    cl_id = models.CharField(max_length=20)  # 课序号
    cl_credit = models.FloatField()  # 学分
    total_number=models.IntegerField()  #总数
    qian_number=models.IntegerField() #钱院学生总数

class qianxuesen_project19(models.Model):
    id = models.IntegerField(primary_key=True)
    st_id = models.CharField(max_length=30)  # 课程名称
    st_name = models.CharField(max_length=30)  # 课程编号
    st_school = models.CharField(max_length=30)  # 授课教师
    st_major = models.CharField(max_length=30)  # 课序号
    major_2 = models.CharField(max_length=30)  # 方向
    st_class = models.CharField(max_length=30)  # 班级
    st_grade = models.CharField(max_length=30)  # 授课教师
    schoolyear = models.CharField(max_length=30)  # 课程名称
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 授课教师
    cl_credit = models.FloatField()  # 学分
    cl_type = models.CharField(max_length=30)  # 课程名称
    cl_attribute = models.CharField(max_length=30)  # 课程编号
    cl_school = models.CharField(max_length=30)  # 授课教师
    cl_lanuage = models.CharField(max_length=30)  # 课序号

class qianxuesen_project19_copy(models.Model):
    id = models.IntegerField(primary_key=True)
    st_id = models.CharField(max_length=30)  # 课程名称
    st_name = models.CharField(max_length=30)  # 课程编号
    st_school = models.CharField(max_length=30)  # 授课教师
    st_major = models.CharField(max_length=30)  # 课序号
    major_2=models.CharField(max_length=30)  # 方向
    st_class=models.CharField(max_length=30)  # 班级
    st_grade = models.CharField(max_length=30)  # 授课教师
    schoolyear = models.CharField(max_length=30)  # 课程名称
    cl_cid = models.CharField(max_length=30)  # 课程编号
    cl_name = models.CharField(max_length=30)  # 授课教师
    cl_credit = models.FloatField()  # 学分
    cl_type = models.CharField(max_length=30)  # 课程名称
    cl_attribute = models.CharField(max_length=30)  # 课程编号
    cl_school = models.CharField(max_length=30)  # 授课教师
    cl_lanuage = models.CharField(max_length=30)  # 课序号

class qianxuesen_kebiao(models.Model):
    cl_school=models.CharField(max_length=100)
    cl_cid=models.CharField(max_length=100)
    cl_id=models.CharField(max_length=100)
    teacher_id=models.CharField(max_length=100)
    teacher=models.CharField(max_length=100)
    teacher_title=models.CharField(max_length=100)
    teacher_school=models.CharField(max_length=100)
    cl_name=models.CharField(max_length=100)
    st_class=models.CharField(max_length=500)
    cl_credit=models.FloatField()
    classroom=models.CharField(max_length=100)
    cl_date=models.CharField(max_length=100)
    jieci_1=models.CharField(max_length=100)
    jieci_2=models.CharField(max_length=100)
    jieci_3=models.CharField(max_length=100)
    jieci_4=models.CharField(max_length=100)
    jieci_5=models.CharField(max_length=100)
    jieci_6=models.CharField(max_length=100)
    jieci_7=models.CharField(max_length=100)

#钱院选课的班级
class qianxuesen_class1(models.Model):
    id = models.IntegerField(primary_key=True)
    number=models.IntegerField()
    cl_cid=models.CharField(max_length=200)
    cl_id=models.CharField(max_length=200)
    t_name=models.CharField(max_length=200)
    t_title=models.CharField(max_length=200)
    t_college=models.CharField(max_length=200)
    cl_name=models.CharField(max_length=200)
    classroom=models.CharField(max_length=200)
    cl_credit=models.FloatField()
    cl_date=models.CharField(max_length=200)
    jieci_1=models.CharField(max_length=200)
    jieci_2=models.CharField(max_length=200)
    jieci_3=models.CharField(max_length=200)
    jieci_4=models.CharField(max_length=200)
    jieci_5=models.CharField(max_length=200)
    jieci_6=models.CharField(max_length=200)
    jieci_7=models.CharField(max_length=200)

class qianxuesen_fangxiang(models.Model):
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=200)
    st_name=models.CharField(max_length=200)
    st_school=models.CharField(max_length=200)
    st_major=models.CharField(max_length=200)
    major_2=models.CharField(max_length=200)
    st_grade=models.CharField(max_length=200)
    st_class=models.CharField(max_length=200)
class qianxuesen_fangxiang19(models.Model):
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=200)
    st_name=models.CharField(max_length=200)
    st_school=models.CharField(max_length=200)
    st_major=models.CharField(max_length=200)
    major_2=models.CharField(max_length=200)
    st_grade=models.CharField(max_length=200)
    st_class=models.CharField(max_length=200)
class qianxuesen_fangxiang20(models.Model):
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=200)
    st_name=models.CharField(max_length=200)
    st_school=models.CharField(max_length=200)
    st_major=models.CharField(max_length=200)
    major_2=models.CharField(max_length=200)
    st_grade=models.CharField(max_length=200)
    st_class=models.CharField(max_length=200)


class qianxuesen_0071(models.Model):
    id = models.IntegerField(primary_key=True)
    cl_cid=models.CharField(max_length=30)
    cl_name=models.CharField(max_length=30)
    cl_credit=models.FloatField()
    schoolyear=models.CharField(max_length=30)
    cl_type=models.CharField(max_length=30)
    cl_attribute=models.CharField(max_length=30)
    cl_school=models.CharField(max_length=30)
    cl_lanuage = models.CharField(max_length=30)

class qianxuesen_007201(models.Model):
    id = models.IntegerField(primary_key=True)
    cl_cid=models.CharField(max_length=30)
    cl_name=models.CharField(max_length=30)
    cl_credit=models.FloatField()
    schoolyear=models.CharField(max_length=30)
    cl_type=models.CharField(max_length=30)
    cl_attribute=models.CharField(max_length=30)
    cl_school=models.CharField(max_length=30)
    cl_lanuage = models.CharField(max_length=30)

class qianxuesen_007202(models.Model):
    id = models.IntegerField(primary_key=True)
    cl_cid=models.CharField(max_length=30)
    cl_name=models.CharField(max_length=30)
    cl_credit=models.FloatField()
    schoolyear=models.CharField(max_length=30)
    cl_type=models.CharField(max_length=30)
    cl_attribute=models.CharField(max_length=30)
    cl_school=models.CharField(max_length=30)
    cl_lanuage = models.CharField(max_length=30)

class qianxuesen_007301(models.Model):
    id = models.IntegerField(primary_key=True)
    cl_cid=models.CharField(max_length=30)
    cl_name=models.CharField(max_length=30)
    cl_credit=models.FloatField()
    schoolyear=models.CharField(max_length=30)
    cl_type=models.CharField(max_length=30)
    cl_attribute=models.CharField(max_length=30)
    cl_school=models.CharField(max_length=30)
    cl_lanuage = models.CharField(max_length=30)

class qianxuesen_007302(models.Model):
    id = models.IntegerField(primary_key=True)
    cl_cid=models.CharField(max_length=30)
    cl_name=models.CharField(max_length=30)
    cl_credit=models.FloatField()
    schoolyear=models.CharField(max_length=30)
    cl_type=models.CharField(max_length=30)
    cl_attribute=models.CharField(max_length=30)
    cl_school=models.CharField(max_length=30)
    cl_lanuage = models.CharField(max_length=30)

class qianxuesen_wxordx(models.Model):
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=200)
    st_name = models.CharField(max_length=200)
    st_school = models.CharField(max_length=200)
    st_major = models.CharField(max_length=200)
    major_2 = models.CharField(max_length=200)
    st_grade = models.CharField(max_length=200)
    st_class = models.CharField(max_length=200)
    num_wx = models.IntegerField()
    num_dx = models.IntegerField()
    total_credit=models.FloatField()

class qianxuesen_fanganbidui1(models.Model):
    id = models.IntegerField(primary_key=True)
    cl_cid=models.CharField(max_length=200)
    cl_name=models.CharField(max_length=200)
    num_wx=models.IntegerField()

class qianxuesen_wxst(models.Model):
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=200)
    st_name = models.CharField(max_length=200)
    st_school = models.CharField(max_length=200)
    st_major = models.CharField(max_length=200)
    major_2 = models.CharField(max_length=200)
    cl_cid = models.CharField(max_length=200)
    cl_name = models.CharField(max_length=200)
    st_grade = models.CharField(max_length=200)
    st_class = models.CharField(max_length=200)
    num_wx = models.IntegerField()
    num_dx = models.IntegerField()
    total_credit=models.FloatField()

class qianxuesen_chengji(models.Model):
    id = models.IntegerField(primary_key=True)
    st_id=models.CharField(max_length=200)
    st_name = models.CharField(max_length=200)
    class_num=models.IntegerField()
    cl_name = models.CharField(max_length=200)
    cl_credit = models.CharField(max_length=200)
    cl_performance = models.CharField(max_length=200)
    cl_type = models.CharField(max_length=200)
    cl_attribute = models.CharField(max_length=200)
    year=models.CharField(max_length=200)

class qianxuesen_exam1(models.Model):
    id = models.IntegerField(primary_key=True)
    cl_name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)

class qianxuesen_examst(models.Model):
    id = models.IntegerField(primary_key=True)
    cl_name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    st_id=models.CharField(max_length=200)
    st_name=models.CharField(max_length=200)
    st_class=models.CharField(max_length=200)

class qianxuesen_bujige_num(models.Model):
    id = models.IntegerField(primary_key=True)
    st_id = models.CharField(max_length=200)
    st_name = models.CharField(max_length=200)
    bujige_num = models.IntegerField()