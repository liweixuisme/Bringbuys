#encoding: UTF-8
import requests
import json
import time

def get_nums():
    with open('num8.txt','a',encoding="utf-8") as f:
        t=time.time()
        # now=int(t)
        now=int(1611250800-86400)
        searchDay=1451610483
        now_long=int(round(t * 1000))
        while now>=searchDay:
            current = 1
            total = 2
            while current<=total:
                url='https://trioprima.net/pt/provider/mem/game/results/B1SC?timestamp=%d&timestamp=%d&lang=zh-cn&gametype=B1SC&search_type=1&start=%d&page=%s'%(now_long,now_long-1,now,current)
                header={
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
                    'cookie': 'charset=zh-cn; nsk_webver=b9a6a81; eMobile=0; BBSESSID=3c1084a3dbbe1f633490793e475d6dc58869e06b; SESSION_ID=3c1084a3dbbe1f633490793e475d6dc58869e06b; PHPSESSID=asnfnudn5nh49v5vpvjbbip513; color=gray; ipl_menu=LT; bbinwin=true; exit_option=3; exit_info=none; GoldCatch=Array%285%2C10%2C20%2C50%29; isLogin=y; mfid=x-OOcI_GYlUewxLXRbXeB8ZxO57yYoAivumE_LfsLF3Bgl1_tIQsExKn8ufD_AZ51rw0EXNCElayD8baBSsHi2hYMGRWZUxKamhmT2t1ZlNWT2NMTlF1ZHN4VjNlRDl6Vk4zSzh1dlJKLU0; casino_url=http%3A%2F%2F777.bge777.com; _ga=GA1.2.252751072.1614688777; _gid=GA1.2.244472937.1614688777; _gat_UA-98257209-2=1',
                    'accept': 'application/json, text/plain, */*',
                }
                rp=requests.get(url,headers=header)
                data=json.loads(rp.text)
                print(data)
                nums=data['ret']['results']
                if nums:
                    current=int(data['ret']['pages']['current'])+1
                    total=int(data['ret']['pages']['total'])
                    ali=[]
                    for v in nums.values():
                        ali.append(v)

                    rp=sorted(ali,key=lambda x:x["game_id"],reverse=True)
                    for i in rp:
                        f.write(str(i)+"\n")
                    time.sleep(60)
                else:
                    break
            now-=86400

if __name__ == '__main__':
    get_nums()


    # t = time.time()
    # now = int(t)
    # searchDay = 1609473600
    # now_long = int(round(t * 1000))
    # current = 1
    # total = 2
    # url = 'https://trioprima.net/pt/provider/mem/game/results/B1SC?timestamp=%d&timestamp=%d&lang=zh-cn&gametype=B1SC&search_type=1&start=%d&page=%s' % (now_long, now_long - 1, now, current)
    # header = {
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    #     'cookie': 'charset=zh-cn; nsk_webver=b9a6a81; eMobile=0; BBSESSID=3c1084a3dbbe1f633490793e475d6dc58869e06b; SESSION_ID=3c1084a3dbbe1f633490793e475d6dc58869e06b; PHPSESSID=asnfnudn5nh49v5vpvjbbip513; color=gray; ipl_menu=LT; bbinwin=true; exit_option=3; exit_info=none; GoldCatch=Array%285%2C10%2C20%2C50%29; isLogin=y; mfid=x-OOcI_GYlUewxLXRbXeB8ZxO57yYoAivumE_LfsLF3Bgl1_tIQsExKn8ufD_AZ51rw0EXNCElayD8baBSsHi2hYMGRWZUxKamhmT2t1ZlNWT2NMTlF1ZHN4VjNlRDl6Vk4zSzh1dlJKLU0; casino_url=http%3A%2F%2F777.bge777.com; _ga=GA1.2.252751072.1614688777; _gid=GA1.2.244472937.1614688777; _gat_UA-98257209-2=1',
    #     'accept': 'application/json, text/plain, */*',
    # }
    # rp = requests.get(url, headers=header)
    # data = json.loads(rp.text)
    # print(data)