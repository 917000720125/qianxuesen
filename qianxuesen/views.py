from django.shortcuts import render
from qianxuesen.models import *
import json
import string
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.models import model_to_dict
from collections import Counter
from django.db.models import Q
# Create your views here.
#2020钱学森院录取统计
def qianxuesen_admit(require):
    d=require.GET
    res=[]
    if len(d)==0:
       kind='college'
    else:
        kind = d['kind']
        print('kind',end='')
        print(kind)
        if kind=='专业':
            kind='major'
        elif kind=='性别':
            kind='sex'
        elif kind=='省份':
            kind='province'
    res=qianxuesen_kind(kind)
    return HttpResponse(json.dumps(res), content_type="application/json")
def qianxuesen_kind(kind):
     datas=qianxuesen_summary.objects.values_list(kind)
     # for data in datas :
     #     print(data)
     res=[]
     result=Counter(datas).most_common()
     for i in result:
        print(i[0][0])
        print(i[1])
        res.append({'key':i[0][0],'number':i[1]})
     return res
def qianxuesen_details(require):
    d=require.GET
    res=[]
    option={}
    kind=d['option']
    if kind =='':
        kind='major'
    parameter=d['parameter']
    if kind == '专业':
        kind = 'major'
    elif kind == '性别':
        kind = 'sex'
    elif kind == '省份':
        kind = 'province'
    option[kind]=parameter
    datas=qianxuesen_summary.objects.all()
    datas=datas.filter(**option)
    for data in datas:
        res.append({'s_name':data.s_name,'sex':data.sex,'province':data.province,'cescore':data.cescore,"prrank":data.prrank,"score1":data.score1,
                    "score2": data.score2,"score3":data.score3,"score4":data.score4,'rank':data.rank,"major":data.major})
    return HttpResponse(json.dumps(res), content_type="application/json")
#2020-2021春秋学期，钱学森院开课统计
#学院—开棵数  ：collgeg->t_college->banji
def qianxuesen_college(require):
    d = require.GET
    res=[]
    college_list=['体育部','理学院','化工学院','电子工程与光电技术学院','马克思主义学院','计算机科学与工程学院','钱学森学院','机械工程学院',
                  '材料科学与工程学院','工程训练中心','自动化学院','外国语学院','设计艺术与传媒学院','能源与动力工程学院','教务处','研究生院','艺术与文化素质教育部']
    num_list=[0 for i in range(0,len(college_list))]
    datas = qianxuesen_class.objects.all()
    cl_list=[[]for i in range(0,len(college_list))]
    for data in datas:
            college = data.t_college
            college = college.split(',')
            college = list(set(college))
            cl_id=data.cl_id
            for i in college:
                if i in college_list:
                    if cl_id not in cl_list[college_list.index(i)]:
                        num_list[college_list.index(i)]+=1;
                        cl_list[college_list.index(i)].append(cl_id)
    for i in range(0,len(college_list)):
        res.append({'key':college_list[i],'number':num_list[i]})
    res.sort(key=lambda x:(x.get('number',0)),reverse=True)
    return HttpResponse(json.dumps(res), content_type="application/json")
#学院—开课详情
def qianxuesen_t_college(request):
    d=request.GET
    datas=qianxuesen_class.objects.filter(t_college=d['college'])
    print(d)
    if len(d['jieci'])==0:
        jieci='全选'
    else:
        jieci=d['jieci']
    if len(d['week'])==0:
        week1='全选'
    else:
        week1=d['week']
    res = dispose(datas, week1, jieci)
    return HttpResponse(json.dumps(res), content_type="application/json")
#课程id,学院-班级
def qianxuesen_banji(request):
    d=request.GET
    print(d)
    t_college=d['t_college']
    cl_id=d['cl_id']
    datas=qianxuesen_class.objects.filter(t_college=t_college,cl_id=cl_id)
    if len(d['jieci'])==0:
        jieci='全选'
    else:
        jieci=d['jieci']
    if len(d['week'])==0:
        week1='全选'
    else:
        week1=d['week']
    res=dispose1(datas,week1,jieci)
    return HttpResponse(json.dumps(res), content_type="application/json")
#对cl_id去重
def dispose(datas,week1,jieci):
    res=[]
    cl_list=[]
    for data in datas:
        if week1 == "全选":
            if data.cl_id not in cl_list:
                time = tojieci(data.time)
                if jieci == "全选":
                    res.append({'cl_name': data.cl_name, 'cl_id': data.cl_id, 't_name': data.t_name,
                                't_college': data.t_college,
                                'time': time, 'place': data.place, 'week': data.week, 'sord': data.sord,
                                'semester': data.semester})
                    cl_list.append(data.cl_id)
                else:
                    if jieci in time:
                        res.append({'cl_name': data.cl_name, 'cl_id': data.cl_id, 't_name': data.t_name,
                                    't_college': data.t_college,
                                    'time': time, 'place': data.place, 'week': data.week, 'sord': data.sord,
                                    'semester': data.semester})
                        cl_list.append(data.cl_id)
        else:
            week = data.week
            week = week.split(',')
            if week1 in week:
                if data.cl_id not in cl_list:
                    time = tojieci(data.time)
                    if jieci == "全选":
                        res.append({'cl_name': data.cl_name, 'cl_id': data.cl_id, 't_name': data.t_name,
                                    't_college': data.t_college,
                                    'time': time, 'place': data.place, 'week': data.week, 'sord': data.sord,
                                    'semester': data.semester})
                        cl_list.append(data.cl_id)
                    else:
                        if jieci in time:
                            res.append({'cl_name': data.cl_name, 'cl_id': data.cl_id, 't_name': data.t_name,
                                        't_college': data.t_college,
                                        'time': time, 'place': data.place, 'week': data.week, 'sord': data.sord,
                                        'semester': data.semester})
                            cl_list.append(data.cl_id)
    return res
def tojieci(time):#分离开课节次
    if len(time)==5:
        section1="第"+time[1:3]+"节"
        section2='第'+time[3:5]+'节'
        ans=section1+","+section2
    elif len(time)==7:
        section1="第"+time[1:3]+"节"
        section2='第'+time[3:5]+'节'
        section3= '第' + time[5:7] + '节'
        ans = section1 + "," + section2+","+section3
    elif len(time)==11:
        section1="第"+time[1:3]+"节"
        section2='第'+time[3:5]+'节'
        section3= '第' + time[5:7] + '节'
        section4= '第' + time[7:9] + '节'
        section5 = '第' + time[9:11] + '节'
        ans = section1 + "," + section2+","+section3+","+section4+","+section5
    else:
        ans="第"+time[1:3]+"节"
        for i in range(3,len(time)-1):
            if (i% 2) == 1:
                ans=ans+","+"第"+time[i:i+2]+"节"
    return time[0],ans
###########################################
#学院-班级数
def qianxuesen_bj_college(require):
    d = require.GET
    res=[]
    college_list=['体育部','理学院','化工学院','电子工程与光电技术学院','马克思主义学院','计算机科学与工程学院','钱学森学院','机械工程学院',
                  '材料科学与工程学院','工程训练中心','自动化学院','外国语学院','设计艺术与传媒学院','能源与动力工程学院','教务处','研究生院','艺术与文化素质教育部']
    num_list=[0 for i in range(0,len(college_list))]
    datas = qianxuesen_class.objects.all()
    for data in datas:
            college = data.t_college
            college = college.split(',')
            college = list(set(college))
            for i in college:
                if i in college_list:
                        num_list[college_list.index(i)]+=1;
    for i in range(0,len(college_list)):
        res.append({'key':college_list[i],'number':num_list[i]})
    res.sort(key=lambda x:(x.get('number',0)),reverse=True)
    return HttpResponse(json.dumps(res), content_type="application/json")
#学院-班级详情
def qianxuesen_banji1(request):
    d=request.GET
    datas=qianxuesen_class.objects.filter(t_college=d['college'])
    if len(d['jieci'])==0:
        jieci='全选'
    else:
        jieci=d['jieci']
    if len(d['week'])==0:
        week1='全选'
    else:
        week1=d['week']
    res = dispose1(datas, week1, jieci)
    return HttpResponse(json.dumps(res), content_type="application/json")
#不对cl_id去重
def dispose1(datas,week1,jieci):
    res=[]
    for data in datas:
        if week1 == "全选":
                time1,time2 = tojieci(data.time)
                if jieci == "全选":
                    res.append({'cl_name': data.cl_name, 'cl_id': data.cl_id, 't_name': data.t_name,
                                't_college': data.t_college,
                                'time1': time1, 'time2': time2, 'place': data.place, 'week': data.week, 'sord': data.sord,
                                'semester': data.semester})
                else:
                    if jieci in time2:
                        res.append({'cl_name': data.cl_name, 'cl_id': data.cl_id, 't_name': data.t_name,
                                    't_college': data.t_college,
                                    'time1': time1, 'time2': time2, 'place': data.place, 'week': data.week, 'sord': data.sord,
                                    'semester': data.semester})
        else:
            week = data.week
            week = week.split(',')
            if week1 in week:
                    time1,time2 = tojieci(data.time)
                    if jieci == "全选":
                        res.append({'cl_name': data.cl_name, 'cl_id': data.cl_id, 't_name': data.t_name,
                                    't_college': data.t_college,
                                    'time1': time1,'time2':time2, 'place': data.place, 'week': data.week, 'sord': data.sord,
                                    'semester': data.semester})
                    else:
                        if jieci in time2:
                            res.append({'cl_name': data.cl_name, 'cl_id': data.cl_id, 't_name': data.t_name,
                                        't_college': data.t_college,
                                        'time1': time1, 'time2': time2, 'place': data.place, 'week': data.week, 'sord': data.sord,
                                        'semester': data.semester})
    return res
