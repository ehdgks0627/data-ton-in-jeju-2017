#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

pattern = re.compile("([xX]?\d*[캔병]|[xX]?\d*[개입]|\*?\d*[캔병]|\*?\d*[개입])")
map_data ={'bed': ' 침대 ',
 'dining table': ' 책상 ',
 'mouse': ' 마우스 ',
 'keyboard': ' 키보드 ',
 'cell phone': ' 휴대전화 ',
 'refrigerator': ' 냉장고 ',
 'book': ' 책 ',
 'clock': ' 시계 ',
 'vase': ' 꽃병 ',
 'scissors': ' 가위 ',
 'hair drier': ' 드라이기 ',
 'toothbrush': ' 칫솔 ',
 'backpack': ' 가방 ',
 'umbrella': ' 우산 ',
 'handbag': ' 핸드백 ',
 'tie': ' 넥타이 ',
 'suitcase': ' 캐리어 ',
 'bottle': ' 물 ',
 'wine glass': ' 와인잔 ',
 'cup': ' 물 ',
 'fork': ' 포크 ',
 'knife': ' 나이프 ',
 'spoon': ' 수저 ',
 'bowl': ' 그릇 ',
 'hot dog': ' 핫도그 ',
 'pizza': ' 피자 ',
 'donut': ' 도넛 ',
 'cake': ' 케이크 ',
 'chair': ' 의자 ',
 'couch': ' 등받이 의자 ',
 'pen': ''}

def getItemPrice(word):
    print("Finding ", word)
    if word == "pen":
        return 1382
    return_value = 0
    avg=0
    count=0
    item={}
    f = open('output.csv')
    with open('output.csv') as f:
        for line in f:
            if line.split(",")[4].find(map_data[word]) is not -1:
                                #print line
                item.update({line.split(",")[4]:line.split(",")[5]})
    for i in item:
        avg = avg + int(item[i])
        count = count + 1
    f.close()
        #print avg
        #print count

    if count or avg > 0:
         return_value = (avg / count)
    else:
         return_value = avg

    if word == 'bottle':
        return_value = 883
    elif word == 'couch':
        return_value = 18721
    elif word == 'dining table':
        return_value = 38748
    elif word == 'chair':
        return_value = 13873
    return return_value
