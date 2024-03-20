import os,platform
bit = platform.architecture()[0]
if '64' in str(bit):
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
      exit('\nGk support cuy atau file kepisah.')
