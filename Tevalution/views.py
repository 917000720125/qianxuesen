from django.shortcuts import render
from Tevalution.models import *
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from emotionanalysis.Function import *
# Create your views here.
#学院综合成绩
collegelist = {'2015-2016春学期': te_college_16c, '2015-2016秋学期': te_college_16q, '2016-2017春学期': te_college_17c,
               '2016-2017秋学期': te_college_17q, '2017-2018春学期': te_college_18c, '2017-2018秋学期': te_college_18q,
               '2018-2019春学期': te_college_19c, '2018-2019秋学期': te_college_19q, '2019-2020春学期': te_college_20c,
               '2019-2020秋学期': te_college_20q}
courselist = {'2015-2016春学期': te_course_16c(), '2015-2016秋学期': te_course_16q(), '2016-2017春学期': te_course_17c(),
              '2016-2017秋学期': te_course_17q(), '2017-2018春学期': te_course_18c(), '2017-2018秋学期': te_course_18q(),
              '2018-2019春学期': te_course_19c(), '2018-2019秋学期': te_course_19q(), '2019-2020春学期': te_course_20c(),
              '2019-2020秋学期': te_course_20q()}
courselist1 = {'2015-2016春学期': te_course_16c, '2015-2016秋学期': te_course_16q, '2016-2017春学期': te_course_17c,
              '2016-2017秋学期': te_course_17q, '2017-2018春学期': te_course_18c, '2017-2018秋学期': te_course_18q,
              '2018-2019春学期': te_course_19c, '2018-2019秋学期': te_course_19q, '2019-2020春学期': te_course_20c,
              '2019-2020秋学期': te_course_20q}
def TE_college(request):
    res = []
    d=request.GET
    if  len(d)!=0:
        datas =collegelist.get(d['semester']).objects.all()
        print(datas)
    else:
        datas=te_college_20c.objects.all()
    save_score=0
    length=0
    for data in datas:
        res.append({'college': data.college, "ave_score": data.ave_score})
        save_score += data.ave_score
        length+=1
        #sclass += data.classnum
    save_score=round(save_score/length,1)
    res.sort(key=lambda x: (x.get('ave_score', 0)), reverse=True)
    res.insert(0, {"college": '均分', "ave_score": save_score})
    print(res)
    return HttpResponse(json.dumps(res), content_type="application/json")
def TE_course(request):
    res=[]
    length=0
    save_score=0
    d=request.GET
    datas = courselist1.get(d['semester']).objects.all()
    print('course')
    print(datas)
    #datas=te_course_20c.objects.all()
    datas=course_type(datas,d['project'])
    datas=datas.filter(college=d['college'], c_name__contains=d['cname'])
    if d['fstart'] is not '':
        fstart = float(d['fstart'])
    else:
        fstart = 100
    if d['fend'] is not '':
        fend = float(d['fend'])
    else:
        fend = 0
    if d['project'] == '英文':
        for data in datas:
            if is_all_eng(data.c_name) ==1:
                if data.ave_score <= fstart and data.ave_score >= fend:
                     res.append({'c_id': data.c_id, 'c_name': data.c_name, "ave_score": data.ave_score})
                     save_score += data.ave_score
                     length=length+1
    elif d['project'] == '中文':
        for data in datas:
            if is_all_eng(data.c_name) ==0:
                if data.ave_score <= fstart and data.ave_score >= fend:
                    res.append({'c_id': data.c_id, 'c_name': data.c_name, "ave_score": data.ave_score})
                    save_score += data.ave_score
                    length = length + 1
    else:
        for data in datas:
            if data.ave_score <= fstart and data.ave_score >= fend:
                res.append({'c_id': data.c_id, 'c_name': data.c_name, "ave_score": data.ave_score})
                save_score += data.ave_score
                length = length + 1
    save_score = round(save_score/length, 1)
    res.sort(key=lambda x: (x.get('ave_score', 0)), reverse=True)
    res.insert(0, {"c_name": '均分', "ave_score": save_score})
    # res.insert(0, {"college": '总计', "coursenum": scour, "classnum": sclass})
    print(res)
    return HttpResponse(json.dumps(res), content_type="application/json")
