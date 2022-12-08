import requests,json, secrets,names
sessionid = secrets.token_hex(8)*2
name1 = [names.get_first_name()]
domin = input('Enter domain Ex. @gmail.com..... : ')
while True :
    name =names.get_first_name(gender='femal')
    req = requests.get('https://www.instagram.com/web/search/topsearch/?context=blended&query=' +name+domin,headers ={'cookie':'sessionid='+sessionid})
    #print(req.json())
    req= req.json()['users'][0]['user']['full_name']
    #if ' ' in req:
        #email = req.split(' ')[1].split('@')[0]+domin
    if '@' in req and not ' '  in req:
        print(req)
