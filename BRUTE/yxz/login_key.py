#######################################################
# Name           : Brute Facebook (BF)                #
# File           : login_key.py                       #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 3.11                               #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import time, os, json

from urllib.error import URLError
from rich import print as prints
from rich.panel import Panel
from urllib import request

from .logo import Logo
from platform import platform

M = '\x1b[1;91m' # MERAH
N = '\x1b[0m'    # MATI

class Log_key:

    def __init__(self, url, mmk):
        self.url = url; self.aks = mmk
        self.cek_key()

    def login_key(self):
        Logo();print("");prints(Panel("""[italic]               SELAMAT DATANG DI TOOLS BRUTE FB 👋

    Ketik [green]ADMIN[/] untuk mendapatkan lisensi script dari admin
        """,title="[green]PESAN[/]", style="bold white", width=70))
        key = input(f"[{M}*{N}] masukan api key kamu : ")
        if key in[""]:
            print("");prints(Panel("😡[bold red] jangan kosong", style="bold white", width=70));time.sleep(3);Log_key(self.url)
        elif key in ["admin", "ADMIN", "Admin"]:
            print("");prints(Panel("            😋[italic green] anda akan di alihkan ke WhatsApp", style="bold white", width=70));time.sleep(3);os.system("xdg-open https://wa.me/6287799183568?text=RATU+ERROR+BELI+LISENSINYA+DOOONG.......???");exit()
        try:
            reso = request.urlopen(f"{self.url}/api.php?key={key}&dev={platform()}")
            xnxx = json.loads(reso.read())
            if xnxx["status"] == "error":
                print("");prints(Panel(f"😔  [italic bold red]{xnxx['msg'].replace('Anda telah menggunakan semua device yang tersisa, chat admin untuk menghapusnya', 'Akses login di tolak! Dikarenakan anda sudah login di device atau perangkat sebelumnya.')}", style="bold white", width=70));time.sleep(3);Log_key(self.url)
            else:
                kadaluarsa = xnxx["expired"];user = xnxx["nama"]
                open(self.aks, "w").write(key)
                print("");prints(Panel(f"""[italic]Hallo [green]{user}[/] apikey anda masih berlaku sampai tanggal: [bold red]{kadaluarsa}[/]
silahkan gunakan dengan bijak yah tools nya 😊😊😊""", style="bold white", width=70));time.sleep(2)
                exit(f"\n[{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py")
        except URLError:print("");prints(Panel("😭[bold red] gagal menghubungkan ke server, silahkan cek koneksi anda dan mainkan mode pesawat 5 detik.", style="bold white", width=70));exit()

    def cek_key(self):
        try:open(self.aks, "r").read();self.key_cp()
        except FileNotFoundError:self.login_key()

    def key_cp(self):
        Logo();print("");prints(Panel("""😝[bold red] akses login di tolak dikarenakan anda sebelumnya sudah register[/]
🤔 ketik[bold green] Upgrade[/] jika ingin upgrade ke premuim, ketik [bold red]Tidak[/] untuk exit atau keluar program.""", title="[italic bold red]LOGIN DI TOLAK[/]", style="bold white", width=70))
        upd = input(f"  [{M}?{N}] ketik : ")
        if upd in[""]:print("");prints(Panel("                    😡[bold red] jangan kosong kentod", style="bold white", width=70));time.sleep(3);self.key_cp()
        elif upd in["upgrade","Upgrade","UPGRADE"]:
            print("");prints(Panel("     🧐 [italic bold cyan]anda akan di arahkan ke whatsapp untuk chat admin!", style="bold white", width=70));time.sleep(3);os.system("xdg-open https://wa.me/6285603036683?text=Asalamualaikum+bang");exit()
        elif upd in["tidak","Tidak","TIDAK"]:print("");prints(Panel("🤠[bold red] terima kasih telah menggunakan script Brute semoga hari² anda menyenangkan", style="bold white", width=70));exit()
        else:prints(Panel("       😡[bold red] tinggal ketik upgrade atau tidak apasusah nya memek", style="bold white", width=70));time.sleep(3);self.key_cp()