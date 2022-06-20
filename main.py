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
	M = types.InlineKeyboardButton('DEVELOPER', url='https://t.me/ONCLIK')
	mas.add(I,F,T,S,M)
	bot.send_message(message.chat.id, f"- WELCOME TO MY BOT PLEASE CHOISE ANY FUCTION️",reply_markup=mas)

@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	global nam
	if call.data =="MohammedNajih":
		mas = types.InlineKeyboardMarkup(row_width=2)
		I = types.InlineKeyboardButton(text ="INSTAGRAM", callback_data="F1")
		F = types.InlineKeyboardButton(text ="FACEBOOK", callback_data="F2")
		T = types.InlineKeyboardButton(text =" TIKTOK ", callback_data="F3")
		S = types.InlineKeyboardButton(text ="SNAPCHAT", callback_data="F4")
		M = types.InlineKeyboardButton('DEVELOPER', url='https://t.me/ONCLIK')
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="- WELCOME TO MY BOT PLEASE CHOISE ANY FUCTION️",reply_markup=mas)
	if call.data =="F1":
			pr = 'https://firebasestorage.googleapis.com/v0/b/shoteriq.appspot.com/o/IMG_20220527_223323_610.jpg?alt=media&token=20802a14-94fe-481e-a404-aaed52bb7784' 
			bot.send_photo(call.message.chat.id,pr,"GO TO START INSTAGRAM PLEASE\n SEND /insta IN BOOT" )
		
@bot.message_handler(commands=['insta'])
def sms(message):
	IN = types.InlineKeyboardMarkup(row_width=2) 
	C = types.InlineKeyboardButton(text ="CHECKER", callback_data="I1")
	H = types.InlineKeyboardButton(text ="HUNTER", callback_data="I2")
	U = types.InlineKeyboardButton(text ="CHECK USER", callback_data="I3")
	G = types.InlineKeyboardButton(text ="GREAT ACCOUNT", callback_data="I4")
	M = types.InlineKeyboardButton('DEVELOPER', url='https://t.me/ONCLIK')
	IN.add(C,H,U,G,M)
	bot.send_message(message.chat.id, f"- WELCOME TO MY BOT PLEASE CHOISE ANY FUCTION️",reply_markup=IN)
@bot.callback_query_handler(func=lambda call: True)
def Nop(call):
	global nam
	if call.data =="MohammmedNajih":
		IN = types.InlineKeyboardMarkup(row_width=2)
		C = types.InlineKeyboardButton(text ="CHECKER", callback_data="I1")
		H = types.InlineKeyboardButton(text ="HUNTER", callback_data="I2")
		U = types.InlineKeyboardButton(text ="CHECK USER", callback_data="I3")
		G = types.InlineKeyboardButton(text ="GREAT ACCOUNT", callback_data="I4") 
		M = types.InlineKeyboardButton('DEVELOPER', url='https://t.me/ONCLIK')
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="- WELCOME TO MY BOT PLEASE CHOISE ANY FUCTION️",reply_markup=IN)
	if call.data == 'I1':
		bot.send_message(message.chat.id, f"- WELCOME TO MY BOT PLEASE CHOISE ANY FUCTION️")
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
