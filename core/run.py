import os
import json
import requests
import hashlib

from core import utils

class Memec:
    def __init__(self):
        pass

    def EliteHashChek(self, jalur):
        hasher = hashlib.sha256()
        try:
            with open(jalur, 'rb') as f:
                while chunk := f.read(8192):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except FileNotFoundError:
            exit(f"[ERROR] File {jalur} tidak ditemukan.")
    
    def Logger(self):
        utils.clear()
        print('Wah, keliatan ada yang suka oprek nih! Tapi sayangnya, file ini gak boleh diubah. Silakan buat versi sendiri ya!')
        exit()

    def EliteHashVerifier(self):pass
