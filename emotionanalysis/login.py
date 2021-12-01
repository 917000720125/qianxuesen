
import json
from django.http import HttpResponseRedirect, HttpResponse
import pyecharts as Map
from Emotion.models import *
import time
from django.forms.models import model_to_dict
from emotionanalysis.Function import *


def gp_college_declare(request):#留学统计-学院申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    d=request.GET
    print(d)
    datas =college_declare.objects.all()
    sdeclare=0
    ssuccessful=0
    for data in datas:
        per=float(data.successful)/float(data.declare)*100
        res.append({"college":data.college,"declare":data.declare,"successful":data.successful,'per':per})
        ssuccessful+=data.successful
        sdeclare+=data.declare
    sper=ssuccessful/sdeclare
    print(res)
    res.sort(key=lambda x:(x.get(d['st'],0)),reverse=True)
    print(res)
    res.insert(0,{"college":'总计',"declare":sdeclare,"successful":ssuccessful,"per":sper})
    return HttpResponse(json.dumps(res), content_type="application/json")
def gp_grade_declare(request):#留学统计-在读年级申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    d=request.GET
    print(d)
    datas =grade_declare.objects.all()
   # sdeclare=0
   # ssuccessful=0
    for data in datas:
        per=float(data.successful)/float(data.declare)*100
        res.append({"grade":data.grade,"declare":data.declare,"successful":data.successful,'per':per})
        #ssuccessful+=data.successful
      #  sdeclare+=data.declare
   #sper=ssuccessful/sdeclare
    print(res)
    res.sort(key=lambda x:(x.get(d['st'],0)),reverse=True)
    print(res)
   # res.insert(0,{"college":'总计',"declare":sdeclare,"successful":ssuccessful,"per":sper})
    return HttpResponse(json.dumps(res), content_type="application/json")
def gp_type_declare(request):#留学统计-联培/学位申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    d=request.GET
    print(d)
    datas =type_declare.objects.all()
    for data in datas:
        per=float(data.successful)/float(data.declare)*100
        res.append({"type":data.type,"declare":data.declare,"successful":data.successful,'per':per})
    print(res)
    res.sort(key=lambda x:(x.get(d['st'],0)),reverse=True)
    print(res)

    return HttpResponse(json.dumps(res), content_type="application/json")

def gp_time_declare(request):#留学统计-留学期限申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    d=request.GET
    print(d)
    datas =time_declare.objects.all()
    for data in datas:
        per=float(data.successful)/float(data.declare)*100
        res.append({"time":data.time,"declare":data.declare,"successful":data.successful,'per':per})
    if d['st']=='time':
        res.sort(key=lambda x: (x.get(d['st'], 0)))
    else:
       res.sort(key=lambda x:(x.get(d['st'],0)),reverse=True)

    return HttpResponse(json.dumps(res), content_type="application/json")


def gp_QS_declare(request):#留学统计-QS排名申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    d=request.GET
    print(d)
    datas =QS_declare.objects.all()
    for data in datas:
         if data.declare!=0:
            per=float(data.successful)/float(data.declare)*100
         else:
             per=0
         res.append({"QS":data.QS,"declare":data.declare,"successful":data.successful,'per':per})
    if d['st'] == 'QS':
        res.sort(key=lambda x: (x.get(d['st'], 0)))
    else:
        res.sort(key=lambda x: (x.get(d['st'], 0)), reverse=True)
    return HttpResponse(json.dumps(res), content_type="application/json")
