from datetime import datetime
from emotionanalysis.login import *
from django.views.decorators.csrf import csrf_exempt
import functools
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

def index(request):
    return HttpResponseRedirect('/html/index.html')
def main(request):
    return HttpResponseRedirect('/html/main.html')



