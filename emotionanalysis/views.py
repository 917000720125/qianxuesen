from datetime import datetime

from Emotion.models import *
from emotionanalysis.login import *
from django.views.decorators.csrf import ensure_csrf_cookie


def operation(userid, o_object, o_type):
    """
    :param userid: 用户id
    :param o_object: 操作对象表名
    :param o_type: 操作类型 曾删改
    :return: true or false
    """
    try:
        user = User.objects.get(userid=userid)
        o = Figure_operation(userid=user, operation_object=o_object, operation_type=o_type)
        o.time = datetime.now()
        o.save()
    except Exception as e:
        print(e)
        return False
    return True


@ensure_csrf_cookie
def index(request):
    return HttpResponseRedirect('/html/index.html')


@do_login
def main(request):
    return HttpResponseRedirect('/html/main.html')


# s:select#u:update#i:insert#d:delete
@do_login
def t1_1_s(request):
    res = []
    datas = Basic_information.objects.all();

    for data in datas:
        r = {'cno': data.cno, 'chinese_name': data.chinese_name, 'english_name': data.english_name,
             'biecheng_chinese': '', 'biecheng_english': ''}
        # 以空格隔开，输出所有别称
        for i in data.agname_set.all():
            if i.agname_chinese:
                r['biecheng_chinese'] += i.agname_chinese + ' '
            if i.agname_english:
                r['biecheng_english'] += i.agname_english + ' '
        r['actor'] = data.actor
        r['nation'] = data.nno.nation_chinese
        r['sex'] = data.sex
        r1=[]
        if data.birth:
            time= data.birth
            tt=time.timetuple()
            strbirth=str(tt.tm_year)+'-'+str(tt.tm_mon)+"-"+str(tt.tm_mday)
            r['birth']=strbirth
        if data.death:
            time1 = data.birth
            tt1 = time.timetuple()
            strbirth1 = str(tt1.tm_year) + '-' + str(tt1.tm_mon) + "-" + str(tt1.tm_mday)
            r['death'] = strbirth1
        res.append(r)
        print(r)
    operation(request.COOKIES.get("username", ""), "Basic_information", "select")
    return HttpResponse(json.dumps(res), content_type="application/json")