def TE_class(request):
    res=[]
    d=request.GET
    print('class')
    print(d)
    parameter=d['parameter']
    semester=d['semester']
    if d['kind'] == 'course':
       datas = Tea_evalution_summary.objects.filter(c_id=parameter,semester=semester)
    elif d['kind'] == 'banji':
        cl_name=d['parameter']
        datas = Tea_evalution_summary.objects.filter(semester=semester, cl_name=cl_name)
    if d['fstart'] is not '':
        fstart = float(d['fstart'])
    else:
        fstart = 100
    if d['fend'] is not '':
        fend = float(d['fend'])
    else:
        fend = 0
    for data in datas:
        if data.score <= fstart and data.score >= fend:
         res.append({'cl_name':data.cl_name,"t_id":data.t_id,"t_name":data.t_name,"number":data.number,'score':data.score,'advise':data.advise})
    res.sort(key=lambda x: (x.get('score', 0)), reverse=True)
    return HttpResponse(json.dumps(res), content_type="application/json")
def TE_Getlist(request):
    res = []
    d =request.GET
    print(d)
    datas=courselist1.get(d['semester']).objects.all()
    datas=course_type(datas,d['ctype'])
    datas = datas.filter(college=d['college'])
    i = 1
    if d['ctype']=='英文':
       for data in datas:
           if is_all_eng(data.c_name)==1:
              res.append({'value': i, "key": data.c_name,'suggest':data.c_name})
              i = i + 1
    elif d['ctype']=='中文':
        for data in datas:
            if is_all_eng(data.c_name)==0:
                res.append({'value': i, "key": data.c_name, 'suggest': data.c_name})
                i = i + 1
    else:
        for data in datas:
            res.append({'value': i, "key": data.c_name, 'suggest': data.c_name})
            i = i + 1
    return HttpResponse(json.dumps(res), content_type="application/json")
def TE_GetClist(request):#获取班级
    res = []
    d =request.GET
    datas=Tea_evalution_summary.objects.filter(c_id=d['c_id'],semester=d['semester'])
    banji=[]
    i = 0
    for data in datas:
        if data.cl_name not in banji:
           banji.append(data.cl_name)
    for data in banji:
         res.append({'value': i, "key": data,'suggest':data})
         i = i + 1
    return HttpResponse(json.dumps(res), content_type="application/json")
def TE_tiaotingke(request):#更加教师编号和班级名称获取平均成绩和调停课次数
    res = []
    d =request.GET
    t_id=d['t_id']
    cl_name=d['cl_name']
    datas=Tea_evalution_summary.objects.filter(cl_name=cl_name,t_id=t_id)
    t_name=datas[0].t_name
    data1 = te_tiaotingke.objects.filter(t_name=t_name,cl_name=cl_name)
    semester,ave_score,times=tiaotingke(datas,data1)
    for i in range(0,len(semester)):
      res.append({'t_name':t_name,'t_id':t_id,'cl_name':cl_name,'semester': semester[i], "Ave_score": ave_score[i],'times':times[i]})
    return HttpResponse(json.dumps(res), content_type="application/json")
def tiaotingke(datas,data1):
    semester=[]
    ave_score=[]
    times=[]
    for data in datas:
        if data.semester not in semester:
            semester.append(data.semester)
    for i in semester:
        datascore=datas.filter(semester=i)
        datatimes=data1.filter(semester=i)
        if len(datascore)!=0:
            sumscore=0
            for data in datascore:
                sumscore=sumscore+data.score
            ave_score.append(round(sumscore/len(datascore),1))
        else:
            ave_score.append(0)
        times.append(len(datatimes))
    return semester,ave_score,times
