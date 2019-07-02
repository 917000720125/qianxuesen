"""emotionalises URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from News.views import *
from emotionanalysis.login import *
from emotionanalysis.views import *

urlpatterns = [
                  # path('',)
                  path('admin/', admin.site.urls),
                  # 登陆系统
                  path('', index), path('html/index.html', index),
                  path('html/main.html', main),
                  path('login', login), path('logup', logup), path('logout', logout),
                  path('user_info', user_info), path('history', history),
                  # 爬虫相关
                  path('get_name_base', get_name_base), path('get_nation_base', get_nation_base),
                  path('get_organization_base', get_organization_base),
                  path('get_huanqiu_news', get_huanqiu_news),
                  path('add_name_base', add_name_base), path('add_nation_base', add_nation_base),
                  # 语料管理相关
                  path('get_source', get_source), path('add_source', add_source), path('del_source', del_source),
                  path('emotion_analyse', emotion_analyse),
                  path('emotion_analyse_figure1', emotion_analyse_figure1),
                  path('emotion_analyse_figure2', emotion_analyse_figure2),
                  path('emotion_analyse_figure3', emotion_analyse_figure3),
                  path('emotion_analyse_figure4', emotion_analyse_figure4),
                  # 重点事件管理
                  path('get_event', get_event), path('add_event', add_event), path('del_event', del_event),
                  path('t1_1_s', t1_1_s), path('t1_1_i', t1_1_i), path('t1_1_d', t1_1_d),
                  # t1_1_s:查询人物基本信息
                  # t1_1_i:插入和更改人物基本信息(人物编号)
                  # t1_1_d:删除人物基本信息(人物编号)
                  path('t1_2_s', t1_2_s), path('t1_2_i', t1_2_i), path('t1_2_d', t1_2_d),
                  # t1_2_s:查询人物任职记录
                  # t1_2_i:插入和更改人物任职记录(人物编号,一级组织编号,二级组织编号,职位)
                  # t1_2_d:删除人物任职记录(人物编号,一级组织编号,二级组织编号,职位)

                  path('t1_3_s', t1_3_s), path('t1_3_i', t1_3_i), path('t1_3_d', t1_3_d),
                  # 人物相关特征词操作(人物编号,特征词)

                  path('t1_4_s', t1_4_s), path('t1_4_i', t1_4_i), path('t1_4_d', t1_4_d),
                  # 人物相关特征词操作(人物编号,联系方式,联系渠道)
                  path('t2_1_s', t2_1_s), path('t2_1_i', t2_1_i), path('t2_1_d', t2_1_d),path('t2_1_u', t2_1_u),
                  # 一级组织管理
                  path('t2_2_s', t2_2_s), path('t2_2_i', t2_2_i), path('t2_2_d', t2_2_d),
                  # 二级组织管理
                  path('t2_3_s', t2_3_s), path('t2_3_i', t2_3_i), path('t2_3_d', t2_3_d),
                  # 组织联系方式(好像没有这个表)
                  path('t3_1_s', t3_1_s), path('t3_1_i', t3_1_i), path('t3_1_d', t3_1_d)
                  # 国家信息
              ]