#2020留学申请统计
# def gp_sum_20():#20留学总表数据处理,将总表按学院，留学期限等生成对应子表，但不够灵活每有一组新数据就要生成对应的新库，
#                  考虑到每次的数据都较少，采取每次查询对总表进行一次统计。
#     cnum=0#学院数
#     gnum=0#年级数
#     tnum=2#联培，学位两种类型
#     tmnum=0#留学期限数
#     datas=gp_summary20.objects.all()
#     dc=college_declare20()
#     dg=grade_declare()
#     dt=type_declare()
#     dqs=QS_declare20()
#     dtime=time_declare20()
#     rows=len(datas)#总表长度
#     flagc = [0] * (rows + 1)#学院的标记
#     flagg = [0] * (rows + 1)#在读年级的标记
#     flagt = [0] * (rows + 1)  # time的标记
#     college = [''] * 100
#     grade=[''] * 100
#     time= [''] * 100
#     type=['联培','学位']
#     j=0
#     sheete=[0]* (rows + 1)
#     sheetg =[0] * (rows + 1)
#     sheett = [0] * (rows + 1)
#     for data in datas:#初始化
#         sheete[j] = data.college
#         sheetg[j] = data.grade
#         sheett[j] = data.time_mon
#         j +=1
#     for i in range(0, rows):#学院
#         if flagc[i] != -1:
#             college[cnum] = sheete[i]
#             for k in range(i + 1, rows + 1):
#                 if sheete[k] == college[cnum]:
#                     flagc[k] = -1
#             cnum = cnum + 1
#     for i in range(0, rows):  #在读年级
#         if flagg[i] != -1:
#             grade[gnum] = sheetg[i]
#             for k in range(i + 1, rows + 1):
#                 if sheetg[k] == grade[gnum]:
#                     flagg[k] = -1
#             gnum = gnum + 1
#     for i in range(0, rows):  # 留学年限
#         if flagt[i] != -1:
#             if sheett[i]=='':
#                 time[tmnum]='未知'
#             time[tmnum] = sheett[i]
#             for k in range(i + 1, rows + 1):
#                 if sheett[k] == time[tmnum]:
#                     flagt[k] = -1
#             tmnum = tmnum + 1
#     #学院
#     cdeclare=[0]*cnum
#     csuccessful=[0]*cnum
#     for data in datas:
#         for i in range(0,cnum):
#             if data.college==college[i]:
#                 cdeclare[i]+=1
#                 # if data.csc=="基金委录取":
#                 #   csuccessful[i]+=1
#     for i in range(0, cnum):
#         dc.college=college[i]
#         dc.declare=cdeclare[i]
#         #dc.successful=csuccessful[i]
#         dc.save()
#     #在读年级
#     gdeclare = [0] * gnum
#     gsuccessful = [0] * gnum
#     for data in datas:
#         for i in range(0, gnum):
#             if data.grade == grade[i]:
#                 gdeclare[i] += 1
#                 #if data.csc == "基金委录取":
#                  #   gsuccessful[i] += 1
#     for i in range(0, gnum):
#         dg.grade = grade[i]
#         dg.declare = gdeclare[i]
#        # dg.successful = gsuccessful[i]
#         #dg.save()
#     #联培/学位
#     tdeclare = [0] * 2
#     tsuccessful = [0] * 2
#     for data in datas:
#         for i in range(0, 2):
#             if data.type == type[i]:
#                 tdeclare[i] += 1
#                 #if data.csc == "基金委录取":
#                 #    tsuccessful[i] += 1
#     # for i in range(0, 2):
#     #     dt.type = type[i]
#     #     dt.declare = tdeclare[i]
#     #     dt.successful = tsuccessful[i]
#     #     dt.save()
#     #留学年限
#     tmdeclare = [0] * tmnum
#     tmsuccessful = [0] * tmnum
#     for data in datas:
#         for i in range(0, tmnum):
#             if data.time_mon == time[i]:
#                 tmdeclare[i] += 1
#                # if data.csc == "基金委录取":
#                 #    tmsuccessful[i] += 1
#     for i in range(0, tmnum):
#         dtime.time = time[i]
#         dtime.declare = tmdeclare[i]
#        # dtime.successful = tmsuccessful[i]
#         #dtime.save()
#         # QS排名
#         fr = [{"QS": '', "declare": 0} for i in range(11)]
#         for i in range(10):
#             print(i)
#             fr[i]['QS'] = str(i * 50) + '-' + str((i + 1) * 50 - 1)
#         fr[10]['QS'] = "500+"
#         for data in datas:
#             score = int(data.QS)
#             if 0 < score <= 49:
#                 fr[0]['declare'] += 1
#             elif 49 < score <= 99:
#                 fr[1]['declare'] += 1
#             elif 99 < score <= 149:
#                 fr[2]['declare'] += 1
#             elif 149 < score <= 199:
#                 fr[3]['declare'] += 1
#             elif 199 < score <= 249:
#                 fr[4]['declare'] += 1
#             elif 249 < score <= 299:
#                 fr[5]['declare'] += 1
#             elif 299 < score <= 349:
#                 fr[6]['declare'] += 1
#             elif 349 < score <= 399:
#                 fr[7]['declare'] += 1
#             elif 399 < score <= 449:
#                 fr[8]['declare'] += 1
#             elif 449 < score <= 499:
#                 fr[9]['declare'] += 1
#             else:
#                 fr[10]['declare'] += 1
#         for i in range(0, 11):
#             print(i)
#             dqs.QS = fr[i]['QS']
#             dqs.declare = fr[i]['declare']
#             dqs.save()
def gp_college_declare20(request):#留学统计-学院申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    d = request.GET
    print(d['project'])
    if d['project'] == '所有项目':
        datas = gp_summary20.objects.all()
    else:
        datas = gp_summary20.objects.filter(projects=d['project'])
    res = college(datas)
    print(res)
    res.sort(key=lambda x: (x.get('declare', 0)))
    return HttpResponse(json.dumps(res), content_type="application/json")
