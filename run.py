#!/usr/bin/env python

import os
import sys
import menu
from rich.panel import Panel
from rich.console import Console
from rich.box import ROUNDED

console = Console()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
if not os.path.isfile('.alert'):
    clear()
    text = """[bold white]
Elite3 adalah tools multifungsi yang dirancang untuk 
membantu dalam proses cracking dan pengamanan akun.

🚀 [bold white]Fitur Utama:[/bold white]
- Membantu mengamankan akun tanpa nunggu device lengket.
- Menyediakan metode cracking yang lebih efisien.
- Dilengkapi sistem manajemen lisensi berbasis poin.
- Api selalu terupdate mengikuti perkembangan instagram.

⭐ [bold white]Sistem Poin & Lisensi:[/bold white]
- User membeli licensi 1 minggu bonus 1 point.
- Setiap user yang mengumpulkan 5 poin dapat menukar lisensi 1 minggu.

🔒 [bold white]Keamanan & Kepercayaan:[/bold white]
- Admin amanah dan terpercaya.
- Elite3 dibangun dengan standar keamanan tinggi, memastikan 
  setiap proses berjalan dengan aman dan optimal.
"""

    panel = Panel(
        text, 
        title="[bold white]ELITE3 TOOLS[/bold white]", 
        subtitle="[green]Dikembangkan oleh Khamdihi Dev[/green]",
        title_align="center",
        subtitle_align="center",
        box=ROUNDED,
        expand=True,
        border_style="white"
    )

    console.print(panel)
    input('[Press enter to continue]')

class Main:
    def __init__(self):
        pass

    def run(self):
        menu.languages_set()

if __name__ == '__main__':
    os.system('git pull')
    Main().run()

    # cmt 971dfd32a0e3cc9947665128af2fc6a75c030f1b
