#!/usr/bin/env python

"""
Copyright (c) 2023-2025 ibrut developers (https://github.com/khamdihi-dev)
Ganti Nama, Jual Enak Banget Lu, Gk Punya Malu??
"""

H = "\033[32m"   # Hijau
K = "\033[37m"   # Putih (White - Alternative)

class languages:
    def __init__(self, lang):
        self.lang = lang
    
    def login_lang(self):
        self.inv = {
            "id": {"header": "Login instagram menggunakan cokie"},
            "en": {"header": "Login to Instagram using a cookie"}
        }
        return self.inv[self.lang]
    
    def login_withs(self):
        self.inv = {
            "id":{"header": ["Login dari cookie","Login dari hasil crack"]},
            "en": {"header": ["Login from cookie", "Login from crack results"]}
        }
        return self.inv[self.lang]
    
    def Error_lang(self):
        self.inv = {
            "id": {"header":"\nterjadi kesalahan saat permintaan, coba lagi"},
            "en": {"header":"\nan error occurred during the request, please try again."}
        }
        return self.inv[self.lang]
    
    def select_file(self):
        self.inv = {
            "id": {"header": "pilih nama file kamu :", "input": "nama file : "},
            "en": {"header": "select your file name :", "input": "file name : "}
        }
        return self.inv[self.lang]
    
    def menu_list(self):
        self.inv = {
            "id": {
                "message": "pilih menu",
                "header": [
                    "Postback telegram api",
                    "Dump list Pencarian",
                    "Dump list followers",
                    "Dump list following",
                    "Dump list komentar",
                    "Chek hasil crack",
                    "Crack ulang result",
                    "Inboxkitten Chatid",
                    "Buat akun instagram",
                    "Email dan kode verifikasi",
                    "Keluar"
                ]
            },
            "en": {
                "message": "choose menu",
                "header": [
                    "Postback Telegram api",
                    "Dump list of search",
                    "Dump list of followers",
                    "Dump list of following",
                    "Dump list of comments",
                    "Check crack results",
                    "Re-crack result",
                    "Inboxkitten Chatid",
                    "Create instagram account",
                    "Email and verification code",
                    "Exit"
                ]
            }
        }
        return self.inv[self.lang]
    
    def userandkeyinfo(self):
        self.inv = {
            "id": {
                "username": "",
                "followers": 0,
                "following": 0,
                "postingan": 0,
                "license": "",
                "bergabung": "",
                "kadarluarsa": ""
            },
            "en": {
                "username": "",
                "followers": 0,
                "following": 0,
                "postingan": 0,
                "license": "",
                "joined": "",
                "expired": "" 
            }
        }
        return self.inv[self.lang]
    
    def dumpflfw(self):
        self.inv = {
            "id": {"message":" masukan username target, pastikan akun bersifat publik","input":f" masukan username : "},
            "en": {"message":" Enter the target username, make sure the account is public.","input":f" enter username : "}
        }
        return self.inv[self.lang]
    
    def komentar(self):
        self.inv = {
            "id":{"message": " masukan tautan link postingan atau reels","input":" masukan tautan : "},
            "en": {"message": " Enter the link to the post or reels.","input": " Enter link : "}
        }
        return self.inv[self.lang]
    
    def pencarian(self):
        self.inv = {
            "id":{"message": " masukan nama seseorang bebas","input":" nama orang : "},
            "en": {"message": " Enter any person's name.","input":" Person's name : "}
        }
        return self.inv[self.lang]

    def app_login(self):
        self.inv = {
            'id': {
                'app':[
                    'Aplikasi thread',
                    'Aplikasi instagram'
                ]
            },
            'en': {
                'app':[
                    'app thread',
                    'app instagram'
                ]
            }
        }
        return self.inv[self.lang]
    
    def methodlist(self):
        self.inv = {
            "id": {
                "message":"Api",
                "method": [
                    "Login api thread",
                    "Login api smartlock new",
                    "Login api basel instagram Edits"
                ]
            },
            "en": {
                "message":"Api",
                "method": [
                    "Login app thread",
                    "Login app smartlock new",
                    "Login api basel instagram Edits"
                ]
            }
        }
        return self.inv[self.lang]

    def userandkeyinfo(self):
        self.inv = {
            "id": {"headers": {"username":"Khamdihi","bergabung":"","kadarluarsa":"","licensi":"","insta_username":"","insta_follower":"","insta_following":"","insta_postingan":"","insta_cookie":""}},
            "en": {"headers": {"username":"Khamdihi","joined":"","expired":"","licensi":"","insta_username":"","insta_follower":"","insta_following":"","insta_post":"","insta_cookie":"",}}
        }
        return {'lang':self.lang, 'name': self.inv[self.lang]}
    
    def chekhasil(self):
        self.inv = {
            "id": {
                "message": "pilih",
                "header":['periksa akun sukses','periksa akun checkpoint'],
                "message1":"pilih nama filenya"

            },
           "en": {
                "message": "choose",
                "message1": "choose the filename",
                "header": ['check successful accounts', 'check checkpoint accounts'],
            }
        }
        return self.inv[self.lang]
    
    def findwithinbox(self):
        self.inv = {
            'id':{
                'message': ' Cari akun yang terkait dengan inboxkitten',
                'message1': ' Masukan kata kunci, pisahkan dengan koma : ',
                'message2': ' Filter akun medsos Y/T : '
            },
            'en':{
                'message': " Find accounts associated with InboxKitten",
                'message1': " Enter keywords, separated by commas : ",
                'message2': ' Filter social media accounts Y/N: '
            }
        }
        return self.inv[self.lang]
    
    def MedsosList(self):
        self.inv = {
            'id': {
                'head':'Pilih medsos yang mau di ambil',
                'message': [
                    'akun tiktok',
                    'akun instagram',
                    'akun facebook',
                    'akun twitter',
                ]
            },
            'en': {
                'head': 'Select the social media platform to retrieve',
                'message': [
                    'TikTok account',
                    'Instagram account',
                    'Facebook account',
                    'Twitter account',
                ]
            }
        }
        return self.inv[self.lang]