def gp_time_declare20(request):#2020留学申请统计-留学期限申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    d = request.GET
    if d['project'] == '所有项目':
        datas = gp_summary20.objects.all()
    else:
        datas = gp_summary20.objects.filter(projects=d['project'])
    res = time(datas)
    res.sort(key=lambda x: (x.get('time', 0)))
    return HttpResponse(json.dumps(res), content_type="application/json")
def gp_QS_declare20(request):#留学申请统计-QS排名申报人数，成功人数
    d = request.GET
    if d['project'] == '所有项目':
        datas = gp_summary20.objects.all()
    else:
        datas = gp_summary20.objects.filter(projects=d['project'])
    res = QS(datas)
    return HttpResponse(json.dumps(res), content_type="application/json")
def gp_project_declare20(request):#留学统计-申报项目申报人数
    res = []
    datas =project_declare20.objects.all()
    for data in datas:
         res.append({"project":data.project,"declare":data.declare})
    print(res)
    return HttpResponse(json.dumps(res), content_type="application/json")
def gp_world_declare20(request):#留学统计-申报人数，成功人数 地图统计
    # 进行情感分析并把结果插入数据库,然后返回结果
    d = request.GET
    if d['project'] == '所有项目':
        datas = gp_summary20.objects.all()
    else:
        datas = gp_summary20.objects.filter(projects=d['project'])
    res,map0=world(datas,"留学国家分布图")
    map0.render(path="./html1/sample_skin/demo/gp_nworld_20.html")
    return HttpResponse(json.dumps(res), content_type="application/json")
def gp_details_20(request):#学院详情
    res=[]
    d=request.GET
    print(d["kind"])
    parameter=d['parameter'];
    if d['kind']=='QS':
        if d['project']=='所有项目':
            datas=gp_summary20.objects.all()
        else:
            datas = gp_summary20.objects.filter(projects=d['project'])
        print(parameter)
        if parameter=="500+":
           datas=datas.filter(QS=parameter)
           for data in datas:
               json_dict = model_to_dict(data)
               res.append(json_dict)
        # if parameter=="0-49":
        #     print('aaaa')
        #     min = 1
        #     max = 49
        #     for data in datas:
        #         print(data)
        #         if data.QS != '500+':
        #             print(data.QS)
        #             if min <= int(data.QS) <= max:
        #                 json_dict = model_to_dict(data)
        #                 res.append(json_dict)
        else:
          min=int(parameter.split("-")[0])
          max=int(parameter.split("-")[1])
          for data in datas:
             print(data)
             if data.QS!='500+':
                print(data.QS)
                if min<=int(data.QS)<=max:
                  json_dict = model_to_dict(data)
                  res.append(json_dict)
    elif d['kind']=='college':
        if d['project'] == '所有项目':
            datas = gp_summary20.objects.filter(college=parameter)
        else:
            datas = gp_summary20.objects.filter(projects=d['project'],college=parameter)
        for data in datas:
             json_dict = model_to_dict(data)
             res.append(json_dict)
    elif d['kind']=='time':
        if d['project'] == '所有项目':
            datas = gp_summary20.objects.filter(time_mon=parameter)
        else:
            datas = gp_summary20.objects.filter(projects=d['project'],time_mon=parameter)
        for data in datas:
             json_dict = model_to_dict(data)
             res.append(json_dict)
    elif d['kind']=='country':
        if d['project'] == '所有项目':
            datas = gp_summary20.objects.filter(country=parameter)
        else:
            datas = gp_summary20.objects.filter(projects=d['project'],country=parameter)
        for data in datas:
             json_dict = model_to_dict(data)
             res.append(json_dict)
    return HttpResponse(json.dumps(res), content_type="application/json")