######################
#班级详情表
def qianxuesen_course(request):
    d=request.GET
    print(d)
    if d['teacher']=='全选':
        teacher=''
    else:
        teacher=d['teacher']
    if d['place']=='全选':
        place=''
    elif d['place']=='I':
        place="I-"
    else:
        place=d['place']
    datas=qianxuesen_class.objects.filter(t_name__contains=teacher, place__istartswith=place)
    if len(d['jieci'])==0:
        jieci='全选'
    else:
        jieci=d['jieci']
    if len(d['week'])==0:
        week1='全选'
    else:
        week1=d['week']
    teacher=d['teacher']
    res=dispose1(datas,week1,jieci)
    return HttpResponse(json.dumps(res), content_type="application/json")
def qianxuesen_Getlist3(request):
    d =request.GET
    print(d)
    datas=qianxuesen_class.objects.values_list('t_name')
    res = []
    teacher_list=[]
    result = Counter(datas).most_common()
    for i in result:
        teacher=i[0][0]
        teacher=list(set(teacher.split(',')))
        for i in teacher:
            i = list(set(i.split('，')))
            if len(i)==1:
             if i not in teacher_list:
                teacher_list.append(i)
             else:
                for j in i:
                    if j not in teacher_list:
                        teacher_list.append(j)
    for i,j in enumerate(teacher_list):
           res.append({'value': i, "key": j, 'suggest': j})
    return HttpResponse(json.dumps(res), content_type="application/json")
def qianxuesen_Getlist4(request):
    d =request.GET
    print(d)
    datas=qianxuesen_class.objects.values_list('place')
    res = []
    place_list=[]
    result = Counter(datas).most_common()
    for i in result:
        teacher=i[0][0]
        teacher=list(set(teacher.split(',')))
        for i in teacher:
            i = list(set(i.split('，')))
            place_list.append(i)
    for i,j in enumerate(place_list):
           res.append({'value': i, "key": j, 'suggest': j})
    return HttpResponse(json.dumps(res), content_type="application/json")


#获取开课列表
def qianxuesen_Getcourse(request):
    d = request.GET
    print(d)

    res = []
    cl_cid=d['cl_cid']
    cl_id=d['cl_id']
    datas=qianxuesen_kebiao.objects.filter(cl_cid=cl_cid,cl_id=cl_id)
    map={
        "01,02,03":"第一大节",
        "01,02":"第一大节",
        "02,03": "第一大节",
        "04,05":"第二大节",
        "06,07":"第三大节",
        "08,09,10":"第四大节",
        "08,09": "第四大节",
        "09,10": "第四大节",
        "11,12,13":"第五大节",
        "11,12": "第五大节",
        "12,13": "第五大节",
        "01,02,03,06,07,08,09,10,11,12,13":"全天",
        "01,02,03,04,05,06,07,08,09,10,11,12,13":"全天",
        "04,05,06,07,08,09,10,11,12,13":"全天",
        "01,02,03,04,05":"上午",
        "01,02,03,04": "上午",
        "02,03,04,05": "上午",
        "02,03,04": "上午",
        "06,07,08,09,10":"下午",
        "04,05,01,02,03":"上午",
        "08,09,10,06,07":"下午",
        "02,03,04,05,06,07,08,09,10,11,12,13": "全天",
        "02,03,06,07,08,09,10,11,12,13": "全天",
        "06,07,08,09":"下午",
        "01,02,03,06,07,08,09,10": "全天",
        "01,02,03,04,05,06,07,08,09,10": "全天",
        "02,03,06,07,08,09,10": "全天",
        "01,02,03,06,07,08,09": "全天",
        "02,03,06,07,08,09": "全天",
    }
    for data in datas:
        cl_school = data.cl_school
        teacher_id = data.teacher_id
        teacher = data.teacher
        teacher_title = data.teacher_title
        teacher_school = data.teacher_school
        cl_credit = data.cl_credit
        classroom = data.classroom
        cl_date=data.cl_date
        jieci_1 = map.get(data.jieci_1)
        jieci_2 = map.get(data.jieci_2)
        jieci_3 = map.get(data.jieci_3)
        jieci_4 = map.get(data.jieci_4)
        jieci_5 = map.get(data.jieci_5)
        jieci_6 = map.get(data.jieci_6)
        jieci_7 = map.get(data.jieci_7)
        # if data.jieci_1!="":
        #     zhouci="周一"+":"+data.jieci_1
        # if data.jieci_2!= "":
        #     if zhouci=="":
        #         zhouci="周二"+":"+data.jieci_2
        #     else:
        #         zhouci=zhouci+"\n"+"周二"+":"+data.jieci_2
        # if data.jieci_3 != "":
        #     if zhouci == "":
        #         zhouci = "周三"+":"+data.jieci_3
        #     else:
        #         zhouci =zhouci+ "\n" + "周三"+":"+data.jieci_3
        # if data.jieci_4 != "":
        #     if zhouci == "":
        #         zhouci = "周四"+":"+data.jieci_4
        #     else:
        #         zhouci =zhouci+ "\n" + "周四"+":"+data.jieci_4
        # if data.jieci_5 != "":
        #     if zhouci == "":
        #         zhouci = "周五"+":"+data.jieci_5
        #     else:
        #         zhouci =zhouci+ "\n" + "周五"+":"+data.jieci_5
        # if data.jieci_6 != "":
        #     if zhouci == "":
        #         zhouci = "周六"+":"+data.jieci_6
        #     else:
        #         zhouci = zhouci+"\n" + "周六"+":"+data.jieci_6
        # if data.jieci_7 != "":
        #     if zhouci == "":
        #         zhouci = "周日"+":"+data.jieci_7
        #     else:
        #         zhouci = zhouci+"\n" + "周日"+":"+data.jieci_7
        zhouci = ""
        if data.jieci_1!="":
            zhouci="周一"+":"+jieci_1
        if data.jieci_2!= "":
            if zhouci=="":
                zhouci="周二"+":"+jieci_2
            else:
                zhouci=zhouci+"\n"+"周二"+":"+jieci_2
        if data.jieci_3 != "":
            if zhouci == "":
                zhouci = "周三"+":"+jieci_3
            else:
                zhouci =zhouci+ "\n" + "周三"+":"+jieci_3
        if data.jieci_4 != "":
            if zhouci == "":
                zhouci = "周四"+":"+jieci_4
            else:
                zhouci =zhouci+ "\n" + "周四"+":"+jieci_4
        if data.jieci_5 != "":
            if zhouci == "":
                zhouci = "周五"+":"+jieci_5
            else:
                zhouci =zhouci+ "\n" + "周五"+":"+jieci_5
        if data.jieci_6 != "":
            if zhouci == "":
                zhouci = "周六"+":"+jieci_6
            else:
                zhouci = zhouci+"\n" + "周六"+":"+jieci_6
        if data.jieci_7 != "":
            if zhouci == "":
                zhouci = "周日"+":"+jieci_7
            else:
                zhouci = zhouci+"\n" + "周日"+":"+jieci_7


        res.append({"cl_school": cl_school, "teacher_id": teacher_id, "teacher": teacher, "teacher_title": teacher_title, "teacher_school": teacher_school,
                    "cl_credit": cl_credit, "classroom": classroom,"cl_date":cl_date,"zhouci":zhouci})

        # sorted(res, key=lambda keys: keys['cl_name'])
    res = sorted(res, key=lambda x: x["zhouci"])

    return HttpResponse(json.dumps(res), content_type="application/json")


#获取课序列表
def qianxuesen_Getclid(request):
    d =request.GET
    print(d)
    datas=qianxuesen_xuanke.objects.values_list('cl_id')
    res = []
    teacher_list=[]
    result = Counter(datas).most_common()
    for i in result:
        teacher=i[0][0]
        teacher=list(set(teacher.split(',')))
        for i in teacher:
            i = list(set(i.split('，')))
            if len(i)==1:
             if i not in teacher_list:
                teacher_list.append(i)
             else:
                for j in i:
                    if j not in teacher_list:
                        teacher_list.append(j)
    for i,j in enumerate(teacher_list):
           res.append({'value': i, "key": j, 'suggest': j})
    return HttpResponse(json.dumps(res), content_type="application/json")

