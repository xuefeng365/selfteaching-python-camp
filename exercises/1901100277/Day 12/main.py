#使用另一个个人微信分享一篇文章 给登录微信机器人的个人微信号,并统计好文章词频,将处理结果返回给发送消息过来的好友

# # 导入模块
# from wxpy import *
# # 初始化机器人，扫码登陆
# bot = Bot()
# # 找到所以好友 
# my_friend = bot.friends()
# # 监听好友信息，自动响应分享类型的消息
# @bot.register(my_friend,SHARING)   #对于 --我的好友和其他群聊中 分享类型 SHARING的消息:
# # @bot.register([my_friend,Group],SHARING)   #对于 --我的好友和其他群聊中 分享类型 SHARING的消息:
# def get_friend_url(msg) :
#     if isinstance(msg.type,SHARING):
#         import requests
#         response=requests.get(msg.url)

#         from pyquery import PyQuery
#         document=PyQuery(response.text)
#         content=document('#js_content').text()

#         from mymodule import stats_word  
#         email_content = str(stats_word.stats_text_cn(content))

#         msg.reply(email_content)
#         # print ("我的好友或群里成员 分享的内容,转化为从大到小的词频为 >>>" + email_content)
# # 进入 Python 命令行、让程序保持运行
# embed()



#转化成图表
import requests
response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

from pyquery import PyQuery
document=PyQuery(response.text)
content=document('#js_content').text()


# from mymodule import stats_word
# email_content = str(stats_word.stats_text_cn(content))
# # print (email_content)


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pylab import mpl
mpl.rcParams['font.sans-serif']=['Microsoft YaHei']

from mymodule import stats_word
data = stats_word.stats_text_cn(content)
print (data)    # data 是一个大字典

key_s = data.keys()
value_s = data.values()
# for keys,values in data.items() :

print (f"词频中所有的 词_键) 为: {key_s}")

print (f"词频中所有的词 词频_值 为: {value_s}")

plt.rcParams.update({'figure.autolayout':True})
fig,ax=plt.subplots()
ax.barh(key_s,value_s)
plt.style.use('seaborn-paper')
labels=ax.get_xticklabels()
plt.setp(labels,horizontalalignment='right')
ax.set(xlabel='词频',ylabel='中文汉字',title='中文汉字词频统计')
plt.show()