def QS(datas):
    fr = [{"QS": '', "declare": 0} for i in range(11)]
    for i in range(10):
        fr[i]['QS'] = str(i * 50) + '-' + str((i + 1) * 50 - 1)
    fr[10]['QS'] = "500+"
    for data in datas:
        if data.QS=='500+':
            fr[10]['declare'] += 1
        else:
            score = int(data.QS)
            if 0 < score <= 49:
                fr[0]['declare'] += 1
            elif 49 < score <= 99:
                fr[1]['declare'] += 1
            elif 99 < score <= 149:
                fr[2]['declare'] += 1
            elif 149 < score <= 199:
                fr[3]['declare'] += 1
            elif 199 < score <= 249:
                fr[4]['declare'] += 1
            elif 249 < score <= 299:
                fr[5]['declare'] += 1
            elif 299 < score <= 349:
                fr[6]['declare'] += 1
            elif 349 < score <= 399:
                fr[7]['declare'] += 1
            elif 399 < score <= 449:
                fr[8]['declare'] += 1
            elif 449 < score <= 499:
                fr[9]['declare'] += 1
    res=[]
    for i in range(0, 11):
        res.append({"QS": fr[i]['QS'], "declare": fr[i]['declare']})
    return res
def time(datas):
    res = []
    declare = [0] * 30
    time = [''] * 30
    num = 0
    for data in datas:
        flag = 0
        for i in range(0, num):
            if data.time_mon== time[i]:
                flag = 1
                declare[i] += 1
        if flag == 0:
            time[num] = data.time_mon
            declare[num] = 1
            num += 1
    for j in range(num):
        res.append({"time": time[j], "declare": declare[j]})
    return res
# def gp_sum_20_1():#20留学报送总表数据处理
#     # 进行情感分析并把结果插入数据库,然后返回结果
#     cnum=0#学院数
#     gnum=0#年级数
#     tmnum=0#留学期限数
#     datas=gp_summary20_1.objects.all()
#     dc=college_declare20_1()
#     dtime=time_declare20_1()
#     dqs=QS_declare20_1()
#     rows=len(datas)#总表长度
#     flagc = [0] * (rows + 1)#学院的标记
#     flagg = [0] * (rows + 1)#在读年级的标记
#     flagt = [0] * (rows + 1) # time的标记
#     college = [''] * 100
#     grade=[''] * 100
#     time= [''] * 100
#     j=0
#     sheete=[0]* (rows + 1)
#     sheetg =[0] * (rows + 1)
#     sheett = [0] * (rows + 1)
#     for data in datas:#初始化
#         sheete[j] = data.college
#         sheetg[j] = data.grade
#         sheett[j] = data.time_mon
#         j +=1
#     for i in range(0, rows):#学院
#         if flagc[i] != -1:
#             college[cnum] = sheete[i]
#             for k in range(i + 1, rows + 1):
#                 if sheete[k] == college[cnum]:
#                     flagc[k] = -1
#             cnum = cnum + 1
#     for i in range(0, rows):  # 留学年限
#         if flagt[i] != -1:
#             if sheett[i]=='':
#                 time[tmnum]='未知'
#             time[tmnum] = sheett[i]
#             for k in range(i + 1, rows + 1):
#                 if sheett[k] == time[tmnum]:
#                     flagt[k] = -1
#             tmnum = tmnum + 1
#     #学院
#     cdeclare=[0]*cnum
#     for data in datas:
#         for i in range(0,cnum):
#             if data.college==college[i]:
#                 cdeclare[i]+=1
#     for i in range(0, cnum):
#         dc.college=college[i]
#         dc.declare=cdeclare[i]
#         dc.save()
#     #留学年限
#     tmdeclare = [0] * tmnum
#     for data in datas:
#         for i in range(0, tmnum):
#             if data.time_mon == time[i]:
#                 tmdeclare[i] += 1
#     for i in range(0, tmnum):
#         dtime.time = time[i]
#         dtime.declare = tmdeclare[i]
#         dtime.save()
#     #QS排名
#     fr = [{"QS": '', "declare": 0} for i in range(11)]
#     for i in range(10):
#         print(i)
#         fr[i]['QS'] = str(i * 50) + '-' + str((i + 1) * 50-1)
#     fr[10]['QS']="500+"
#     for data in datas:
#         score = int(data.QS)
#         if 0<score <= 49:
#             fr[0]['declare'] += 1
#         elif 49< score <= 99:
#             fr[1]['declare'] += 1
#         elif 99 < score <= 149:
#             fr[2]['declare'] += 1
#         elif 149< score <=199:
#             fr[3]['declare'] += 1
#         elif 199 < score <= 249:
#             fr[4]['declare'] += 1
#         elif 249 < score <= 299:
#             fr[5]['declare'] += 1
#         elif 299 < score <= 349:
#             fr[6]['declare'] += 1
#         elif 349 < score <= 399:
#             fr[7]['declare'] += 1
#         elif 399 < score <= 449:
#             fr[8]['declare'] += 1
#         elif 449 < score <= 499:
#             fr[9]['declare'] += 1
#         else:
#             fr[10]['declare'] += 1
#     for i in range(0, 11):
#         print(i)
#         dqs.QS = fr[i]['QS']
#         dqs.declare = fr[i]['declare']
#         dqs.save()
def gp_college_declare20_1(request):#留学统计-学院申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    d=request.GET
    if d['project'] == '所有项目':
        datas = gp_summary20_1.objects.all()
    else:
        datas = gp_summary20_1.objects.filter(projects=d['project'])
    res=college(datas)
    res.sort(key=lambda x: (x.get('declare', 0)))
    return HttpResponse(json.dumps(res), content_type="application/json")
