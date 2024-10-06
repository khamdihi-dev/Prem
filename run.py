import marshal
import os

def auth(files = None):
    exit('sedang dalam perbaikan..')
    with open(files, 'rb') as file:btcd = file.read()
    code_object = marshal.loads(btcd)
    module = type('module', (), {})()
    exec(code_object, vars(module))
    if hasattr(module, 'KhamdihiDev'):
        call= getattr(module, 'KhamdihiDev')
        call()

auth('code/menu.bin')