@do_login
def t1_1_i(request):
    d = request.POST
    res = {}
    if 'cno' not in d:
        res['why'] = '人物编码不能为空'
        res['success'] = 'no'
        return HttpResponse(json.dumps(res), content_type="application/json")
    try:
        data = Basic_information.objects.get(cno=d['cno'])
    except Basic_information.DoesNotExist as e:
        data = Basic_information(cno=d['cno'])
    if 'nno' in d:
        try:
            nation = Nations.objects.get(nno=d['nno'])
            data.nno = nation
        except Nations.DoesNotExist as e:
            res['why'] = '国家编码不存在'
            res['success'] = 'no'
            return HttpResponse(json.dumps(res), content_type="application/json")
    if 'chinese_name' in d:
        data.chinese_name = d['chinese_name']
    if 'english_name' in d:
        data.english_name = d['english_name']
    if 'actor' in d:
        data.actor = d['actor']
    if 'sex' in d:
        data.sex = '男' if d['sex'] == '1' else '女'
    if 'birth' in d:
        data.birth = d['birth']
    if 'death' in d:
        data.death = d['death']
    try:
        data.save()
        res['success'] = 'yes'
    except Exception as e:
        res['why'] = str(e)
        res['success'] = 'no'
    operation(request.COOKIES.get("username", ""), "Basic_information", "insert")
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t1_1_d(request):
    d = request.GET
    res = {}
    if 'cno' in d:
        cno = request.GET['cno']
        try:
            a = Basic_information.objects.get(cno=cno)
            a.delete()
            res['success'] = 'yes'
        except Exception as e:
            res['success'] = 'no'
            res['why'] = str(e)
    else:
        res['success'] = 'no'
        res['why'] = '人物编号不存在'
    operation(request.COOKIES.get("username", ""), "Basic_information", "delete")
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t1_2_s(request):
    res = []
    datas = Positions.objects.all()
    for data in datas:
        r = {'cno_name': data.cno.chinese_name, 'ono_name': data.ono.organization_chinese}
        if data.sono is not None:
            r['sono_name'] = data.sono.name_chinese
        r['position'] = data.position
        if data.position_start:
            r['position_start'] = data.position_start.strftime("%Y-%m-%d")
        if data.position_end:
            r['position_end'] = data.position_end.strftime("%Y-%m-%d")
        res.append(r)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t1_2_i(request):
    d = request.POST
    res = {}
    if 'cno' not in d:
        res['success'] = 'no'
        res['why'] = '人物编号不能为空'
        return HttpResponse(json.dumps(res), content_type="application/json")
    if 'ono' not in d:
        res['success'] = 'no'
        res['why'] = '一级组织编号不能为空'
        return HttpResponse(json.dumps(res), content_type="application/json")
    if 'sono' not in d:
        res['success'] = 'no'
        res['why'] = '二级组织编号不能为空'
        return HttpResponse(json.dumps(res), content_type="application/json")
    if 'position' not in d:
        res['success'] = 'no'
        res['why'] = '职位不能为空'
        return HttpResponse(json.dumps(res), content_type="application/json")
    data = Positions()
    try:
        cno = Basic_information.objects.get(cno=d['cno'])
        data.cno = cno
    except Basic_information.DoesNotExist as e:
        res['why'] = '人物不存在'
        res['success'] = 'no'
        return HttpResponse(json.dumps(res), content_type="application/json")
    try:
        ono = Organization.objects.get(ono=d['ono'])
        data.ono = ono
    except Organization.DoesNotExist as e:
        res['why'] = '一级组织不存在'
        res['success'] = 'no'
        return HttpResponse(json.dumps(res), content_type="application/json")
    try:
        sono = S_organization.objects.get(sono=d['sono'])
        data.sono = sono
    except S_organization.DoesNotExist as e:
        res['why'] = '二级组织不存在'
        res['success'] = 'no'
        return HttpResponse(json.dumps(res), content_type="application/json")
    data.position = d['position']
    if 'position_start' in d:
        data.position_start = datetime.strptime(d['position_start'], '%Y-%m-%d')
    if 'position_end' in d:
        data.position_end = datetime.strptime(d['position_end'], '%Y-%m-%d')
    try:
        data.save()
        res['success'] = 'yes'
    except Exception as e:
        res['why'] = str(e)
        res['success'] = 'no'
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t1_2_d(request):
    d = request.POST
    res = {}
    try:
        cno = Basic_information.objects.get(chinese_name=d['cno_name'])
        ono = Organization.objects.get(organization_chinese=d['ono_name'])
        sono = S_organization.objects.get(name_chinese=d['sono_name'])
        position = d['position']
        data = Positions.objects.get(cno=cno, ono=ono, sono=sono, position=position)
        data.delete()
        res['success'] = 'yes'
    except Exception as e:
        res['success'] = 'no'
        res['why'] = str(e)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t1_3_s(request):
    """
    get
    [{cno_name:中文名字,subject:特征词}...]
    """
    res = []
    datas = Character_subjects.objects.all()
    for data in datas:
        r = {'cno': data.cno.cno, 'subject': data.subject}
        res.append(r)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t1_3_i(request):
    """
    post
    {cno_name:中文名字,subject:特征词}
    """
    d = request.POST
    res = {}
    try:
        data = Character_subjects()
        data.cno = Basic_information.objects.get(cno=d['cno'])
        data.subject = d['subject']
        data.save()
        res['success'] = 'yes'
    except Exception as e:
        res['success'] = 'no'
        res['why'] = str(e)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t1_3_d(request):
    """
    post
    {cno:人物编号,subject:特征词}
    """
    d = request.POST
    res = {}
    try:
        data = Character_subjects.objects.get(
            Basic_information.objects.get(cno=d['cno']),
            subject=d['subject'])
        data.delete()
        res['success'] = 'yes'
    except Exception as e:
        res['success'] = 'no'
        res['why'] = str(e)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t1_4_s(request):
    res = []
    dates = Contact.objects.all()
    for data in dates:
        r = {'cno': data.cno.cno, 'contact': data.contact, 'contact_type': data.contact_type}
        res.append(r)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t1_4_i(request):
    d = request.POST
    res = {}
    try:
        data = Contact()
        data.cno = Basic_information.objects.get(cno=d['cno'])
        data.contact = d['contact']
        data.contact_type = d['contact_type']
        data.save()
        res['success'] = 'yes'
    except Exception as e:
        res['success'] = 'no'
        res['why'] = str(e)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t1_4_d(request):
    d = request.POST
    res = {}
    try:
        data = Contact.objects.get(cno=Basic_information.objects.get(cno=d['cno']), contact=d['contact'],
                                   contact_type=d['contact_type'])
        data.delete()
        res['sucess'] = 'yes'
    except Exception as e:
        res['sucess'] = 'no'
        res['why'] = str(e)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t2_1_s(request):
    res = []
    dates = Organization.objects.all()
    for data in dates:
        r = {'ono': data.ono, 'organization_chinese': data.organization_chinese,
             'organization_english': data.organization_english, 'nno_name': data.nno.nation_chinese,
             'main_duty': data.main_duty, 'organization_type': data.organization_type}
        if data.setup_time:
            r['setup_time'] = data.setup_time.strftime("%Y-%m-%d")
        res.append(r)
    operation(request.COOKIES.get("username", ""), "Organization", "select")
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t2_1_i(request):
    res = {'success': 'yes'}
    try:
        data = Organization()
        data.ono = request.POST['ono']
        data.organization_chinese = request.POST['o_chinese']
        data.organization_english = request.POST['o_english']
        data.nno = Nations.objects.get(nno=request.POST['nno'])
        data.main_duty = request.POST['main_duty']
        data.organization_type = request.POST['organization_type']
        data.setup_time = datetime.strptime(request.POST['setup_time'], '%Y-%m-%d')
        data.save()
        res['success'] = 'yes'
    except Exception as e:
        res['success'] = 'no'
        res['why'] = str(e)
    operation(request.COOKIES.get("username", ""), "Organization", "insert")
    return HttpResponse(json.dumps(res), content_type="application/json")