def gp_time_declare20_1(request):#2020留学申请统计-留学期限申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    d = request.GET
    if d['project'] == '所有项目':
        datas = gp_summary20_1.objects.all()
    else:
        datas = gp_summary20_1.objects.filter(projects=d['project'])
    res=time(datas)
    res.sort(key=lambda x: (x.get('time', 0)))
    return HttpResponse(json.dumps(res), content_type="application/json")
def gp_QS_declare20_1(request):#留学申请统计-QS排名申报人数，成功人数
    d=request.GET
    if d['project']=='所有项目':
      datas =gp_summary20_1.objects.all()
    else:
      datas=gp_summary20_1.objects.filter(projects=d['project'])
    res=QS(datas)
    return HttpResponse(json.dumps(res), content_type="application/json")
def gp_project_declare20_1(request):#留学统计-QS排名申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    datas =project_declare20_1.objects.all()
    for data in datas:
         res.append({"project":data.project,"declare":data.declare})
    print(res)
    return HttpResponse(json.dumps(res), content_type="application/json")
def gp_world_declare20_1(request):#留学统计-申报人数，成功人数 地图统计
    # 进行情感分析并把结果插入数据库,然后返回结果
    d = request.GET
    if d['project'] == '所有项目':
        datas = gp_summary20_1.objects.all()
    else:
        datas = gp_summary20_1.objects.filter(projects=d['project'])
    res, map0 = world(datas,"留学国家分布图")
    map0.render(path="./html1/sample_skin/demo/gp_nworld_20_1.html")
    return HttpResponse(json.dumps(res), content_type="application/json")
def gp_details_20_1(request):#学院详情
    res=[]
    d=request.GET
    parameter=d['parameter']
    print(d['kind'])
    print(d['parameter'])
    if d['kind']=='QS':
        if d['project']=='所有项目':
            datas=gp_summary20_1.objects.all()
        else:
            datas = gp_summary20_1.objects.filter(projects=d['project'])
        if parameter=="500+":
           datas=datas.filter(QS=parameter)
           for data in datas:
               json_dict = model_to_dict(data)
               res.append(json_dict)
        else:
          min=int(parameter.split("-")[0])
          max=int(parameter.split("-")[1])
          for data in datas:
             if data.QS!='500+':
                print(data.QS)
                if min<=int(data.QS)<=max:
                  json_dict = model_to_dict(data)
                  res.append(json_dict)
    elif d['kind']=='college':
        if d['project'] == '所有项目':
            datas = gp_summary20_1.objects.filter(college=parameter)
        else:
            datas = gp_summary20_1.objects.filter(projects=d['project'],college=parameter)
        for data in datas:
             json_dict = model_to_dict(data)
             res.append(json_dict)
    elif d['kind']=='time':
        if d['project'] == '所有项目':
            datas = gp_summary20_1.objects.filter(time_mon=parameter)
        else:
            datas = gp_summary20_1.objects.filter(projects=d['project'],time_mon=parameter)
        for data in datas:
             json_dict = model_to_dict(data)
             res.append(json_dict)
    elif d['kind']=='country':
        if d['project'] == '所有项目':
            datas = gp_summary20_1.objects.filter(country=parameter)
        else:
            datas = gp_summary20_1.objects.filter(projects=d['project'],country=parameter)
        for data in datas:
             json_dict = model_to_dict(data)
             res.append(json_dict)
    return HttpResponse(json.dumps(res), content_type="application/json")
