from django.shortcuts import render
from Conference.models import *
import json
from django.http import HttpResponseRedirect, HttpResponse
from emotionanalysis.Function import *
import time
from django.forms.models import model_to_dict
# Create your views here.
def cf_sum19():#19国际会议总表数据处理,将总表按学院，
    cnum=0#学院数
    datas=cf_summary19.objects.all()
    dc=cf_college_declare_19()
    rows=len(datas)#总表长度
    flagc = [0] * (rows + 1)#学院的标记
    college = [''] * 100#学院名称
    j=0
    sheetc=[0]* (rows + 1)#存储学院名称
    for data in datas:#初始化
        sheetc[j] = data.college
        j +=1
    #学院
    for i in range(0, rows):#遍历总表
        if flagc[i] != -1:#第一次出现的学院
            college[cnum] = sheetc[i]
            for k in range(i + 1, rows + 1):
                if sheetc[k] == college[cnum]:
                    flagc[k] = -1
            cnum = cnum + 1
    #学院
    cdeclare=[0]*cnum
    csuccessful=[0]*cnum
    for data in datas:
        for i in range(0,cnum):
            if data.college==college[i]:
               cdeclare[i]+=1
               if data.approved=="通过":
                   csuccessful[i]+=1
    for i in range(0, cnum):
        dc.college=college[i]
        dc.declare=cdeclare[i]
        dc.successful=csuccessful[i]
        dc.save()
    ctnum=0#国家数
    dct = cf_country_declare_19()
    rows = len(datas)  # 总表长度
    flagct = [0] * (rows + 1)  # 国家的标记
    country = [''] * 100  # 国家名称
    j = 0
    sheetct = [0] * (rows + 1)  # 存储国家名称
    for data in datas:  # 初始化
        sheetct[j] = data.country
        j += 1
    # 国家
    for i in range(0, rows):  # 遍历总表
        if flagct[i] != -1:  # 第一次出现的国家
            country[ctnum] = sheetct[i]
            for k in range(i + 1, rows + 1):
                if sheetct[k] == country[ctnum]:
                    flagct[k] = -1
            ctnum = ctnum + 1
    # 国家
    ctdeclare = [0] * ctnum
    ctsuccessful = [0] * ctnum
    for data in datas:
        for i in range(0, ctnum):
            if data.country == country[i]:
                ctdeclare[i] += 1
                if data.approved == "通过":
                    ctsuccessful[i] += 1
    for i in range(0, ctnum):
        dct.country = country[i]
        dct.declare = ctdeclare[i]
        dct.successful = ctsuccessful[i]
        dct.save()
    mjnum = 0  # 专业数
    dmj = cf_major_declare_19()
    rows = len(datas)  # 总表长度
    flagmj = [0] * (rows + 1)  # 专业的标记
    major= [''] * 100  # 专业名称
    j = 0
    sheetmj = [0] * (rows + 1)  # 存储专业名称
    for data in datas:  # 初始化
        sheetmj[j] = data.major
        j += 1
    # 专业
    for i in range(0, rows):  # 遍历总表
        if flagmj[i] != -1:  # 第一次出现的国家
            major[mjnum] = sheetmj[i]
            for k in range(i + 1, rows + 1):
                if sheetmj[k] == major[mjnum]:
                    flagmj[k] = -1
            mjnum = mjnum + 1
    # 专业
    mjdeclare = [0] * mjnum
    mjsuccessful = [0] * mjnum
    for data in datas:
        for i in range(0, mjnum):
            if data.major == major[i]:
                mjdeclare[i] += 1
                if data.approved == "通过":
                    mjsuccessful[i] += 1
    for i in range(0, mjnum):
        dmj.major = major[i]
        dmj.declare = mjdeclare[i]
        dmj.successful = mjsuccessful[i]
        dmj.save()
    cdnum = 0  # 状态
    dcd= cf_condition_declare_19()
    rows = len(datas)  # 总表长度
    flagcd= [0] * (rows + 1)  # 专业的标记
    condition = [''] * 100  # 专业名称
    j = 0
    sheetcd = [0] * (rows + 1)  # 存储专业名称
    for data in datas:  # 初始化
        sheetcd[j] = data.condition
        j += 1
    # 专业
    for i in range(0, rows):  # 遍历总表
        if flagcd[i] != -1:  # 第一次出现的国家
            condition[cdnum] = sheetcd[i]
            for k in range(i + 1, rows + 1):
                if sheetcd[k] == condition[cdnum]:
                    flagcd[k] = -1
            cdnum = cdnum + 1
    # 专业
    cddeclare = [0] * cdnum
    cdsuccessful = [0] * cdnum
    for data in datas:
        for i in range(0, cdnum):
            if data.condition == condition[i]:
                cddeclare[i] += 1
                if data.approved == "通过":
                    cdsuccessful[i] += 1
    for i in range(0, cdnum):
        dcd.condition= condition[i]
        dcd.declare = cddeclare[i]
        dcd.successful = cdsuccessful[i]
        dcd.save()
    mtnum = 0  # 导师数
    dmt = cf_mentor_declare_19()
    rows = len(datas)  # 总表长度
    flagmt = [0] * (rows + 1)  # 专业的标记
    mentor= [''] * 100  # 导师姓名
    j = 0
    sheetmt = [0] * (rows + 1)  # 存储导师姓名
    for data in datas:  # 初始化
        sheetmt[j] = data.mentor
        j += 1
    # 导师
    for i in range(0, rows):  # 遍历总表
        if flagmt[i] != -1:  # 第一次出现的国家
            mentor[mtnum] = sheetmt[i]
            for k in range(i + 1, rows + 1):
                if sheetmt[k] == mentor[mtnum]:
                    flagmt[k] = -1
            mtnum = mtnum + 1
    # 专业
    mtdeclare = [0] * mtnum
    mtsuccessful = [0] * mtnum
    for data in datas:
        for i in range(0, mtnum):
            if data.mentor== mentor[i]:
                mtdeclare[i] += 1
                if data.approved == "通过":
                    mtsuccessful[i] += 1
    for i in range(0, mtnum):
        dmt.mentor = mentor[i]
        dmt.declare = mtdeclare[i]
        dmt.successful = mtsuccessful[i]
        dmt.save()
    cfnum = 0  #会议数
    dcf = cf_cfname_declare_19()
    rows = len(datas)  # 总表长度
    flagcf = [0] * (rows + 1)  # 专业的标记
    cfname= [''] * 100  # 导师姓名
    j = 0
    sheetcf = [0] * (rows + 1)  # 存储导师姓名
    for data in datas:  # 初始化
        sheetcf[j] = data.cfname
        j += 1
    # 导师
    for i in range(0, rows):  # 遍历总表
        if flagcf[i] != -1:  # 第一次出现的国家
            cfname[cfnum] = sheetcf[i]
            for k in range(i + 1, rows + 1):
                if sheetcf[k] == cfname[cfnum]:
                    flagcf[k] = -1
            cfnum = cfnum + 1
    # 专业
    cfdeclare = [0] * cfnum
    cfsuccessful = [0] * cfnum
    for data in datas:
        for i in range(0, cfnum):
            if data.cfname== cfname[i]:
                cfdeclare[i] += 1
                if data.approved == "通过":
                    cfsuccessful[i] += 1
    for i in range(0, cfnum):
        dcf.cfname = cfname[i]
        dcf.declare = cfdeclare[i]
        dcf.successful = cfsuccessful[i]
        dcf.save()
    fnum = 0  # 参会形式数
    df = cf_form_declare_19()
    rows = len(datas)  # 总表长度
    flagf = [0] * (rows + 1)  # 专业的标记
    form = [''] * 100  # 导师姓名
    j = 0
    sheetf = [0] * (rows + 1)  # 存储导师姓名
    for data in datas:  # 初始化
        sheetf[j] = data.form
        j += 1
    # 参会形式
    for i in range(0, rows):  # 遍历总表
        if flagf[i] != -1:  # 第一次出现的国家
            form[fnum] = sheetf[i]
            for k in range(i + 1, rows + 1):
                if sheetf[k] == form[fnum]:
                    flagf[k] = -1
            fnum = fnum + 1
    # 参会形式
    fdeclare = [0] * fnum
    fsuccessful = [0] * fnum
    for data in datas:
        for i in range(0, fnum):
            if data.form ==form[i]:
                fdeclare[i] += 1
                if data.approved == "通过":
                    fsuccessful[i] += 1
    for i in range(0, fnum):
        df.form= form[i]
        df.declare = fdeclare[i]
        df.successful = fsuccessful[i]
        df.save()
