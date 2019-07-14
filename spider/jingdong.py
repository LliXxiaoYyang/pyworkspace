import requests
import json
import os
import time
import random
import jieba
from wordcloud import WordCloud
from imageio import imread



def crawl_comment(page=0):
    """爬取京东商品数据"""
    url = 'https://sclub.jd.com/comment/productPageComments.action?' \
          'callback=fetchJSON_comment98vv745&productId=49298658030&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1'%page
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Referer': 'https://item.jd.com/49298658030.html'
    }

    try:
        r = requests.get(url, headers=header)
        r.raise_for_status()
        # print('数据：'+r.text[0:500])
    except:
        print('爬取失败！')

    r_json_str = r.text[25:-2]
    #print(r_json_str)
    r_json_obj = json.loads(r_json_str,encoding='utf-8')
    r_json_comments = r_json_obj['comments']

    #print('评论为：')


    for r_json_comment in r_json_comments:
        with open('JD_comments.txt','a+',encoding='utf-8') as file:
            file.write(r_json_comment['content']+'\n')
        #print(r_json_comment['content'])

def bacth_spider_comment():
    """爬取京东某商品评价前100页"""
    for i in range(100):
        crawl_comment(i)
        time.sleep(random.random()*5)

def cut_word():
    with open('JD_comments.txt','r',encoding='utf-8')as f:
        content = f.read()
        word_list = jieba.cut(content,cut_all=True)
        word = ' '.join(word_list)
        #print(word_list)
        return word

def creat_wordcloud():
    coloring = imread('123.png')
    wc = WordCloud(background_color='white',mask=coloring,scale=4,
                   max_font_size=80,random_state=42,font_path='C:\\Windows\\Fonts\\simsun.ttc')
    wc.generate(cut_word())
    wc.to_file('lufei_clound.png')




if __name__ == '__main__':
    print(time.ctime())

    creat_wordcloud()
    print(time.ctime())
