#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
- META 2024 -

Dump Members Group.
Code By Khamdihi Dev - Purbalingga
"""

try:
    import requests, re
except Exception as e:
    exit(f'\n Error: {e}')

class MAIN:

   payload = {'__a':'1','__req':'12','dpr':'2','__ccg':'GOOD','__s':'','__dyn':'','__csr':'','__comet_req':'15','__aaid':'0','__spin_b':'trunk','qpl_active_flow_ids':'431626709','fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'GroupsCometMembersPageNewMembersSectionRefetchQuery','server_timestamps':'true','doc_id':'6621621524622624'}
   url,ids,headers = 'https://web.facebook.com/groups/%s/members/', [], {}

   def __init__(self):
       pass

   def Dumper(self, uid: str, coki: str, next: str) -> str:
       self.headers.update({'cookie':coki})
       with requests.Session() as r:
         try:
             r.headers.update(self.headers)
             req = r.get(self.url%(uid)).text
             self.payload.update({
                'av':re.search('{"actorID":"(\d+)"',str(req)).group(1),
                '__user':re.search('{"actorID":"(\d+)"',str(req)).group(1),
                '__hs':re.search('"haste_session":"(.*?)"',str(req)).group(1),
                '__rev':re.search('{"rev":(\d+)}',str(req)).group(1),
                'fb_dtsg':re.search('"DTSGInitialData":{"token":"(.*?)"}',str(req)).group(1),
                'jazoest':re.search('jazoest=(\d+)',str(req)).group(1),
                'lsd':re.search('"LSD":{"token":"(.*?)"}',str(req)).group(1),
                '__spin_r':re.search('"__spin_r":(\d+)',str(req)).group(1),
                '__spin_t':re.search('"__spin_t":(\d+)',str(req)).group(1),
                'variables':'{"count":10,"cursor":"'+next+'","groupID":"'+uid+'","recruitingGroupFilterNonCompliant":false,"scale":2,"id":"'+uid+'"}'}
             )
             self.headers.update({'x-fb-lsd':self.payload.get('lsd'),'x-fb-friendly-name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery'})
             self.response = r.post('https://web.facebook.com/api/graphql/', data=self.payload).json()['data']['node']['new_members']['edges']
             for self.xyz in self.response:
                 self.xac = self.xyz['node']['id'] +'|'+ self.xyz['node']['name']
                 print(f'[+] Success Mendapatkan: {len(self.ids)} user',end='\r')
                 if self.xac not in self.ids:self.ids.append(self.xac)
             self.Dumper(uid, coki, self.xyz['cursor'])
         except:pass

       if len(self.ids) > 0:
          return self.ids
       else:
          return None
