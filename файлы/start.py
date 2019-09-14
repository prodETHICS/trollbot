#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys,time,requests
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
	QInputDialog, QApplication,QToolTip,QFileDialog,QMessageBox)
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets,QtGui,QtCore
import vk_api,random,requests,traceback,glob,time,json
from vk_api.longpoll import VkLongPoll, VkEventType, VkChatEventType
from python3_anticaptcha import ImageToTextTask
from python3_anticaptcha import errors
from CONFIG import info
from threading import Thread

def friends():
	while True:
		try:
			zayavki=requests.get("https://api.vk.com/method/friends.getRequests?access_token=%s" % info.token+"&v=5.92").json()['response']['items']
			print(zayavki)
			requests.get("https://api.vk.com/method/friends.add?access_token=%s" % info.token+"&v=5.92&user_id="+str(random.choice(zayavki)))
		except:
			pass
		try:
			zayavki1=requests.get("https://api.vk.com/method/friends.getRequests?access_token=%s" % info.token+"&out=true&v=5.92").json()['response']['items']
			print(zayavki1)
			requests.get("https://api.vk.com/method/friends.delete?access_token=%s" % info.token+"&v=5.92&user_id="+str(random.choice(zayavki1)))
		except:
			pass
		sleep(10)
def msgs(event,vk):
	peer_id = event.peer_id
	user_id = event.user_id
	b=event.text
	c=random.choice([1,2])
	if c == 1 and event.text != '' and event.user_id > 0 and not event.user_id in info.idvk:
		if peer_id > 2000000000 and not peer_id-2000000000 in info.conflist and not event.user_id in info.ignorelist:
			time.sleep(random.randint(1,5))
			f = open(info.msgs,encoding='utf-8')
			data1 = f.read()
			msg = data1.split('\n')[random.randint(0,len(open('фразы.txt', 'r',encoding='utf-8').readlines()))]
			g = open(info.fotki,encoding='utf-8')
			data2 = g.read()
			photo = data2.split('\n')[random.randint(0,len(open('фотки.txt', 'r',encoding='utf-8').readlines()))]
			c = open(info.name,encoding='utf-8')
			data3 = c.read()
			name = data3.split('\n')[random.randint(0,len(open('name.txt', 'r',encoding='utf-8').readlines()))]
			vk.messages.setActivity(peer_id=peer_id,type='typing')
			time.sleep(random.randint(5,10))
			vk.messages.send(peer_id=peer_id,random_id=random.randint(100000,999999),message=random.choice(["[id"+str(user_id)+"|"+name+"], "+msg,msg]),attachment=random.choice([str(photo),'','','','','','','']))
		if peer_id < 2000000000 and user_id > 0:
			if b[0:8] != "https://":
				time.sleep(random.randint(1,5))
				f = open(info.msgs)
				data = f.read()
				msg = data.split('\n')[random.randint(0,len(open('фразы.txt', 'r').readlines()))]
				vk.messages.setActivity(peer_id=peer_id,type='typing')
				g = open(info.fotki)
				data2 = g.read()
				photo = data2.split('\n')[random.randint(0,len(open('фотки.txt', 'r',encoding='utf-8').readlines()))]
				time.sleep(random.randint(5,10))
				vk.messages.send(peer_id=peer_id,random_id=random.randint(100000,999999),message=msg,attachment=random.choice([str(photo),'','','','','','','']))
			if b[0:8] == "https://":
				try:
					vk.messages.joinChatByInviteLink(link=b)
				except:
					pass
	if c == 2 and b[0:8] != "https://" and event.text != '' and event.user_id > 0 and not event.user_id in info.idvk and not peer_id-2000000000 in info.conflist:
		try:
			if peer_id > 2000000000 and not event.user_id in info.ignorelist:
				time.sleep(random.randint(1,5))
				a=vk.docs.getMessagesUploadServer(type='audio_message',peer_id=user_id)['upload_url']
				say=random.choice(glob.glob("voice msgs/*.mp3"))
				img = {'file': ('a.mp3', open(say, 'rb'))}
				response = requests.post(a, files=img)
				result = json.loads(response.text)['file']
				owner=vk.docs.save(file=result)['audio_message']['owner_id']
				document=vk.docs.save(file=result)['audio_message']['id']
				send = 'doc'+str(owner)+'_'+str(document)
				vk.messages.setActivity(peer_id=peer_id,type="audiomessage")
				time.sleep(random.randint(5,10))
				vk.messages.send(random_id=random.randint(100000,999999),attachment=send,peer_id=peer_id)
			if peer_id < 2000000000:
				time.sleep(random.randint(1,5))
				a=vk.docs.getMessagesUploadServer(type='audio_message',peer_id=user_id)['upload_url']
				say=random.choice(glob.glob("voice msgs/*.mp3"))
				img = {'file': ('a.mp3', open(say, 'rb'))}
				response = requests.post(a, files=img)
				result = json.loads(response.text)['file']
				owner=vk.docs.save(file=result)['audio_message']['owner_id']
				document=vk.docs.save(file=result)['audio_message']['id']
				send = 'doc'+str(owner)+'_'+str(document)
				vk.messages.setActivity(peer_id=peer_id,type="audiomessage")
				time.sleep(random.randint(5,10))
				vk.messages.send(random_id=random.randint(100000,999999),attachment=send,peer_id=peer_id)
		except:
			if peer_id > 2000000000 and not peer_id-2000000000 in info.conflist and not event.user_id in info.ignorelist:
				time.sleep(random.randint(1,5))
				f = open(info.msgs,encoding='utf-8')
				data1 = f.read()
				msg = data1.split('\n')[random.randint(0,len(open('фразы.txt', 'r',encoding='utf-8').readlines()))]
				g = open(info.fotki,encoding='utf-8')
				data2 = g.read()
				photo = data2.split('\n')[random.randint(0,len(open('фотки.txt', 'r',encoding='utf-8').readlines()))]
				c = open(info.name,encoding='utf-8')
				data3 = c.read()
				name = data3.split('\n')[random.randint(0,len(open('name.txt', 'r',encoding='utf-8').readlines()))]
				vk.messages.setActivity(peer_id=peer_id,type='typing')
				time.sleep(random.randint(5,10))
				vk.messages.send(peer_id=peer_id,random_id=random.randint(100000,999999),message=random.choice(["[id"+str(user_id)+"|"+name+"], "+msg,msg]),attachment=random.choice([str(photo),'','','','','','','']))
			if peer_id < 2000000000 and user_id > 0:
				if b[0:8] != "https://":
					time.sleep(random.randint(1,5))
					f = open(info.msgs,encoding='utf-8')
					data = f.read()
					msg = data.split('\n')[random.randint(0,len(open('фразы.txt', 'r',encoding='utf-8').readlines()))]
					vk.messages.setActivity(peer_id=peer_id,type='typing')
					g = open(info.fotki,encoding='utf-8')
					data2 = g.read()
					photo = data2.split('\n')[random.randint(0,len(open('фотки.txt', 'r',encoding='utf-8').readlines()))]
					time.sleep(random.randint(5,10))
					vk.messages.send(peer_id=peer_id,random_id=random.randint(100000,999999),message=msg,attachment=random.choice([str(photo),'','','','','','','']))
				if b[0:8] == "https://":
					try:
						vk.messages.joinChatByInviteLink(link=b)
					except:
						pass