#会议类型
    catenum = 4 # 会议类型数
    dcate= cf_category_declare_19()
    category= ['A','B','C','其它'] #会议类别
    catedeclare = [0] * catenum
    catesuccessful = [0] * catenum
    for data in datas:
        for i in range(0, catenum):
            if data.cfcategory ==category[i]:
                catedeclare[i] += 1
                if data.approved == "通过":
                    catesuccessful[i] += 1
    for i in range(0, catenum):
        dcate.category= category[i]
        dcate.declare = catedeclare[i]
        dcate.successful = catesuccessful[i]
        dcate.save()
def cf_college_declare19(request):#留学统计-学院申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    #cf_sum19()
    d=request.GET
    datas =cf_college_declare_19.objects.all()
    sdeclare=0
    ssuccessful=0
    for data in datas:
        per=float(data.successful)/float(data.declare)*100
        res.append({"college":data.college,"declare":data.declare,"successful":data.successful,'per':per})
        #res.append({"college": data.college, "declare": data.declare, "successful": data.successful})
        ssuccessful+=data.successful
        sdeclare+=data.declare
   # sper=ssuccessful/sdeclare
    res.sort(key=lambda x:(x.get(d['st'],0)),reverse=True)
    #res.insert(0,{"college":'总计',"declare":sdeclare,"successful":ssuccessful,"per":sper})
    return HttpResponse(json.dumps(res), content_type="application/json")
