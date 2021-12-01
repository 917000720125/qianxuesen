#数据处理函数
import pyecharts as Map
def fanyi(content):#将中文翻译成英文
    map = {
        "阿富汗": "Afghanistan",
        "阿尔巴尼亚": "Albania",
        "阿尔及利亚": "Algeria",
        "安道尔": "Andorra",
        "安哥拉": "Angola",
        "安圭拉": "Anguilla",
        "安提瓜和巴布达": "Antigua_and_Barbuda",
        "阿根廷": "Argentina",
        "亚美尼亚": "Armenia",
        "澳大利亚": "Australia",
        "奥地利": "Austria",
        "阿塞拜疆": "Azerbaijan",
        "巴林": "Bahrain",
        "孟加拉国": "Bangladesh",
        "巴巴多斯": "Barbados",
        "白俄罗斯": "Belarus",
        "比利时": "Belgium",
        "伯利兹": "Belize",
        "贝宁": "Benin",
        "百慕达群岛": "Bermuda",
        "不丹": "Bhutan",
        "玻利维亚": "Bolivia",
        "波斯尼亚-黑塞哥维那": "Bosnia_and_Herzegovina",
        "博茨瓦纳": "Botswana",
        "巴西": "Brazil",
        "英属印度洋领地": "British_Indian_Ocean_Territory",
        "英属维尔京群岛": "British_Virgin_Islands",
        "文莱": "Brunei",
        "保加利亚": "Bulgaria",
        "布基纳法索": "Burkina_Faso",
        "蒲隆地": "Burundi",
        "柬埔寨": "Cambodia",
        "喀麦隆": "Cameroon",
        "加拿大": "Canada",
        "佛得角": "Cape_Verde",
        "开曼群岛": "Cayman_Islands",
        "中非共和国": "Central_African_Republic",
        "乍得": "Chad",
        "智利": "Chile",
        "哥伦比亚": "Colombia",
        "科摩罗": "Comoros",
        "刚果-布拉柴维尔": "Congo-Brazzaville",
        "刚果金": "Congo-Kinshasa",
        "库克群岛": "Cook_Islands",
        "珊瑚海群岛领地": "Coral_Sea_Islands_Territory",
        "哥斯达黎加": "Costa_Rica",
        "克罗地亚": "Croatia",
        "古巴": "Cuba",
        "塞浦路斯": "Cyprus",
        "捷克": "Czechia",
        "丹麦": "Denmark",
        "吉布提": "Djibouti",
        "多米尼克": "Dominica",
        "多米尼加共和国": "Dominican_Republic",
        "东帝汶": "East_Timor",
        "厄瓜多尔": "Ecuador",
        "埃及": "Egypt",
        "萨尔瓦多": "El_Salvador",
        "赤道几内亚": "Equatorial_Guinea",
        "厄立特里亚": "Eritrea",
        "爱沙尼亚": "Estonia",
        "埃塞俄比亚": "Ethiopia",
        "福克兰群岛": "Falkland_Islands",
        "法罗群岛": "Faroe_Islands",
        "密克罗尼西亚联邦": "Federated_States_of_Micronesia",
        "斐济": "Fiji",
        "芬兰": "Finland",
        "法国": "France",
        "加蓬": "Gabon",
        "格鲁吉亚": "Georgia",
        "德国": "Germany",
        "加纳": "Ghana",
        "直布罗陀": "Gibraltar",
        "希腊": "Greece",
        "格陵兰": "Greenland",
        "危地马拉": "Guatemala",
        "根西": "Guernsey",
        "几内亚比索": "Guinea-Bissau",
        "几内亚": "Guinea",
        "圭亚那": "Guyana",
        "海地": "Haiti",
        "洪都拉斯": "Honduras",
        "匈牙利": "Hungary",
        "冰岛": "Iceland",
        "印度": "India",
        "印度尼西亚, 印尼": "Indonesia",
        "伊拉克": "Iraq",
        "爱尔兰": "Ireland",
        "伊朗": "Islamic_Republic_of_Iran",
        "马恩岛": "Isle_of_Man",
        "以色列": "Israel",
        "意大利": "Italy",
        "牙买加": "Jamaica",
        "日本": "Japan",
        "泽西": "Jersey",
        "约旦": "Jordan",
        "哈萨克斯坦": "Kazakhstan",
        "肯尼亚": "Kenya",
        "基里巴斯": "Kiribati",
        "科威特": "Kuwait",
        "吉尔吉斯斯坦": "Kyrgyzstan",
        "老挝": "Laos",
        "拉脱维亚": "Latvia",
        "黎巴嫩": "Lebanon",
        "莱索托": "Lesotho",
        "利比里亚": "Liberia",
        "利比亚": "Libya",
        "列支敦士登": "Liechtenstein",
        "立陶宛": "Lithuania",
        "卢森堡": "Luxemburg",
        "马其顿": "Macedonia",
        "马达加斯加": "Madagascar",
        "马拉维": "Malawi",
        "马来西亚": "Malaysia",
        "马尔代夫": "Maldives",
        "马里": "Mali",
        "马耳他": "Malta",
        "马绍尔群岛": "Marshall_Islands",
        "毛里塔尼亚": "Mauritania",
        "毛里求斯": "Mauritius",
        "墨西哥": "Mexico",
        "摩尔多瓦": "Moldova",
        "摩纳哥": "Monaco",
        "蒙古": "Mongolia",
        "黑山": "Montenegro",
        "蒙特塞拉特": "Montserrat",
        "摩洛哥": "Morocco",
        "莫桑比克": "Mozambique",
        "缅甸": "Myanmar",
        "纳米比亚": "Namibia",
        "尼泊尔": "Nepal",
        "新西兰": "New_Zealand",
        "尼加拉瓜": "Nicaragua",
        "尼日尔": "Niger",
        "尼日利亚": "Nigeria",
        "纽埃": "Niue",
        "朝鲜": "North_Korea",
        "挪威": "Norway",
        "阿曼": "Oman",
        "巴基斯坦": "Pakistan",
        "帕劳": "Palau",
        "巴勒斯坦": "Palestine",
        "巴拿马": "Panama",
        "巴布亚新几内亚": "Papua_New_Guinea",
        "巴拉圭": "Paraguay",
        "秘鲁": "Peru",
        "菲律宾": "Philippines",
        "皮特凱恩群島": "Pitcairn_Islands",
        "波兰": "Poland",
        "葡萄牙": "Portugal",
        "卡塔尔": "Qatar",
        "科索沃": "Republic_of_Kosovo",
        "罗马尼亚": "Romania",
        "俄罗斯": "Russia",
        "卢旺达": "Rwanda",
        "撒拉威阿拉伯民主共和国": "Sahrawi_Arab_Democratic_Republic",
        "圣赫勒拿-阿森松和特里斯坦-达库尼亚": "Saint_Helena_Ascension_and_Tristan_da_Cunha",
        "圣基茨和尼维斯": "Saint_Kitts_and_Nevis",
        "圣卢西亚": "Saint_Lucia",
        "圣文森特和格林纳丁斯": "Saint_Vincent_and_the_Grenadines",
        "萨摩亚": "Samoa",
        "圣马力诺": "San_Marino",
        "沙特阿拉伯王国": "Saudi Arabia",
        "塞内加尔": "Senegal",
        "塞尔维亚": "Serbia",
        "塞舌尔": "Seychelles",
        "塞拉利昂": "Sierra_Leone",
        "新加坡": "Singapore",
        "斯洛伐克": "Slovakia",
        "斯洛文尼亚": "Slovenia",
        "所罗门群岛": "Solomon_Islands",
        "索马里": "Somalia",
        "南非": "South_Africa",
        "南乔治亚和南桑威奇群岛": "South_Georgia_and_the_South_Sandwich_Islands",
        "韩国": "South_Korea",
        "南苏丹": "South_Sudan",
        "西班牙": "Spain",
        "斯里兰卡": "Sri_Lanka",
        "苏丹": "Sudan",
        "苏里南": "Suriname",
        "史瓦济兰": "Swaziland",
        "瑞典": "Sweden",
        "叙利亚": "Syria",
        "塔吉克斯坦": "Tajikistan",
        "坦桑尼亚": "Tanzania",
        "泰国": "Thailand",
        "巴哈马": "The_Bahamas",
        "冈比亚": "The_Gambia",
        "荷兰": "The_Netherlands",
        "多哥": "Togo",
        "托克劳": "Tokelau",
        "汤加": "Tonga",
        "特立尼达和多巴哥": "Trinidad_and_Tobago",
        "突尼斯": "Tunisia",
        "土耳其": "Turkey",
        "土库曼": "Turkmenistan",
        "特克斯和凯科斯群岛": "Turks_and_Caicos_Islands",
        "吐瓦鲁": "Tuvalu",
        "乌干达": "Uganda",
        "乌克兰": "Ukraine",
        "阿拉伯联合酋长国": "United_Arab_Emirates",
        "英国": "United_Kingdom",
        "乌拉圭": "Uruguay",
        "美国": "United States",
        "乌兹别克斯坦": "Uzbekistan",
        "瓦努阿图": "Vanuatu",
        "梵蒂冈": "Vatican_City",
        "委内瑞拉": "Venezuela",
        "越南": "Vietnam",
        "也门": "Yemen",
        "赞比亚": "Zambia",
        "津巴布韦": "Zimbabwe",
        "中国": "China"
    }
    return map.get(content)