def t2_1_u(request):
    res={'success':'yes'}
    try:
        data = Organization()
        data.ono = request.POST['ono']
        data.organization_chinese = request.POST['o_chinese']
        data.organization_english = request.POST['o_english']
        nno=Nations.objects.get(nation_chinese=request.POST['nno'])
        data.nno = nno
        data.main_duty = request.POST['main_duty']
        data.organization_type = request.POST['organization_type']
        data.setup_time = datetime.strptime(request.POST['setup_time'], '%Y-%m-%d')
        data.save()
        res['success'] = 'yes'
    except Exception as e:
        res['success'] = 'no'
        res['why'] = str(e)
    operation(request.COOKIES.get("username", ""), "Organization", "insert")
    return HttpResponse(json.dumps(res), content_type="application/json")

@do_login
def t2_1_d(request):
    d = request.GET
    res = {}
    if 'ono' in d:
        ono = request.GET['ono']
        try:
            a =Organization.objects.get(ono=ono)
            a.delete()
            res['success'] = 'yes'
        except Exception as e:
            res['success'] = 'no'
            res['why'] = str(e)
            print(str(e))
        operation(request.COOKIES.get("username", ""), "Nations", "delete")
    else:
        res['success'] = 'no'
        res['why'] = '需要编号'
    return HttpResponse(json.dumps(res), content_type="application/json")

