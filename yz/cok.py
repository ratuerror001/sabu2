#######################################################
# Name           : Brute Facebook (BF)                #
# File           : cok.py                             #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 3.11                               #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import requests, os, sys, json, time, random

from platform import platform
from urllib.error import URLError
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from urllib import request

from data import cokz, dump
from src import chs, asw, ycn
from yxz import loading_rich, login_key, logo

from .cek import Cek_has

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
#---------------------
warna_rich = random.choice(["[bold red]","[deep_pink3]","[blue]","[green]","[cyan]"])
############################ RESPONSE FACEBOOK ######################################
class Cindy_aulia:

    def __init__(self):
        self.ses = requests.Session()
        self.url = "https://ratuerror69.com"
        self.aks = "assets/lisen.txt"

    def hapus_log(self):
        try:os.remove("assets/.token.txt")
        except:pass
        try:os.remove("assets/.cokie.txt")
        except:pass

    def moch_yayan(self):
        logo.Logo()
        wow = []
        try:key = open(self.aks, "r").read()
        except FileNotFoundError:exit(login_key.Log_key(self.url, self.aks))
        loading_rich.Load().cek_lisen()
        try:
            xnxx = request.urlopen(f"{self.url}/api.php?key={key}&dev={platform()}")
            asuu = json.loads(xnxx.read())
            todz = asuu["usage"];tod  = asuu["usage"].replace("premium", "Prem ([bold green]yes premium[/])").replace("trial", "Trial ([bold red]not premium[/])")
            notc = asuu["readtext"];bergabung = asuu["join"];kadaluarsa = asuu["expired"]
            if asuu["status"] == "error":
                print("");prints(Panel(f"😔 [italic bold red]{asuu['msg'].replace('Anda telah menggunakan semua device yang tersisa, chat admin untuk menghapusnya', 'Akses login di tolak! Dikarenakan anda sudah login di device atau perangkat sebelumnya.')}", style="bold white", width=70));exit()
            elif asuu["status"] in ["kadaluarsa", "sudah kadaluarsa"]:
                print("");prints(Panel("😔 [italic bold red] oppsh key anda telah mencapai batas masa aktif nya, silahkan upgrade ke premium.", style="bold white", width=70));time.sleep(5);exit(login_key.Log_key(self.url, self.aks))
        except KeyError:print("");prints(Panel(f"😔 [italic bold red]{asuu['msg'].replace('Anda telah menggunakan semua device yang tersisa, chat admin untuk menghapusnya', 'Akses login di tolak! Dikarenakan anda sudah login di device atau perangkat sebelumnya.')}", style="bold white", width=70));exit()
        except (json.decoder.JSONDecodeError, URLError):
            print("");prints(Panel("😔[bold red] gagal menghubungkan ke server, silahkan cek koneksi anda dan mainkan mode pesawat 5 detik.", style="bold white", width=70));exit()
        wow.append(Panel(f"""[[bold cyan]+[/]] license keys: {tod}
[[bold cyan]+[/]] created keys: {bergabung} ([bold green]{notc}[/])
[[bold cyan]+[/]] expired keys: {kadaluarsa}""", title="[bold red]•[bold yellow]•[bold green]• DATA LISENSI •[bold yellow]•[bold red]•[/]"))
        Console(width=70, style="bold white").print(Columns(wow), justify="center");time.sleep(1)
        try:cookie = {"cookie": open("assets/.cokie.txt", "r").read()}; tokenz = open("assets/.token.txt", "r").read()
        except FileNotFoundError:cokz.Login()
        loading_rich.Load().cek_coki()
        try:
            nama = self.ses.get(f"https://graph.facebook.com/me?fields=name&access_token={tokenz}", cookies=cookie).json()["name"]
            prints(Panel(f"      Selamat datang [italic bold green]{nama}[/] Di Brute Facebook", style="bold white", width=70))
        except requests.exceptions.ConnectionError:
            print("");prints(Panel("😔[bold red] Tidak ada koneksi", style="bold white", width=70));exit()
        except KeyError:
            print("");prints(Panel("😢[bold red] opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.", style="bold white", width=70));time.sleep(5);self.hapus_log();cokz.Login()
        prints(Panel("""    [[bold cyan]01[/]]. Crack anggota grup     [[bold cyan]05[/]]. Crack pencarian nama
    [[bold cyan]02[/]]. Crack teman publik     [[bold cyan]06[/]]. Checkpoint detector
    [[bold cyan]03[/]]. Crack total followers  [[bold cyan]07[/]]. Fitur lainnya
    [[bold cyan]04[/]]. Crack random id massal [[bold cyan]00[/]]. [bold red]Exit program[/]""", title="[bold red]•[bold yellow]•[bold green]• MENU PILIHAN •[bold yellow]•[bold red]•[/]", width=70, style="bold white"))
        pepek = input(f"[{O}?{N}] menu : ")
        if pepek in[""," "]:print("");prints(Panel("                    😡[bold red] jangan kosong kentod", style="bold white", width=70));time.sleep(2);self.moch_yayan()
        elif pepek in["1","01"]:
            if todz == "trial":print("");prints(Panel("😔 anda adalah user [bold red]trial[/] cuma bisa menggunakan menu nomor [bold red]02.[/] upgrade ke premium untuk menikmati semua fiture...", style="bold white", width=70));exit()
            else:dump.Dump(cookie, tokenz).dump_grup()
        elif pepek in["2","02"]:
            if todz == "trial":dump.Dump(cookie, tokenz).dump_free()
            else:dump.Dump(cookie, tokenz).dump_prem()
        elif pepek in["3","03"]:
            if todz == "trial":print("");prints(Panel("😔 anda adalah user [bold red]trial[/] cuma bisa menggunakan menu nomor [bold red]02.[/] upgrade ke premium untuk menikmati semua fiture...", style="bold white", width=70));exit()
            else:dump.Dump(cookie, tokenz).followers()
        elif pepek in["4","04"]:
            if todz == "trial":print("");prints(Panel("😔 anda adalah user [bold red]trial[/] cuma bisa menggunakan menu nomor [bold red]02.[/] upgrade ke premium untuk menikmati semua fiture...", style="bold white", width=70));exit()
            else:dump.Dump(cookie, tokenz).rendem()
        elif pepek in["5","05"]:
            if todz == "trial":print("");prints(Panel("😔 anda adalah user [bold red]trial[/] cuma bisa menggunakan menu nomor [bold red]02.[/] upgrade ke premium untuk menikmati semua fiture...", style="bold white", width=70));exit()
            else:dump.Dump(cookie, tokenz).pencarian()
        elif pepek in["6","06"]:
            if todz == "trial":print("");prints(Panel("😔 anda adalah user [bold red]trial[/] cuma bisa menggunakan menu nomor [bold red]02.[/] upgrade ke premium untuk menikmati semua fiture...", style="bold white", width=70));exit()
            else:Cek_has().gabut()
        elif pepek in["7","07"]:self.kontol(cookie, tokenz)
        elif pepek in["0","00"]:
            titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
            for x in titik:
                sys.stdout.write(f"\r[{M}×{N}] menghapus cookie {N}{x}{N}");sys.stdout.flush()
                time.sleep(1)
            self.hapus_log()
            print("");prints(Panel("[[bold green]✓[/]] berhasil menghapus cookie", padding=(0,5), style="bold white", width=70));exit()
        else:print("");prints(Panel("           😡[bold red] input yang bener, cek menu nya lah asu", style="bold white", width=70));time.sleep(2);self.moch_yayan()

    def kontol(self, cok, tok):
        prints(Panel("""    [[bold cyan]01[/]] check hasil crack       [[bold cyan]03[/]] bot facebook
    [[bold cyan]02[/]] auto pasang a2f         [[bold red]00[/]] kembali""", title="[bold red]•[bold yellow]•[bold green]• FITURE LAINNYA •[bold yellow]•[bold red]•[/]", width=70, style="bold white"))
        pil = input(f"[{M}?{N}] pilih: ")
        if pil in[""," "]:print("");prints(Panel("                    😡[bold red] jangan kosong kentod", style="bold white", width=70));self.kontol(cok, tok)
        elif pil in["1","01"]:chs.Cek_Crack().hasil()
        elif pil in["2", "02"]:ycn.Ngocok().menu()
        elif pil in["3", "03"]:asw.Bot_Facebook(cok, tok).menu()
        elif pil in["0", "00"]:self.moch_yayan()
        else:print("");prints(Panel("           😡[bold red] input yang bener, cek menu nya lah asu", style="bold white", width=70));self.kontol(cok, tok)