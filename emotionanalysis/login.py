import csv
import functools
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Emotion.models import *
from News.models import News


@csrf_exempt
def login(request):
    """
    登陆保存cookie
    :param request:
    :return:
    """
    d = request.POST
    try:
        userid = d['user']
        password = d['password']
    except KeyError:
        return HttpResponseRedirect('/html/index.html')
    user = User.objects.filter(userid=userid, password=password)
    if user:
        response = HttpResponseRedirect('/html/main.html')
        response.set_cookie('username', userid, 3600)
        return response
    else:
        return HttpResponseRedirect('/html/index.html')

@csrf_exempt
def logup(request):
    d = request.POST
    res = dict(success="yes")
    userid, password, qq_mail = d["userid"], d["password"], d["qq_mail"]
    print(qq_mail)
    try:
        user = User(userid=userid, password=password,name=userid)
        user.save()
    except Exception as e:
        res['success'] = "no"
        res['why'] = str(e)
    return HttpResponse(json.dumps(res), content_type="application/json")


# 检测是否登陆
def do_login(func):
    @functools.wraps(func)
    def wrapper(request):
        username = request.COOKIES.get('username', '')
        if username:
            response = func(request)
        else:
            response = HttpResponseRedirect('/html/index.html')
        return response

    return wrapper


def logout(request):
    response = HttpResponseRedirect('/html/index.html')
    # 清理cookie里保存username
    response.delete_cookie('username')
    return response


@do_login
def user_info(request):
    userid = request.COOKIES.get('username', '')
    user = User.objects.get(userid=userid)
    res = dict(userid=user.userid, permissions=user.permissions, name=user.name, sex=user.sex,
               national=user.national, telephone=user.telephone, address=user.address)
    return HttpResponse(json.dumps(res), content_type="application/json")


def history(request):
    userid = request.COOKIES.get('username', '')
    user = User.objects.get(userid=userid)
    datas = Figure_operation.objects.filter(userid=user)
    res = []
    for data in datas:
        r = dict(obj=data.operation_object, typ=data.operation_type, time=data.time.strftime("%Y-%m-%d"))
        res.append(r)
    return HttpResponse(json.dumps(res), content_type="application/json")


# 爬虫相关
@do_login
def get_name_base(request):
    name = request.POST["name"]
    from scrapyd.basespider import get_name_info
    res = get_name_info(name)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def get_nation_base(request):
    name = request.POST["name"]
    from scrapyd.basespider import get_nation_info
    res = get_nation_info(name)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def get_organization_base(request):
    name = request.POST["name"]
    from scrapyd.basespider import get_organization_info
    res = get_organization_info(name)
    return HttpResponse(json.dumps(res), content_type="application/json")


# 爬虫结果插入数据库
@do_login
def add_name_base(request):
    res = dict(success='yes', why='')
    try:
        nation = request.POST['nation_base']
        nation = Nations.objects.get(nation_chinese=nation)
        data = Basic_information()
        if Basic_information.objects.last() is None:
            data.cno = '10000'
        else:
            data.cno = str(int(Basic_information.objects.last().cno) + 1)
        data.chinese_name = request.POST['chinese_name']
        data.english_name = request.POST['english_name']
        data.nno = nation
        data.actor = request.POST['act']
        data.birth = request.POST['birth']
        data.death = request.POST['death']
        data.sex = request.POST['sex']
        data.save()
        if request.POST['agname_chinese']:
            for i in request.POST['agname_chinese'].split(','):
                ag = Agname()
                ag.cno = data
                ag.agname_chinese = i
                ag.save()
        if request.POST['agname_english']:
            for i in request.POST['agname_english'].split(','):
                ag = Agname()
                ag.cno = data
                ag.agname_english = i
                ag.save()
    except Exception as e:
        res['success'] = 'no'
        res['why'] = str(e)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def add_nation_base(request):
    res = dict(success='yes', why='')
    try:
        if len(Nations.objects.filter(nation_chinese=request.POST['nation_chinese'])) != 0:
            res['success'] = 'no'
            res['why'] = '国家已经存在'
            return HttpResponse(json.dumps(res), content_type="application/json")
        data = Nations()
        data.nno = str(int(Nations.objects.last().nno) + 1)
        data.nation_chinese = request.POST['nation_chinese']
        data.nation_english = request.POST['nation_english']
        data.economic_situation = request.POST['economic_situation']
        data.geographical_position = request.POST['geographical_position']
        data.save()
    except Exception as e:
        res['success'] = 'no'
        res['why'] = str(e)
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def add_organization_base(request):
    pass