#选课详情表
def qianxuesen_allcourse(request):
    d=request.GET
    print(d)

    # datas = qianxuesen_xuanke.objects.values_list('cl_name',"cl_cid","teacher","cl_id","cl_credit")
    # result = Counter(datas).most_common()
    res = []

    # db=qianxuesen_chake()
    #
    # for i in result:
    #     cl_name = i[0][0]
    #     cl_cid=i[0][1]
    #     teacher = i[0][2]
    #     cl_id = i[0][3]
    #     cl_credit = i[0][4]
    #     num=i[1]
    #     qdatas=qianxuesen_qianxuesen.objects.filter(cl_cid=cl_cid).filter(cl_name=cl_name).filter(cl_id=cl_id)
    #     qian_num=qdatas.count()
    #     db.cl_name=cl_name
    #     db.cl_cid=cl_cid
    #     db.teacher=teacher
    #     db.cl_id=cl_id
    #     db.cl_credit=cl_credit
    #     db.total_number=num
    #     db.qian_number=qian_num
    #     db.save()
    q = d.get('q')
    totalnum=d.get('totalnum')
    qiannum=d.get('qiannum')
    print(q)
    print(d.get('totalnum'))
    if d.get('totalnum')=="0~50":
        left=0
        right=50
    elif d.get('totalnum')=="50~100":
        left=49
        right=100
    elif d.get('totalnum') == "100~200":
        left = 99
        right = 200
    elif d.get('totalnum') == "200~":
        left = 199
        right = 1000
    elif d.get('totalnum')=="全选":
        left=0
        right=1000
    else:
        left=0
        right=1000

    if d.get('qiannum')=="0~30":
        qleft=0
        qright=30
    elif d.get('qiannum')=="30~50":
        qleft=29
        qright=50
    elif d.get('qiannum') == "50~80":
        qleft = 49
        qright = 80
    elif d.get('qiannum') == "80~":
        qleft = 79
        qright = 500
    elif d.get('qiannum')=="全选":
        qleft=0
        qright=500
    else:
        qleft=0
        qright=500
    # datas = qianxuesen_chake.objects.filter(Q(cl_name__icontains=q) | Q(teacher__icontains=q)).filter(
    #     total_number__gt=left).filter(total_number__lt=right)
    if not q :
        # datas=qianxuesen_chake.objects.all()
        if not totalnum and not qiannum:
            datas = qianxuesen_chake.objects.all()
        else:
            datas = qianxuesen_chake.objects.filter(total_number__gt=left).filter(total_number__lt=right).filter(qian_number__gt=qleft).filter(qian_number__lt=qright)
    else:
        if not totalnum and not qiannum:
            datas = qianxuesen_chake.objects.filter(Q(cl_name__icontains=q) | Q(teacher__icontains=q))
        else:
            datas = qianxuesen_chake.objects.filter(Q(cl_name__icontains=q) | Q(teacher__icontains=q)).filter(total_number__gt=left).filter(total_number__lt=right).filter(qian_number__gt=qleft).filter(qian_number__lt=qright)
    for data in datas:
        cl_name=data.cl_name
        cl_cid=data.cl_cid
        teacher=data.teacher
        cl_id=data.cl_id
        cl_credit=data.cl_credit
        cl_credit=str(cl_credit)
        num=data.total_number
        qian_num=data.qian_number
        num=tostr(num)
        qian_num=tostr(qian_num)

        res.append({"cl_name":cl_name, "cl_cid": cl_cid, "teacher": teacher, "cl_id": cl_id, "cl_credit": cl_credit,
                    "total_number": num,"qian_number":qian_num})

        #sorted(res, key=lambda keys: keys['cl_name'])
    res=sorted(res,key=lambda x:x["cl_name"])


    return HttpResponse(json.dumps(res), content_type="application/json")

def tostr(num):
    if num<10:
        return '0'+'0'+str(num)
    elif num<100:
        return '0'+str(num)
    else:
        return str(num)

def qianxuesen_Getallst(request):
    d=request.GET
    print(d)
    cl_cid=d['cl_cid']
    cl_id=d['cl_id']
    res=[]
    datas=qianxuesen_xuanke.objects.filter(cl_cid__contains=cl_cid).filter(cl_id__contains=cl_id)
    for data in datas:
        res.append({"st_name":data.st_name,"st_id":data.st_id,"st_school":data.st_school,"st_class":data.st_class})
    # res.append({"st_name": "a", "st_id": "a", "st_school":"a", "st_class": "a"})
    return HttpResponse(json.dumps(res), content_type="application/json")

def qianxuesen_Getqianst(request):
    d=request.GET
    cl_cid=d['cl_cid']
    cl_id=d['cl_id']
    res=[]
    datas=qianxuesen_qianxuesen.objects.filter(cl_cid__contains=cl_cid).filter(cl_id__contains=cl_id)

    for data in datas:
        infos=qianxuesen_qianxuesenst.objects.filter(st_id__icontains=data.st_id)
        for info in infos:
            st_major=info.st_major
            major_2=info.major_2
            st_grade=info.st_grade
        res.append({"st_name":data.st_name,"st_id":data.st_id,"st_school":data.st_school,"st_class":data.st_class,"st_major":st_major,"major_2":major_2,"st_grade":st_grade})
    res=sorted(res,key=lambda x:x['st_grade'])
    return HttpResponse(json.dumps(res), content_type="application/json")


#2021培养方案------学生选课详情
def qianxuesen_xuanke(request):
    d=request.GET
    q=d.get('q')
    p=d.get('totalnum')
#     if p =="小于15":
#         right=15
#     else:
#         right=200
#     res=[]
#     if not q:
#         if not p:
#             datass=qianxuesen_qianxuesenst.objects.all()
#         else:
#             datass = qianxuesen_qianxuesenst.objects.filter(total_credit__lt=right)
#     else:
#         if not p:
#             datass = qianxuesen_qianxuesenst.objects.filter(st_name__icontains=q)
#         else:
#             datass = qianxuesen_qianxuesenst.objects.filter(total_credit__lt=right).filter(st_name__icontains=q)
# #---------------------------------------------------------------------------------------------
#     db=qianxuesen_wxordx()
#     for st in datass:
#         num_wx = 0
#         num_dx = 0
#         yx = []
#         sx = []
#         wx = []
#         # 选课
#         datas = qianxuesen_qianxuesen.objects.filter(st_id__icontains=st.st_id)
#         # 方案
#         infos = qianxuesen_project19.objects.filter(st_id__icontains=st.st_id).filter(schoolyear="2021-2022-1")
#         for data in infos:
#             yx.append({"courseid": data.cl_cid, "coursename": data.cl_name})
#         for data in datas:
#             if data.cl_cid == "21120102":
#                 sx.append({"courseid": "21120101", "coursename": data.cl_name})
#             elif data.cl_cid == "21320102":
#                 sx.append({"courseid": "21320101", "coursename": data.cl_name})
#             else:
#                 sx.append({"courseid": data.cl_cid, "coursename": data.cl_name})
#         for i in yx:
#             if i not in sx:
#                 wx.append({"courseid": i.get("courseid"), "coursename": i.get("coursename"), "beizhu": "未选"})
#                 num_wx = num_wx + 1
#         num_wx=str(num_wx)
#         for i in sx:
#             if i not in yx:
#                 wx.append({"courseid": i.get("courseid"), "coursename": i.get("coursename"), "beizhu": "多选"})
#                 num_dx = num_dx + 1
#         num_dx=str(num_dx)
#
#         # st_id=i[0][0]
#         # st_name = i[0][1]
#         # st_class = i[0][2]
#         # st_school = i[0][3]
#         # infos=qianxuesen_qianxuesen.objects.filter(st_id__icontains=st_id,st_name__icontains=st_name)
#         # num=0
#         # for info in infos:
#         #     num+=info.cl_credit
#         # total_credit=num
#         st_id = st.st_id
#         st_name = st.st_name
#         st_class = st.st_class
#         st_school = st.st_school
#         st_major = st.st_major
#         major_2 = st.major_2
#         st_grade = st.st_grade
#         total_credit=st.total_credit
#         db.st_id=st_id
#         db.st_name=st_name
#         db.num_wx=num_wx
#         db.num_dx=num_dx
#         db.st_class=st_class
#         db.st_school=st_school
#         db.st_major=st_major
#         db.total_credit=total_credit
#         db.major_2=major_2
#         db.st_grade=st_grade
#         db.save()
#
#         # db.st_id=st_id
#         # db.st_name=st_name
#         # db.st_class=st_class
#         # db.st_school=st_school
#         # db.total_credit=total_credit
#         # db.save()

#---------------------------------------------------------------------------------------------

    if p =="小于15":
        right=15
    else:
        right=200
    res=[]
    if not q:
        if not p:
            datas=qianxuesen_wxordx.objects.all()
        else:
            datas = qianxuesen_wxordx.objects.filter(total_credit__lt=right)
    else:
        if not p:
            datas = qianxuesen_wxordx.objects.filter(st_name__icontains=q)
        else:
            datas = qianxuesen_wxordx.objects.filter(total_credit__lt=right).filter(st_name__icontains=q)
    for data in datas:
        # st_id=i[0][0]
        # st_name = i[0][1]
        # st_class = i[0][2]
        # st_school = i[0][3]
        # infos=qianxuesen_qianxuesen.objects.filter(st_id__icontains=st_id,st_name__icontains=st_name)
        # num=0
        # for info in infos:
        #     num+=info.cl_credit
        # total_credit=num
        st_id=data.st_id
        st_name=data.st_name
        st_class=data.st_class
        st_school=data.st_school
        st_major=data.st_major
        major_2=data.major_2
        st_grade=data.st_grade
        total_credit=tostr1(data.total_credit)
        num_wx=tostr1(data.num_wx)
        num_dx=tostr1(data.num_dx)

        # db.st_id=st_id
        # db.st_name=st_name
        # db.st_class=st_class
        # db.st_school=st_school
        # db.total_credit=total_credit
        # db.save()
        # print(i[0][0])
        # print(i[0][1])
        # print(i[1])
        res.append({"st_name":st_name,"st_id":st_id,"st_school":st_school,"st_class":st_class,"total_credit":total_credit,"st_major":st_major,"major_2":major_2,"st_grade":st_grade,"year":"2021-2022-1","num_wx":num_wx,"num_dx":num_dx})
    res=sorted(res,key=lambda x:x['num_wx'],reverse=True)
    return HttpResponse(json.dumps(res), content_type="application/json")
    # return HttpResponse("hello bug")

#两位字符转换函数
def tostr1(a):
    if a<10:
        return '0'+str(a)
    if a>=10 and a<=100:
        return str(a)

#2021培养方案------学生选课详情------查看选课情况
def qianxuesen_Getxuanke(request):
    d=request.GET
    print(d)
    st_id=d['st_id']
    st_name=d['st_name']
    res=[]
    datas=qianxuesen_qianxuesen.objects.filter(st_id__icontains=st_id).filter(st_name__icontains=st_name)
    for data in datas:
        res.append({"cl_name":data.cl_name,"cl_cid":data.cl_cid,"cl_id":data.cl_id,"cl_credit":data.cl_credit})
    # res.append({"st_name": "a", "st_id": "a", "st_school":"a", "st_class": "a"})
    return HttpResponse(json.dumps(res), content_type="application/json")