#学院综合成绩
def TE_college_20c(request):
    res = []
    datas = te_college_20c.objects.all()
    save_score=0
    for data in datas:
        res.append({'college': data.college, "ave_score": data.ave_score})
        save_score += data.ave_score
        #sclass += data.classnum
    save_score=round(save_score/len(datas),1)
    res.sort(key=lambda x: (x.get('ave_score', 0)), reverse=True)
    res.insert(0, {"college": '均分', "ave_score": save_score})
    print(res)
    return HttpResponse(json.dumps(res), content_type="application/json")
#判断是否是纯英文
def is_all_eng(strs):
    import string
    strs=strs.replace(" ", "")
    strs=strs.replace("-", "")
    strs = strs.replace("&", "")
    print(strs)
    for i in strs:
        if i not in string.ascii_lowercase+string.ascii_uppercase:
            return 0
    return 1
def course_type(datas,course_type):
    if course_type=='硕士':
        newdatas=datas.filter(c_id__startswith='S')
    elif course_type=='博士':
        newdatas = datas.filter(c_id__startswith='B')
    elif course_type=='L':
        newdatas = datas.filter(c_id__startswith='L')
    else:
        newdatas=datas
    return newdatas
#课程
def TE_course_20c(request):
    #course()
    res=[]
    length=0
    save_score=0
    d=request.GET
    print(d)
    datas=te_course_20c.objects.all()
    datas=course_type(datas,d['project'])
    datas=datas.filter(college=d['college'], c_name__contains=d['cname'])
    if d['fstart'] is not '':
        fstart = float(d['fstart'])
    else:
        fstart = 100
    if d['fend'] is not '':
        fend = float(d['fend'])
    else:
        fend = 0
    if d['project'] == '英文':
        for data in datas:
            if is_all_eng(data.c_name) ==1:
                if data.ave_score <= fstart and data.ave_score >= fend:
                     res.append({'c_id': data.c_id, 'c_name': data.c_name, "ave_score": data.ave_score})
                     save_score += data.ave_score
                     length=length+1
    elif d['project'] == '中文':
        for data in datas:
            if is_all_eng(data.c_name) ==0:
                if data.ave_score <= fstart and data.ave_score >= fend:
                    res.append({'c_id': data.c_id, 'c_name': data.c_name, "ave_score": data.ave_score})
                    save_score += data.ave_score
                    length = length + 1
    else:
        for data in datas:
            if data.ave_score <= fstart and data.ave_score >= fend:
                res.append({'c_id': data.c_id, 'c_name': data.c_name, "ave_score": data.ave_score})
                save_score += data.ave_score
                length = length + 1
    save_score = round(save_score/length, 1)
    res.sort(key=lambda x: (x.get('ave_score', 0)), reverse=True)
    res.insert(0, {"c_name": '均分', "ave_score": save_score})
    # res.insert(0, {"college": '总计', "coursenum": scour, "classnum": sclass})
    print(res)
    return HttpResponse(json.dumps(res), content_type="application/json")
def TE_class_20c(request):
    res=[]
    d=request.GET
    parameter=d['parameter']
    print(d)
    if d['kind'] == 'course':
       datas = Tea_evalution_summary_20c.objects.filter(c_id=parameter)
    if d['fstart'] is not '':
        fstart = float(d['fstart'])
    else:
        fstart = 100
    if d['fend'] is not '':
        fend = float(d['fend'])
    else:
        fend = 0
    for data in datas:
        if data.score <= fstart and data.score >= fend:
         res.append({'cl_name':data.cl_name,"t_id":data.t_id,"t_name":data.t_name,"number":data.number,'score':data.score,'advise':data.advise})
    res.sort(key=lambda x: (x.get('score', 0)), reverse=True)
    return HttpResponse(json.dumps(res), content_type="application/json")
