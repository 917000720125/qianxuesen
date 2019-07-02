# Create your views here.
from News.models import *
from emotionanalysis.views import *


@do_login
def get_source(request):
    datas = Source.objects.all()
    res = []
    for data in datas:
        r = {'id': data.id, 'name': data.name, 'url': data.url}
        res.append(r)
    operation(request.COOKIES.get("username", ""), "Source", "select")
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def add_source(request):
    res = {'success': 'yes'}
    try:
        data = Source()
        data.id = request.POST['id']
        data.url = request.POST['url']
        data.name = request.POST['name']
        data.save()
    except Exception as e:
        res['success'] = 'no'
        res['why'] = str(e)
    operation(request.COOKIES.get("username", ""), "Source", "insert")
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def del_source(request):
    res = {'success': 'yes'}
    try:
        data = Source.objects.get(id=request.GET['id'])
        data.delete()
    except Exception as e:
        res['success'] = 'no'
        res['why'] = str(e)
    operation(request.COOKIES.get("username", ""), "Source", "delete")
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def get_event(request):
    datas = Event.objects.all()
    res = []
    for data in datas:
        r = {'id': data.id, 'name': data.name, 'agname': data.agname}
        res.append(r)
    operation(request.COOKIES.get("username", ""), "Event", "select")
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def add_event(request):
    res = {'success': 'yes'}
    try:
        data = Event()
        data.id = request.POST['id']
        data.agname = request.POST['agname']
        data.name = request.POST['name']
        data.save()
    except Exception as e:
        res['success'] = 'no'
        res['why'] = str(e)
    operation(request.COOKIES.get("username", ""), "Event", "insert")
    return HttpResponse(json.dumps(res), content_type="application/json")


@do_login
def del_event(request):
    d = request.GET
    res = {}
    if 'id' in d:
        id = request.GET['id']
        try:
            a = Event.objects.get(id=id)
            a.delete()
            res['success'] = 'yes'
        except Exception as e:
            res['success'] = 'no'
            res['why'] = str(e)
        operation(request.COOKIES.get("username", ""), "Nations", "delete")
    else:
        res['success'] = 'no'
        res['why'] = '需要事件ID'
    return HttpResponse(json.dumps(res), content_type="application/json")


