import requests
import time
import random
from imageio import imread
from wordcloud import WordCloud
import jieba

url = 'https://www.huya.com/cache1min.php?m=chatMessage&tid=74049834&sid=74049834'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Referer': 'https://www.huya.com/12323',
}

n = 0
d = []

masks = imread('huyajpg.jpg')

del_list = ['{', '}', 'fe', 'hh', '/', '......', ',', '!']

while n < 20:
    try:
        r = requests.post(url, headers=header)
        r.raise_for_status()
        dan_dict = r.json()['result']['chats']
        danMu_list = [dan_dict[i]['chat'] for i in range(len(dan_dict))]
        for i in range(len(danMu_list)):
            danMu_cut_list = jieba.lcut(danMu_list[i])
            for j in danMu_cut_list:
                if j not in del_list:
                    d.append(j)
        n += 1
        time.sleep(random.randint(1, 3) * 5)
    except:
        print('爬取失败')

print(d)
danMu = ' '.join(d)
wc = WordCloud(mask=masks, font_path='C:\\Windows\\Fonts\\STKAITI', background_color='white',
               scale=32)
wc.generate(danMu)
wc.to_file('虎牙弹幕2.png')
