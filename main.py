#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
import re
from urllib import urlretrieve as dw
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")

bot = telebot.TeleBot('TOKEN')
admin = 68747297

@bot.message_handler(func=lambda m: m.text)
def n(m):
    text = m.text
    id = m.from_user.id
    if re.match('^/(id)$',text):
        bot.send_message(m.chat.id, m.from_user.id)
    if re.match('^([/]help)$',text):
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
    if m.chat.type == 'group' or  m.chat.type == 'supergroup':
        if m.reply_to_message:
            if m.reply_to_message.from_user.username == 'test_isdafsbot':
                if re.match('(ftp|http|https)://.*\.(png)$',text):
                    bot.send_message(m.chat.id, 'ok wait')
                    dw(text,'s.png')
                    bot.send_photo(m.chat.id, open('s.png'))
                    os.remove('s.png') 
                if re.match('(ftp|http|https)://.*\.(jpg)$',text):
                    bot.send_message(m.chat.id, 'ok wait')
                    dw(text,'s.jpg')
                    bot.send_photo(m.chat.id, open('s.jpg'))
                    os.remove('s.jpg') 


bot.polling()
