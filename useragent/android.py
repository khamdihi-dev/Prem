#!/usr/bin/env python

"""
Copyright (c) 2023-2025 ibrut developers (https://github.com/khamdihi-dev)
Ganti Nama, Jual Enak Banget Lu, Gk Punya Malu??
"""

import os
import dotenv
import random

dotenv.load_dotenv()

INSTAGRAM_VERSION = os.getenv('INSTAGRAM_APP_VERSION')
INSTAGRAM_VERSION_CODE = os.getenv('INSTAGRAM_APP_CODE')
BARCELONA_VERSION = os.getenv('BARCELONA_APP_VERSION')
BARCELONA_VERSION_CODE = os.getenv('BARCELONA_APP_CODE')

if None in [INSTAGRAM_VERSION, INSTAGRAM_VERSION_CODE, BARCELONA_VERSION, BARCELONA_VERSION_CODE]:
    raise KeyError("Missing environment variables for app versions")

class UserAgentGenerator:
    def __init__(self, app_event='instagram'):
        self.app_event = app_event
        
        # Android versions (API Level / Release)
        self.android_versions = [
            '28/9', '29/10', '30/11', '31/12', '32/12', '33/13', '34/14'
        ]
        
        # DPI options
        self.dpi_options = [
            '320dpi', '400dpi', '440dpi', '480dpi', '560dpi', '640dpi', '720dpi'
        ]
        
        # Resolutions (width x height)
        self.resolutions = [
            '720x1280', '1080x1920', '1080x2400', '1440x2560', '1440x3088', 
            '1600x3200', '2160x3840', '2400x1080', '2560x1440'
        ]

        self.devices = [
            ('Asus', 'ASUS_Z01QD', 'intel'),
            ('motorola', 'moto e(7) plus', 'qcom'),
            ('TCL', 'T810S', 'qcom'),
            ('Xiaomi/Redmi', '23100RN82L', 'mt6768'),
            ('Amazon', 'KFONWI', 'mt8168'),
            ('realme', 'RMX3491', 'qcom'),
            ('Samsung', 'SM-G991B', 'exynos2100'),
            ('OnePlus', 'ONEPLUS A6013', 'qcom'),
            ('Vivo', 'V2027', 'mt6853'),
            ('Huawei', 'P30 Pro', 'kirin980'),
            ('Sony', 'Xperia 5 II', 'qcom'),
            ('Google', 'Pixel 6', 'google'),
            ('Oppo', 'CPH2219', 'mt6877'),
            ('Nothing', 'A063', 'qcom'),
            ('Lenovo', 'Tab P11 Pro', 'mt6785'),
            ('ZTE', 'Axon 30', 'qcom'),
            ('Poco', 'Poco X3 Pro', 'qcom'),
            ('Infinix', 'X680', 'mt6765'),
            ('Nokia', 'G50', 'qcom'),
            ('Tecno', 'Camon 18P', 'mt6781'),
            ('Meizu', 'M18', 'exynos990'),
            ('iQOO', 'iQOO 7', 'qcom'),
            ('Black Shark', 'BlackShark 4', 'qcom'),
            ('Asus', 'Zenfone 8', 'qcom'),
            ('Xiaomi', 'Redmi 9', 'mt6769'),
            ('Samsung', 'Galaxy A12', 'exynos850'),
            ('Oppo', 'A52', 'qcom'),
            ('Vivo', 'Y20', 'mt6765'),
            ('Realme', 'C3', 'mt6765'),
            ('Nokia', '2.3', 'mt6761'),
            ('Tecno', 'Pova', 'mt6765'),
            ('Infinix', 'Smart 5', 'mt6761'),
            ('Itel', 'A25', 'mt6739'),
            ('Lava', 'Z61', 'mt6739'),
            ('Micromax', 'IN 1', 'mt6765'),
            ('Motorola', 'Moto E', 'qcom'),
            ('OnePlus', 'Nord N10', 'qcom'),
            ('Google', 'Pixel 4a', 'qcom'),
            ('Sony', 'Xperia L4', 'mt6762'),
            ('Huawei', 'P30 Lite', 'kirin710'),
            ('Honor', '9X Pro', 'kirin810'),
            ('Xiaomi', 'Mi 10', 'qcom'),
            ('Oppo', 'Find X2', 'qcom'),
            ('Vivo', 'X50 Pro', 'qcom'),
            ('Realme', 'X50 Pro', 'qcom'),
            ('Samsung', 'Galaxy S20', 'exynos990'),
            ('Apple', 'iPhone 12', 'apple'),
            ('Google', 'Pixel 5', 'qcom'),
            ('OnePlus', '8 Pro', 'qcom'),
            ('Huawei', 'Mate 40 Pro', 'kirin9000'),
            ('Xiaomi', 'Mi 11', 'qcom'),
            ('Oppo', 'Find X3 Pro', 'qcom'),
            ('Vivo', 'X60 Pro', 'qcom'),
            ('Realme', 'GT', 'qcom'),
            ('Samsung', 'Galaxy S21', 'exynos2100'),
            ('Apple', 'iPhone 13', 'apple'),
            ('Google', 'Pixel 6 Pro', 'google'),
            ('OnePlus', '9 Pro', 'qcom'),
            ('Huawei', 'P40 Pro', 'kirin990'),
            ('Xiaomi', 'Mi 11 Ultra', 'qcom'),
            ('Oppo', 'Find X4 Pro', 'qcom'),
            ('Vivo', 'X70 Pro', 'qcom'),
            ('Realme', 'GT 2', 'qcom'),
            ('Samsung', 'Galaxy S22', 'exynos2200'),
            ('Apple', 'iPhone 14', 'apple'),
            ('Google', 'Pixel 7 Pro', 'google'),
            ('OnePlus', '10 Pro', 'qcom'),
            ('Huawei', 'Mate 50 Pro', 'kirin9000s'),
            ('Xiaomi', 'Mi 12', 'qcom'),
            ('Oppo', 'Find X5 Pro', 'qcom'),
            ('Vivo', 'X80 Pro', 'qcom'),
            ('Realme', 'GT 3', 'qcom'),
            ('Samsung', 'Galaxy S23', 'exynos2300'),
            ('Apple', 'iPhone 15', 'apple'),
            ('Google', 'Pixel 8 Pro', 'google'),
            ('OnePlus', '11 Pro', 'qcom'),
            ('Huawei', 'P50 Pro', 'kirin9000s'),
            ('Xiaomi', 'Mi 13', 'qcom'),
            ('Oppo', 'Find X6 Pro', 'qcom'),
            ('Vivo', 'X90 Pro', 'qcom'),
            ('Realme', 'GT 4', 'qcom'),
            ('Samsung', 'Galaxy S24', 'exynos2400'),
            ('Apple', 'iPhone 16', 'apple'),
            ('Google', 'Pixel 9 Pro', 'google'),
            ('OnePlus', '12 Pro', 'qcom'),
            ('Huawei', 'Mate 60 Pro', 'kirin9100'),
            ('Xiaomi', 'Mi 14', 'qcom'),
            ('Oppo', 'Find X7 Pro', 'qcom'),
            ('Vivo', 'X100 Pro', 'qcom'),
            ('Realme', 'GT 5', 'qcom'),
            ('Samsung', 'Galaxy S25', 'exynos2500'),
            ('Apple', 'iPhone 17', 'apple'),
            ('Google', 'Pixel 10 Pro', 'google'),
            ('OnePlus', '13 Pro', 'qcom'),
            ('Huawei', 'P60 Pro', 'kirin9200'),
            ('Xiaomi', 'Mi 15', 'qcom'),
            ('Oppo', 'Find X8 Pro', 'qcom'),
            ('Vivo', 'X110 Pro', 'qcom'),
            ('Realme', 'GT 6', 'qcom'),
            ('Samsung', 'Galaxy S26', 'exynos2600'),
            ('Apple', 'iPhone 18', 'apple'),
            ('Google', 'Pixel 11 Pro', 'google'),
            ('OnePlus', '14 Pro', 'qcom'),
            ('Huawei', 'Mate 70 Pro', 'kirin9300'),
            ('Xiaomi', 'Mi 16', 'qcom'),
            ('Oppo', 'Find X9 Pro', 'qcom'),
            ('Vivo', 'X120 Pro', 'qcom'),
            ('Realme', 'GT 7', 'qcom'),
            ('Samsung', 'Galaxy S27', 'exynos2700'),
            ('Apple', 'iPhone 19', 'apple'),
            ('Google', 'Pixel 12 Pro', 'google'),
            ('OnePlus', '15 Pro', 'qcom'),
            ('Huawei', 'P70 Pro', 'kirin9400'),
            ('Xiaomi', 'Mi 17', 'qcom'),
            ('Oppo', 'Find X10 Pro', 'qcom'),
            ('Vivo', 'X130 Pro', 'qcom'),
            ('Realme', 'GT 8', 'qcom'),
            ('Samsung', 'Galaxy S28', 'exynos2800'),
            ('Apple', 'iPhone 20', 'apple'),
            ('Google', 'Pixel 13 Pro', 'google'),
            ('OnePlus', '16 Pro', 'qcom'),
            ('Huawei', 'Mate 80 Pro', 'kirin9500'),
            ('Xiaomi', 'Mi 18', 'qcom'),
            ('Oppo', 'Find X11 Pro', 'qcom'),
            ('Vivo', 'X140 Pro', 'qcom'),
            ('Realme', 'GT 9', 'qcom'),
            ('Samsung', 'Galaxy S29', 'exynos2900'),
            ('Apple', 'iPhone 21', 'apple'),
            ('Google', 'Pixel 14 Pro', 'google'),
            ('OnePlus', '17 Pro', 'qcom'),
            ('Huawei', 'P80 Pro', 'kirin9600'),
            ('Xiaomi', 'Mi 19', 'qcom'),
            ('Oppo', 'Find X12 Pro', 'qcom'),
            ('Vivo', 'X150 Pro', 'qcom'),
            ('Realme', 'GT 10', 'qcom'),
            ('Samsung', 'Galaxy S30', 'exynos3000'),
            ('Apple', 'iPhone 22', 'apple'),
            ('Google', 'Pixel 15 Pro', 'google'),
            ('OnePlus', '18 Pro', 'qcom'),
            ('Huawei', 'Mate 90 Pro', 'kirin9700'),
            ('Xiaomi', 'Mi 20', 'qcom'),
            ('Oppo', 'Find X13 Pro','qcom')]
    def generate(self):
        brand, model, chipset = random.choice(self.devices)
        android_version = random.choice(self.android_versions)
        dpi = random.choice(self.dpi_options)
        resolution = random.choice(self.resolutions)
        user_agent = "Instagram {0} Android ({1}; {2}; {3}; {4}; {5}; {6}; in_ID; {7})".format(INSTAGRAM_VERSION, android_version, dpi, resolution, brand, model, chipset, INSTAGRAM_VERSION_CODE)
        if self.app_event != 'instagram':
            user_agent = user_agent.replace('Instagram', 'Barcelona') \
                .replace(INSTAGRAM_VERSION, BARCELONA_VERSION) \
                .replace(INSTAGRAM_VERSION_CODE, BARCELONA_VERSION_CODE)

        return user_agent
