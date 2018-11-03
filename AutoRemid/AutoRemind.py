#coding:utf-8

from apscheduler.schedulers.blocking import BlockingScheduler
import itchat

def remind(author, msg):
	author.send(msg)

def login():
	print ('Login Success :)')

def logout():
	print ('Logout~')

if __name__ == '__main__':

	# 创建微信使用接口
	itchat.auto_login(hotReload=True, enableCmdQR=True, loginCallback=login, exitCallback=logout)
	# 创建调度器
	scheduler = BlockingScheduler()
	# 获取通知群
	itchat.get_chatrooms(update=True)
	author = itchat.search_chatrooms(name='打卡自动化')[0]
	# 设置通知消息
	msg = '打卡打卡~';

	# 设置定时任务
	# 周一 —— 周五，每天早上9点 [10、20、25] 分提醒
	scheduler.add_job(remind, 'cron', day_of_week='mon-fri', hour=9, minute='10,20,25', kwargs={'author': author, 'msg': msg})
	# 周一 —— 周五，每天晚上 19点-21点，0分 | 30分提醒一次
	scheduler.add_job(remind, 'cron', day_of_week='mon-fri', hour='19-21', minute='0,30', kwargs={'author': author, 'msg': msg})
	scheduler.start()
