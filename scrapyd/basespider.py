# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


# 删除字符串中的a标签和&nbsp
def _del_a_nbsp(v: str) -> str:
    v = v.replace("&nbsp;", "")
    v = v.replace("\n", "")
    for i in range(1, 10):
        v = v.replace(r"["+str(i)+"]", "")
    v = v.replace("\xa0", "")
    return v


def _basic_spider(name: str) -> dict:
    """
    从百度百科获取词条基本信息
    :param name: 人物名字
    :return: None 或 人物信息dict{}
    """
    url = "https://baike.baidu.com/item/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) "}
    r = requests.get(url+name, headers=headers)
    soup = BeautifulSoup(r.content.decode("utf-8"), features="lxml")
    values = list(map(lambda x: x.getText(), soup.select('.value')))
    names = list(map(lambda x: x.getText(), soup.select('.name')))
    '''
    names = re.findall(r'<dt class="basicInfo-item name">(.*)</dt>|', r.content.decode("utf-8"))
    values = re.findall(r'<dd class="basicInfo-item value">\n(.*)\n</dd>', r.content.decode("utf-8"))

    print(names)
    print(values)
    '''
    res = dict()
    for i, j in zip(names, values):
        res[_del_a_nbsp(i)] = _del_a_nbsp(j)
    return res


# 从爬取的信息里面获取需要的信息
def _need_name_dict(dic: dict) -> dict:
    res = dict(english_name="", chinese_name="", nation_base="",
               act="", sex="", birth="", death="",
               agname_chinese="", agname_english="")
    if "外文名" in dic:
        res["english_name"] = dic["外文名"]
    if "中文名" in dic:
        res["chinese_name"] = dic["中文名"]
    if "职业" in dic:
        res["act"] = dic["职业"]
    if "性别" in dic:
        res["sex"] = dic["性别"]
    if "出生日期" in dic:
        res["birth"] = dic["出生日期"]
    if "逝世日期" in dic:
        res["death"] = dic["逝世日期"]
    if "别名" in dic:
        temp = dic["别名"].replace('、', '，')
        temp = temp.split('，')
        for i in temp:
            if u'\u4e00' <= i[0] <= u'\u9fff':
                res['agname_chinese'] += i + ','
            else:
                res['agname_english'] += i + ','
        res['agname_chinese'] = res['agname_chinese'][:-1]
        res['agname_english'] = res['agname_english'][:-1]
    if "国籍" in dic:
        res["nation_base"] = dic["国籍"]
    return res


def _need_nation_dict(dic: dict) -> dict:
    res = dict(nation_chinese="", nation_english="", geographical_position="",
               economic_situation="")
    if "中文名称" in dic:
        res["nation_chinese"] = dic["中文名称"]
    if "英文名称" in dic:
        res["nation_english"] = dic["英文名称"]
    if "所属洲" in dic:
        res["geographical_position"] = dic["所属洲"]
    if "GDP总计" in dic:
        res["economic_situation"] = dic["GDP总计"]
    return res


def _need_organization_dict(dic: dict) -> dict:
    res = dict(english_o="", chinese_o="", nation_o="", economic="")
    if "外文名" in dic:
        res["english_o"] = dic["外文名"]
    if "中文名" in dic:
        res["chinese_o"] = dic["中文名"]
    if "GDP总计" in dic:
        res["economic"] = dic["别名"]
    if "国籍" in dic:
        res["nation_o"] = dic["国籍"]
    return res


# 外部api,通过名字获取人物信息
def get_name_info(name: str) -> dict:
    return _need_name_dict(_basic_spider(name))


def get_nation_info(nation: str) -> dict:
    return _need_nation_dict(_basic_spider(nation))


def get_organization_info(organization: str) -> dict:
    return _need_organization_dict(_basic_spider(organization))


if __name__ == '__main__':
    print(_need_name_dict(_basic_spider("习近平")))
    print(_need_name_dict(_basic_spider("斯蒂芬·威廉·霍金")))
    print(_need_name_dict(_basic_spider("唐纳德·特朗普")))

    print(_need_nation_dict(_basic_spider("英国")))
    print(_need_nation_dict(_basic_spider("美国")))
    print(_need_nation_dict(_basic_spider("中国")))

