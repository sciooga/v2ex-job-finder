# v2ex-job-finder
帮助 V2EXer 更方便的寻找工作

分词功能使用[结巴中文分词](https://github.com/fxsjy/jieba)根据 V2EX 的情况更新了部分词条

目前支持提取公司名与公司所在城市(对四字公司名支持不太好)

代码示例：

<pre><code>
str = u'#上海# [诺亚财富] 财富管理领域巨头-专注财富金字塔尖客户-低风险创业机会------互联网金融'
name, place_list = search_company_keyworks(str)
print name
for i in place_list:
  print i
 
#<out>(正确)
#诺亚
#上海


str = u'[上海] 百度糯米团购 C 端_iOS 高级研发工程师'
name, place_list = search_company_keyworks(str)
print name
for i in place_list:
  print i
 
#<out>(正确)
#百度
#上海

str = u'[北京] 魔力盒 app 招 iOS、Android 大拿（ 15-30K）'
name, place_list = search_company_keyworks(str)
print name
for i in place_list:
  print i
 
#<out>(错误)
#魔力
#北京

str = u'掌赢科技欢迎最棒的安卓 iOS~'
name, place_list = search_company_keyworks(str)
print name
for i in place_list:
  print i
 
#<out>(正确)
#掌赢
#

</code></pre>