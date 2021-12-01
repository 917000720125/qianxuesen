from django.db import models

# Create your models here.
#2015-2020年教学评价总表
class Tea_evalution_summary(models.Model):
    semester = models.CharField(max_length=20) # 学期
    TE_id=models.IntegerField(primary_key=True)
    college = models.CharField(max_length=30)#学院名称
    c_id = models.CharField(max_length=255)#课程编号
    c_name = models.CharField(max_length=255)  # 课程名称
    cl_name=models.CharField(max_length=255)  # 班级名称
    t_id = models.CharField(max_length=30)  # 教师编号
    t_name = models.CharField(max_length=30)  # 教师姓名
    number=models.IntegerField()#评教人数
    Ave_score=models.FloatField()#综合成绩
    s_id=models.CharField( max_length=255)#学生学号
    score=models.FloatField()#成绩
    advise=models.TextField( max_length=255)#学生建议
class te_college(models.Model):
    semester = models.CharField(max_length=20)  # 学期
    college = models.CharField(primary_key=True, max_length=30)#学院名称
    ave_score= models.FloatField()#学院平均成绩
class te_course(models.Model):
    semester = models.CharField(max_length=20)  # 学期
    t_name = models.CharField(max_length=30)  # 教师姓名
    c_id = models.CharField(primary_key=True,max_length=30)  # 课程编号
    c_name = models.CharField(max_length=255)  # 课程名称
    college = models.CharField( max_length=30)  # 学院名称
    ave_score = models.FloatField()  # 学院平均成绩
#2020春学期教学评价统计
class Tea_evalution_summary_20c(models.Model):
    TE_id=models.IntegerField(primary_key=True)
    college = models.CharField(max_length=30)#学院名称
    c_id = models.CharField(max_length=255)#课程编号
    c_name = models.CharField(max_length=255)  # 课程名称
    cl_name=models.CharField(max_length=255)  # 班级名称
    t_id = models.CharField(max_length=30)  # 教师编号
    t_name = models.CharField(max_length=30)  # 教师姓名
    number=models.IntegerField()#评教人数
    Ave_score=models.FloatField()#综合成绩
    s_id=models.CharField( max_length=255)#学生学号
    score=models.FloatField()#成绩
    advise=models.TextField( max_length=255)#学生建议
class te_college_20c(models.Model):
    college = models.CharField(primary_key=True, max_length=30)#学院名称
    ave_score= models.FloatField()#学院平均成绩
class te_course_20c(models.Model):
    c_id = models.CharField(primary_key=True,max_length=255)  # 课程编号
    c_name = models.CharField(max_length=255)  # 课程名称
    college = models.CharField( max_length=30)  # 学院名称
    ave_score = models.FloatField()  # 学院平均成绩
#2020秋学期教学评价统计
# class Tea_evalution_summary_20q(models.Model):
#     TE_id=models.IntegerField(primary_key=True)
#     college = models.CharField(max_length=10)#学院名称
#     c_id = models.CharField(max_length=255)#课程编号
#     c_name = models.CharField(max_length=255)  # 课程名称
#     cl_name=models.CharField(max_length=255)  # 班级名称
#     t_id = models.CharField(max_length=30)  # 教师编号
#     t_name = models.CharField(max_length=30)  # 教师姓名
#     number=models.IntegerField()#评教人数
#     Ave_score=models.FloatField()#综合成绩
#     s_id=models.CharField( max_length=255)#学生学号
#     score=models.FloatField()#成绩
#     advise=models.TextField( max_length=255)#学生建议
class te_college_20q(models.Model):
    college = models.CharField(primary_key=True, max_length=30)#学院名称
    ave_score= models.FloatField()#学院平均成绩
class te_course_20q(models.Model):
    c_id = models.CharField(primary_key=True,max_length=255)  # 课程编号
    c_name = models.CharField(max_length=255)  # 课程名称
    college = models.CharField( max_length=30)  # 学院名称
    ave_score = models.FloatField()  # 学院平均成绩
#2018-2019春学期教学评价统计
# class Tea_evalution_summary_19c(models.Model):
#     TE_id=models.IntegerField(primary_key=True)
#     college = models.CharField(max_length=30)#学院名称
#     c_id = models.CharField(max_length=255)#课程编号
#     c_name = models.CharField(max_length=255)  # 课程名称
#     cl_name=models.CharField(max_length=255)  # 班级名称
#     t_id = models.CharField(max_length=30)  # 教师编号
#     t_name = models.CharField(max_length=30)  # 教师姓名
#     number=models.IntegerField()#评教人数
#     Ave_score=models.FloatField()#综合成绩
#     s_id=models.CharField( max_length=255)#学生学号
#     score=models.FloatField()#成绩
#     advise=models.TextField( max_length=255)#学生建议
class te_college_19c(models.Model):
    college = models.CharField(primary_key=True, max_length=30)#学院名称
    ave_score= models.FloatField()#学院平均成绩
