#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
- META 2024 -

Menu Premium.
Code By Khamdihi Dev - Purbalingga
"""
xx, un = 0, []
import urllib.parse

try:
    import os, re, time, sys
    import requests, platform
    from bs4 import BeautifulSoup as bsp
except Exception as e:
    print(f'[!] Kesalahan Module : {e}')
    x = urllib.parse.quote_plus(f'Error type : {e}')
    os.system(f'xdg-open https://wa.me/+6285729416714?text={x}')
    exit(1)

try:
    from dump import Group as Grp, Friends as MyFriends
    from method import main as Crm, ibrut as Bdt
except Exception as e:
    print(f'[!] Kesalahan. Files Tidak Ada : {e}')
    x = urllib.parse.quote_plus(f'Error type : {e}')
    os.system(f'xdg-open https://wa.me/+6285729416714?text={x}')
    exit(1)

P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K = "\033[33m"
M, K2 = K, K

class MAIN:

   bersih = lambda xyz, plt: os.system('clear' if plt.lower() == 'linux' else 'cls')
   userid = []
   pk_idg = []
   def __init__(self):
       try:self.bersih(platform.system())
       except:pass
       super(MAIN).__init__()

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
           if os.path.isfile('data/OK-Instagram_dibawah_100.txt') is True:
              for a in open('data/OK-Instagram_dibawah_100.txt','r').read().splitlines():
                  xyz = re.findall('ds_user_id=(.*)',str(a))
                  if len(xyz) == 0:continue
                  else:
                      if xyz not in meki:meki.append('ds_user_id=%s'%(xyz[0]))
           if os.path.isfile('data/OK-Instagram_diatas_100.txt') is True:
              for a in open('data/OK-Instagram_diatas_100.txt','r').read().splitlines():
                  xyz = re.findall('ds_user_id=(.*)',str(a))
                  if len(xyz) == 0:continue
                  else:
                      if xyz not in meki:meki.append('ds_user_id=%s'%(xyz[0]))
       except:pass

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
                  return(memek)
              except Exception as e:
                  print(f'\n{P}[{K}!{P}] Expired: {K}{memek}')

   def aset_ig(self):
       if os.path.isfile('data/IG-login.txt') is True:
           self.coki = {'cookie':open('data/IG-login.txt','r').read()}
       else:
           self.momo = {'cookie':input('[ Login instagram ]\n\n[?] Masukan cookie : ')}
           if self.momo['cookie'] == 'res':
              self.coki = {'cookie':self.find_res()}
           else:self.coki = self.momo
       try:
           xyz = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
           uid = re.search('ds_user_id=(\d+)', str(self.coki['cookie'])).group(1)
           req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies=self.coki).json()['user']['full_name']
           open('data/IG-login.txt','w').write(f'{self.coki["cookie"]}')
       except Exception as e:
           os.system('rm -rf data/IG-login.txt')
           exit(f'\n[!] Invalid cookie : {e}')
       try:self.bersih(platform.system())
       except:pass
       return self.coki

   def insta(self):
       self.aset = self.aset_ig()
       print('\t[ Instagram Main Menu ]\n')
       Bdt.MAIN().konfirkeys()
       print(f'''
{P}[{H}1{P}] Dump Followers  [{H}5{P}] Dump Explore
{P}[{H}2{P}] Dump Following  [{H}6{P}] Dump Komentar
{P}[{H}3{P}] Chek Checkpoin  [{H}7{P}] Dump Unlimited
{P}[{H}4{P}] Chek Results    [{H}0{P}] Log, Out\n''')
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
         elif x in ['00','0']:os.system('rm -rf data/IG-login.txt');exit()
         else: continue

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
       Bdt.MAIN().List(self.pk_idg)

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
       print(f'\n[{H}?{P}] Masukan username, Cukup Ambil 20-50 ID!')
       self.user = input(f'[{H}?{P}] Username : ')
       try:
           req = requests.get(f'https://www.instagram.com/{self.user}/', cookies = cokie).text
           uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
           print(f'\n[{H}!{P}] Mengambil ID klik CTRL + C Untuk Stop')
           self.Exekusi(uid, cokie, '', True,True)
       except:pass
       if len(un) > 0:
          print(f'\n[{H}!{P}] Di sini Matikan Data Untuk Stop!')
          for self.momok in un:
              self.Graphql(True, self.momok, cokie['cookie'], '')
       else:exit('\n[!] Ganti Username/Tumbal!')
       Bdt.MAIN().List(self.pk_idg)

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
            print(f'[{H}3{P}] Tampilkan Semua Tanpa Kecuali\n')
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
                 if os.path.isfile('data/OK-Instagram_dibawah_100.txt') is True:
                    for a in open('data/OK-Instagram_dibawah_100.txt','r').read().splitlines():
                        print(f'\r {P}{a}')
                 if os.path.isfile('data/OK-Instagram_diatas_100.txt') is True:
                    for a in open('data/OK-Instagram_diatas_100.txt','r').read().splitlines():
                        print(f'\r {P}{a}')
                 exit()
         elif x in ['02','2']:
            print(f'\n[{H}1{P}] Cek Akun Followers Di Bawah 100')
            print(f'[{H}2{P}] Cek Akun Followers DI Atas 100')
            print(f'[{H}3{P}] Tampilkan Semua Tanpa Kecuali\n')
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
                 if os.path.isfile('data/CP-Instagram_dibawah_100.txt') is True:
                    for a in open('data/CP-Instagram_dibawah_100.txt','r').read().splitlines():
                        print(f'\r {P}{a}')
                 if os.path.isfile('data/CP-Instagram_diatas_100.txt') is True:
                    for a in open('data/CP-Instagram_diatas_100.txt','r').read().splitlines():
                        print(f'\r {P}{a}')
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
          for rest in open('data//CP-Instagram.txt','r').read().splitlines():
              uid, pas = rest.split('|')[0], rest.split('|')[1]
              self.pk_idg.append(f'{uid}|{pas}')
              print(f'\r[+] Berhasil dump {len(self.pk_idg)}',end=' ')
       except (FileNotFoundError,ValueError):
          exit('\n[!] File Tidak Ada Atau Pemisahan Salah.')
       Bdt.MAIN().List(self.pk_idg)

   def dumps(self, cintil, typess, xyz = []):
       if 'csrftoken' not in str(cintil):
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
                  self.Exekusi(kintil, cintil, '', 'following')
       except:pass
       Bdt.MAIN().List(self.pk_idg)

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
           for self.xyz in self.req['data']['user']['edge_followed_by']['edges']:
               self.xy = self.xyz['node']['username'] + '|' + self.xyz['node']['full_name']
               if self.xy not in self.pk_idg:
                  xx +=1
                  self.pk_idg.append(self.xy)
                  print(f'\r[+] Berhasil dump {xx} id {userid}',end=' ')
           self.end = self.req['data']['user']['edge_followed_by']['page_info']['has_next_page']
           if self.end is True:
               self.after = self.req['data']['user']['edge_followed_by']['page_info']['end_cursor']
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

def ListTools():
    try:MAIN().bersih(platform.system())
    except:pass
    print('\t[ Tools Brute ]\n')
    print(f'{P}[{H}1{P}] Facebook  : {K2}Free{P}')
    print(f'[{H}2{P}] Instagram : {H}Prem{P}')
    print(f'[{K}0{P}] Exit\n')
    while True:
      x = input(f'[{H}?{P}] Pilih : ')
      if x in   ['01','1']:MAIN().Menu()
      elif x in ['02','2']:MAIN().insta()
      elif x in ['00','0']:exit()

if __name__ == '__main__':
   os.system('git pull')
   ListTools()

