import random, platform, base64, re, requests, os, urllib, sys, time
from datetime import date, datetime
P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K = H
M = "\x1b[1;91m"
J = "\033[33m"

class UserKey:

   def __init__(self) -> None:
       pass

   def konfirkeys(self):
       if os.path.isfile('data/.keys.txt') is True:
          try:
              self.mmk  = open('data/.keys.txt','r').read()
              self.cari = requests.get('https://pastebin.com/raw/N3uvQ7FV').text
              self.kunci = re.findall(self.mmk+'.*', self.cari)[0]
              self.data_exp = self.kunci.split('|')[2]
              hari,bulan,tahun = self.data_exp.split('-')
              self.sisa = date(int(tahun),int(bulan),int(hari))
              self.ptim = datetime.strptime(str(self.sisa),"%Y-%m-%d")
              self.xtim = self.ptim.date() - date.today()
              if self.xtim.days <1:
                 os.system('rm -rf data/.keys.txt')
                 print(f'{P}{J}!{P}] Licensi Anda Sudah Kadarluarsa');time.sleep(3)
                 self.BuyLicen()
              else:
                 if os.path.isfile('data/.join.txt') is True:
                    self.Joined = open('data/.join.txt','r').read()
                 else:self.Joined = None
                 self.dev = base64.b16encode(platform.platform().encode('utf-8')).decode()
                 open('data/.keys.txt','w').write(f'{self.mmk}')
                 open('data/.info.txt','w').write(f'{self.mmk}|{self.kunci.split("|")[1]}|{self.xtim.days}')
          except IndexError:
              self.BuyLicen()
              
       else:
           self.BuyLicen()

   def BuyLicen(self):
       from datetime import datetime as Date
       os.system('clear' if 'linux' in platform.system().lower() else 'cls')
       self.new = base64.b16encode(platform.platform().encode('utf-8')).decode()
       try:
            self.req = requests.get('https://pastebin.com/raw/N3uvQ7FV').text
            self.key = re.findall(self.new+'.*', str(self.req))
            if len(self.key) > 0:
               self.abc = 'abcdefghijklmnopwrstuvwxyz'
               self.asc = ''.join(random.choice(self.abc) for i in range(10))
               self.des = '%s%s'%(platform.platform(), self.asc)
               self.dev = base64.b16encode(self.des.encode('utf-8')).decode('utf-8')
            else:
               self.dev = self.new
       except Exception as e:
            exit(f'\n{P}[{J}!{P}] Kesalahan {e}')
       self.new = Date.now()
       self.mon = 'Januari, Februari, Maret, April, Mei, Juni, Juli, Agustus, September, Oktober, November, Desember'.split(',')
       self.hari, self.bulan, self.tahun = self.new.day, self.mon[self.new.month -1], self.new.year
       self.join = '%s/%s/%s'%(self.hari, self.bulan.replace(' ',''), self.tahun)
       self.un = input(f'{P}[{J}?{P}] Enter your name : ')
       self.xx = urllib.parse.quote(f'{self.dev}|{self.un}|')
       os.system(f'xdg-open https://wa.me/+6283853140469?text={self.xx}')
       open('data/.keys.txt','w').write(f'{self.dev}')
       open('data/.join.txt','w').write(f'{self.join}')
       sys.exit()

#-> Simpel Code By Khamdihi Dev