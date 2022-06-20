import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)



@bot.message_handler(commands=['start'])
def boten(message):
	mas = types.InlineKeyboardMarkup(row_width=2) 
	I = types.InlineKeyboardButton(text ="INSTAGRAM", callback_data="F1")
	F = types.InlineKeyboardButton(text ="FACEBOOK", callback_data="F2")
	T = types.InlineKeyboardButton(text =" TIKTOK ", callback_data="F3")
	S = types.InlineKeyboardButton(text ="SNAPCHAT", callback_data="F4")
	W = types.InlineKeyboardButton(text ="Twitter", callback_data="F5")
	M = types.InlineKeyboardButton('DEVELOPER', url='https://t.me/ONCLIK')
	mas.add(I,F,T,S,W,M)
	logo = 'https://firebasestorage.googleapis.com/v0/b/shoteriq.appspot.com/o/IMG_20220527_223323_610.jpg?alt=media&token=20802a14-94fe-481e-a404-aaed52bb7784'
	bot.send_photo(message.chat.id,logo, f"- WELCOME TO MY BOT PLEASE CHOISE ANY FUCTION️",reply_markup=mas)

@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	global nam
	if call.data =="MohammedNajih":
		mas = types.InlineKeyboardMarkup(row_width=2)
		I = types.InlineKeyboardButton(text ="INSTAGRAM", callback_data="F1")
		F = types.InlineKeyboardButton(text ="FACEBOOK", callback_data="F2")
		T = types.InlineKeyboardButton(text =" TIKTOK ", callback_data="F3")
		S = types.InlineKeyboardButton(text ="SNAPCHAT", callback_data="F4")
		W = types.InlineKeyboardButton(text ="Twitter", callback_data="F4")
		M = types.InlineKeyboardButton('DEVELOPER', url='https://t.me/ONCLIK')
		logo = 'https://firebasestorage.googleapis.com/v0/b/shoteriq.appspot.com/o/IMG_20220527_223323_610.jpg?alt=media&token=20802a14-94fe-481e-a404-aaed52bb7784'
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="- WELCOME TO MY BOT PLEASE CHOISE ANY FUCTION️",reply_markup=mas)
	if call.data =="F1":
		instagram = 'https://firebasestorage.googleapis.com/v0/b/shoteriq.appspot.com/o/PicsArt%20MQ_06-20-04.37.10.png?alt=media&token=cdcb997c-a027-40c9-8951-e381984d8a4b'
		bot.send_photo(call.message.chat.id,instagram,"GO TO START INSTAGRAM PLEASE\n SEND /insta IN BOOT" )
	if call.data =="F2":
		facebook = 'https://firebasestorage.googleapis.com/v0/b/shoteriq.appspot.com/o/PicsArt%20MQ_06-20-04.35.54.png?alt=media&token=1722f74c-b08b-4113-8d32-42379703f56f'
		bot.send_photo(call.message.chat.id,facebook,"Welcome to Menu Facebook\nSEND /face IN BOOT" )
	if call.data =="F3":
		tiktok = 'https://firebasestorage.googleapis.com/v0/b/shoteriq.appspot.com/o/PicsArt%20MQ_06-20-04.36.55.png?alt=media&token=3683d194-2703-4b1e-9649-7f8521a663d7' 
		bot.send_photo(call.message.chat.id,tiktok,"Welcome to Menu TikTok\nSEND /tik IN BOOT" )
	if call.data =="F4":
		snapchat = 'https://firebasestorage.googleapis.com/v0/b/shoteriq.appspot.com/o/PicsArt%20MQ_06-20-04.41.34.png?alt=media&token=a8946655-367b-4d41-b6b7-16d5fa9e13b7'
		bot.send_photo(call.message.chat.id,snapchat,"Welcome to Menu SnapChat\nSEND /snap IN BOOT" )
	if call.data =="F5":
		twi = 'https://firebasestorage.googleapis.com/v0/b/shoteriq.appspot.com/o/PicsArt%20MQ_06-20-04.41.03.png?alt=media&token=e3825d71-2b1a-45ac-8e76-4cf33f6a34d4'
		bot.send_photo(call.message.chat.id,twi,"Welcome to Menu Twitter\nSEND /twi IN BOOT" )
@bot.message_handler(commands=['insta'])
def sms(message):
	instj = 'https://firebasestorage.googleapis.com/v0/b/shoteriq.appspot.com/o/PicsArt%20MQ_06-20-04.37.10.png?alt=media&token=cdcb997c-a027-40c9-8951-e381984d8a4b'
	bot.send_photo(call.message.chat.id,instj,"مرحبا بك في قائمة الانستا اختر الان احد الخيارات ¶ 1 لبدأ فحص الحسابات قم بارسال /checkinsta في البوت ¶ 2 لبدأ فحص المتاحان قم بارسال /huntinsta في البوت ¶ 3 لبدأ فحص اليوزرات قم بارسال /userinsta في البوت ¶ 4 لبدأ انشاء الحسابات قم بارسال /ginsta في البوت ")
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://php-sot.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