def cf_major_declare19(request):#留学统计-学院申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
   # cf_sum19()
    d=request.GET
    datas =cf_major_declare_19.objects.all()
    sdeclare=0
    ssuccessful=0
    for data in datas:
        per=float(data.successful)/float(data.declare)*100
        res.append({"major":data.major,"declare":data.declare,"successful":data.successful,'per':per})
        #res.append({"college": data.college, "declare": data.declare, "successful": data.successful})
        ssuccessful+=data.successful
        sdeclare+=data.declare
   # sper=ssuccessful/sdeclare
    res.sort(key=lambda x:(x.get(d['st'],0)),reverse=True)
    #res.insert(0,{"college":'总计',"declare":sdeclare,"successful":ssuccessful,"per":sper})
    return HttpResponse(json.dumps(res), content_type="application/json")
def cf_category_declare19(request):#留学统计-学院申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    #cf_sum19()
    d=request.GET
    datas =cf_category_declare_19.objects.all()
    sdeclare=0
    ssuccessful=0
    print(d['st'])
    for data in datas:
        per=float(data.successful)/float(data.declare)*100
        res.append({"category":data.category,"declare":data.declare,"successful":data.successful,'per':per})
        #res.append({"college": data.college, "declare": data.declare, "successful": data.successful})
        ssuccessful+=data.successful
        sdeclare+=data.declare
   # sper=ssuccessful/sdeclare
    res.sort(key=lambda x:(x.get(d['st'],0)),reverse=True)
    #res.insert(0,{"college":'总计',"declare":sdeclare,"successful":ssuccessful,"per":sper})
    return HttpResponse(json.dumps(res), content_type="application/json")
def cf_cfname_declare19(request):#留学统计-学院申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    #cf_sum19()
    d=request.GET
    datas =cf_cfname_declare_19.objects.all()
    sdeclare=0
    ssuccessful=0
    print(d['st'])
    for data in datas:
        per=float(data.successful)/float(data.declare)*100
        res.append({"cfname":data.cfname,"declare":data.declare,"successful":data.successful,'per':per})
        #res.append({"college": data.college, "declare": data.declare, "successful": data.successful})
        ssuccessful+=data.successful
        sdeclare+=data.declare
   # sper=ssuccessful/sdeclare
    res.sort(key=lambda x:(x.get(d['st'],0)),reverse=True)
    #res.insert(0,{"college":'总计',"declare":sdeclare,"successful":ssuccessful,"per":sper})
    return HttpResponse(json.dumps(res), content_type="application/json")
def cf_condition_declare19(request):#留学统计-学院申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    #cf_sum19()
    d=request.GET
    datas =cf_condition_declare_19.objects.all()
    sdeclare=0
    ssuccessful=0
    print(d['st'])
    for data in datas:
        per=float(data.successful)/float(data.declare)*100
        res.append({"condition":data.condition,"declare":data.declare,"successful":data.successful,'per':per})
        #res.append({"college": data.college, "declare": data.declare, "successful": data.successful})
        ssuccessful+=data.successful
        sdeclare+=data.declare
   # sper=ssuccessful/sdeclare
    res.sort(key=lambda x:(x.get(d['st'],0)),reverse=True)
    #res.insert(0,{"college":'总计',"declare":sdeclare,"successful":ssuccessful,"per":sper})
    return HttpResponse(json.dumps(res), content_type="application/json")