#19级培养方案导入
#获取19级学生
def qianxuesen_Getstudent19(request):
    d = request.GET
    q = d.get('q')

    res = []
    if not q:
        datas = qianxuesen_project19.objects.values_list('st_id', "st_name",  "st_school", "st_major", "st_grade")
        result = Counter(datas).most_common()
    else:
        datas = qianxuesen_project19.objects.filter(Q(st_name__icontains=q) | Q(st_id__icontains=q)).values_list(
            'st_id', "st_name",  "st_school", "st_major", "st_grade")
        result = Counter(datas).most_common()
    for i in result:
        st_id = i[0][0]
        st_name = i[0][1]
        st_school = i[0][2]
        st_major = i[0][3]
        st_grade = i[0][4]
        # print(i[0][0])
        # print(i[0][1])
        # print(i[1])
        # for data in datas:
        res.append({"st_name": st_name, "st_id": st_id, "st_school": st_school, "st_major": st_major,"st_grade":st_grade})
    res=sorted(res,key=lambda x:x['st_id'])
    return HttpResponse(json.dumps(res), content_type="application/json")
    # return HttpResponse("hello bug")

#培养方案详情---查看学生培养方案
def qianxuesen_Getproject19(request):
    d = request.GET
    q = d.get('q')
    print(d)
    st_id = d['st_id']
    st_name = d['st_name']
    res = []
    if not q:
        datas = qianxuesen_project19.objects.filter(st_id__icontains=st_id).filter(st_name__icontains=st_name)
    else:
        datas = qianxuesen_project19.objects.filter(st_id__icontains=st_id).filter(st_name__icontains=st_name).filter(schoolyear__icontains=q)
        # res.append({"st_name": "a", "st_id": "a", "st_school":"a", "st_class": "a"})
    total=0
    for data in datas:
        total+=data.cl_credit
        res.append(
            {"cl_name": data.cl_name, "cl_credit": data.cl_credit, "cl_type": data.cl_type, "cl_cid": data.cl_cid,
             "cl_attribute": data.cl_attribute, "cl_school": data.cl_school, "cl_lanuage": data.cl_lanuage,
             "schoolyear": data.schoolyear})

    res=sorted(res,key= lambda x:x["schoolyear"])
    return HttpResponse(json.dumps(res), content_type="application/json")


