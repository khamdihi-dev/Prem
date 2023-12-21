#!usr/bin/env python
# -*- coding:utf-8

"""
Created on Kamis, 21 Desember 2023

@author: Khamdihi dev
"""

class main:
   def __init__(self):
       self.update()
       self.main_()

   def update(self):
       import os
       os.system('git pull')

   def main_(self):
       import os, urllib.parse as xyz
       try:
           from asset import run
       except Exception as fail:
           text = xyz.quote_plus(f'Failed Run : {fail}')
           exit(os.system(f'xdg-open https://wa.me/+6285729416714?text={text}'))
       return run.CFF()

main()
