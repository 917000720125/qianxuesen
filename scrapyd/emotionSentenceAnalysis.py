# -*- coding: utf-8 -*-
import random


def emotionSentenceAnalysis(oneNew):
    rand2=random.randint(1,5)
    if(rand2>3):
        oneNew["emotion"] = "正向"
        oneNew["level"] = random.randint(1, 2)
    elif(rand2<3):
        oneNew["emotion"] = "负向"
        oneNew["level"] = random.randint(1, 2)
    else:
        oneNew["emotion"] = "中立"
        oneNew["level"] = 0
    return oneNew

test={}
print(emotionSentenceAnalysis(test))