def qianxuesen_compare(request):
    d=request.GET
    st_id=d['st_id']
    st_name=d['st_name']
    yx=[]
    sx=[]
    wx=[]
    #选课
    datas=qianxuesen_qianxuesen.objects.filter(st_id__icontains=st_id)
    #方案
    infos=qianxuesen_project19.objects.filter(st_id__icontains=st_id).filter(schoolyear="2021-2022-1")


    for data in infos:
        yx.append({"courseid":data.cl_cid,"coursename":data.cl_name})
    for data in datas:
        if data.cl_cid=="21120102":
            sx.append({"courseid":"21120101","coursename":data.cl_name})
        elif data.cl_cid=="21320102":
            sx.append({"courseid": "21320101", "coursename": data.cl_name})
        else:
            sx.append({"courseid":data.cl_cid,"coursename":data.cl_name})
    for i in yx:
        if i not in sx:
            wx.append({"courseid":i.get("courseid"),"coursename":i.get("coursename"),"beizhu":"未选"})
    for i in sx:
        if i not in yx:
            wx.append({"courseid": i.get("courseid"), "coursename": i.get("coursename"), "beizhu": "多选"})
    return HttpResponse(json.dumps(wx), content_type="application/json")
    #---------------------------------------------------------------------------------------------------------------
    # d = request.GET
    # yx = []
    # sx = []
    # wx = []
    # students=qianxuesen_qianxuesenst.objects.all()
    # for st in students:
    #     num_wx = 0
    #     num_dx = 0
    #     # 选课
    #     datas = qianxuesen_qianxuesen.objects.filter(st_id__icontains=st.st_id)
    #     # 方案
    #     infos = qianxuesen_project19.objects.filter(st_id__icontains=st.st_id).filter(schoolyear="2021-2022-1")
    #     for data in infos:
    #         yx.append({"courseid": data.cl_cid, "coursename": data.cl_name})
    #     for data in datas:
    #         if data.cl_cid == "21120102":
    #             sx.append({"courseid": "21120101", "coursename": data.cl_name})
    #         elif data.cl_cid == "21320102":
    #             sx.append({"courseid": "21320101", "coursename": data.cl_name})
    #         else:
    #             sx.append({"courseid": data.cl_cid, "coursename": data.cl_name})
    #     for i in yx:
    #         if i not in sx:
    #             wx.append({"courseid": i.get("courseid"), "coursename": i.get("coursename"), "beizhu": "未选"})
    #             num_wx=num_wx+1
    #     for i in sx:
    #         if i not in yx:
    #             wx.append({"courseid": i.get("courseid"), "coursename": i.get("coursename"), "beizhu": "多选"})
    #             num_dx = num_dx + 1
    # return HttpResponse("hello bug")
    # --------------------------------------------------------------------------------------------------------------
    # datas=qianxuesen_qianxuesen.objects.filter(st_class="9200007100").values_list("st_id","st_name","st_school")
    # result=Counter(datas).most_common()
    # db = qianxuesen_fangxiang20()
    # for data in result:
    #     db.st_id=data[0][0]
    #     db.st_name=data[0][1]
    #     db.st_school=data[0][2]
    #     db.st_major="机械工程类"
    #     db.major_2="机械"
    #     db.st_grade="2020"
    #     db.st_class="9200007100"
    #     db.save()
    # return HttpResponse("hello bug")
    # ------------------------------------------------------------------------------------------------------------
    # datas=qianxuesen_fangxiang19.objects.all()
    # db=qianxuesen_project19_copy()
    # for data in datas:
    #     db.st_id=data.st_id
    #     db.st_name=data.st_name
    #     db.st_school=data.st_school
    #     db.st_major=data.st_major
    #     db.major_2=data.major_2
    #     db.st_class=data.st_class
    #     db.st_grade=data.st_grade
    #     infos=qianxuesen_project19.objects.filter(st_id__icontains=data.st_id)
    #     for info in infos:
    #         db.schoolyear=info.schoolyear
    #         db.cl_cid=info.cl_cid
    #         db.cl_name=info.cl_name
    #         db.cl_credit=info.cl_credit
    #         db.cl_type=info.cl_type
    #         db.cl_attribute=info.cl_attribute
    #         db.cl_school=info.cl_school
    #         db.cl_lanuage=info.cl_lanuage
    #         db.save()
    # return HttpResponse("hello bug")
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    # 机械-------------------------------------------------------------------------------------------------------------
    # datas=qianxuesen_fangxiang19.objects.filter(st_class="9190007100")
    # infos=qianxuesen_0071.objects.all()
    # db=qianxuesen_project19_copy()
    # for data in datas:
    #     db.st_id=data.st_id
    #     db.st_name=data.st_name
    #     db.st_school=data.st_school
    #     db.st_major=data.st_major
    #     db.major_2=data.major_2
    #     db.st_class=data.st_class
    #     db.st_grade=data.st_grade
    #     for info in infos:
    #         db.schoolyear=info.schoolyear
    #         db.cl_cid=info.cl_cid
    #         db.cl_name=info.cl_name
    #         db.cl_credit=info.cl_credit
    #         db.cl_type=info.cl_type
    #         db.cl_attribute=info.cl_attribute
    #         db.cl_school=info.cl_school
    #         db.cl_lanuage=info.cl_lanuage
    #         db.save()
    # return HttpResponse("hello bug")
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
 # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    # 电子-------------------------------------------------------------------------------------------------------------
    # datas=qianxuesen_fangxiang19.objects.filter(st_major="电气信息类").filter(major_2="方向一(电子类)")
    # infos=qianxuesen_007201.objects.all()
    # db=qianxuesen_project19_copy()
    # for data in datas:
    #     db.st_id=data.st_id
    #     db.st_name=data.st_name
    #     db.st_school=data.st_school
    #     db.st_major=data.st_major
    #     db.major_2=data.major_2
    #     db.st_class=data.st_class
    #     db.st_grade=data.st_grade
    #     for info in infos:
    #         db.schoolyear=info.schoolyear
    #         db.cl_cid=info.cl_cid
    #         db.cl_name=info.cl_name
    #         db.cl_credit=info.cl_credit
    #         db.cl_type=info.cl_type
    #         db.cl_attribute=info.cl_attribute
    #         db.cl_school=info.cl_school
    #         db.cl_lanuage=info.cl_lanuage
    #         db.save()
    # return HttpResponse("hello bug")
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    # 计算机-------------------------------------------------------------------------------------------------------------
    # datas=qianxuesen_fangxiang19.objects.filter(st_major="电气信息类").filter(major_2="方向二(计算机类)")
    # infos=qianxuesen_007202.objects.all()
    # db=qianxuesen_project19_copy()
    # for data in datas:
    #     db.st_id=data.st_id
    #     db.st_name=data.st_name
    #     db.st_school=data.st_school
    #     db.st_major=data.st_major
    #     db.major_2=data.major_2
    #     db.st_class=data.st_class
    #     db.st_grade=data.st_grade
    #     for info in infos:
    #         db.schoolyear=info.schoolyear
    #         db.cl_cid=info.cl_cid
    #         db.cl_name=info.cl_name
    #         db.cl_credit=info.cl_credit
    #         db.cl_type=info.cl_type
    #         db.cl_attribute=info.cl_attribute
    #         db.cl_school=info.cl_school
    #         db.cl_lanuage=info.cl_lanuage
    #         db.save()
    # return HttpResponse("hello bug")
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    # 化工-------------------------------------------------------------------------------------------------------------
    # datas=qianxuesen_fangxiang19.objects.filter(st_major="材料化工类").filter(major_2="方向一（化工）")
    # infos=qianxuesen_007301.objects.all()
    # db=qianxuesen_project19_copy()
    # for data in datas:
    #     db.st_id=data.st_id
    #     db.st_name=data.st_name
    #     db.st_school=data.st_school
    #     db.st_major=data.st_major
    #     db.major_2=data.major_2
    #     db.st_class=data.st_class
    #     db.st_grade=data.st_grade
    #     for info in infos:
    #         db.schoolyear=info.schoolyear
    #         db.cl_cid=info.cl_cid
    #         db.cl_name=info.cl_name
    #         db.cl_credit=info.cl_credit
    #         db.cl_type=info.cl_type
    #         db.cl_attribute=info.cl_attribute
    #         db.cl_school=info.cl_school
    #         db.cl_lanuage=info.cl_lanuage
    #         db.save()
    # return HttpResponse("hello bug")
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
# 21级-------------------------------------------------------------------------------------------------------------
#     datas=qianxuesen_qianxuesen.objects.filter(st_class__icontains="92100073").values_list("st_id","st_name","st_school","st_class")
#     result=Counter(datas).most_common()
#     db=qianxuesen_project19_copy()
#     for data in result:
#         db.st_id=data[0][0]
#         db.st_name=data[0][1]
#         db.st_school=data[0][2]
#         db.st_major="材料化工类"
#         db.major_2="未分"
#         db.st_class=data[0][3]
#         db.st_grade="2021"
#         db.schoolyear = "2021-2022-1"
#         db.cl_cid="36100002"
#         db.cl_name="形势与政策（Ⅰ）"
#         db.cl_credit=0.3
#         db.cl_type=""
#         db.cl_attribute="必修"
#         db.cl_school=""
#         db.cl_lanuage="中文"
#         db.save()
#
#     for data in result:
#         db.st_id=data[0][0]
#         db.st_name=data[0][1]
#         db.st_school=data[0][2]
#         db.st_major="材料化工类"
#         db.major_2="未分"
#         db.st_class=data[0][3]
#         db.st_grade="2021"
#         db.schoolyear = "2021-2022-2"
#         db.cl_cid="36200002"
#         db.cl_name="形势与政策（Ⅱ）"
#         db.cl_credit=0.2
#         db.cl_type=""
#         db.cl_attribute="必修"
#         db.cl_school=""
#         db.cl_lanuage="中文"
#         db.save()
#     return HttpResponse("hello bug")
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
# 19机械  形势与政策-------------------------------------------------------------------------------------------------------------
#     datas=qianxuesen_fangxiang19.objects.filter(st_class__icontains="919000")
#     db=qianxuesen_project19_copy()
#     for data in datas:
#         db.st_id=data.st_id
#         db.st_name=data.st_name
#         db.st_school=data.st_school
#         db.st_major=data.st_major
#         db.major_2=data.major_2
#         db.st_class=data.st_class
#         db.st_grade=data.st_grade
#         db.schoolyear="2021-2022-1"
#         db.cl_cid="17021001"
#         db.cl_name="系统工程"
#         db.cl_credit=2
#         db.cl_type="通识教育课"
#         db.cl_attribute="选修"
#         db.cl_school="钱学森学院"
#         db.cl_lanuage="中文"
#         db.save()
#     return HttpResponse("hello bug")
#     for data in datas:
#         db.st_id=data.st_id
#         db.st_name=data.st_name
#         db.st_school=data.st_school
#         db.st_major=data.st_major
#         db.major_2=data.major_2
#         db.st_class=data.st_class
#         db.st_grade=data.st_grade
#         db.schoolyear="2020-2021-2"
#         db.cl_cid="36200002"
#         db.cl_name="形势与政策（Ⅱ）"
#         db.cl_credit=0.2
#         db.cl_type=""
#         db.cl_attribute="必修"
#         db.cl_school=""
#         db.cl_lanuage="中文"
#         db.save()
#
#     for data in datas:
#         db.st_id=data.st_id
#         db.st_name=data.st_name
#         db.st_school=data.st_school
#         db.st_major=data.st_major
#         db.major_2=data.major_2
#         db.st_class=data.st_class
#         db.st_grade=data.st_grade
#         db.schoolyear="2021-2022-1"
#         db.cl_cid="36300002"
#         db.cl_name="形势与政策（Ⅲ）"
#         db.cl_credit=0.3
#         db.cl_type=""
#         db.cl_attribute="必修"
#         db.cl_school=""
#         db.cl_lanuage="中文"
#         db.save()
#
#     for data in datas:
#         db.st_id=data.st_id
#         db.st_name=data.st_name
#         db.st_school=data.st_school
#         db.st_major=data.st_major
#         db.major_2=data.major_2
#         db.st_class=data.st_class
#         db.st_grade=data.st_grade
#         db.schoolyear="2021-2022-2"
#         db.cl_cid="36400002"
#         db.cl_name="形势与政策（Ⅳ）"
#         db.cl_credit=0.2
#         db.cl_type=""
#         db.cl_attribute="必修"
#         db.cl_school=""
#         db.cl_lanuage="中文"
#         db.save()

    # for data in datas:
    #     db.st_id=data.st_id
    #     db.st_name=data.st_name
    #     db.st_school=data.st_school
    #     db.st_major=data.st_major
    #     db.major_2=data.major_2
    #     db.st_class=data.st_class
    #     db.st_grade=data.st_grade
    #     db.schoolyear="2021-2022-1"
    #     db.cl_cid="36500002"
    #     db.cl_name="形势与政策（Ⅴ）"
    #     db.cl_credit=0.2
    #     db.cl_type=""
    #     db.cl_attribute="必修"
    #     db.cl_school=""
    #     db.cl_lanuage="中文"
    #     db.save()
    #
    # for data in datas:
    #     db.st_id=data.st_id
    #     db.st_name=data.st_name
    #     db.st_school=data.st_school
    #     db.st_major=data.st_major
    #     db.major_2=data.major_2
    #     db.st_class=data.st_class
    #     db.st_grade=data.st_grade
    #     db.schoolyear="2021-2022-2"
    #     db.cl_cid="36600002"
    #     db.cl_name="形势与政策（Ⅵ）"
    #     db.cl_credit=0.3
    #     db.cl_type=""
    #     db.cl_attribute="必修"
    #     db.cl_school=""
    #     db.cl_lanuage="中文"
    #     db.save()
    #
    # for data in datas:
    #     db.st_id=data.st_id
    #     db.st_name=data.st_name
    #     db.st_school=data.st_school
    #     db.st_major=data.st_major
    #     db.major_2=data.major_2
    #     db.st_class=data.st_class
    #     db.st_grade=data.st_grade
    #     db.schoolyear="2022-2023-1"
    #     db.cl_cid="36700002"
    #     db.cl_name="形势与政策（Ⅶ）"
    #     db.cl_credit=0.3
    #     db.cl_type=""
    #     db.cl_attribute="必修"
    #     db.cl_school=""
    #     db.cl_lanuage="中文"
    #     db.save()
    #
    # for data in datas:
    #     db.st_id=data.st_id
    #     db.st_name=data.st_name
    #     db.st_school=data.st_school
    #     db.st_major=data.st_major
    #     db.major_2=data.major_2
    #     db.st_class=data.st_class
    #     db.st_grade=data.st_grade
    #     db.schoolyear="2022-2023-2"
    #     db.cl_cid="36800002"
    #     db.cl_name="形势与政策（Ⅷ）"
    #     db.cl_credit=0.2
    #     db.cl_type=""
    #     db.cl_attribute="必修"
    #     db.cl_school=""
    #     db.cl_lanuage="中文"
    #     db.save()
    # return HttpResponse("hello bug")
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
#2021-2022春秋学期，钱学森院开课统计
#学院—开棵数  ：collgeg->t_college->banji
def qianxuesen_college1(request):
    # datas=qianxuesen_chake.objects.filter(qian_number__gt=0)
    # db=qianxuesen_class1()
    # for data in datas:
    #     db.cl_cid=data.cl_cid
    #     db.cl_name=data.cl_name
    #     db.cl_id=data.cl_id
    #
    #     db.number=data.qian_number
    #     infos=qianxuesen_kebiao.objects.filter(cl_cid=data.cl_cid).filter(cl_id=data.cl_id)
    #     for info in infos:
    #         # db.cl_cid=data.cl_cid
    #         # db.cl_name=data.cl_name
    #         # db.cl_id=data.cl_id
    #         # db.t_name=data.teacher
    #         # db.number=data.qian_number
    #         db.t_name = info.teacher
    #         db.t_college=info.cl_school
    #         db.cl_date=info.cl_date
    #         db.classroom=info.classroom
    #         db.t_title=info.teacher_title
    #         db.cl_credit=info.cl_credit
    #         db.jieci_1=info.jieci_1
    #         db.jieci_2=info.jieci_2
    #         db.jieci_3=info.jieci_3
    #         db.jieci_4=info.jieci_4
    #         db.jieci_5=info.jieci_5
    #         db.jieci_6=info.jieci_6
    #         db.jieci_7=info.jieci_7
    #         db.save()
    # return HttpResponse("hello bug")
    d = request.GET
    res=[]
    college_list=['机械','环生','化工','电光','计算机','经管','能动',
                  '自动化','理学院','外院','公物','材料','钱学森','马院','学生工作处',
                '体育部','工程训练中心','艺文部','知产']
    num_list=[0 for i in range(0,len(college_list))]
    datas = qianxuesen_class1.objects.all()
    cl_list=[[]for i in range(0,len(college_list))]
    for data in datas:
            college = data.t_college
            college = college.split(',')
            college = list(set(college))
            cl_cid=data.cl_cid
            for i in college:
                if i in college_list:
                    if cl_cid not in cl_list[college_list.index(i)]:
                        num_list[college_list.index(i)]+=1;
                        cl_list[college_list.index(i)].append(cl_cid)
    for i in range(0,len(college_list)):
        res.append({'key':college_list[i],'number':num_list[i]})
    res.sort(key=lambda x:(x.get('number',0)),reverse=True)
    return HttpResponse(json.dumps(res), content_type="application/json")


