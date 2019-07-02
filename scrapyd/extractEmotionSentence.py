# -*- coding: utf-8 -*-
import os
import jieba
import jieba.analyse
import jieba.posseg


def extractEmotionSentence(oneNew):
    path1 = "./Stable/fenci.txt"
    path2="./Stable/checkedFenci.txt"
    path3="./Stable/crfResult.txt"
    content=oneNew['content']
    clean(content,path1)
    check(path1,path2)
    exeCRF(path2,path3)
    oneNew['sentence'],oneNew['subject']=toSentence(path3)
    return oneNew

def clean(content,path1):
    f = open(path1, 'w')
    s = content.replace('【环球网综合报道】', '')
    s = s.replace('££££', '')
    s = s.replace('　', '')
    s=s.replace('\xa0\xa0','')
    s = s.replace('\u3000\u3000', '')
    result = fenci(s)
    f.write(result)
    f.close()
def fenci(s):
    sentence_seged = jieba.posseg.cut(s.strip())
    outstr = ''
    for x in sentence_seged:
        outstr += "{} {}\n".format(x.word, x.flag)#迭代训练
    return outstr
def check(path1,path2):
    checked = []
    with open(path1, 'r')as f:
        list = f.readlines()
        i = 1
        for line in list:
            i = i + 1
            if line != "":
                a = line.split()
                if (len(a) == 2):
                    checked.append(line)
    with open(path2, 'w')as ff:
        for line in checked:
            ff.write(line)

#此处的model还在训练，可替换成相对路径
def exeCRF(path2,path3):
    cmd1 = "/Users/apple-pc/Desktop/CRF++-0.58/crf_test -m /Users/apple-pc/Desktop/CRF++-0.58/example/seg/model ./Stable/test.data"  # 结果预测
    # cmd2 = "/Users/apple-pc/Desktop/CRF++-0.58/crf_learn /Users/apple-pc/Desktop/CRF++-0.58/example/seg/template /Users/apple-pc/Desktop/CRF++-0.58/example/seg/train.data /Users/apple-pc/Desktop/CRF++-0.58/example/seg/model"  # 训练算法
    rr=os.popen("cp "+path2+" ./Stable/test.data")
    r = os.popen(cmd1)
    text = r.read()
    r.close()
    with open(path3, 'w')as f:
        f.write(text)
        f.close()
def toSentence(path3):
    rightSentence=""
    rightSubject=""
    text = ""
    news = []
    with open(path3, 'r')as f:
        list = f.readlines()
        # i=1
        for line in list:
            if(len(line.split())==3):
                tip = line.split()[-1]
                str = line.split()[0]
                # i=i+1
                # print(i)
                # print str
                if (tip == 'B') | (tip == 'b'):
                    text = str
                if (tip == 'M') | (tip == 'm'):
                    text += str
                if (tip == 'E') | (tip == 'e'):
                    text += str
                    news.append(text)
                if (tip == 'W') | (tip == 'w'):
                    news.append(str)
        f.close()
#此处对于多情感句的情况还未有明确的解决方案，目前只选取有完整主语的情感句作为该新闻的情感句
    if(news!=[]):
        for sentence in news:
            rightSentence=sentence
            if(getSubject(sentence)!=""):
                rightSubject=getSubject(sentence)
                return rightSentence, rightSubject
    else:
        print("no motion sentences in current news")
        return rightSentence, rightSubject
def getSubject(sentence):
    for item in fenci(sentence).split('\n'):
        if(len(item.split(' '))==2):
            word=item.split(' ')[1]
            if(word=="nr")|(word=="ns")|(word=="nt"):
                if((word!="中国")|(word!="南海")):
                    return item.split(' ')[0]


#
# test={}
# test["test"]="test"
# test["content"]="因此，美军必定会继续强化在南海军事存在和挑衅动作。美国《华盛顿邮报》10月9日文章，原题：特朗普总统正如何帮助中国在南海获胜多年来，中国一直与美国在南海争斗。中国之道是遵循古老的孙子兵法“不战而屈人之兵”。中国人一直是每次迈出一小步：在这里开垦个岛屿，在那里修建一条飞机跑道，在争议海域临时部署一座石油钻塔，设置一个行政区等。每步都旨在形成一种“小现实”，却不会引发其他方的军事反应。 　　鉴于中国的地缘政治目标合情合理，其政策完全合理。北京如今在南海的做法，与美国19世纪和20世纪初寻求在周边海域确立战略支配地位时在加勒比海的做法很类似。对南海的有效控制将令中国能自由出入更广阔的太平洋并进一步“软化”台湾地区，最重要的是，这正令中国成为一个“两洋”海军强国。实际上，南海是通往印度洋的门户，而后者是21世纪至关重要的水域，相当于中东油田和东亚各大都市之间的全球能源“州际公路”。中国在南海的行动与其打造从印度洋到苏伊士运河和东地中海的“商业帝国”密不可分。 　　从中国视角看，美国才是好斗的霸权国家。美国海军从遥远的北美驶入南海，而后者如同加勒比海之于美国，是中国的“后院水域”。美国须直面一种重要现实：西太平洋不再是美海军一家独大的“湖泊”，中国重获大国身份必定带来一种更为复杂的多极状况。(如今)美国必须在印太地区为中国的空军、海军力量至少腾出一定空间，而关键问题在于腾出多少空间。 谨记，美国在南海周边的主要盟友越南和菲律宾别无选择，只能与体量庞大、经济上占主导地位且地理上更靠近的中国和睦相处。这些国家需要美国扮演制衡中国的角色，而非彻底成为中国的敌人。他们深知美国在亚洲的强大军事存在终究具有可选择性，所以中国才是在地区行事的核心考量要素。特朗普已向亚洲盟友传递出更多不确定性。这可能迫使这些国家决定单独与中国达成谅解。此类过程将悄然进行，鲜被承认。但总有一天，我们(美国)将被唤醒并意识到亚洲已发生不可逆转的变化。"
# print(extractEmotionSentence(test))