def bot():
	def captcha_handler(captcha):
		key = ImageToTextTask.ImageToTextTask(anticaptcha_key=info.captcha, save_format='const') \
				.captcha_handler(captcha_link=captcha.get_url())
		return captcha.try_again(key['solution']['text'])
	vk_session = vk_api.VkApi(token=info.token, captcha_handler=captcha_handler)

	vk = vk_session.get_api()

	selfid = info.ignorelist
	ignore = info.conflist

	while True:
		try:
			longpoll = VkLongPoll(vk_session)
			for event in longpoll.listen():
				if event.type_id == VkChatEventType.USER_JOINED:
					a=event.info['user_id']
					chat_id = event.chat_id
					peer_id = event.peer_id
					if int(a) in info.idvk:
						try:
							vk.messages.editChat(chat_id=chat_id,title=random.choice(info.titlel))
							j=vk.photos.getChatUploadServer(chat_id=chat_id,crop_x=10,crop_y=25)['upload_url']
							img = {'photo': (random.choice(info.photo), open(random.choice(info.photo), 'rb'))}
							response = requests.post(j, files=img)
							result = json.loads(response.text)['response']
							vk.messages.setChatPhoto(file=result)
						except:
							pass
						try:
							vk.messages.unpin(peer_id=peer_id)
						except:
							pass
						try:
							vk.messages.addChatUser(chat_id=chat_id,user_id=556099083)
						except:
							pass
				if event.type_id == VkChatEventType.MESSAGE_PINNED:
					peer_id=event.peer_id
					r=vk.messages.getConversationsById(peer_ids=peer_id)['items'][0]['last_message_id']
					f=vk.messages.getById(message_ids=r,preview_length='0')['items'][0]['from_id']
					if not int(f) in info.idvk and int(f) > 0:
						vk.messages.unpin(peer_id=peer_id)
				if event.type_id == VkChatEventType.PHOTO:
					chat_id = event.chat_id
					peer_id = event.peer_id
					r=vk.messages.getConversationsById(peer_ids=peer_id)['items'][0]['last_message_id']
					f=vk.messages.getById(message_ids=r,preview_length='0')['items'][0]['from_id']
					title=vk.messages.getChat(chat_id=chat_id)['title']
					if not int(f) in info.idvk and int(f) > 0 and not event.chat_id in info.conflist:
						a=vk.photos.getChatUploadServer(chat_id=event.chat_id,crop_x=10,crop_y=25)['upload_url']
						img = {'photo': (random.choice(info.photo), open(random.choice(info.photo), 'rb'))}
						response = requests.post(a, files=img)
						result = json.loads(response.text)['response']
						vk.messages.setChatPhoto(file=result)
				if event.type_id == VkChatEventType.TITLE:
					chat_id = event.chat_id
					peer_id = event.peer_id
					r=vk.messages.getConversationsById(peer_ids=peer_id)['items'][0]['last_message_id']
					f=vk.messages.getById(message_ids=r,preview_length='0')['items'][0]['from_id']
					if not int(f) in info.idvk and int(f) > 0 and not event.chat_id in info.conflist:
						vk.messages.editChat(chat_id=chat_id,title=random.choice(info.titlel))
				if event.type == VkEventType.MESSAGE_NEW and not event.user_id in info.ignorelist:
					class message(Thread):
						def __init__(self,vk,event):
							Thread.__init__(self)
							self.vk = vk
							self.event = event
						def run(self):
							msgs(event,vk)
					my_thread1 = message(vk,event)
					my_thread1.start()
		except Exception as e:
			print('Ошибка:\n', traceback.format_exc())
			pass