#学院—开课详情
def qianxuesen_t_college1(request):
   d = request.GET
   college=d['college']
   res=[]
   datas=qianxuesen_class1.objects.filter(t_college=college).values_list('cl_cid','cl_name','t_college')
   result=Counter(datas).most_common()
   for i in result:
       cl_cid=i[0][0]
       cl_name=i[0][1]
       t_college=i[0][2]
       res.append({"cl_name":cl_name,"cl_cid":cl_cid,"t_college":t_college})
   res=sorted(res,key=lambda x:x['cl_name'])
   return HttpResponse(json.dumps(res), content_type="application/json")

def qianxuesen_bj_college1(require):
    d = require.GET
    res=[]
    college_list=['机械','环生','化工','电光','计算机','经管','能动',
                  '自动化','理学院','外院','公物','材料','钱学森','马院','学生工作处',
                '体育部','工程训练中心','艺文部','知产']
    num_list=[0 for i in range(0,len(college_list))]
    datas = qianxuesen_class1.objects.all()
    for data in datas:
            college = data.t_college
            college = college.split(',')
            college = list(set(college))
            for i in college:
                if i in college_list:
                        num_list[college_list.index(i)]+=1;
    for i in range(0,len(college_list)):
        res.append({'key':college_list[i],'number':num_list[i]})
    res.sort(key=lambda x:(x.get('number',0)),reverse=True)
    return HttpResponse(json.dumps(res), content_type="application/json")

def qianxuesen_banji2(request):
    d=request.GET
    t_college=d['college']
    week=d.get('week')
    jieci=d.get('jieci')
    res=[]
    if not week and not jieci:
        datas = qianxuesen_class1.objects.filter(t_college=t_college)
    elif not week:
        if jieci=="全选":
            datas = qianxuesen_class1.objects.filter(t_college=t_college)
        else:
            datas = qianxuesen_class1.objects.filter(t_college=t_college).filter(
                Q(jieci_1__icontains=jieci) | Q(jieci_2__icontains=jieci) | Q(jieci_3__icontains=jieci) |
                Q(jieci_4__icontains=jieci) | Q(jieci_5__icontains=jieci) |
                Q(jieci_6__icontains=jieci) | Q(jieci_7__icontains=jieci))
    elif not jieci:
        if week=="全选":
            datas = qianxuesen_class1.objects.filter(t_college=t_college)
        else:
              datas=qianxuesen_class1.objects.filter(t_college=t_college).filter(cl_date__icontains=week)
    elif week=="全选" and jieci=="全选":
        datas = qianxuesen_class1.objects.filter(t_college=t_college)
    else:
        datas = qianxuesen_class1.objects.filter(t_college=t_college).filter(cl_date__icontains=week).filter(Q(jieci_1__icontains=jieci)|Q(jieci_2__icontains=jieci)|Q(jieci_3__icontains=jieci)|
                                               Q(jieci_4__icontains=jieci)|Q(jieci_5__icontains=jieci)|
                                               Q(jieci_6__icontains=jieci)|Q(jieci_7__icontains=jieci))

    map={
        "01,02,03":"第一大节",
        "01,02":"第一大节",
        "02,03": "第一大节",
        "04,05":"第二大节",
        "06,07":"第三大节",
        "08,09,10":"第四大节",
        "08,09": "第四大节",
        "09,10": "第四大节",
        "11,12,13":"第五大节",
        "11,12": "第五大节",
        "12,13": "第五大节",
        "01,02,03,06,07,08,09,10,11,12,13":"全天",
        "01,02,03,04,05,06,07,08,09,10,11,12,13":"全天",
        "04,05,06,07,08,09,10,11,12,13":"全天",
        "01,02,03,04,05":"上午",
        "01,02,03,04": "上午",
        "02,03,04,05": "上午",
        "02,03,04": "上午",
        "06,07,08,09,10":"下午",
        "04,05,01,02,03":"上午",
        "08,09,10,06,07":"下午",
        "02,03,04,05,06,07,08,09,10,11,12,13": "全天",
        "02,03,06,07,08,09,10,11,12,13": "全天",
        "06,07,08,09":"下午",
        "06,07,": "第三大节",
        "01,02,03,06,07,08,09,10": "全天",
        "01,02,03,04,05,06,07,08,09,10": "全天",
        "02,03,06,07,08,09,10": "全天",
        "01,02,03,06,07,08,09": "全天",
        "02,03,06,07,08,09": "全天",
        "04,05,06,07":"二三大节",
        "06,07,  ": "第三大节",
        "14,  ": "14",
    }
    for data in datas:
        cl_name=data.cl_name
        cl_cid=data.cl_cid
        cl_id=data.cl_id
        cl_school = data.t_college
        cl_credit=data.cl_credit
        t_title=data.t_title
        teacher = data.t_name
        classroom = data.classroom
        cl_date=data.cl_date
        jieci_1 = map.get(data.jieci_1)
        jieci_2 = map.get(data.jieci_2)
        jieci_3 = map.get(data.jieci_3)
        jieci_4 = map.get(data.jieci_4)
        jieci_5 = map.get(data.jieci_5)
        jieci_6 = map.get(data.jieci_6)
        jieci_7 = map.get(data.jieci_7)
        zhouci = ""
        if data.jieci_1!="":
            zhouci="周一"+":"+jieci_1
        if data.jieci_2!= "":
            if zhouci=="":
                zhouci="周二"+":"+jieci_2
            else:
                zhouci=zhouci+"\n"+"周二"+":"+jieci_2
        if data.jieci_3 != "":
            if zhouci == "":
                zhouci = "周三"+":"+jieci_3
            else:
                zhouci =zhouci+ "\n" + "周三"+":"+jieci_3
        if data.jieci_4 != "":
            if zhouci == "":
                zhouci = "周四"+":"+jieci_4
            else:
                zhouci =zhouci+ "\n" + "周四"+":"+jieci_4
        if data.jieci_5 != "":
            if zhouci == "":
                zhouci = "周五"+":"+jieci_5
            else:
                zhouci =zhouci+ "\n" + "周五"+":"+jieci_5
        if data.jieci_6 != "":
            if zhouci == "":
                zhouci = "周六"+":"+jieci_6
            else:
                zhouci = zhouci+"\n" + "周六"+":"+jieci_6
        if data.jieci_7 != "":
            if zhouci == "":
                zhouci = "周日"+":"+jieci_7
            else:
                zhouci = zhouci+"\n" + "周日"+":"+jieci_7


        res.append({"cl_name":cl_name,"cl_cid":cl_cid,"cl_id":cl_id,"cl_school": cl_school,  "teacher": teacher,
                     "classroom": classroom,"cl_date":cl_date,"zhouci":zhouci,"cl_credit":cl_credit,"t_title":t_title})

        # sorted(res, key=lambda keys: keys['cl_name'])
    res = sorted(res, key=lambda x: x["zhouci"])

    return HttpResponse(json.dumps(res), content_type="application/json")

def qianxuesen_detail2(request):
    d=request.GET
    week=d.get('week')
    jieci=d.get('jieci')
    res=[]

    if not week and not jieci:
        datas = qianxuesen_class1.objects.all()
    elif not week:
        if jieci=="全选":
            datas = qianxuesen_class1.objects.all()
        else:
            datas = qianxuesen_class1.objects.filter(
                Q(jieci_1__icontains=jieci) | Q(jieci_2__icontains=jieci) | Q(jieci_3__icontains=jieci) |
                Q(jieci_4__icontains=jieci) | Q(jieci_5__icontains=jieci) |
                Q(jieci_6__icontains=jieci) | Q(jieci_7__icontains=jieci))
    elif not jieci:
        if week=="全选":
            datas = qianxuesen_class1.objects.all()
        else:
            if week != 20:
                week = str(week) + ","
            datas=qianxuesen_class1.objects.filter(cl_date__icontains=week)
    elif week=="全选" and jieci=="全选":
        datas = qianxuesen_class1.objects.all()
    else:
        if week != 20:
            week = str(week) + ","
        datas = qianxuesen_class1.objects.filter(cl_date__icontains=week).filter(Q(jieci_1__icontains=jieci)|Q(jieci_2__icontains=jieci)|Q(jieci_3__icontains=jieci)|
                                               Q(jieci_4__icontains=jieci)|Q(jieci_5__icontains=jieci)|
                                               Q(jieci_6__icontains=jieci)|Q(jieci_7__icontains=jieci))

    map={
        "01,02,03":"第一大节",
        "01,02":"第一大节",
        "02,03": "第一大节",
        "04,05":"第二大节",
        "06,07":"第三大节",
        "08,09,10":"第四大节",
        "08,09": "第四大节",
        "09,10": "第四大节",
        "11,12,13":"第五大节",
        "11,12": "第五大节",
        "12,13": "第五大节",
        "01,02,03,06,07,08,09,10,11,12,13":"全天",
        "01,02,03,04,05,06,07,08,09,10,11,12,13":"全天",
        "04,05,06,07,08,09,10,11,12,13":"全天",
        "01,02,03,04,05":"上午",
        "01,02,03,04": "上午",
        "02,03,04,05": "上午",
        "02,03,04": "上午",
        "06,07,08,09,10":"下午",
        "04,05,01,02,03":"上午",
        "08,09,10,06,07":"下午",
        "02,03,04,05,06,07,08,09,10,11,12,13": "全天",
        "02,03,06,07,08,09,10,11,12,13": "全天",
        "06,07,08,09":"下午",
        "06,07,":"第三大节",
        "01,02,03,06,07,08,09,10": "全天",
        "01,02,03,04,05,06,07,08,09,10": "全天",
        "02,03,06,07,08,09,10": "全天",
        "01,02,03,06,07,08,09": "全天",
        "02,03,06,07,08,09": "全天",
        "04,05,06,07":"二三大节",
        "06,07,  ": "第三大节",
        "14,  ": "14",

    }
    for data in datas:
        cl_name=data.cl_name
        cl_cid=data.cl_cid
        cl_id=data.cl_id
        cl_credit=data.cl_credit
        t_title=data.t_title
        cl_school = data.t_college
        teacher = data.t_name
        classroom = data.classroom
        cl_date=data.cl_date
        jieci_1 = map.get(data.jieci_1)
        jieci_2 = map.get(data.jieci_2)
        jieci_3 = map.get(data.jieci_3)
        jieci_4 = map.get(data.jieci_4)
        jieci_5 = map.get(data.jieci_5)
        jieci_6 = map.get(data.jieci_6)
        jieci_7 = map.get(data.jieci_7)

        # jieci_1 = data.jieci_1
        # jieci_2 = data.jieci_2
        # jieci_3 = data.jieci_3
        # jieci_4 = data.jieci_4
        # jieci_5 = data.jieci_5
        # jieci_6 = data.jieci_6
        # jieci_7 = data.jieci_7


        zhouci = ""
        if data.jieci_1!="":
            zhouci="周一"+":"+jieci_1
        if data.jieci_2!= "":
            if zhouci=="":
                zhouci="周二"+":"+jieci_2
            else:
                zhouci=zhouci+"\n"+"周二"+":"+jieci_2
        if data.jieci_3 != "":
            if zhouci == "":
                zhouci = "周三"+":"+jieci_3
            else:
                zhouci =zhouci+ "\n" + "周三"+":"+jieci_3
        if data.jieci_4 != "":
            if zhouci == "":
                zhouci = "周四"+":"+jieci_4
            else:
                zhouci =zhouci+ "\n" + "周四"+":"+jieci_4
        if data.jieci_5 != "":
            if zhouci == "":
                zhouci = "周五"+":"+jieci_5
            else:
                zhouci =zhouci+ "\n" + "周五"+":"+jieci_5
        if data.jieci_6 != "":
            if zhouci == "":
                zhouci = "周六"+":"+jieci_6
            else:
                zhouci = zhouci+"\n" + "周六"+":"+jieci_6
        if data.jieci_7 != "":
            if zhouci == "":
                zhouci = "周日"+":"+jieci_7
            else:
                zhouci = zhouci+"\n" + "周日"+":"+jieci_7


        res.append({"cl_name":cl_name,"cl_cid":cl_cid,"cl_id":cl_id,"cl_school": cl_school,  "teacher": teacher,
                     "classroom": classroom,"cl_date":cl_date,"zhouci":zhouci,"cl_credit":cl_credit,"t_title":t_title})

        # sorted(res, key=lambda keys: keys['cl_name'])
    res = sorted(res, key=lambda x: x["zhouci"])

    return HttpResponse(json.dumps(res), content_type="application/json")

