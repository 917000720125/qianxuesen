from Emotion.models import *
def ff(x):
    return Nations.objects.filter(nation_chinese=x)[0]

import pandas as pd

d=pd.read_excel('C://Users/lenovo/Desktop/人物信息表.xlsx')
for i in range(500,2000):
    a=Basic_information()
    a.cno=str(d['序号'][i]).rjust(5,'0')
    a.chinese_name=d['中文'][i]
    a.english_name=d['英文'][i]
    a.actor=d['角色'][i]
    a.sex=1 if d['性别'][i]=='男' else 0
    if str(d['出生日期'][i])!='NaT':
        a.birth=d['出生日期'][i]
    a.nno=ff(d['国家'][i])
    a.save()

d=pd.read_excel('C://Users/lenovo/Desktop/别称.xlsx')
for i in range(len(d['cno'])):
    a=Agname()
    a.cno=Basic_information.objects.filter(cno=str(d['cno'][i]).rjust(5,'0'))[0]
    a.agname_chinese=d['agname_chinese'][i]
    a.agname_english=d['agname_english'][i]
    a.save()

d=pd.read_excel('C://Users/lenovo/Desktop/一级组织.xlsx')
for i in range(len(d['编号'])):
    a=Organization()
    a.ono=str(d['编号'][i]).rjust(5,'0')
    a.organization_chinese=d['组织名称'][i]
    a.organization_english=d['英文名称'][i]
    a.nno=ff(d['国家'][i])
    a.main_duty=d['职责'][i]
    a.save()

d=pd.read_excel('C://Users/lenovo/Desktop/二级组织.xlsx')
for i in range(len(d['编号'])):
    a=S_organization()
    a.sono=str(d['编号'][i]).rjust(7,'0')
    a.ono=Organization.objects.filter(ono=str(d['编号'][i]).rjust(7,'0')[:5])[0]
    a.name_chinese=d['中文名称'][i]
    a.name_english=d['英文名称'][i]
    a.main_duty=d['职责'][i]
    a.save()

d=pd.read_excel('C://Users/lenovo/Desktop/position.xlsx')
for i in range(len(d['编号'])):
    a=Positions()
    a.cno=Basic_information.objects.filter(cno=str(d['编号'][i]).rjust(5,'0'))[0]
    a.ono=Organization.objects.filter(ono=str(d['onoo'][i])[1:6])[0]
    if len(str(d['onoo'][i])[1:])==7:
        a.sono=S_organization.objects.filter(sono=str(d['onoo'][i])[1:])[0]
    a.position=d['position'][i]
    a.position_start=d['职位开始'][i]
    if str(d['职位结束'][i])!='nan':
        a.position_end=d['职位结束'][i]
    a.save()