def cf_mentor_declare19(request):#留学统计-学院申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    #cf_sum19()
    d=request.GET
    datas =cf_mentor_declare_19.objects.all()
    sdeclare=0
    ssuccessful=0
    print(d['st'])
    for data in datas:
        per=float(data.successful)/float(data.declare)*100
        res.append({"mentor":data.mentor,"declare":data.declare,"successful":data.successful,'per':per})
        #res.append({"college": data.college, "declare": data.declare, "successful": data.successful})
        ssuccessful+=data.successful
        sdeclare+=data.declare
   # sper=ssuccessful/sdeclare
    res.sort(key=lambda x:(x.get(d['st'],0)),reverse=True)
    #res.insert(0,{"college":'总计',"declare":sdeclare,"successful":ssuccessful,"per":sper})
    return HttpResponse(json.dumps(res), content_type="application/json")
def cf_form_declare19(request):#留学统计-学院申报人数，成功人数
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    #cf_sum19()
    d=request.GET
    datas =cf_form_declare_19.objects.all()
    sdeclare=0
    ssuccessful=0
    print(d['st'])
    for data in datas:
        per=float(data.successful)/float(data.declare)*100
        res.append({"form":data.form,"declare":data.declare,"successful":data.successful,'per':per})
        #res.append({"college": data.college, "declare": data.declare, "successful": data.successful})
        ssuccessful+=data.successful
        sdeclare+=data.declare
   # sper=ssuccessful/sdeclare
    res.sort(key=lambda x:(x.get(d['st'],0)),reverse=True)
    #res.insert(0,{"college":'总计',"declare":sdeclare,"successful":ssuccessful,"per":sper})
    return HttpResponse(json.dumps(res), content_type="application/json")
def cf_world_declare19(request):#留学统计-申报人数，成功人数 地图统计
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    #cf_sum19()
    d = request.GET
    print(d['st'])
    datas = cf_country_declare_19.objects.all()
    sdeclare = 0
    ssuccessful = 0
    for data in datas:
        per = float(data.successful) / float(data.declare) * 100
        res.append({"country": data.country, "declare": data.declare, "successful": data.successful, 'per': per})
        # res.append({"college": data.college, "declare": data.declare, "successful": data.successful})
        ssuccessful += data.successful
        sdeclare += data.declare
    # sper=ssuccessful/sdeclare
    res.sort(key=lambda x: (x.get(d['st'], 0)), reverse=True)
    # res.insert(0,{"college":'总计',"declare":sdeclare,"successful":ssuccessful,"per":sper})
    if d['st']=="declare":
        datas=cf_summary19.objects.all()
        res1, map0 = world(datas, "会议国家分布图—申报")
    else:
        datas=cf_summary19.objects.filter(approved="通过")
        res2, map0 = world(datas, "会议国家分布图—审核通过")
    map0.render(path="./html1/sample_skin/demo/cf_nworld_19.html")
    return HttpResponse(json.dumps(res), content_type="application/json")
def cf_details_19(request):#学院详情
    res=[]
    d=request.GET
    print(d["parameter"])
    print(d["kind"])
    parameter=d['parameter'];
    if  d['kind']=='college':
        datas = cf_summary19.objects.filter(college=parameter)
        for data in datas:
             json_dict = model_to_dict(data)
             res.append(json_dict)
    elif d['kind']=='country':
        datas = cf_summary19.objects.filter(country=parameter)
        for data in datas:
             json_dict = model_to_dict(data)
             res.append(json_dict)
    elif d['kind']=='category':
        datas = cf_summary19.objects.filter(cfcategory=parameter)
        for data in datas:
             json_dict = model_to_dict(data)
             res.append(json_dict)
    elif d['kind']=='major':
        datas = cf_summary19.objects.filter(major=parameter)
        for data in datas:
             json_dict = model_to_dict(data)
             res.append(json_dict)
    elif d['kind']=='condition':
        datas = cf_summary19.objects.filter(condition=parameter)
        for data in datas:
             json_dict = model_to_dict(data)
             res.append(json_dict)
    elif d['kind']=='mentor':
        datas = cf_summary19.objects.filter(mentor=parameter)
        for data in datas:
             json_dict = model_to_dict(data)
             res.append(json_dict)
    elif d['kind'] == 'cfname':
        datas = cf_summary19.objects.filter(cfname=parameter)
        for data in datas:
            json_dict = model_to_dict(data)
            res.append(json_dict)
    elif d['kind'] == 'form':
        datas = cf_summary19.objects.filter(form=parameter)
        for data in datas:
            json_dict = model_to_dict(data)
            res.append(json_dict)
    return HttpResponse(json.dumps(res), content_type="application/json")