class ha(QWidget):


	def __init__(self):
		super().__init__()

		self.initUI()
	def acc(self):
		try:
			tel,ok = QInputDialog.getText(self, 'доступ к акку',
				'Введите номер мобилы:')
			if str(ok) == 'True':
				pas,ok = QInputDialog.getText(self, 'доступ к акку',
					'Введите пароль:')
				title,ok = QInputDialog.getText(self, 'доступ к акку',
					'Введите название для бесед:')
				photo,ok = QFileDialog.getOpenFileName(self, 'Выберите фото для беседы',
					'Введите фото для бесед\nвместе с форматом:')
				captcha,ok = QInputDialog.getText(self, 'доступ к акку',
					'Введите ключ от anti-captcha.com:')
				f=requests.get("https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username=%s" % str(tel) + "&password="+str(pas))
				text='class info():\n	token = "'+str(f.json()["access_token"])+'"\n	idvk = ['+str(f.json()["user_id"])+']\n	ignorelist = ['+str(f.json()["user_id"])+']\n	conflist = []\n	fotki = "фотки.txt"\n	msgs = "фразы.txt"\n	name="name.txt"\n	titlel=["'+title+'"]\n	photo = ["'+photo+'"]\n	captcha="'+captcha+'"'
				k=open('CONFIG.py',"wt",encoding='utf8')
				k.write(text)
				k.close()
				QInputDialog.getText(self, 'Внимание!','Всё введено правильно')
			else:
				QInputDialog.getText(self, 'Ошибка!','Неправильно введены данные')
		except:
			QInputDialog.getText(self, 'Ошибка!','Неправильно введены данные')
	def initUI(self):
		def on_click():
			QInputDialog.getText(self, 'Внимание!','Бот запущен!\nЕсли он не работает, то перезапустите\nприложение и нажмите на эту кнопку снова')
			a="a"
			class MyThread(Thread):
				def __init__(self,a):
					Thread.__init__(self)
					self.a = a
				def run(self):
					bot()
					friends()
			my_thread = MyThread(a)
			my_thread.start()

		self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap("icon.png")))
		self.lbl = QtWidgets.QLabel(self)
		self.pix = QtGui.QPixmap("logo.png")
		self.lbl.setPixmap(self.pix)
		self.lbl.move(0, 0)


		self.btn3 = QPushButton('ДОСТУП К АККУ', self)
		self.btn3.move(205, 250)
		self.btn3.clicked.connect(self.acc)

		btn = QPushButton('ЗАПУСТИТЬ БОТА!', self)
		btn.setToolTip('<b>Ахахаха! Запускай!</b>')
		btn.resize(btn.sizeHint())
		btn.move(195, 450)
		btn.clicked.connect(on_click)

		self.lbl = QtWidgets.QLabel(self)
		self.pix = QtGui.QPixmap("troll.png")
		self.lbl.setPixmap(self.pix)
		self.lbl.resize(300, 200)
		self.lbl.move(125, 50)
		self.lbl1 = QtWidgets.QLabel(self)
		self.lbl1.setText('Бот для троллинга в Вконтакте!\nЧтобы разносить лошков, вам нужно:\n1.Завести страницу вк\n2.Заполнить "фразы.txt" для фраз (обяз.), "name.txt" для текста в \nупоминаниях (обяз.) и "photo.txt" ссылками на фото, например, \n"photo556099083_457266439"\n3.Заполнить папку "voice msgs" mp3 файлами\n4.Пройти опрос в кнопке "ДОСТУП К АККУ"\n5.Запустить бота!')
		self.lbl1.move(10, 300)

		self.setFixedSize(500, 500)
		self.setWindowTitle('TrollBot vk')
		self.show()

app = QApplication(sys.argv)
ex = ha()
sys.exit(app.exec_())