def cj_college_fail(request):#各个学院不及格人数和平均分
    res = []
    datas=cj_college.objects.all()
    for data in datas:
        res.append({"college":data.college,"fail":data.fail,'average':data.average})
    res.sort(key=lambda x: (x.get('fail', 0)), reverse=True)
    return HttpResponse(json.dumps(res), content_type="application/json")
def gp_major_declare(request):#留学统计-留学期限申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    d=request.GET
    datas =major_declare.objects.filter(college=d['college'])
    for data in datas:
         if data.declare!=0:
            per=float(data.successful)/float(data.declare)*100
         else:
             per=0
         res.append({"major":data.major,"declare":data.declare,"successful":data.successful,'per':per})
    res.sort(key=lambda x: (x.get(d['st'], 0)), reverse=True)

    return HttpResponse(json.dumps(res), content_type="application/json")
def gp_world_declare():#留学统计-申报人数，成功人数 地图统计
    # 进行情感分析并把结果插入数据库,然后返回结果
    datas=gp_summary.objects.all()
    val =[0]*30
    world =['']*30
    attr=[]
    value=[]
    num=0
    for data in datas:
        flag = 0
        for i in range(0, num):
            if data.country== world[i]:
                flag = 1
                val[i]+= 1
        if flag == 0:
           world[num] = data.country
           val[num] = 1
           num += 1
    print(world)
    for j in range(num):
        attr.append(fanyi(world[j]))
        value.append(val[j])
    map0 = Map("世界地图示例", width=1200, height=600)
    map0.add("世界", attr, value, maptype="world", is_visualmap=True, visual_text_color='#000')
    map0.render(path="./html1/sample_skin/demo/gp_nworld.html")

def major():
    datas=gp_summary.objects.all()
    dm=major_declare()
    j=0
    rows=len(datas)
    flagc=[0]*(rows+1)
    sheetm=[0]*(rows+1)
    sheetc = [0]*(rows+1)
    mnum=0
    major=['']*100
    college=['']*100
    mdeclare=[0]*100
    msuccessful=[0]*100
    for data in datas:  # 初始化
        sheetm[j] = data.major
        sheetc[j] = data.college
        j+=1
    for i in range(0, rows):  # 学院
        if flagc[i] != -1:
           major[mnum] = sheetm[i]
           college[mnum]=sheetc[i]
           for k in range(i + 1, rows + 1):
                if sheetm[k] == major[mnum]:
                    flagc[k] = -1
           mnum = mnum + 1
    for data in datas:
        for i in range(0, mnum):
            if data.major == major[i]:
                mdeclare[i] += 1
                if data.csc == "基金委录取":
                    msuccessful[i] += 1
    for i in range(0, mnum):
            dm.major=major[i]
            dm.college =college[i]
            dm.declare =mdeclare[i]
            dm.successful = msuccessful[i]
            dm.save()

def cj_analyse(request):#高数不及格人数表处理
    res = []
    d = request.GET
    datas=cj_summary.objects.all()
    datac=cj_college()
    rows=len(datas)
    cj=[{'college':"",'fail':0,"average":0}for i in range(15)]
    summary=[0]*2
    cnum=0#学院数
    i=0
    print(type(cj[0]['college']))
    for data in datas :
        flag=0
        for i in range(0,cnum):
           if data.college==cj[i]['college']:
             flag=1
             cj[i]['fail']+=1
             cj[i]['average'] +=int(data.score)
        if flag==0:
             cj[cnum]['college']=data.college
             cj[cnum]['fail']=1
             cj[cnum]['average']=int(data.score)
             cnum+=1
    print(cnum)
    for i in range(0,cnum):
        print(cj[i]['college'])
        print(cj[i]['fail'])
        datac.college=cj[i]['college']
        datac.fail=cj[i]['fail']
        datac.average=cj[i]['average']/cj[i]['fail']
        datac.save()
        summary[0]+=cj[i]['fail']
        summary[1]+=cj[i]['average']
        res.append({"college":cj[i]['college'],'fail':cj[i]['fail'],'average':cj[i]['average']})
    print(summary[0])
    datac.college='总计'
    datac.fail=summary[0]
    datac.average=summary[1]/summary[0]
    datac.save()
    return HttpResponse(json.dumps(res), content_type="application/json")