#教师职称详情
def qianxuesen_title(request):
    d = request.GET
    res=[]
    title_list=['助教','讲师','副教授','教授','工程师','高级工程师','助理研究员','副研究员','研究员']
    num_list=[0 for i in range(0,len(title_list))]
    datas = qianxuesen_class1.objects.all()
    for data in datas:
            college = data.t_title
            college = college.split(',')
            college = list(set(college))
            for i in college:
                if i in title_list:
                        num_list[title_list.index(i)]+=1;
    for i in range(0,len(title_list)):
        res.append({'key':title_list[i],'number':tostr(num_list[i])})
    res.sort(key=lambda x:(x.get('number',0)),reverse=True)
    return HttpResponse(json.dumps(res), content_type="application/json")

def qianxuesen_title_class(request):
    d=request.GET
    q=d.get('q')
    t_title=d.get('t_title')
    res=[]
    if not q:
        datas=qianxuesen_class1.objects.all()
    else:
        datas=qianxuesen_class1.objects.filter(Q(cl_name__icontains=q)|Q(cl_cid__icontains=q))
    # for data in datas:
    #     res.append({"cl_cid":data.cl_cid,"cl_id":data.cl_id,"cl_name":data.cl_name,"cl_credit":data.cl_credit,"teacher":data.t_name,"qian_number":data.number,"t_title":data.t_title})


    for data in datas:
        title = data.t_title
        title =  title.split(',')
        if t_title in title:
            res.append({"cl_cid":data.cl_cid,"cl_id":data.cl_id,"cl_name":data.cl_name,"cl_credit":data.cl_credit,"teacher":data.t_name,"qian_number":data.number,"t_title":data.t_title})
    res = sorted(res, key=lambda x: x['qian_number'])
    return HttpResponse(json.dumps(res), content_type="application/json")

def qianxuesen_fanganbidui(request):
    students=qianxuesen_wxordx.objects.all()
    db=qianxuesen_fanganbidui1()
    wx=[]
    res=[]
    # for st in students:
    #     # 选课
    #     yx=[]
    #     sx=[]
    #     datas = qianxuesen_qianxuesen.objects.filter(st_id__icontains=st.st_id)
    #     # 方案
    #     infos = qianxuesen_project19.objects.filter(st_id__icontains=st.st_id).filter(schoolyear="2021-2022-1")
    #     for data in infos:
    #         yx.append({"courseid": data.cl_cid, "coursename": data.cl_name})
    #     for data in datas:
    #         if data.cl_cid == "21120102":
    #             sx.append({"courseid": "21120101", "coursename": data.cl_name})
    #         elif data.cl_cid == "21320102":
    #             sx.append({"courseid": "21320101", "coursename": data.cl_name})
    #         else:
    #             sx.append({"courseid": data.cl_cid, "coursename": data.cl_name})
    #     for i in yx:
    #         if i not in sx:
    #             if i not in wx:
    #                 wx.append({"courseid": i.get("courseid"), "coursename": i.get("coursename")})
    # num=[0 for i in range(0,len(wx))]
    # for st in students:
    #     # 选课
    #     yx=[]
    #     sx=[]
    #     datas = qianxuesen_qianxuesen.objects.filter(st_id__icontains=st.st_id)
    #     # 方案
    #     infos = qianxuesen_project19.objects.filter(st_id__icontains=st.st_id).filter(schoolyear="2021-2022-1")
    #     for data in infos:
    #         yx.append({"courseid": data.cl_cid, "coursename": data.cl_name})
    #     for data in datas:
    #         if data.cl_cid == "21120102":
    #             sx.append({"courseid": "21120101", "coursename": data.cl_name})
    #         elif data.cl_cid == "21320102":
    #             sx.append({"courseid": "21320101", "coursename": data.cl_name})
    #         else:
    #             sx.append({"courseid": data.cl_cid, "coursename": data.cl_name})
    #     for i in yx:
    #         if i not in sx:
    #             num[wx.index(i)] = num[wx.index(i)]+1
    #
    # for i in range(0,len(wx)):
    #     db.cl_cid=wx[i].get("courseid")
    #     db.cl_name=wx[i].get("coursename")
    #     db.num_wx=num[i]
    #     db.save()
    datas = qianxuesen_fanganbidui1.objects.all()
    for data in datas:
        res.append({'cid':data.cl_cid,'cname':data.cl_name,'number':data.num_wx})
    res.sort(key=lambda x:(x.get('number',0)),reverse=True)
    return HttpResponse(json.dumps(res), content_type="application/json")
    # return HttpResponse("hello bug")

def qianxuesen_fanganbidui_st(request):
    d=request.GET
    cl_cid=d.get("cl_cid")
    q=d.get("q")
    # datas=qianxuesen_wxordx.objects.all()
    # db=qianxuesen_wxst()
    # for st in datas:
    #     num_wx = 0
    #     num_dx = 0
    #     yx = []
    #     sx = []
    #     wx = []
    #     # 选课
    #     datas = qianxuesen_qianxuesen.objects.filter(st_id__icontains=st.st_id)
    #     # 方案
    #     infos = qianxuesen_project19.objects.filter(st_id__icontains=st.st_id).filter(schoolyear="2021-2022-1")
    #     for data in infos:
    #         yx.append({"courseid": data.cl_cid, "coursename": data.cl_name})
    #     for data in datas:
    #         if data.cl_cid == "21120102":
    #             sx.append({"courseid": "21120101", "coursename": data.cl_name})
    #         elif data.cl_cid == "21320102":
    #             sx.append({"courseid": "21320101", "coursename": data.cl_name})
    #         else:
    #             sx.append({"courseid": data.cl_cid, "coursename": data.cl_name})
    #     for i in yx:
    #         if i not in sx:
    #             wx.append({"courseid": i.get("courseid"), "coursename": i.get("coursename"), "beizhu": "未选"})
    #             db.cl_cid=i.get("courseid")
    #             db.cl_name=i.get("coursename")
    #             st_id = st.st_id
    #             st_name = st.st_name
    #             st_class = st.st_class
    #             st_school = st.st_school
    #             st_major = st.st_major
    #             major_2 = st.major_2
    #             st_grade = st.st_grade
    #             total_credit = st.total_credit
    #             num_wx = st.num_wx
    #             num_dx = st.num_dx
    #             db.st_id = st_id
    #             db.st_name = st_name
    #             db.num_wx = num_wx
    #             db.num_dx = num_dx
    #             db.st_class = st_class
    #             db.st_school = st_school
    #             db.st_major = st_major
    #             db.total_credit = total_credit
    #             db.major_2 = major_2
    #             db.st_grade = st_grade
    #             db.save()
    #     for i in sx:
    #         if i not in yx:
    #             wx.append({"courseid": i.get("courseid"), "coursename": i.get("coursename"), "beizhu": "多选"})

    # return HttpResponse("hello bug")
    res=[]
    datas=qianxuesen_wxst.objects.filter(cl_cid=cl_cid)
    for data in datas:
        st_id = data.st_id
        st_name = data.st_name
        st_class = data.st_class
        st_school = data.st_school
        st_major = data.st_major
        major_2 = data.major_2
        st_grade = data.st_grade
        total_credit = tostr(data.total_credit)

        res.append({"st_name": st_name, "st_id": st_id, "st_school": st_school, "st_class": st_class,
                    "total_credit": total_credit, "st_major": st_major, "major_2": major_2, "st_grade": st_grade})
    return HttpResponse(json.dumps(res),content_type="application/json")

