# -*- coding: utf-8 -*-
# __author__ = 'sciooga'

import re
import jieba.posseg as pseg





def search_place_name(str):
    t = '('
    for line in open("place name.txt"):
        t += line.decode('utf-8').strip('\n')+'|'
    place_name=t[:-1]+')'
    place_name_list = re.findall(place_name, str) or []
    return list(set(place_name_list))

def search_company_keyworks(str):
    couple = u'(\[|\]|\【|\】|\『|\』|\「|\」|\(.+?\)|\（.+?\）|\<.+?\>|\《.+?\》)'
    new_str = re.sub(couple, '', str)
    print u'去括号后：%s' % new_str
    new_str = re.sub(u'[~@#$%^&*-=\！\|\\\~\\￥\…]', '', new_str)
    print u'去特殊符号后：%s' % new_str
    place_name_list = search_place_name(new_str)
    for i in place_name_list:
        new_str = re.sub(i, '', new_str)
    print u'去地名后：%s' % new_str
    k = re.search(u'(招|聘|诚|寻|找|做|来|求|邀)', new_str) or ''
    if (k and k.start()>10):
        new_str = new_str[:k.start()]
    print u'去职位后：%s' % new_str
    seg_list = pseg.cut(new_str)
    words = []
    keywords = []
    for i in seg_list:
        words.append(i)
    t = '('
    for line in open("del key.txt"):
        t += line.decode('utf-8').strip('\n')+'|'
    del_key=t[:-1]+')'
    for i in words[::-1]:
        print u'词：%s 词性：%s 词长：%d' % (i.word, i.flag, len(i.word))
        if (re.search(del_key, i.word)):
            new_str = re.sub(i.word, '', new_str)
        print u'去关键词后：%s' % new_str
        if (i.flag in ('r', 'd', 'x', 'uj', 'ul', 'zg', 'ns', 'p', 'q', 'b', 'c', 'u', 'y')):
            new_str = re.sub(i.word, '', new_str)
        elif (i.flag in ('a', 'm', 'v', 'v', 'n', 'vn', 'eng', 'nt', 'nr')):
            keywords.append(i.word)
    for i in keywords:
        if (len(new_str)-len(i) < 2 ):
            print u'减去后字符串小于2'
            break
        new_str = re.sub(i, '', new_str)
    print u'原句：%s' % str
    for i in place_name_list:
        print u'所在城市：%s' % i
    print u'语义分析去关键词后：%s' % new_str
    return new_str, place_name_list




str = u'掌赢科技欢迎最棒的安卓 iOS~'
name, place_list = search_company_keyworks(str)
print name
for i in place_list:
  print i