def cj_fractional(request):#按分数段查询
    res = []
    d = request.GET
    fstart=0#分数段左区间
    fend=60#分数段右区间
    if d['college']=='总计':
        datas=cj_summary.objects.all()
    else:
       datas=cj_summary.objects.all().filter(college=d['college'])
    if d['fstart'] is not '':
        fstart=d['fstart']
    if d['fend'] is not '':
         fend=d['fend']
    if d['fstart'] is '' and d['fend'] is '':
         print('aaa')
         fr=[{"分数段":'',"人数":0} for i in range(6)]
         for i in range(6):
             fr[i]['分数段']=str(i*10)+'-'+str((i+1)*10)
         for data in datas:
            score=data.score
            if score<=10:
                fr[0]['人数']+=1
            elif  10<score<=20:
                fr[1]['人数'] += 1
            elif 20 < score <=30:
                fr[2]['人数'] += 1
            elif 30 < score <= 40:
                fr[3]['人数'] += 1
            elif 40 < score <= 50:
                fr[4]['人数'] += 1
            elif 50 < score <= 60:
                fr[5]['人数'] += 1
         for i in range(6):
                print('bbb')
                res.append(fr[i])
    else:
        num=0
        for data in datas:
           score = data.score
           if  int(fstart)<=score<=int(fend):

               num+=1
        res.append({"分数段":str(fstart)+'-'+str(fend),"人数":num})
    return HttpResponse(json.dumps(res), content_type="application/json")

def course_place__analyse(course):#地点统计
    dc=course_place()
    for i in range(0,17):
        datac=course_summary.objects.all().filter(college=course[i]['college'])
        place=['']*20
        classnum=[0]*20
        pnum=0#地点数
        for data in datac:
            flag = 0
            for j in range(0, pnum):
                if data.place == place[j]:
                    classnum[j] += 1
                    flag = 1
            if flag == 0:
                place[pnum] = data.place
                classnum[pnum] = 1
                pnum += 1
        for k in range(0,pnum):
            dc.college=course[i]['college']
            dc.place=place[k]
            dc.classnum=classnum[k]
            dc.save()

def course_analyse(request):#课程表处理
    print('aaa')
    res = []
    d = request.GET
    datas=course_summary.objects.all()
    datac=course_coll()
    rows=len(datas)
    course=[{'college':"",'coursenum':0,"classnum":0}for i in range(20)]
    summary=[0]*2
    cnum=0#学院数\
    crnum=0#课程数
    i=0
    for data in datas :
        flag=0
        for i in range(0,cnum):
           if data.college==course[i]['college']:
              course[i]['classnum']+=1
              flag=1
        if flag==0:
             course[cnum]['college']=data.college
             datac.college=data.college
             course[cnum]['classnum']=1
             cnum+=1

    for i in range(cnum):
            cour=['']*100
            cournum=0
            for data in datas :
              if course[i]['college']==data.college:
                 flag=0
                 for j in range(cournum):
                     if data.c_name==cour[j]:
                         flag=1
                 if flag==0:
                     cour[cournum]=data.c_name
                     cournum+=1
            course[i]['coursenum']=cournum
            print(course[i]['college'])

    for i in range(cnum):
        datac.college=course[i]['college']
        datac.coursenum = course[i]['coursenum']
        datac.classnum = course[i]['classnum']
        datac.save()
    course_place__analyse(course)
    return HttpResponse(json.dumps(res), content_type="application/json")
def course_details(request):#学院详情
    res=[]
    d=request.GET
    print(d)
    if d['kind']=='place':
        datas = course_summary.objects.filter(college=d['college'],place=d['parameter'])
    for data in datas:
        json_dict = model_to_dict(data)
        print()
        res.append(json_dict)
    print(res)
    return HttpResponse(json.dumps(res), content_type="application/json")
def course_college(request):#学院开课数统计
    res = []
    d = request.GET
    datas=course_coll.objects.all()
    scour=0
    sclass=0
    for data in datas:
        res.append({'college':data.college,"coursenum":data.coursenum,"classnum":data.classnum})
        scour+=data.coursenum
        sclass+=data.classnum
    res.sort(key=lambda x: (x.get(d['st'], 0)), reverse=True)
    res.insert(0, {"college": '总计', "coursenum": scour, "classnum": sclass})
    print(res)
    return HttpResponse(json.dumps(res), content_type="application/json")
