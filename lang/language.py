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

    def get_python_update_instructions(self):
        self.inv = {
            "id": {"header": "\nUpdate python kamu -> pkg install python --upgrade"},
            "en": {"header": "\nUpdate your python -> pkg install python --upgrade"}
        }
        return self.inv[self.lang]
    
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
                    "Informasi pengguna",
                    "Dump list followers",
                    "Dump list following",
                    "Dump list komentar",
                    "Cek hasil crack",
                    "Crack ulang akun checkpoint",
                    "Decode Bearer token",
                    "Beli akun di author",
                    "Cari akun di inboxkitten",
                    "Hapus data akun dan a2f (Gratis beberapa fitur)",
                    "Keluar"
                ]
            },
            "en": {
                "message": "choose menu",
                "header": [
                    "User information",
                    "Dump list of followers",
                    "Dump list of following",
                    "Dump list of comments",
                    "Check crack results",
                    "Re-crack checkpoint accounts",
                    "Decode Bearer token",
                    "Buy an account from the author.",
                    "Find accounts on InboxKitten",
                    "Delete account data and 2FA (Free some features)",
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
            "id": {"message":f"[{H}?{K}] masukan username target, pastikan akun bersifat publik","input":f"[{H}?{K}] masukan username : "},
            "en": {"message":f"[{H}?{K}] Enter the target username, make sure the account is public.","input":f"[{H}?{K}] enter username : "}
        }
        return self.inv[self.lang]
    
    def komentar(self):
        self.inv = {
            "id":{"message": f"[{H}?{K}] masukan tautan link postingan atau reels","input":f"[{H}?{K}] masukan tautan : "},
            "en": {"message": f"[{H}?{K}] Enter the link to the post or reels.","input": f"[{H}?{K}] Enter link : "}
        }
        return self.inv[self.lang]
    
    def pencarian(self):
        self.inv = {
            "id":{"message": f"[{H}?{K}] masukan nama seseorang bebas","input":f"[{H}?{K}] nama orang : "},
            "en": {"message": f"[{H}?{K}] Enter any person's name.","input": f"[{H}?{K}] Person's name : "}
        }
        return self.inv[self.lang]

    def methodlist(self):
        self.inv = {
            "id": {
                "message":"pilih method",
                "method": [
                    "Login api app manual",
                    "Login api app recovery",
                    "Login api app smartlock",
                    "Login api app threads"
                ]
            },
            "en": {
                "message":"choose method",
                "method": [
                    "Login api app manual",
                    "Login api app recovery",
                    "Login api app smartlock",
                    "Login api app threads"
                ]
            }
        }
        return self.inv[self.lang]
    
    def passetlist(self):
        self.inv = {
            "id": {
                "message": "pilih kombinasi sandi",
                "header": [
                    "sandi nama angka 0-5",
                    "sandi nama angka 0-6",
                    "sandi nama dan username 0-5",
                    "sandi nama dan custom angka belakang"
                ]
            },
            "en": {
                "message": "choose password combination",
                "header": [
                    "password name number 0-5",
                    "password name number 0-6",
                    "password name and username 0-5",
                    "password name and custom number behind"
                ]
            }
        }
        return self.inv[self.lang]

    def message_sandi(self):
        self.inv = {
            "id": {"header": f"\n[{H}?{K}] masukan kata sandi, sandi harus lebih dari 6huruf. banyak password pisahkan dengan koma"},
            "en": {"header": f"\n[{H}?{K}] enter the password, the password must be more than 6 characters. separate multiple passwords with a comma"},
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
                'message':f'\n[{H}?{K}] Cari akun yang terkait dengan inboxkitten',
                'message1':f'\n[{H}?{K}] Masukan kata kunci, pisahkan dengan koma : ',
                'message2':f'[{H}?{K}] Filter akun medsos Y/T : '
            },
            'en':{
                'message': f"\n[{H}?{K}] Find accounts associated with InboxKitten",
                'message1': f"\n[{H}?{K}] Enter keywords, separated by commas : ",
                'message2': f'[{H}?{K}] Filter social media accounts Y/N: '
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

    def MenuSecurity(self):
        self.inv = {
            'id': {
                'head': 'Pilih menu keamanan yang mau di ambil',
                'message': [
                    'tambahkan akun yang mau di amanin',
                    'hapus nomor, email dan tambah email',
                    'hapus akun yang sudah di amanin',
                    'ganti kata sandi -> gratis',
                    'Hapus akun yang sudah terhubung',
                    'Log out, Ganti tumbal',
                    'Kembali ke instagram tools'
                ]
            },
            'en': {
                'head': 'Select the security menu you want to use',
                'message': [
                    'add the account you want to secure',
                    'remove phone number, email, and add email',
                    'delete the account that has been secured',
                    'change password -> free',
                    'delete accounts that are already connected',
                    'Log out, Replace dummy',
                    'Back to instagram tools'
                ]
            }
        }
        return self.inv[self.lang]
