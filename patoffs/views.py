from django.shortcuts import render
from patoffs.models import *
import json
from django.http import HttpResponseRedirect, HttpResponse
from emotionanalysis.Function import *
from django.forms.models import model_to_dict
from collections import Counter
# Create your views here.
# def Pat_GetCollegelist(require):
#     d=require.GET
#     res=[]
#     if d['kind']=='paper':
#        res= paper()
#     print(res)
#     return HttpResponse(json.dumps(res), content_type="application/json")
# def Pat_GetMajorlist(require):
#     d=require.GET
#     res=[]
#     kind=d['kind']
#     college=d['college']
#     if kind=='paper':
#         res=paper_major(college)
#     return HttpResponse(json.dumps(res), content_type="application/json")
def paper():
    datas=paper_summary.objects.values('college').distinct()
    res=[]
    for index,data in enumerate(datas):
        res.append({'value': index, "key": data['college'], 'suggest': data['college']})
    return res
def paper_college(require):
    datas = paper_summary.objects.values_list('college')
    res = []
    result = Counter(datas).most_common()
    for i in result:
        print(i[0][0])
        print(i[1])
        res.append({'college': i[0][0], 'number': i[1]})
    return HttpResponse(json.dumps(res), content_type="application/json")
def paper_all(require):
    d=require.GET
    res=[]
    if len(d)==0:
       kind='college'
    else:
        kind = d['kind']
        print('kind',end='')
        print(kind)
        if kind=='学院':
           kind='college'
        elif kind=='专业':
            kind='major'
        elif kind=='学生类别':
            kind='s_type'
        elif kind=='排名':
            kind='rank'
        elif kind=='发表情况':
            kind='publish'
        elif kind=='收录期刊':
            kind='included'
    res=paper_kind(kind)
    return HttpResponse(json.dumps(res), content_type="application/json")
def paper_kind(kind):
    if kind=='included':
        res=paper_included()
        print(res)
    elif kind=='year':
        res=paper_year()
        print(res)
    else:
     datas=paper_summary.objects.values_list(kind)
     res=[]
     result=Counter(datas).most_common()
     for i in result:
        print(i[0][0])
        print(i[1])
        res.append({'key':i[0][0],'number':i[1]})
    return res
def paper_included():
    res=[]
    list=['EI','SCI',"CSSCI",'ISTP','其他']
    number=[0,0,0,0,0]
    datas=paper_summary.objects.all()
    for data in datas:
        for i in range(0,len(list)):
            if list[i] in data.included:
                number[i]=number[i]+1
    number[4]=len(datas)-(number[0]+number[1]+number[2]+number[3])
    print(number)
    for i in range(1,4):
        res.append({'key':list[i],'number':number[i]})
    return res
def paper_year():
    datas = paper_summary.objects.values_list('year')
    res=[]
    yearlist=[]
    for data in datas:
        year=data[0][:4]
        print(year)
        yearlist.append(year)
    result = Counter(yearlist).most_common()
    for i in result:
        year=i[0]
        res.append({'key': year, 'number': i[1]})
    return res
def paper_details(require):
    d=require.GET
    res=[]
    option={}
    college=d['college']
    kind=d['option']
    parameter=d['parameter']
    if kind == '学院':
        kind = 'college'
    elif kind == '专业':
        kind = 'major'
    elif kind == '学生类别':
        kind = 's_type'
    elif kind == '排名':
        kind = 'rank'
    elif kind == '发表情况':
        kind = 'publish'
    elif kind == '收录期刊':
        kind = 'included'
    option[kind]=parameter
    datas=paper_summary.objects.all()
    datas=datas.filter(college=college)
    datas=datas.filter(**option)
    for data in datas:
        res.append({'s_id':data.s_id,'s_name':data.s_name,'college':college,"major":data.major,'s_type':data.s_type,'title':data.title,'journal':data.journal,
                    'rank':data.rank,'publish':data.publish,'included':data.included})
    return HttpResponse(json.dumps(res), content_type="application/json")