@do_login
def t2_2_s(request):
    res = []
    dates = S_organization.objects.all()
    for data in dates:
        r = {'sono': data.sono, 'ono_name': data.ono.organization_chinese, 'name_chinese': data.name_chinese,
             'name_english': data.name_english, 'main_duty': data.main_duty}
        res.append(r)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t2_2_i(request):
    res = {'success': 'yes'}
    try:
        data = S_organization()
        data.sono = request.POST['sono']
        data.name_chinese = request.POST['so_chinese']
        data.name_english = request.POST['so_english']
        nno = Organization.objects.get()
        data.nno = nno
        data.main_duty = request.POST['main_duty']
        data.save()
        res['success'] = 'yes'
    except Exception as e:
        res['success'] = 'no'
        res['why'] = str(e)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t2_2_d(request):
    d = request.GET
    res = {'success': 'yes'}
    if 'sono' in d:
        sono = request.GET['sono']
        try:
            a =S_organization.objects.get(sono=sono)
            a.delete()
            res['success'] = 'yes'
        except Exception as e:
            res['success'] = 'no'
            res['why'] = str(e)
            print(str(e))
        operation(request.COOKIES.get("username", ""), "Nations", "delete")
    else:
        res['success'] = 'no'
        res['why'] = '需要编号'
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t2_3_s(request):
    res = []
    datas = S_contact.objects.all()
    for data in datas:
        r = {'sono': data.sono.sono, 'contact': data.contact, 'contact_type': data.contact_type}
        res.append(r)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t2_3_i(request):
    res = {'success': 'yes'}
    try:
        data = S_contact()
        data.sono = S_organization.objects.get(sono=request.POST['sono'])
        data.contact = request.POST['contact']
        data.contact_type = request.POST['contact_type']
        data.save()
        res['success'] = 'yes'
    except Exception as e:
        res['success'] = 'no'
        res['why'] = str(e)

    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t2_3_d(request):
    d = request.GET
    res = {}
    if 'sono' in d:
        sono = request.GET['sono']
        try:
            a = S_contact.objects.get(sono=sono)
            a.delete()
            res['success'] = 'yes'
        except Exception as e:
            res['success'] = 'no'
            res['why'] = str(e)
        operation(request.COOKIES.get("username", ""), "Nations", "delete")
    else:
        res['success'] = 'no'
        res['why'] = '需要编号'
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t3_1_s(request):
    res = []
    dates = Nations.objects.all()
    for data in dates:
        r = {'nno': data.nno, 'nation_chinese': data.nation_chinese, 'nation_english': data.nation_english,
             'geographical_position': data.geographical_position, 'economic_situation': data.economic_situation}
        res.append(r)
    operation(request.COOKIES.get("username", ""), "Nations", "select")
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t3_1_i(request):
    res = {'success': 'yes'}
    print('aaa')
    print(request.POST)
    try:
        data = Nations()
        data.nno = request.POST['nno']
        data.nation_chinese = request.POST['nation_chinese']
        data.nation_english = request.POST['nation_english']
        data.geographical_position = request.POST['geographical_position']
        data.economic_situation = request.POST['economic_situation']
        data.save()
    except Exception as e:
        res['success'] = 'no'
        res['why'] = str(e)
    operation(request.COOKIES.get("username", ""), "Nations", "insert")
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def t3_1_d(request):
    d = request.GET
    res = {}
    if 'nno' in d:
        nno = request.GET['nno']
        try:
            a = Nations.objects.get(nno=nno)
            a.delete()
            res['success'] = 'yes'
        except Exception as e:
            res['success'] = 'no'
            res['why'] = str(e)
        operation(request.COOKIES.get("username", ""), "Nations", "delete")
    else:
        res['success'] = 'no'
        res['why'] = '需要编号'
    return HttpResponse(json.dumps(res), content_type="application/json")
