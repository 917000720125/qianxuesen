import sys
import os
import django
# 这两行很重要，用来寻找项目根目录，os.path.dirname要写多少个根据要运行的python文件到根目录的层数决定
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emotionanalysis.settings')
django.setup()
from Tevalution.models import *
from emotionanalysis.Function import *
# 学期列表
semlist = ['2015-2016春学期', '2015-2016秋学期', '2016-2017春学期', '2016-2017秋学期', '2017-2018春学期', '2017-2018秋学期',
           '2018-2019春学期', '2018-2019秋学期', '2019-2020春学期', '2019-2020秋学期']
collegelist = {'2015-2016春学期': te_college_16c(), '2015-2016秋学期': te_college_16q(), '2016-2017春学期': te_college_17c(),
               '2016-2017秋学期': te_college_17q(), '2017-2018春学期': te_college_18c(), '2017-2018秋学期': te_college_18q(),
               '2018-2019春学期': te_college_19c(), '2018-2019秋学期': te_college_19q(), '2019-2020春学期': te_college_20c(),
               '2019-2020秋学期': te_college_20q()}
courselist = {'2015-2016春学期': te_course_16c(), '2015-2016秋学期': te_course_16q(), '2016-2017春学期': te_course_17c(),
              '2016-2017秋学期': te_course_17q(), '2017-2018春学期': te_course_18c(), '2017-2018秋学期': te_course_18q(),
              '2018-2019春学期': te_course_19c(), '2018-2019秋学期': te_course_19q(), '2019-2020春学期': te_course_20c(),
              '2019-2020秋学期': te_course_20q()}
#对教学评价表进行处理
def TE_analy():
    for i in semlist:
        print(i)
        datas=Tea_evalution_summary.objects.filter(semester=i)
        dcollege=collegelist.get(i)
        dcourse=courselist.get(i)
        course(datas,dcourse)
        college(datas,dcollege,i)
def college(datas,dc,dcourse):
    rows = len(datas)  # 总表长度
    flagc = [0] * (rows + 1)  # 学院的标记
    college = [''] * 30
    j = 0
    sheetc = [0] * (rows + 1)
    cnum = 0
    for data in datas:  # 初始化
        sheetc[j] = data.college
        j += 1
    for i in range(0, rows):  # 学院
        if flagc[i] != -1:
            college[cnum] = sheetc[i]
            for k in range(i + 1, rows + 1):
                if sheetc[k] == college[cnum]:
                    flagc[k] = -1
            cnum = cnum + 1
    # 学院
    for i in range(0, cnum):
        dc.college = college[i]
        ave=ave_score(college[i],dcourse)
        dc.ave_score = ave
        dc.save()
def course(datas,dc):
    cnum =0 # 课程数
    num=0
    course_name= [''] * 2000  # 课程名称
    course_id = [''] * 2000  # 课程编号
    college=[''] * 2000
    ave_score=[''] * 2000
    # 课程
    for data in datas:
        if course_id[num]!=data.c_id:
            course_id[cnum]=data.c_id
            course_name[cnum] = data.c_name
            college[cnum]=data.college
            ave_score[cnum]=data.Ave_score
            cnum=cnum+1
            num=cnum-1
    #课程
    for i in range(0, cnum):
        dc.c_id= course_id[i]
        dc.c_name = course_name[i]
        dc.college = college[i]
        dc.ave_score=ave_score[i]
        dc.save()
def banji(datas,dc):
    cnum =0 # 课程数
    num=0
    banji_name = [''] * 2000  # 班级名称
    course_name= [''] * 2000  # 课程名称
    course_id = [''] * 2000  # 课程编号
    college=[''] * 2000
    ave_score=[''] * 2000
    # 课程
    for data in datas:
        if course_id[num]!=data.c_id:
            course_id[cnum]=data.c_id
            course_name[cnum] = data.c_name
            college[cnum]=data.college
            ave_score[cnum]=data.Ave_score
            cnum=cnum+1
            num=cnum-1
    #课程
    for i in range(0, cnum):
        dc.c_id= course_id[i]
        dc.c_name = course_name[i]
        dc.college = college[i]
        dc.ave_score=ave_score[i]
        dc.save()
#计算学院平均分
def ave_score(college,semester):
    courselist = {'2015-2016春学期': te_course_16c, '2015-2016秋学期': te_course_16q, '2016-2017春学期': te_course_17c,
                  '2016-2017秋学期': te_course_17q, '2017-2018春学期': te_course_18c, '2017-2018秋学期': te_course_18q,
                  '2018-2019春学期': te_course_19c, '2018-2019秋学期': te_course_19q, '2019-2020春学期': te_course_20c,
                  '2019-2020秋学期': te_course_20q}
    ave_score=0
    datas=courselist.get(semester).objects.filter(college=college)
    for data in datas:
        ave_score=ave_score+data.ave_score
    ave_score=ave_score/len(datas)
    return ave_score
if __name__ == "__main__":
    TE_analy()
    print('处理完成')