#专利
def patent_college(require):
    datas = patent_summary.objects.values_list('college')
    res = []
    result = Counter(datas).most_common()
    for i in result:
        print(i[0][0])
        print(i[1])
        res.append({'college': i[0][0], 'number': i[1]})
    return HttpResponse(json.dumps(res), content_type="application/json")
def patent_all(require):
    d=require.GET
    print('patent_all')
    res=[]
    if len(d)==0:
       kind='college'
    else:
        kind = d['kind']
        print('kind',end='')
        print(kind)
        if kind=='学院':
           kind='college'
        elif kind=='专业':
            kind='major'
        elif kind=='学生类别':
            kind='s_type'
        elif kind=='排名':
            kind='rank'
        elif kind=='专利类型':
            kind='p_type'
        elif kind=='公告日期':
            kind='year'
    res=patent_kind(kind)
    return HttpResponse(json.dumps(res), content_type="application/json")
def patent_kind(kind):
    if kind=='year':
        res=patent_year()
        print(res)
    else:
     datas=patent_summary.objects.values_list(kind)
     res=[]
     result=Counter(datas).most_common()
     for i in result:
        print(i[0][0])
        print(i[1])
        res.append({'key':i[0][0],'number':i[1]})
    return res
def patent_year():
    datas = patent_summary.objects.values_list('year')
    res=[]
    yearlist=[]
    for data in datas:
        year=data[0][:4]
        print(year)
        yearlist.append(year)
    result = Counter(yearlist).most_common()
    for i in result:
        year=i[0]
        #print(year)
        res.append({'key': year, 'number': i[1]})
    return res
def patent_details(require):
    d=require.GET
    res=[]
    option={}
    college=d['college']
    kind=d['option']
    parameter=d['parameter']
    if kind == '学院':
        kind = 'college'
    elif kind == '专业':
        kind = 'major'
    elif kind == '学生类别':
        kind = 's_type'
    elif kind == '排名':
        kind = 'rank'
    elif kind == '专利类型':
        kind = 'p_type'
    elif kind == '公告日期':
        kind = 'year'
    option[kind]=parameter
    datas=patent_summary.objects.all()
    datas=datas.filter(college=college)
    datas=datas.filter(**option)
    for data in datas:
        res.append({'s_id':data.s_id,'s_name':data.s_name,'college':college,"major":data.major,'s_type':data.s_type,'title':data.title,'pat_id':data.pat_id,
                    'rank':data.rank,'p_type':data.p_type,'year':data.year})
    return HttpResponse(json.dumps(res), content_type="application/json")
#科研项目
def project_college(require):
    datas = project_summary.objects.values_list('college')
    res = []
    result = Counter(datas).most_common()
    for i in result:
        print(i[0][0])
        print(i[1])
        res.append({'college': i[0][0], 'number': i[1]})
    return HttpResponse(json.dumps(res), content_type="application/json")
def project_all(require):
    d=require.GET
    print('project_all')
    res=[]
    if len(d)==0:
       kind='college'
    else:
        kind = d['kind']
        print('kind',end='')
        print(kind)
        if kind=='学院':
           kind='college'
        elif kind=='专业':
            kind='major'
        elif kind=='学生类别':
            kind='s_type'
        elif kind=='来源':
            kind='source'
        elif kind=='负责人':
            kind='principal'
    res=project_kind(kind)
    return HttpResponse(json.dumps(res), content_type="application/json")
def project_kind(kind):
    if kind=='year':
        res=project_year()
        print(res)
    else:
     datas=project_summary.objects.values_list(kind)
     res=[]
     result=Counter(datas).most_common()
     for i in result:
        print(i[0][0])
        print(i[1])
        res.append({'key':i[0][0],'number':i[1]})
    return res
