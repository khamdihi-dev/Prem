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
            "id": {"message":"masukan username target, pastikan akun bersifat publik","input":"masukan username : "},
            "en": {"message":"Enter the target username, make sure the account is public.","input":"enter username : "}
        }
        return self.inv[self.lang]
    
    def komentar(self):
        self.inv = {
            "id":{"message": "masukan tautan link postingan atau reels","input":"masukan tautan : "},
            "en": {"message": "Enter the link to the post or reels.","input": "Enter link : "}
        }
        return self.inv[self.lang]
    
    def pencarian(self):
        self.inv = {
            "id":{"message": "masukan nama seseorang bebas","input":"nama orang : "},
            "en": {"message": "Enter any person's name.","input": "Person's name : "}
        }
        return self.inv[self.lang]

    def methodlist(self):
        self.inv = {
            "id": {
                "message":"pilih method",
                "method": [
                    "Login api app v1",
                    "Login api app manual instagram",
                    "Login api app smartlock instagram"
                ]
            },
            "en": {
                "message":"choose method",
                "method": [
                    "Login api app v1",
                    "Login api app manual instagram",
                    "Login api app smartlock instagram"
                ]
            }
        }
        return self.inv[self.lang]
    
    def passetlist(self):
        self.inv = {
            "id": {
                "message": "pilih kombinasi sandi",
                "header": [
                    "buat sandi otomatis",
                    "buat sandi manual"
                ]
            },
            "en": {
                "message": "choose password combination",
                "header": [
                    "create automatic password",
                    "create manual password"
                ]
            }
        }
        return self.inv[self.lang]

    def message_sandi(self):
        self.inv = {
            "id": {"header": "\nmasukan kata sandi, sandi harus lebih dari 6huruf. banyak password pisahkan dengan koma"},
            "en": {"header": "\nenter the password, the password must be more than 6 characters. separate multiple passwords with a comma"},
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
