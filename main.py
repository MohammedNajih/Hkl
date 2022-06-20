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
	logo = 'https://t.me/z9oon/7'
	bot.send_video(message.chat.id,logo, caption=" Welcome to My Bot Fuction All Websites ",reply_markup=mas)

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
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=" Welcome to My Bot Fuction All Websites ",reply_markup=mas)
	elif call.data =="F1":
		instagram = 'https://t.me/z9oon/5'
		bot.send_video(call.message.chat.id,instagram,caption="Welcome to Menu INSTAGRAM PLEASE\nSEND /insta IN BOOT" )
	elif call.data =="F2":
		facebook = 'https://t.me/z9oon/12'
		bot.send_video(call.message.chat.id,facebook,caption="Welcome to Menu Facebook\nSEND /face IN BOOT" )
	elif call.data =="F3":
		tiktok = 'https://t.me/z9oon/11'
		bot.send_video(call.message.chat.id,tiktok,caption="Welcome to Menu TikTok\nSEND /tik IN BOOT" )
	elif call.data =="F4":
		snapchat = 'https://t.me/z9oon/8'
		bot.send_video(call.message.chat.id,snapchat,caption="Welcome to Menu SnapChat\nSEND /snap IN BOOT" )
	elif call.data =="F5":
		twi = 'https://t.me/z9oon/3'
		bot.send_video(call.message.chat.id,twi,caption="Welcome to Menu Twitter\nSEND /twi IN BOOT" )


@bot.message_handler(content_types=['text'])
def start(message):
	if message.text == '/insta' or message.text == '/insta@CH_IG_FB_TK_SNAP_BOT':
		instagram = 'https://t.me/z9oon/5'
		bot.send_video(message.chat.id,instagram,caption= '**ʰᵉˡˡᵒ ʷᵒʳˡᵈ ʷᵉˡˡᶜᵒᵐᵉ ᵗᵒ ᵐᵉᶰᵘ ᶤᶰˢᵗᵃᶠ!ᵍʳᵃᵐ**\n**ˢᵉᶰᵈ /cinsta ᶠᵒʳ ᶜʰᵉᶜᵏᵉʳ ᵃᶜᶜᵒᵘᶰᵗ ᶤᶰˢᵗᵃ**\n**ˢᵉᶰᵈ /hinsta ᶠᵒʳ ʰᵘᶰᵗᵉʳ ᶤᶰˢᵗᵃᵍʳᵃᵐ ᵃᶜᶜᵒᵘᶰᵗ**\n**ˢᵉᶰᵈ /uinsta ᶠᵒʳ ᶜʰᵉᶜᵏᵉʳ ᵘˢᵉʳ ᶤᶰˢᵗᵃᵍʳᵃᵐ**\n **ˢᵉᶰᵈ /ginsta ᶠᵒʳ ᵍʳᵉᵃᵗ ᵃᶜᶜᵒᵘᶰᵗ ᶤᶰˢᵗᵃᵍʳᵃᵐ**\n**ˢᵉᶰᵈ /start ᶠᵒʳ ᵇᵃᶜᵏ ᵗᵒ ʰᵒᵐᵉ ᵐᵉᶰᵘ**',parse_mode = "markdown")
	elif message.text == '/face' or message.text == '/face@CH_IG_FB_TK_SNAP_BOT':
		facebook = 'https://t.me/z9oon/12'
		bot.send_video(message.chat.id,facebook,caption= '**ʰᵉˡˡᵒ ʷᵒʳˡᵈ ʷᵉˡˡᶜᵒᵐᵉ ᵗᵒ ᵐᵉᶰᵘ ᶠᵃᶜᵉᵇᵒᵒᵏ**\n**ˢᵉᶰᵈ /hfb ᶠᵒʳ ʰᵘᶰᵗᵉʳ ᶠᵃᶜᵉᵇᵒᵒᵏ**\n**ˢᵉᶰᵈ /start ᶠᵒʳ ᵇᵃᶜᵏ ᵗᵒ ʰᵒᵐᵉ ᵐᵉᶰᵘ**',parse_mode = "markdown")
	elif message.text == '/tik' or message.text == '/tik@CH_IG_FB_TK_SNAP_BOT':
		tiktok = 'https://t.me/z9oon/11'
		bot.send_video(message.chat.id,tiktok,caption= '**ʰᵉˡˡᵒ ʷᵒʳˡᵈ ʷᵉˡˡᶜᵒᵐᵉ ᵗᵒ ᵐᵉᶰᵘ ᵗᶤᵏᵗᵒᵏ**\n**ˢᵉᶰᵈ /htik ᶠᵒʳ ʰᵘᶰᵗᵉʳ ᵗᶤᵏᵗᵒᵏ**\n**ˢᵉᶰᵈ /utik ᵗᵒ ᶜʰᵉᶜᵏ ᵘˢᵉʳ ᵗᶤᵏᵗᵒᵏ**\n**ˢᵉᶰᵈ /start ᶠᵒʳ ᵇᵃᶜᵏ ᵗᵒ ʰᵒᵐᵉ ᵐᵉᶰᵘ**',parse_mode = "markdown")
	elif message.text == '/twi' or message.text == '/twi@CH_IG_FB_TK_SNAP_BOT':
		twi = 'https://t.me/z9oon/4' 
		bot.send_video(message.chat.id,twi,caption='**ʰᵉˡˡᵒ ʷᵒʳˡᵈ ʷᵉˡˡᶜᵒᵐᵉ ᵗᵒ ᵐᵉᶰᵘ ᵗʷᶤᵗᵗᵉʳ**\n**ˢᵉᶰᵈ /htwi ᶠᵒʳ ʰᵘᶰᵗᵉʳ **\n**ˢᵉᶰᵈ /utwi ᵗᵒ ᶜʰᵉᶜᵏ ᵘˢᵉʳ ᵗʷᶤᵗᵗᵉʳ**\n**ˢᵉᶰᵈ /start ᶠᵒʳ ᵇᵃᶜᵏ ᵗᵒ ʰᵒᵐᵉ ᵐᵉᶰᵘ**',parse_mode = "markdown")
	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':
		snapchat = 'https://t.me/z9oon/10'
		bot.send_video(message.chat.id,snapchat,caption= "**ʰᵉˡˡᵒ ʷᵒʳˡᵈ ʷᵉˡˡᶜᵒᵐᵉ ᵗᵒ ᵐᵉᶰᵘ ˢᶰᵃᵖᶜʰᵃᵗ**\n**ˢᵉᶰᵈ /hsnap ᶠᵒʳ ʰᵘᶰᵗᵉʳ **\n**ˢᵉᶰᵈ /usnap ᵗᵒ ᶜʰᵉᶜᵏ ᵘˢᵉʳ ˢᶰᵃᵖᶜʰᵃᵗ**\n**ˢᵉᶰᵈ /start ᶠᵒʳ ᵇᵃᶜᵏ ᵗᵒ ʰᵒᵐᵉ ᵐᵉᶰᵘ**",parse_mode = "markdown")
	else:
		error = 'https://t.me/z9oon/6'
		bot.send_video(message.chat.id,error, caption="الامر خاطئ ابدأ من جديد /start  🤍")




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
