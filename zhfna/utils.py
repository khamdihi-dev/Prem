import os
from prompt_toolkit.styles import Style

A = "\033[90m"   # Abu-abu
B = "\033[94m"   # Biru
C = "\033[96m"   # Cyan
D = "\033[91m"   # Merah Muda (Danger/Red)
E = "\033[95m"   # Ungu
F = "\033[35m"   # Fuchsia (Magenta)
G = "\033[92m"   # Hijau Muda (Green Light)
H = "\033[32m"   # Hijau
I = "\033[30m"   # Hitam
J = "\033[33m"   # Kuning Muda (Yellow)
K = "\033[37m"   # Putih (White - Alternative)
L = "\033[93m"   # Kuning Cerah (Lemon Yellow)
M = "\033[31m"   # Merah
N = "\033[34m"   # Biru Gelap (Navy Blue)
O = "\033[94m"   # Oranye (via Biru karena kode ANSI terbatas)
P = "\033[97m"   # Putih (Bright White)
Q = "\033[41m"   # Latar Merah (Quick Alert)
R = "\033[31m"   # Merah (Red)
S = "\033[36m"   # Cyan Muda (Sky Blue)
T = "\033[96m"   # Teal
U = "\033[35m"   # Ungu (Ungu Magenta)
V = "\033[34m"   # Biru Tua (Violet-ish)
W = "\033[37m"   # Putih
X = "\033[90m"   # Abu-abu Tua
Y = "\033[93m"   # Kuning
Z = "\033[33m"   # Kuning Gelap (Gold)

M3 = '\033[1m\033[38;5;88m'
BJ = '\033[1m\033[38;5;208m'


custom_style = Style.from_dict({
    "qmark": "fg:#fff bold",
    "question": "fg:#fff bold",
    "answer": "fg:#ff0000 underline",
    "pointer": "fg:#ff0000 bold",
    "highlighted": "fg:#ff0000 underline",
    "separator": "fg:#ffffff",
    "instruction": "fg:#ffffff italic",
})
qursor = {'qmark': '','pointer': ' >'}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''{BJ}       _______ __  ____{P}____{BJ}
      / __/ (_) /_/ __/{P}_  /{BJ}
     / _// / / __/ _/{P}_/_ < {BJ}
    /___/_/_/\__/___/{P}____/{P} 
     
  Welcome to {BJ}Elite3 {H}23.0.1{P}
    A based tools for {BJ}hacking {P}
      Random {BJ}Instagram {P}account\n
''')