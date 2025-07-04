#!/usr/bin/env python

"""
Software instagram bruteforce
Copyright (c) 2023-2025 ELite3 developers (https://github.com/khamdihi-dev)
"""

import requests, uuid, time, json

class android_startup:
    def __init__(self):
        self.path_config_data = 'data/config.json'
        self.android_id = '{}'.format(uuid.uuid4().hex)
        self.family_device_id = str(uuid.uuid4())
        self.device_id = str(uuid.uuid4())
        self.pigeon_id = 'UFS-{}-0'.format(str(uuid.uuid4()))
        self.client_id = str(uuid.uuid4().hex)

    def Android_keyStore(self):
        try:
            headers = {
                'accept-language': 'id-ID, en-US',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'ig-intended-user-id': '0',
                'priority': 'u=3',
                'x-bloks-is-layout-rtl': 'false',
                'x-bloks-prism-button-version': 'CONTROL',
                'x-bloks-prism-colors-enabled': 'false',
                'x-bloks-prism-font-enabled': 'false',
                'x-bloks-prism-indigo-link-version': '0',
                'x-bloks-version-id': '928fc70e922cbb30a0ab7b9a635b66273193d11341a1c833accfe6cbaaa0dae2',
                'x-fb-client-ip': 'True',
                'x-fb-connection-type': 'WIFI',
                'x-fb-friendly-name': 'IgApi: attestation/create_android_keystore/',
                'x-fb-request-analytics-tags': '{"network_tags":{"product":"567067343352427","purpose":"fetch","surface":"undefined","request_category":"api","retry_attempt":"0"}}',
                'x-fb-server-cluster': 'True',
                'x-ig-android-id': 'android-'+self.android_id[:16],
                'x-ig-app-id': '567067343352427',
                'x-ig-app-locale': 'in_ID',
                'x-ig-bandwidth-speed-kbps': '-1.000',
                'x-ig-bandwidth-totalbytes-b': '0',
                'x-ig-bandwidth-totaltime-ms': '0',
                'x-ig-client-endpoint': 'unknown',
                'x-ig-capabilities': '3brTv10=',
                'x-ig-connection-type': 'WIFI',
                'x-ig-device-id': self.device_id,
                'x-ig-device-locale': 'in_ID',
                'x-ig-family-device-id': self.family_device_id,
                'x-ig-mapped-locale': 'id_ID',
                'x-ig-timezone-offset': str(-time.timezone),
                'x-ig-www-claim': '0',
                'x-mid': 'aFWewgABAAEGeEYI35jFmAXWvCkx', 
                'x-pigeon-rawclienttime': str(time.time())[:14],
                'x-pigeon-session-id': self.pigeon_id,
                'x-tigon-is-retry': 'False',
                'x-zero-eh': 'IG0e09d776530888418ab70f3822fbb4e1',
                'user-agent': 'Instagram 378.0.0.52.68 Android (28/9; 255dpi; 768x1366; Asus; ASUS_Z01QD; ASUS_Z01QD; intel; in_ID; 727763717)',
                'x-fb-conn-uuid-client': self.client_id,
                'x-fb-http-engine': 'MNS/TCP'
            }
            data = {
                'app_scoped_device_id': self.device_id,
                'key_hash': '78c66ad2087f6c6be123c9309bfb3acb98e0c8c55bf9dbfcfb36271741f936c8'
            }
            resp = requests.post('https://b.i.instagram.com/api/v1/attestation/create_android_keystore/',data=data,headers=headers)
            if 'challenge_nonce' in str(resp.text):
                nonce_id = resp.json().get('challenge_nonce','okQcrgeJb9DRNZBCv3KM7UzEufXmVIGi')
            else:
                nonce_id = 'okQcrgeJb9DRNZBCv3KM7UzEufXmVIGi'
            mechanize_id = resp.headers.get('ig-set-x-mid','aBWe2QABAAFtY7F2hwtyxbnoG9W2')
            self.data_ku = json.dumps({
                'android_id':'android-'+self.android_id[:16],
                'family_device_id':self.family_device_id,
                'devices_id':self.device_id,
                'pigeon_id':self.pigeon_id,
                'client_id':self.client_id,
                'nonce_id':nonce_id,
                'mechanize':mechanize_id
            })
            open(self.path_config_data,'w').write(self.data_ku)
        except Exception as e:
            print('\n[+] Failed Save device info',e)
            time.sleep(5)

android_startup().Android_keyStore()