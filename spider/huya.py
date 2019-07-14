import requests
import json

url = 'https://www.huya.com/cache1min.php?m=chatMessage&tid=22808102&sid=2644054518'

form = {'m':'chatMessage',
'tid':'22808102',
'sid':'2644054518',
        }

hearder = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Referer':'https://www.huya.com/131499'
}


r = requests.get(url,headers=hearder,params=form)
r.raise_for_status()
print([r.json()['result']['chats'][i]['chat'] for i in range(20)])