def project_year():
    datas = project_summary.objects.values_list('year')
    res = []
    yearlist = []
    for data in datas:
        year = data[0][:4]
        print(year)
        yearlist.append(year)
    result = Counter(yearlist).most_common()
    for i in result:
        year = i[0]
        # print(year)
        res.append({'key': year, 'number': i[1]})
    return res
def project_details(require):
    d=require.GET
    res=[]
    option={}
    college=d['college']
    kind=d['option']
    parameter=d['parameter']
    if kind == '学院':
        kind = 'college'
    elif kind == '专业':
        kind = 'major'
    elif kind == '学生类别':
        kind = 's_type'
    elif kind == '来源':
        kind = 'source'
    elif kind == '负责人':
        kind = 'principal'
    option[kind]=parameter
    datas=project_summary.objects.all()
    datas=datas.filter(college=college)
    datas=datas.filter(**option)
    for data in datas:
        res.append({'s_id':data.s_id,'s_name':data.s_name,'college':college,"major":data.major,'s_type':data.s_type,'project':data.project,'p_id':data.p_id,
                    'source':data.source,'fund':data.fund,'principal':data.principal})
    return HttpResponse(json.dumps(res), content_type="application/json")
#科研成果
def achievement_college(require):
    datas = achievement_summary.objects.values_list('college')
    res = []
    result = Counter(datas).most_common()
    for i in result:
        print(i[0][0])
        print(i[1])
        res.append({'college': i[0][0], 'number': i[1]})
    return HttpResponse(json.dumps(res), content_type="application/json")
def achievement_all(require):
    d=require.GET
    print('project_all')
    res=[]
    if len(d)==0:
       kind='college'
    else:
        kind = d['kind']
        print('kind',end='')
        print(kind)
        if kind=='学院':
           kind='college'
        elif kind=='专业':
            kind='major'
        elif kind=='学生类别':
            kind='s_type'
        elif kind=='排名':
            kind='rank'
        elif kind=='科研成果':
            kind='achievement'
        elif kind=='成果类型':
            kind='type'
        elif kind=='公告日期':
            kind='year'
    res=achievement_kind(kind)
    return HttpResponse(json.dumps(res), content_type="application/json")
def achievement_kind(kind):
    if kind=='year':
        res=project_year()
        print(res)
    else:
     datas=achievement_summary.objects.values_list(kind)
     res=[]
     result=Counter(datas).most_common()
     for i in result:
        print(i[0][0])
        print(i[1])
        res.append({'key':i[0][0],'number':i[1]})
    return res
def achievement_year():
    datas = achievement_summary.objects.values_list('year')
    res = []
    yearlist = []
    for data in datas:
        year = data[0][:4]
        print(year)
        yearlist.append(year)
    result = Counter(yearlist).most_common()
    for i in result:
        year = i[0]
        # print(year)
        res.append({'key': year, 'number': i[1]})
    return res
def achievement_details(require):
    d=require.GET
    res=[]
    option={}
    college=d['college']
    kind=d['option']
    parameter=d['parameter']
    if kind == '学院':
        kind = 'college'
    elif kind == '专业':
        kind = 'major'
    elif kind == '学生类别':
        kind = 's_type'
    elif kind == '排名':
        kind = 'rank'
    elif kind == '科研成果':
        kind = 'achievement'
    elif kind == '成果类型':
        kind = 'type'
    elif kind == '公告日期':
        kind = 'year'
    option[kind]=parameter
    datas=achievement_summary.objects.all()
    datas=datas.filter(college=college)
    datas=datas.filter(**option)
    for data in datas:
        res.append({'s_id':data.s_id,'s_name':data.s_name,'college':college,"major":data.major,'s_type':data.s_type,'title':data.title,'achievement':data.achievement,
                    'rank':data.rank,'type':data.type,'year':data.year})
    return HttpResponse(json.dumps(res), content_type="application/json")
