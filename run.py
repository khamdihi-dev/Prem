#!/usr/bin/env python

"""
Copyright (c) 2023-2025 ibrut developers (https://github.com/khamdihi-dev)
Ganti Nama, Jual Enak Banget Lu, Gk Punya Malu??
"""

import os
import sys
import menu
from twofactor import private_request as factor

class main:
    def __init__(self):
        pass

    def Biji(self):
        if len(sys.argv) == 2:
            if sys.argv[1] == '2fa':
                exit('\nSedang dalam perbaikan..')
                sys.exit()
            else:menu.languages_set()
        else:
            menu.languages_set()

if __name__ == '__main__':
    os.system('git pull')
    main().Biji()