class te_course_19c(models.Model):
    c_id = models.CharField(primary_key=True,max_length=255)  # 课程编号
    c_name = models.CharField(max_length=255)  # 课程名称
    college = models.CharField( max_length=30)  # 学院名称
    ave_score = models.FloatField()  # 学院平均成绩
#2018-2019秋学期教学评价统计
# class Tea_evalution_summary_19q(models.Model):
#     TE_id=models.IntegerField(primary_key=True)
#     college = models.CharField(max_length=30)#学院名称
#     c_id = models.CharField(max_length=255)#课程编号
#     c_name = models.CharField(max_length=255)  # 课程名称
#     cl_name=models.CharField(max_length=255)  # 班级名称
#     t_id = models.CharField(max_length=30)  # 教师编号
#     t_name = models.CharField(max_length=30)  # 教师姓名
#     number=models.IntegerField()#评教人数
#     Ave_score=models.FloatField()#综合成绩
#     s_id=models.CharField( max_length=255)#学生学号
#     score=models.FloatField()#成绩
#     advise=models.TextField( max_length=255)#学生建议
class te_college_19q(models.Model):
    college = models.CharField(primary_key=True, max_length=30)#学院名称
    ave_score= models.FloatField()#学院平均成绩
class te_course_19q(models.Model):
    c_id = models.CharField(primary_key=True,max_length=255)  # 课程编号
    c_name = models.CharField(max_length=255)  # 课程名称
    college = models.CharField( max_length=30)  # 学院名称
    ave_score = models.FloatField()  # 学院平均成绩
#2017-2018春学期教学评价统计
# class Tea_evalution_summary_18c(models.Model):
#     TE_id=models.IntegerField(primary_key=True)
#     college = models.CharField(max_length=30)#学院名称
#     c_id = models.CharField(max_length=255)#课程编号
#     c_name = models.CharField(max_length=255)  # 课程名称
#     cl_name=models.CharField(max_length=255)  # 班级名称
#     t_id = models.CharField(max_length=30)  # 教师编号
#     t_name = models.CharField(max_length=30)  # 教师姓名
#     number=models.IntegerField()#评教人数
#     Ave_score=models.FloatField()#综合成绩
#     s_id=models.CharField( max_length=255)#学生学号
#     score=models.FloatField()#成绩
#     advise=models.TextField( max_length=255)#学生建议
class te_college_18c(models.Model):
    college = models.CharField(primary_key=True, max_length=30)#学院名称
    ave_score= models.FloatField()#学院平均成绩
class te_course_18c(models.Model):
    c_id = models.CharField(primary_key=True,max_length=255)  # 课程编号
    c_name = models.CharField(max_length=255)  # 课程名称
    college = models.CharField( max_length=30)  # 学院名称
    ave_score = models.FloatField()  # 学院平均成绩
#2017-2018秋学期教学评价统计
# class Tea_evalution_summary_18q(models.Model):
#     TE_id=models.IntegerField(primary_key=True)
#     college = models.CharField(max_length=30)#学院名称
#     c_id = models.CharField(max_length=255)#课程编号
#     c_name = models.CharField(max_length=255)  # 课程名称
#     cl_name=models.CharField(max_length=255)  # 班级名称
#     t_id = models.CharField(max_length=30)  # 教师编号
#     t_name = models.CharField(max_length=30)  # 教师姓名
#     number=models.IntegerField()#评教人数
#     Ave_score=models.FloatField()#综合成绩
#     s_id=models.CharField( max_length=255)#学生学号
#     score=models.FloatField()#成绩
#     advise=models.TextField( max_length=255)#学生建议
class te_college_18q(models.Model):
    college = models.CharField(primary_key=True, max_length=30)#学院名称
    ave_score= models.FloatField()#学院平均成绩
class te_course_18q(models.Model):
    c_id = models.CharField(primary_key=True,max_length=255)  # 课程编号
    c_name = models.CharField(max_length=255)  # 课程名称
    college = models.CharField( max_length=30)  # 学院名称
    ave_score = models.FloatField()  # 学院平均成绩
#2016-2017春学期教学评价统计
# class Tea_evalution_summary_17c(models.Model):
#     TE_id=models.IntegerField(primary_key=True)
#     college = models.CharField(max_length=30)#学院名称
#     c_id = models.CharField(max_length=255)#课程编号
#     c_name = models.CharField(max_length=255)  # 课程名称
#     cl_name=models.CharField(max_length=255)  # 班级名称
#     t_id = models.CharField(max_length=30)  # 教师编号
#     t_name = models.CharField(max_length=30)  # 教师姓名
#     number=models.IntegerField()#评教人数
#     Ave_score=models.FloatField()#综合成绩
#     s_id=models.CharField( max_length=255)#学生学号
#     score=models.FloatField()#成绩
#     advise=models.TextField( max_length=255)#学生建议
class te_college_17c(models.Model):
    college = models.CharField(primary_key=True, max_length=30)#学院名称
    ave_score= models.FloatField()#学院平均成绩
