#!/usr/bin/env python

"""
Copyright (c) 2023-2025 ibrut developers (https://github.com/khamdihi-dev)
Ganti Nama, Jual Enak Banget Lu, Gk Punya Malu??
"""

import random

class useragent:
    
    def __init__(self):
        pass

    def instagramAppVersion(self):
        return random.choice([f'{random.randint(150,300)}.1.0.{random.randint(15,50)}.{random.randint(70,150)}',f'{random.randint(150,300)}.0.0.{random.randint(15,50)}.{random.randint(70,150)}'])

    def androidVersion(self):
        return random.choice(['34/12','30/11','29/10','28/9'])
    
    def dpi(self):
        return random.choice(['240dpi', '320dpi', '420dpi', '440dpi', '480dpi', '510dpi', '560dpi', '640dpi'])

    def pxl(self):
        return f'{random.randint(720,1080)}x{random.randint(1344,2291)}'
        
    def techno(self):
        self.tecnoch9 = f'Instagram {self.instagramAppVersion()} Android ({self.androidVersion()}; {self.dpi()}; {self.pxl()}; TECNO MOBILE LIMITED/TECNO; TECNO CH9n; TECNO-CH9n; mt6781; in_ID; 548323755)'
        self.tecnolf7 = f'Instagram {self.instagramAppVersion()} Android ({self.androidVersion()}; {self.dpi()}; {self.pxl()}; TECNO; TECNO LF7; TECNO-LF7; mt6769; in_ID; 517986702)'
        return random.choice([self.tecnolf7,self.tecnoch9])

    def samsung(self):
        self.sam1 = f'Instagram {self.instagramAppVersion()} Android ({self.androidVersion()}; {self.dpi()}; {self.pxl()}; samsung; SM-S916U; dm2q; qcom; in_ID; 536988425)'
        self.sam2 = f'Instagram {self.instagramAppVersion()} Android ({self.androidVersion()}; {self.dpi()}; {self.pxl()}; samsung; SM-A505FN; a50; exynos9610; in_ID; 221134032)'
        return random.choice([self.sam2,self.sam1])

    def xiomai(self):
        self.xio1 = f'Instagram {self.instagramAppVersion()} Android ({self.androidVersion()}; {self.dpi()}; {self.pxl()}; Xiaomi/xiaomi; Redmi Note 8; ginkgo; qcom; in_ID; 548323755)'
        self.xio2 = f'Instagram {self.instagramAppVersion()} Android ({self.androidVersion()}; {self.dpi()}; {self.pxl()}; Xiaomi/xiaomi; Redmi 6A; cactus; mt6762m; in_ID; 298419565)'
        return random.choice([self.xio1,self.xio2])

    def huawai(self):
        self.hua1 = f'Instagram {self.instagramAppVersion()} Android ({self.androidVersion()}; {self.dpi()}; {self.pxl()}; HUAWEI/HONOR; HRY-LX1T; HWHRY-HF; kirin710; in_ID; 300078998)'
        self.hua2 = f'Instagram {self.instagramAppVersion()} Android ({self.androidVersion()}; {self.dpi()}; {self.pxl()}; HUAWEI; DUB-LX1; HWDUB-Q; qcom; in_ID; 225283631)'
        return random.choice([self.hua1,self.hua2])
    
    def randomDevice(self):
        self.dev = random.choice([self.huawai(),self.xiomai(),self.samsung(),self.techno()])
        return self.dev

    