#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
import re
from urllib import urlretrieve as dw
import sys
import os
#import color
reload(sys)
sys.setdefaultencoding("utf-8")

bot = telebot.TeleBot('TOKEN')
admin = 68747297
botusername = 'Usernamebot'

@bot.message_handler(func=lambda m: m.text)
def n(m):
    text = m.text
    id = m.from_user.id
    print 'Text : \033[32m{}\nID : \033[31m{}'.format(text,id)
    if re.match('^/(id|who)$',text):
        bot.send_message(m.chat.id, m.from_user.id)
    if re.match('^/(help|start)$',text):
        bot.send_message(m.chat.id, """
1> /id
2> <code>send url png|jpg</code>
3> #Soon
        """,parse_mode='HTML')
    if m.chat.type == 'private':
        if re.match('(ftp|http)://.*\.(png)$',text):
            bot.send_message(m.chat.id, 'ok wait')
            dw(text,'s.png')
            bot.send_photo(m.chat.id, open('s.png'))
            os.remove('s.png') 
        if re.match('(ftp|http|https)://.*\.(jpg)$',text):
            bot.send_message(m.chat.id, 'ok wait')
            dw(text,'s.jpg')
            bot.send_photo(m.chat.id, open('s.jpg'))
            os.remove('s.jpg') 
        if re.match('(ftp|http|https)://.*\.(zip)$',text):
            bot.send_message(m.chat.id, 'ok wait')
            dw(text,'file.zip')
            bot.send_photo(m.chat.id, open('file.zip'))
            os.remove('file.zip')
    if m.chat.type == 'group' or  m.chat.type == 'supergroup':
        if m.reply_to_message:
            if m.reply_to_message.from_user.username == botusername:
                if re.match('(ftp|http|https)://.*\.(png)$',text):
                    bot.send_message(m.chat.id, 'ok wait')
                    dw(text,'s.png')
                    bot.send_photo(m.chat.id, open('s.png'))
                    os.remove('s.png') 
                if re.match('(ftp|http|https)://.*\.(jpg)$',text):      #
                    bot.send_message(m.chat.id, 'ok wait')              # pic download File (Group by reply)
                    dw(text,'s.jpg')                                    #
                    bot.send_photo(m.chat.id, open('s.jpg'))          
                    os.remove('s.jpg')
                    print 'Remove jpg file'
                if re.match('(ftp|http|https)://.*\.(zip)$',text):
                    bot.send_message(m.chat.id, 'ok wait')              #
                    dw(text,'file.zip')                                 # zip files
                    bot.send_photo(m.chat.id, open('file.zip'))         #
                    os.remove('file.zip')
                    print 'Remove zip file'


bot.polling(True)