@do_login
def get_huanqiu_news(request):
    # 根据关键词，时间爬去对应的新闻
    TEST = False
    res = []
    # res = [{"id": "1", "title": "title", "content": "content", "time": "time", "url": "url"}]
    if not TEST:
        key = request.GET['key']
        start_time = request.GET['begin_time']
        end_time = request.GET['end_time']
        from scrapyd.huanqiu import Huanqiu
        res = Huanqiu.get_huanqiu_news(key=key, start_time=start_time, end_time=end_time)

        for news in readcvs('new.csv'):
            from scrapyd.extractEmotionSentence import extractEmotionSentence
            if(extractEmotionSentence(news)['subject']!=""):
                #当新闻有明确情感句且有情感subject时进行情感分析，否则丢弃
                from emtionanalysis.scrapyd.emotionSentenceAnalysis import emotionSentenceAnalysis
                print(emotionSentenceAnalysis(extractEmotionSentence(news)))


    else:
        # 测试，直接查询
        datas = News.objects.all()
        for data in datas:
            res.append({"id": str(data.id), "title": data.title, "content": data.content,
                        "time": data.time.strftime("%Y-%m-%d"), "url": data.source})
    return HttpResponse(json.dumps(res), content_type="application/json")

def readcvs(path):
    dict_club = []
    i=0
    #由于csv每次读取的列的顺序都不一致，设置开关读取第一行，利用第一行保证有序
    flag=1
    firstRow=[]

    with open(path)as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row!=[]:
                if(flag==1):
                    firstRow.append(row[1])
                    firstRow.append(row[2])
                    firstRow.append(row[3])
                    firstRow.append(row[4])
                    firstRow.append(row[5])
                    firstRow.append(row[6])
                    print (firstRow)
                    flag=0
                else:
                    oneNews={}
                    oneNews[firstRow[0]]=row[1]
                    oneNews[firstRow[1]] = row[2]
                    oneNews[firstRow[2]] = row[3]
                    oneNews[firstRow[3]] = row[4]
                    oneNews[firstRow[4]] = row[5]
                    oneNews[firstRow[5]] = row[6]
                    dict_club.append(oneNews)
                    i = i + 1
        # for v in dict_club:
        #     print (v)
        f.close()
    print('查看一共有多少条新闻')
    print(i)
    return dict_club
@do_login
def emotion_analyse(request):
    # 进行情感分析并把结果插入数据库,然后返回结果
    json={}#情感分析的
    res = []


    datas = News.objects.all()
    for data in datas:
        res.append({"id": str(data.id), "title": data.title, "content": data.content,
                    "time": data.time.strftime("%Y-%m-%d"), "source": data.source,
                    "emotional_event": data.emotional_event, "emotional_words": data.emotional_words,
                    "emotional_plus_or_minus": data.emotional_plus_or_minus,
                    "probability": data.probability, "emotional_express": data.emotional_express})
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def emotion_analyse_figure1(request):
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    datas = News.objects.all()
    for data in datas:
        res.append({"id": str(data.id), "title": data.title, "content": data.content,
                    "time": data.time.strftime("%Y-%m-%d"), "source": data.source,
                    "emotional_event": data.emotional_event, "emotional_words": data.emotional_words,
                    "emotional_plus_or_minus": data.emotional_plus_or_minus,
                    "probability": data.probability, "emotional_express": data.emotional_express})
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def emotion_analyse_figure2(request):
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    datas = News.objects.all()
    for data in datas:
        res.append({"id": str(data.id), "title": data.title, "content": data.content,
                    "time": data.time.strftime("%Y-%m-%d"), "source": data.source,
                    "emotional_event": data.emotional_event, "emotional_words": data.emotional_words,
                    "emotional_plus_or_minus": data.emotional_plus_or_minus,
                    "probability": data.probability, "emotional_express": data.emotional_express})
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def emotion_analyse_figure3(request):
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    datas = News.objects.all()
    for data in datas:
        res.append({"id": str(data.id), "title": data.title, "content": data.content,
                    "time": data.time.strftime("%Y-%m-%d"), "source": data.source,
                    "emotional_event": data.emotional_event, "emotional_words": data.emotional_words,
                    "emotional_plus_or_minus": data.emotional_plus_or_minus,
                    "probability": data.probability, "emotional_express": data.emotional_express})
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def emotion_analyse_figure4(request):
    # 进行情感分析并把结果插入数据库,然后返回结果
    res = []
    datas = News.objects.all()
    for data in datas:
        res.append({"id": str(data.id), "title": data.title, "content": data.content,
                    "time": data.time.strftime("%Y-%m-%d"), "source": data.source,
                    "emotional_event": data.emotional_event, "emotional_words": data.emotional_words,
                    "emotional_plus_or_minus": data.emotional_plus_or_minus,
                    "probability": data.probability, "emotional_express": data.emotional_express})
    return HttpResponse(json.dumps(res), content_type="application/json")

