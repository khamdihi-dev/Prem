#!/usr/bin/env python

"""
Copyright (c) 2023-2025 ibrut developers (https://github.com/khamdihi-dev)
Ganti Nama, Jual Enak Banget Lu, Gk Punya Malu??
"""

import random

class ios:
    def __init__(self):
        pass

    def scale(self):
        return random.choice(['2.00', '3.00'])

    def pixel(self):
        return random.choice(['828x1792', '1290x2796', '1242x2688', '1125x2436', '1080x2536'])
    
    def language(self):
        self.lang = random.choice(['en_US', 'id_ID'])
        self.bahs = self.lang.split('_')[0]
        return self.lang, self.bahs
    
    def appVersion(self):
        return f'{random.randint(200,300)}.1.1.{random.randint(20,90)}.{random.randint(80,130)}'
    
    def appInstagram(self):
        self.location = self.language()
        self.appversion = self.appVersion()
        self.pixel = self.pixel()
        self.scale = self.scale()
        ios_versions = [
            ("iPhone11,8", "iOS 14_4_2", "342678912"), ("iPhone11,2", "iOS 14_6", "432898765"), ("iPhone11,6", "iOS 14_7", "542187654"),
            ("iPhone12,1", "iOS 13_3_1", "211471232"), ("iPhone12,3", "iOS 15_2", "412398473"), ("iPhone12,5", "iOS 15_4_1", "238764219"),
            ("iPhone12,8", "iOS 14_8", "785432198"), ("iPhone14,6", "iOS 16_0", "874213659"),
            ("iPhone13,1", "iOS 16_1_2", "632786213"), ("iPhone13,2", "iOS 16_2", "537288535"), ("iPhone13,3", "iOS 16_3", "632789134"), ("iPhone13,4", "iOS 16_4_1", "789432651"),
            ("iPhone14,4", "iOS 17_0", "985432176"), ("iPhone14,5", "iOS 17_0_1", "987321654"), ("iPhone14,2", "iOS 17_1", "764123980"), ("iPhone14,3", "iOS 17_2", "879654321"),
            ("iPhone14,7", "iOS 17_3", "981237564"), ("iPhone14,8", "iOS 17_4", "874321986"), ("iPhone15,2", "iOS 17_5", "658973214"), ("iPhone15,3", "iOS 17_6", "537288535"),
            ("iPhone15,4", "iOS 18_0", "874213659"), ("iPhone15,5", "iOS 18_1", "987456312"), ("iPhone16,1", "iOS 18_2", "654987213"), ("iPhone16,2", "iOS 18_3", "321789654")
        ]
        model, ios_version, build_number = random.choice(ios_versions)
        return f"Instagram {self.appversion} ({model}; {ios_version}; {self.location[0]}; {self.location[1]}; scale={self.scale}; {self.pixel}; {build_number})"