def cr_place(request):#学院上课地点
    res = []
    d=request.GET
    if d['college'] == '总计':
        datas = course_place.objects.all()
    else:
        datas = course_place.objects.all().filter(college=d['college'])
    for data in datas:
        res.append({'college':data.college,'place':data.place,'classnum':data.classnum})
    return HttpResponse(json.dumps(res), content_type="application/json")

def emotion_analyse_figure3(request):#总表数据处理
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    d = request.GET
    cnum=0#学院数
    gnum=0#年级数
    tnum=2#联培，学位两种类型
    tmnum=0#留学期限数
    datas=gp_summary.objects.all()
    dc=college_declare()
    dg=grade_declare()
    dt=type_declare()
    dtime=time_declare()
    rows=len(datas)#总表长度
    flagc = [0] * (rows + 1)#学院的标记
    flagg = [0] * (rows + 1)#在读年级的标记
    flagt = [0] * (rows + 1)  # time的标记
    college = [''] * 100
    grade=[''] * 100
    time= [''] * 100
    type=['联培','学位']
    j=0
    sheete=[0]* (rows + 1)
    sheetg =[0] * (rows + 1)
    sheett = [0] * (rows + 1)
    for data in datas:#初始化
        sheete[j] = data.college
        sheetg[j] = data.grade
        sheett[j] = data.time_mon
        j +=1
    for i in range(0, rows):#学院
        if flagc[i] != -1:
            college[cnum] = sheete[i]
            for k in range(i + 1, rows + 1):
                if sheete[k] == college[cnum]:
                    flagc[k] = -1
            cnum = cnum + 1
    for i in range(0, rows):  #在读年级
        if flagg[i] != -1:
            grade[gnum] = sheetg[i]
            for k in range(i + 1, rows + 1):
                if sheetg[k] == grade[gnum]:
                    flagg[k] = -1
            gnum = gnum + 1
    for i in range(0, rows):  # 留学年限
        if flagt[i] != -1:
            if sheett[i]=='':
                time[tmnum]='未知'
            time[tmnum] = sheett[i]
            for k in range(i + 1, rows + 1):
                if sheett[k] == time[tmnum]:
                    flagt[k] = -1
            tmnum = tmnum + 1
    #学院
    cdeclare=[0]*cnum
    csuccessful=[0]*cnum
    for data in datas:
        for i in range(0,cnum):
            if data.college==college[i]:
                cdeclare[i]+=1
                if data.csc=="基金委录取":
                   csuccessful[i]+=1
    for i in range(0, cnum):
        dc.college=college[i]
        dc.declare=cdeclare[i]
        dc.successful=csuccessful[i]
        dc.save()
    #在读年级
    gdeclare = [0] * gnum
    gsuccessful = [0] * gnum
    for data in datas:
        for i in range(0, gnum):
            if data.grade == grade[i]:
                gdeclare[i] += 1
                if data.csc == "基金委录取":
                    gsuccessful[i] += 1
    for i in range(0, gnum):
        dg.grade = grade[i]
        dg.declare = gdeclare[i]
        dg.successful = gsuccessful[i]
        dg.save()
    #联培/学位
    tdeclare = [0] * 2
    tsuccessful = [0] * 2
    for data in datas:
        for i in range(0, 2):
            if data.type == type[i]:
                tdeclare[i] += 1
                if data.csc == "基金委录取":
                    tsuccessful[i] += 1
    for i in range(0, 2):
        dt.type = type[i]
        dt.declare = tdeclare[i]
        dt.successful = tsuccessful[i]
        dt.save()
    #留学年限
    tmdeclare = [0] * tmnum
    tmsuccessful = [0] * tmnum
    for data in datas:
        for i in range(0, tmnum):
            if data.time_mon == time[i]:
                tmdeclare[i] += 1
                if data.csc == "基金委录取":
                    tmsuccessful[i] += 1
    for i in range(0, tmnum):
        dtime.time = time[i]
        dtime.declare = tmdeclare[i]
        dtime.successful = tmsuccessful[i]
        dtime.save()
    major()
    gp_world_declare()

    return HttpResponse(json.dumps(res), content_type="application/json")



