import requests,user_agent,json,flask,telebot,random,os,sys,secrets
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request
from uuid import uuid4 
from time import sleep
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start'])
def boten(message):
	mas = types.InlineKeyboardMarkup(row_width=1) 
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
		mas = types.InlineKeyboardMarkup(row_width=1)
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
#	elif message.text == '/cinsta' or message.text == '/cinsta@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/hinsta' or message.text == '/hinsta@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/uinsta' or message.text == '/uinsta@CH_IG_FB_TK_SNAP_BOT':

	elif message.text == '/ginsta' or message.text == '/ginsta@CH_IG_FB_TK_SNAP_BOT':
		while True :
			pro = requests.get('https://gimmeproxy.com/api/getProxy')
			if '"protocol"' in pro.text or '"ip"' in pro.text or '"port"' in pro.text:
				if str(pro.json()['protocol']) == 'socks5':
					proxy = str(pro.json()['curl'])
					bot.send_message(message.chat.id,"¶** جاري انشاء الحساب لطفا انتظر بعض ثواني ** : ",parse_mode = "markdown")
					uid = uuid4()
					Coke=secrets.token_hex(8)*8
					ssid = secrets.token_hex(8)*2
					r = requests.session()
					ERR = 0
					rem = requests.get('https://10minutemail.net/address.api.php',headers = {'cookie':'PHPSESSID='+ssid},proxies={'socks5':proxy})
					email = rem.json()['mail_get_mail']
					bot.send_message(message.chat.id, '**Done Get Email : {}**'.format(email),parse_mode = "markdown")
					num ="0123456789asdfghjklpoiuytrewqzxcvbnm"
					rand=''.join(random.choice(num)for man in   range(8))
					username='medo'+rand
					pas='@ONCLIK-@UT_UB'
					head={'Host': 'www.instagram.com','Cookie': Coke,'User-Agent': generate_user_agent(),'Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Csrftoken': 'missing','X-Instagram-Ajax': 'missing','X-Ig-App-Id': '936619743392459','X-Asbd-Id': '437806','X-Ig-Www-Claim': 'hmac.AR13pf0XdQA_XNAYLrmGWOJtWRr9WkLRRw_dNGcK6i1C5a_k','Content-Type': 'application/x-www-form-urlencoded','X-Requested-With': 'XMLHttpRequest','Content-Length': '432','Origin': 'https://www.instagram.com','Referer': 'https://www.instagram.com/accounts/emailsignup/','Te': 'trailers','Connection': 'close'}
					head_get_code={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','content-length': '67','content-type': 'application/x-www-form-urlencoded','cookie': Coke,'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(),'x-asbd-id': '437806','x-csrftoken': 'missing','x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-instagram-ajax': 'missing',}
					head={'Host': 'www.instagram.com','Cookie': Coke,'User-Agent': generate_user_agent(),'Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Csrftoken': 'missing','X-Instagram-Ajax': 'missing','X-Ig-App-Id': '936619743392459','X-Asbd-Id': '437806','X-Ig-Www-Claim': 'hmac.AR13pf0XdQA_XNAYLrmGWOJtWRr9WkLRRw_dNGcK6i1C5a_k','Content-Type': 'application/x-www-form-urlencoded','X-Requested-With': 'XMLHttpRequest','Content-Length': '432','Origin': 'https://www.instagram.com','Referer': 'https://www.instagram.com/accounts/emailsignup/','Te': 'trailers','Connection': 'close'}
					data_age={'day': '27','month': '8','year': '2000'}
					data_attemp={'email': email,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{pas}','username': username,'first_name': 'BY HIMA - @ar_programmers','client_id': uid,'seamless_login_enabled': '1','opt_into_one_tap': 'false',}
					data_get_code={'device_id': uid,'email': email}
					req_attemp=requests.post(f'https://www.instagram.com/accounts/web_create_ajax/attempt/',headers=head,data=data_attemp,proxies={'socks5':proxy})
					req_age=requests.post(f'https://www.instagram.com/web/consent/check_age_eligibility/',headers=head,data=data_age,proxies={'socks5':proxy})
					req_get_code=requests.post(f'https://i.instagram.com/api/v1/accounts/send_verify_email/',headers=head_get_code,data=data_get_code,proxies={'socks5':proxy})
					bot.send_message(message.chat.id, '**GETING THE CODE ...... **',parse_mode = "markdown")
					sleep(15)
					rei = requests.post('https://10minutemail.net/address.api.php',headers = {'cookie':'PHPSESSID='+ssid},proxies={'socks5':proxy}).text
					code = rei.split(',"subject":"')[1].split(' is')[0]
					data_send_code={'code': code,'device_id': uid,'email': email}
					req_send_code=requests.post(f'https://i.instagram.com/api/v1/accounts/check_confirmation_code/',headers=head_get_code,data=data_send_code,proxies={'socks5':proxy})
					singup_code=req_send_code.json()['signup_code']
					data_crate={'email': email,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{pas}','username': username,'first_name': 'By HIMA','month': '8','day': '27','year': '2002','client_id':uid,'seamless_login_enabled': '1','tos_version': 'row','force_sign_up_code': singup_code,}
					req_crate=requests.post(f'https://www.instagram.com/accounts/web_create_ajax/',headers=head,data=data_crate,proxies={'socks5':proxy})
					bot.send_message(message.chat.id, '**Done GrEaT AccOuNt :** `{}:{}`\n sessionid : `{}`'.format(email,pas,ssid),parse_mode = "markdown")
				else:
					bot.send_message(message.chat.id,"¶** خطأ في الخادم جاري احظار خادم شغال\n¶ ERORR PROXY SERCH IT **",parse_mode = "markdown")
			else:
				bot.send_message(message.chat.id, '**ERORR PROXY **',parse_mode = "markdown")
	elif message.text == 'احبك' or message.text == 'اعشقك' or message.text == 'تحبني':
		bot.send_message(message.chat.id, 'انجب انا احب يوصف🥱')
	elif message.text == 'تخليني' or message.text == 'انيجك':
		bot.send_message(message.chat.id, 'حظر حالك بدي كبك بالزباله')
	elif message.text == 'كس' or message.text == 'كس@CH_IG_FB_TK_SNAP_BOT':
		bot.send_message(message.chat.id, 'جاري اابحث عن كس....')
		sleep(2)
		bot.send_message(message.chat.id, 'تم التاكد من انك كس حقيقي')
#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif message.text == '/snap' or message.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

		
	



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
