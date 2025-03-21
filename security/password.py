#!/usr/bin/env python

"""
Copyright (c) 2023-2025 ibrut developers (https://github.com/khamdihi-dev)
Ganti Nama, Jual Enak Banget Lu, Gk Punya Malu??
"""

import re
import sys
import time
import uuid
import random
import requests
import string


class change:
    def __init__(self, cookie, sandiOLD, sandiNEW):
        if 'mid' not in cookie or 'csrftoken' not in cookie:
            self.data = self.Shared_Data(cookie)
            self.cookie = self.generate_default_cokie(self.data)
        else:
            self.cookie = cookie
        self.NewPas = f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{sandiNEW}'
        self.OldPas = f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{sandiOLD}'

    def WebSession(self) -> str:
        self.a = ''.join(random.choice(string.ascii_lowercase+string.digits) for _ in range(6))
        self.b = ''.join(random.choice(string.ascii_lowercase+string.digits) for _ in range(6))
        self.c = ''.join(random.choice(string.ascii_lowercase+string.digits) for _ in range(6))
        return '{}:{}:{}'.format(self.a,self.b,self.c)

    def Shared_Data(self,cookie) -> None:
        try:
            self.headers_Shared = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dpr': '1',
                'priority': 'u=0, i',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
                'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6834.84", "Microsoft Edge";v="132.0.2957.115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
                'viewport-width': '1358',
            }
            self.respon = requests.get('https://www.instagram.com/data/shared_data/', headers=self.headers_Shared).json()['config']['csrf_token']
            return cookie + f';csrftoken={self.respon};'
        except Exception as e:
            return cookie + ';csrftoken=NPWtMg1bzwTyBCPicx4x1BnMjt77sLTk;'
        
    def generate_default_cokie(self, coks) -> str:
        self.acak = ''.join(random.choice(string.ascii_lowercase.upper()) for _ in range(6))
        self.mecid = f'Z4FI1wABAAET6tZpG_yS09{self.acak}'
        self.igdid = str(uuid.uuid4())
        self.cokie = f'mid={self.mecid}; ig_did={self.igdid}; datr=lTaDZ1Om4hkRE4wiVFZ7TkPz; ps_l=1; ps_n=1; ig_nrcb=1; wd=1358x688; ' + coks
        return(self.cokie.replace(' ',''))

    def password(self) -> None:
        try:
            self.token = re.findall('csrftoken=(.*?);',self.cookie)
            if len(self.token) == 0:
                self.token = ['NPWtMg1bzwTyBCPicx4x1BnMjt77sLTk']
            self.headers = {
                'accept': '*/*',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': self.cookie,
                'origin': 'https://www.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://www.instagram.com/accounts/password/change/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
                'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6834.84", "Microsoft Edge";v="132.0.2957.115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
                'x-asbd-id': '129477',
                'x-csrftoken': self.token[0],
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR1ILcOg1xJ5oN35n4mr2GUs3xvqz00UCJNIwOEwKMiKAp-0',
                'x-instagram-ajax': '1019587826',
                'x-requested-with': 'XMLHttpRequest',
                'x-web-session-id': self.WebSession()
            }
            self.Password_Data = {'enc_old_password': self.OldPas,'enc_new_password1': self.NewPas,'enc_new_password2': self.NewPas}
            self.ChangeRespon = requests.post('https://www.instagram.com/api/v1/web/accounts/password/change/',data=self.Password_Data,headers=self.headers).text
            if 'Kata sandi Anda salah dimasukkan. Harap masukkan kembali.' in self.ChangeRespon or '"status":"fail"' in self.ChangeRespon:
                return False
            elif '"status":"ok"' in self.ChangeRespon:
                return True                
            return False
        except Exception as e:
            return False
            
