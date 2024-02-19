import os

try:
    import platform, wget
except:
    os.system('pip install wget')

bit = platform.architecture()[0]
if '63' in str(bit):
   os.system('git pull')
   if os.path.isfile('menu.py') is True:
      from menu import ListTools as runing
      exit(runing())
   else:
      exit('\nFile Menu Tidak Tersedia.')
else:
   if os.path.isfile('menu.py') is True:
      from menu import ListTools as runing
      exit(runing())
   else:
      os.system('wget https://raw.githubusercontent.com/khamdihi-dev/Prem/main/data/ibrut.zip')
      if os.path.isfile('ibrut.zip') is True:
         exit(os.system('unzip ibrut.zip'))
      else:
         exit('\nDownload gagal silahkan coba lagi..')
