#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
- META 2024 -
Dump List Friends.
Code By Khamdihi Dev - Purbalingga
"""

try:
    import requests
except Exception as e:
    exit(f'\n Error: {e}')

class MAIN:

   id = []
   def __init__(self):
       super(MAIN).__init__()

   def Friends(self, users, cokie, data, head):
       try:
           req = requests.post('https://web.facebook.com/api/graphql/', cookies={'cookie':cokie}, headers=head, data=data).json()['data']['node']['pageItems']
           for rru in req['edges']:
               xyz = rru['node']
               try:
                   uid = xyz['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']['id']
                   nam = xyz['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']['name']
                   xux = f'{uid}|{nam}'
                   if xux not in self.id:
                      self.id.append(xux)
                      print(f'[+] Success Mendapatkan: {len(self.id)} user',end='\r')
               except:pass
           next = req['page_info']['end_cursor']
           data.update({'variables':'{"count":8,"cursor":"'+next+'","scale":2,"search":null,"id":"'+users+'"}'})
           self.Friends(users, cokie, data, head)
       except:pass

       if len(self.id) > 0:
          return self.id
       else:
          return None