class te_course_17c(models.Model):
    c_id = models.CharField(primary_key=True,max_length=255)  # 课程编号
    c_name = models.CharField(max_length=255)  # 课程名称
    college = models.CharField( max_length=30)  # 学院名称
    ave_score = models.FloatField()  # 学院平均成绩
#2016-2017秋学期教学评价统计
# class Tea_evalution_summary_17q(models.Model):
#     TE_id=models.IntegerField(primary_key=True)
#     college = models.CharField(max_length=30)#学院名称
#     c_id = models.CharField(max_length=255)#课程编号
#     c_name = models.CharField(max_length=255)  # 课程名称
#     cl_name=models.CharField(max_length=255)  # 班级名称
#     t_id = models.CharField(max_length=30)  # 教师编号
#     t_name = models.CharField(max_length=30)  # 教师姓名
#     number=models.IntegerField()#评教人数
#     Ave_score=models.FloatField()#综合成绩
#     s_id=models.CharField( max_length=255)#学生学号
#     score=models.FloatField()#成绩
#     advise=models.TextField( max_length=255)#学生建议
class te_college_17q(models.Model):
    college = models.CharField(primary_key=True, max_length=30)#学院名称
    ave_score= models.FloatField()#学院平均成绩
class te_course_17q(models.Model):
    c_id = models.CharField(primary_key=True,max_length=255)  # 课程编号
    c_name = models.CharField(max_length=255)  # 课程名称
    college = models.CharField( max_length=30)  # 学院名称
    ave_score = models.FloatField()  # 学院平均成绩
#2015-2016春学期教学评价统计
# class Tea_evalution_summary_16c(models.Model):
#     TE_id=models.IntegerField(primary_key=True)
#     college = models.CharField(max_length=30)#学院名称
#     c_id = models.CharField(max_length=255)#课程编号
#     c_name = models.CharField(max_length=255)  # 课程名称
#     cl_name=models.CharField(max_length=255)  # 班级名称
#     t_id = models.CharField(max_length=30)  # 教师编号
#     t_name = models.CharField(max_length=30)  # 教师姓名
#     number=models.IntegerField()#评教人数
#     Ave_score=models.FloatField()#综合成绩
#     s_id=models.CharField( max_length=255)#学生学号
#     score=models.FloatField()#成绩
#     advise=models.TextField( max_length=255)#学生建议
class te_college_16c(models.Model):
    college = models.CharField(primary_key=True, max_length=30)#学院名称
    ave_score= models.FloatField()#学院平均成绩
class te_course_16c(models.Model):
    c_id = models.CharField(primary_key=True,max_length=255)  # 课程编号
    c_name = models.CharField(max_length=255)  # 课程名称
    college = models.CharField( max_length=30)  # 学院名称
    ave_score = models.FloatField()  # 学院平均成绩
#2015-2016春学期教学评价统计
# class Tea_evalution_summary_16q(models.Model):
#     TE_id=models.IntegerField(primary_key=True)
#     college = models.CharField(max_length=30)#学院名称
#     c_id = models.CharField(max_length=255)#课程编号
#     c_name = models.CharField(max_length=255)  # 课程名称
#     cl_name=models.CharField(max_length=255)  # 班级名称
#     t_id = models.CharField(max_length=30)  # 教师编号
#     t_name = models.CharField(max_length=30)  # 教师姓名
#     number=models.IntegerField()#评教人数
#     Ave_score=models.FloatField()#综合成绩
#     s_id=models.CharField( max_length=255)#学生学号
#     score=models.FloatField()#成绩
#     advise=models.TextField( max_length=255)#学生建议
class te_college_16q(models.Model):
    college = models.CharField(primary_key=True, max_length=30)#学院名称
    ave_score= models.FloatField()#学院平均成绩
class te_course_16q(models.Model):
    c_id = models.CharField(primary_key=True,max_length=255)  # 课程编号
    c_name = models.CharField(max_length=255)  # 课程名称
    college = models.CharField( max_length=30)  # 学院名称
    ave_score = models.FloatField()  # 学院平均成绩
class te_tiaotingke(models.Model):
    id=models.IntegerField(primary_key=True)
    t_name = models.CharField(max_length=30)  # 教师名称
    cl_name = models.CharField(max_length=255)  # 班级名称
    c_name = models.CharField(max_length=255)  # 课程名称
    c_id = models.CharField(max_length=255)# 课程编号
    college = models.CharField(max_length=255)  # 学院
    case = models.TextField()  # 调停课情况
    content = models.TextField()  # 调停课内容
    type=models.CharField(max_length=10)  # 调停课类别
    semester = models.CharField(max_length=20) # 学期