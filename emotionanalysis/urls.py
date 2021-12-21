"""emotionalises URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from emotionanalysis.login import *
from emotionanalysis.views import *
from Conference.views import *
from Tevalution.views import *
from patoffs.views import *
from qianxuesen.views import *
urlpatterns = [
                  # path('',)
                  path('admin/', admin.site.urls),
                  path('gp_grade_declare',gp_grade_declare),
                  # 登陆系统
                  path('', index),
                  path('html/index.html', index),
                  path('html/main.html', main),
                  path('login', login), path('logup', logup), path('logout', logout),
                  path('user_info', user_info), path('history', history),
                  #2020留学申请统计
                  path('gp_college_declare20', gp_college_declare20),
                  path('gp_time_declare20', gp_time_declare20),
                  path('gp_QS_declare20', gp_QS_declare20),
                  path('gp_world_declare20', gp_world_declare20),
                  path('gp_project_declare20', gp_project_declare20),
                  path('gp_details_20', gp_details_20),
                  #2020留学报送统计
                  path('gp_college_declare20_1', gp_college_declare20_1),
                  path('gp_time_declare20_1', gp_time_declare20_1),
                  path('gp_QS_declare20_1', gp_QS_declare20_1),
                  path('gp_world_declare20_1', gp_world_declare20_1),
                  path('gp_project_declare20_1', gp_project_declare20_1),
                  path('gp_details_20_1', gp_details_20_1),
                  #19成绩统计
                  path('cj_college_fail', cj_college_fail),
                  path('cj_analyse', cj_analyse),
                  path('cj_fractional', cj_fractional),
                  #19课程统计
                  path('course_college', course_college),
                  path('course_analyse', course_analyse),
                  path('course_details', course_details),
                  path('cr_place', cr_place),
                  path('emotion_analyse_figure3', emotion_analyse_figure3),
                  #19国际会议统计
                  path('cf_college_declare19', cf_college_declare19),
                  path('cf_major_declare19', cf_major_declare19),
                  path('cf_mentor_declare19', cf_mentor_declare19),
                  path('cf_cfname_declare19', cf_cfname_declare19),
                  path('cf_form_declare19', cf_form_declare19),
                  path('cf_condition_declare19', cf_condition_declare19),
                  path('cf_category_declare19', cf_category_declare19),
                  path('cf_world_declare19', cf_world_declare19),
                  path('cf_details_19',cf_details_19),
                  # 教学评价统计
                  path('TE_college', TE_college),
                  path('TE_course', TE_course),
                  path('TE_class', TE_class),
                  path('TE_Getlist',TE_Getlist),
                  path('TE_GetClist',TE_GetClist),
                  path('TE_tiaotingke',TE_tiaotingke),
                  path('TE_college_20c', TE_college_20c),
                  path('TE_course_20c', TE_course_20c),
                  path('TE_class_20c', TE_class_20c),
                  #科研成果
                  # path('Pat_GetCollegelist',Pat_GetCollegelist),#学院
                  # path('Pat_GetMajorlist',Pat_GetMajorlist),#专业
                   #论文
                  path('paper_college',paper_college),#学院
                  path('paper_all',paper_all),#学院
                  path('paper_details',paper_details),
                   #专利
                  path('patent_college', patent_college),  # 学院
                  path('patent_all', patent_all),  # 学院
                  path('patent_details',patent_details),
                   #科研项目
                  path('project_college', project_college),  # 学院
                  path('project_all', project_all),  # 学院
                  path('project_details',project_details),
                   #科研竞赛
                  path('achievement_college', achievement_college),  # 学院
                  path('achievement_all', achievement_all),  # 学院
                  path('achievement_details',achievement_details),
                  #钱学森院录取
                  path('qianxuesen_admit', qianxuesen_admit),  # 分类
                  path('qianxuesen_details', qianxuesen_details),#详情
                  #钱学森院开课统计
                  path('qianxuesen_college', qianxuesen_college),#学院开课数统计
                  path('qianxuesen_t_college', qianxuesen_t_college),#教师所在学院统计
                  path('qianxuesen_banji', qianxuesen_banji),  #clid,college-班级
                  ###########
                  path('qianxuesen_bj_college', qianxuesen_bj_college),#学院班级统计
                  path('qianxuesen_banji1', qianxuesen_banji1),#学院—班级
                  #########
                  path('qianxuesen_course', qianxuesen_course),#班级详情表
                  path('qianxuesen_Getlist3', qianxuesen_Getlist3),#获取教师列表
                  path('qianxuesen_Getlist4', qianxuesen_Getlist4),#获取地点列表
                  #钱院查课统计
                  path('qianxuesen_allcourse', qianxuesen_allcourse),  # 全校课程详情
                  path('qianxuesen_Getcourse',qianxuesen_Getcourse),#获取开课列表
                  path('qianxuesen_Getclid', qianxuesen_Getclid),  # 获取课序列表
                  path('qianxuesen_Getallst', qianxuesen_Getallst),  # 获取该课全校学生名单
                  path('qianxuesen_Getqianst', qianxuesen_Getqianst),  # 获取该课钱学森学院学生名单
                  path('qianxuesen_xuanke', qianxuesen_xuanke),  # 钱学森学院学生选课详情
                  path('qianxuesen_Getxuanke', qianxuesen_Getxuanke),  # 该学生选课列表
                  #培养方案
                  path('qianxuesen_Getstudent19',qianxuesen_Getstudent19), #19级学生
                  path('qianxuesen_Getproject19',qianxuesen_Getproject19), #19级方案
                  path('qianxuesen_compare', qianxuesen_compare),  # 对比
                  #2021-2022开课统计
                  path('qianxuesen_college1',qianxuesen_college1),#学院开课数统计2021-2022-1
                  path('qianxuesen_t_college1', qianxuesen_t_college1),  # 开课详情
                  path('qianxuesen_bj_college1', qianxuesen_bj_college1),  # 学院班级统计
                  path('qianxuesen_banji2', qianxuesen_banji2),  # 学院—班级
                  path('qianxuesen_detail2', qianxuesen_detail2),  # 学院—班级详情
                  path('qianxuesen_title', qianxuesen_title),  # 学院—职称详情
                  path('qianxuesen_title_class', qianxuesen_title_class),  # 学院—职称详情
                  path('qianxuesen_fanganbidui', qianxuesen_fanganbidui),  # 2021方案——方案比对
                  path('qianxuesen_fanganbidui_st',qianxuesen_fanganbidui_st),#2021方案——方案比对-详情
                  path('qianxuesen_pf_st', qianxuesen_pf_st),  # 成绩名单
                  path('qianxuesen_performance', qianxuesen_performance),  # 成绩详情
                  path('qianxuesen_bujige',qianxuesen_bujige),#不及格学生名单
                  path('qianxuesen_bujigeclass',qianxuesen_bujigeclass), #不及格学生名单——不及格课程
                  path('qianxuesen_chengjibidui',qianxuesen_chengjibidui),#学生成绩统计——课程成绩分析
                  path('qianxuesen_chengjifenbu',qianxuesen_chengjifenbu),#学生成绩统计——课程成绩分析——课程成绩分布
                  path('qianxuesen_qujianst',qianxuesen_qujianst),#学生成绩统计——课程成绩分析——课程成绩分布-人员详情
                  path('qianxuesen_examst',qianxuesen_examst),#学生考试页面
                  path('qianxuesen_exam', qianxuesen_exam),  # 学生考试页面
                  path('qianxuesen_exam_db', qianxuesen_exam_db),  # 学生考试入库
                  path('qianxuesen_gradesanalyse',qianxuesen_gradesanalyse), #学生成绩分析
                  path('qianxuesen_gradesfenbu',qianxuesen_gradesfenbu),  # 学生成绩分析
              ]