def qianxuesen_pf_st(request):
    d=request.GET
    q=d.get('q')
    p=d.get('st_grade')
    res=[]
    datas=qianxuesen_qianxuesenst.objects.all()
    for data in datas:
        st_id=data.st_id
        st_name=data.st_name
        st_class=data.st_class
        st_school=data.st_school
        st_grade=data.st_grade
        st_major=data.st_major
        major_2=data.major_2
        if not q and not p:
            res.append({"st_name": st_name, "st_id": st_id, "st_school": st_school, "st_class": st_class,
                       "st_major": st_major, "major_2": major_2, "st_grade": st_grade})
        elif not p:
            if q in st_id or q in st_name:
                res.append({"st_name": st_name, "st_id": st_id, "st_school": st_school, "st_class": st_class,
                         "st_major": st_major, "major_2": major_2, "st_grade": st_grade})
        elif not q:
            if p in st_grade:
                res.append({"st_name": st_name, "st_id": st_id, "st_school": st_school, "st_class": st_class,
                        "st_major": st_major, "major_2": major_2, "st_grade": st_grade})
        else:
            if (q in st_id or q in st_name) and p in st_grade:
                res.append({"st_name": st_name, "st_id": st_id, "st_school": st_school, "st_class": st_class,
                         "st_major": st_major, "major_2": major_2, "st_grade": st_grade})
    res = sorted(res, key=lambda x: x['st_grade'])
    return HttpResponse(json.dumps(res),content_type="application/json")

def qianxuesen_performance(request):
    d = request.GET
    st_id = d.get('st_id')
    st_name = d.get('st_name')
    q = d.get('q')
    res = []
    # if not q:
    #     datas = qianxuesen_chengji.objects.filter(st_id__icontains=st_id)
    # else:
    #     datas = qianxuesen_chengji.objects.filter(st_id__icontains=st_id).filter(year__icontains=q)
    datas=qianxuesen_chengji.objects.filter(st_id=st_id)
    for data in datas:
        cl_name=data.cl_name
        cl_credit=data.cl_credit.strip()
        cl_performance=data.cl_performance.strip()
        cl_type=data.cl_type.strip()
        cl_attribute=data.cl_attribute.strip()
        year=data.year.strip()
        if not q:
          res.append({"cl_name": cl_name, "cl_credit": cl_credit, "cl_performance": cl_performance, "cl_type": cl_type,
                        "cl_attribute": cl_attribute, "year": year})
        else:
            if q in year.replace(" ",""):
                res.append(
                    {"cl_name": cl_name, "cl_credit": cl_credit, "cl_performance": cl_performance, "cl_type": cl_type,
                     "cl_attribute": cl_attribute, "year": year})
        # res.append({"cl_name": cl_name, "cl_credit": cl_credit, "cl_performance": cl_performance, "cl_type": cl_type,
        #                 "cl_attribute": cl_attribute, "year": year})
    res = sorted(res, key=lambda x: x['year'])
    return HttpResponse(json.dumps(res), content_type="application/json")
    # return HttpResponse('hello bug')

def qianxuesen_bujige(request):
    # datas=qianxuesen_chengji.objects.all()
    # bujige=[]
    # db=qianxuesen_bujige_num()
    # for data in datas:
    #     chengji=data.cl_performance.replace(" ","")
    #     chengji=tofs(chengji)
    #     if chengji<60:
    #         i={"st_id":data.st_id,"st_name":data.st_name}
    #         if i not in bujige:
    #             bujige.append({"st_id":data.st_id,"st_name":data.st_name})
    # num=[0 for i in range(0,len(bujige))]
    # for data in datas:
    #     chengji=tofs(data.cl_performance.strip())
    #     if chengji<60:
    #         i={"st_id":data.st_id,"st_name":data.st_name}
    #         num[bujige.index(i)]=num[bujige.index(i)]+1
    # for i in bujige:
    #     datas=qianxuesen_chengji.objects.filter(st_id=i.get("st_id"))
    #     for data in datas:
    #
    #         print(data.st_name+data.cl_performance)
    # for i in range(0,len(bujige)):
    #     db.st_id = bujige[i].get("st_id")
    #     db.st_name = bujige[i].get("st_name")
    #     db.bujige_num=num[i]
    #     db.save()
    d=request.GET
    q=d.get("q")
    left=d.get("left")
    if left:
        if left[0].isdigit():
            left=int(left)
    right=d.get("right")
    if right:
        if right[0].isdigit():
            right=int(right)
    res=[]
    datas=qianxuesen_bujige_num.objects.all()
    for data in datas:
        st_id=data.st_id
        st_name=data.st_name
        bujige_num=tostr1(data.bujige_num)
        infos=qianxuesen_qianxuesenst.objects.filter(st_id=st_id)
        for info in infos:
            st_major=info.st_major
            major_2=info.major_2
            st_grade=info.st_grade
            st_class=info.st_class
            st_school=info.st_school
            if not q:
                if not left and not right:
                    res.append({"st_id":st_id,"st_name":st_name,"st_major":st_major,"major_2":major_2,"st_grade":st_grade,"st_class":st_class\
                            ,"st_school":st_school,"bujige_num":bujige_num})
                elif not left:
                    if data.bujige_num<=right:
                        res.append({"st_id": st_id, "st_name": st_name, "st_major": st_major, "major_2": major_2,
                                    "st_grade": st_grade, "st_class": st_class \
                                       , "st_school": st_school, "bujige_num": bujige_num})
                elif not right:
                    if data.bujige_num>=left:
                        res.append({"st_id": st_id, "st_name": st_name, "st_major": st_major, "major_2": major_2,
                                    "st_grade": st_grade, "st_class": st_class \
                                       , "st_school": st_school, "bujige_num": bujige_num})
                else:
                    if data.bujige_num>=left and data.bujige_num<=right:
                        res.append({"st_id": st_id, "st_name": st_name, "st_major": st_major, "major_2": major_2,
                                    "st_grade": st_grade, "st_class": st_class \
                                       , "st_school": st_school, "bujige_num": bujige_num})
            else:
                if q in st_id or q in st_name:
                    if not left and not right:
                        res.append({"st_id": st_id, "st_name": st_name, "st_major": st_major, "major_2": major_2,
                                    "st_grade": st_grade, "st_class": st_class \
                                       , "st_school": st_school, "bujige_num": bujige_num})
                    elif not left:
                        if data.bujige_num <= right:
                            res.append({"st_id": st_id, "st_name": st_name, "st_major": st_major, "major_2": major_2,
                                        "st_grade": st_grade, "st_class": st_class \
                                           , "st_school": st_school, "bujige_num": bujige_num})
                    elif not right:
                        if data.bujige_num >= left:
                            res.append({"st_id": st_id, "st_name": st_name, "st_major": st_major, "major_2": major_2,
                                        "st_grade": st_grade, "st_class": st_class \
                                           , "st_school": st_school, "bujige_num": bujige_num})
                    else:
                        if data.bujige_num >= left and data.bujige_num <= right:
                            res.append({"st_id": st_id, "st_name": st_name, "st_major": st_major, "major_2": major_2,
                                        "st_grade": st_grade, "st_class": st_class \
                                           , "st_school": st_school, "bujige_num": bujige_num})
    res.sort(key=lambda x:x['bujige_num'],reverse=True)
    return HttpResponse(json.dumps(res),content_type="application/json")


def tofs(a):
    if a[0].isdigit():
        return float(a)
    elif a == "优秀":
        return 90
    elif a == "良好":
        return 80
    elif a == "中等":
        return 70
    elif a == "及格":
        return 60
    elif a == "不及格":
        return 50
    elif a == "合格":
        return 50


def qianxuesen_bujigeclass(request):
    d=request.GET
    st_id=d.get("st_id")
    res=[]
    datas=qianxuesen_chengji.objects.filter(st_id=st_id)
    for data in datas:
        chengji=data.cl_performance
        chengji=chengji.replace(" ","")
        chengji=tofs(chengji)
        cl_name=data.cl_name.strip()
        cl_credit=data.cl_credit.strip()
        cl_performance=data.cl_performance.replace(" ","")
        cl_type=data.cl_type.strip()
        cl_attribute=data.cl_attribute.strip()
        if chengji<60:
            res.append({"cl_name":cl_name,"cl_credit":cl_credit,"cl_performance":cl_performance,"cl_type":cl_type,"cl_attribute":cl_attribute})
        res.sort(key=lambda x:x['cl_credit'])
    return HttpResponse(json.dumps(res),content_type="application/json")


        
def qianxuesen_exam(request):
    # db=qianxuesen_examst()
    # datas=qianxuesen_exam1.objects.all()
    # for data in datas:
    #     cl_name=data.cl_name
    #     date=data.date
    #     time=data.time
    #     db.cl_name=cl_name
    #     db.date=date
    #     db.time=time
    #     infos=qianxuesen_qianxuesen.objects.filter(cl_name__icontains=cl_name)
    #     for info in infos:
    #         db.st_id=info.st_id
    #         db.st_name=info.st_name
    #         db.st_class=info.st_class
    #         db.save()
    return HttpResponse("hello bug")
    
def qianxuesen_chengjibidui(request):
    bujige=[]
    res=[]
    datas = qianxuesen_chengji.objects.values_list("cl_name","cl_credit")
    result=Counter(datas).most_common()
    for i in result:
        cl_name=i[0][0]
        cl_credit=i[0][1]
        res.append({"cl_name":cl_name,"cl_credit":cl_credit})
    res.sort(key=lambda x: (x.get('cl_credit', 0)), reverse=True)
    return HttpResponse(json.dumps(res), content_type="application/json")
    # print(i[0])
    # return HttpResponse("HELLO BUG")