def world(datas):#按国家统计
    res=[]
    val = [0] * 30
    world = [''] * 30
    attr = []
    value = []
    num = 0
    for data in datas:
        flag = 0
        for i in range(0, num):
            if data.country == world[i]:
                flag = 1
                val[i] += 1
        if flag == 0:
            world[num] = data.country
            val[num] = 1
            num += 1
    print(world)
    for j in range(num):
        attr.append(fanyi(world[j]))
        value.append(val[j])
        res.append({"country": world[j], "declare": val[j]})
    res.sort(key=lambda x: (x.get('declare', 0)), reverse=False)
    map0 = Map.Map("世界地图示例", width=1200, height=600)
    map0.add("世界", attr, value, maptype="world", is_visualmap=True, visual_text_color='#000')
    return res,map0
def college(datas):#按学院统计
    res=[]
    cnum = 0  # 学院数
    rows = len(datas)  # 总表长度
    flagc = [0] * (rows + 1)  # 学院的标记
    college = [''] * 100
    j = 0
    sheete= [0] * (rows + 1)
    for data in datas:  # 初始化
        sheete[j] = data.college
        j += 1
    for i in range(0, rows):  # 学院
        if flagc[i] != -1:
            college[cnum] = sheete[i]
            for k in range(i + 1, rows + 1):
                if sheete[k] == college[cnum]:
                    flagc[k] = -1
            cnum = cnum + 1
    cdeclare = [0] * cnum
    for data in datas:
        for i in range(0, cnum):
            if data.college == college[i]:
                cdeclare[i] += 1
    for i in range(0, cnum):
        res.append({"college": college[i], "declare": cdeclare[i]})
    return res
def world(datas,title):#按国家统计
    print(title)
    res=[]
    val = [0] * 30
    world = [''] * 30
    attr = []
    value = []
    num = 0
    for data in datas:
        flag = 0
        for i in range(0, num):
            if data.country == world[i]:
                flag = 1
                val[i] += 1
        if flag == 0:
            world[num] = data.country
            val[num] = 1
            num += 1
    print(world)
    for j in range(num):
        attr.append(fanyi(world[j]))
        value.append(val[j])
        res.append({"country": world[j], "declare": val[j]})
    res.sort(key=lambda x: (x.get('declare', 0)), reverse=False)
    map0 = Map.Map(title, width=1200, height=600)
    map0.add("世界", attr, value, maptype="world", is_visualmap=True, visual_text_color='#000')
    return res,map0