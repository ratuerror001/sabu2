#######################################################
# Name           : Brute Facebook (BF)                #
# File           : sett.py                            #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 3.11                               #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import os, re, random, requests, time, sys

#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
#------------------------------->
M = '\x1b[1;91m' # MERAH
N = '\x1b[0m'    # WARNA MATI
O = '\x1b[1;96m' # BIRU MUDA
#------------------------------->

class Setting:

    def __init__(self):
        self.uaa = []
        self.url = "https://user-agents.net"

    def teks_login(self):
        table = Table(title="")
        table.add_column("[bold red]No.")
        table.add_column("[bold cyan]   METHODE LOGIN FOR FACEBOOK", width=35)
        table.add_row("[bold cyan]01", "[italic]Login Api ([bold yellow]mudah spam dan full cp[/])")
        table.add_row("[bold cyan]02", "[italic]Login Validate ([bold green]disarankan[/])")
        table.add_row("[bold cyan]03", "[italic]Login regular ([bold green]disarankan[/])")
        Console().print(table, justify="center", width=70)

    def host(self):
        table = Table(title="")
        table.add_column("[bold red]No.")
        table.add_column("[bold cyan]  HOST METHODE LOGIN FOR FACEBOOK", width=35)
        table.add_row("[bold green]01", "[italic]free.facebook.com ([bold red]fast[/])")
        table.add_row("[bold green]02", "[italic]mbasic.facebook.com ([bold yellow]slow[/])")
        table.add_row("[bold green]03", "[italic]mobile.facebook.com ([bold green]super slow[/])")
        Console().print(table, justify="center", width=70)

    def uass(self):
        table = Table(title="")
        table.add_column("[bold red]No.")
        table.add_column("[bold cyan]   SETTING USER AGENT", width=30)
        table.add_row("[bold blue]01", "[italic white]  User agent single")
        table.add_row("[bold blue]02", "[italic white]  User agent random")
        table.add_row("[bold blue]03", "[italic white]  User agent manual")
        Console().print(table, justify="center", width=70)

    def hapus_ua(self):
        try:os.remove("assets/.xx.txt")
        except:pass
        try:os.remove("assets/.ua.txt")
        except:pass

    def kentod(self, integer):
        lis = list("1234567890")
        gets = [random.choice(lis) for _ in range(integer)]
        return "".join(gets).upper()

    def ngoxok(self, cooz):
        coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
        return(str(coki))

    def ua_mu(self):
        self.hapus_ua();self.uass()
        ua = input(f"[{M}?{N}] pilih: ")
        if ua in [" ", ""]:prints(Panel(f"[[bold red![/]] jangan kosong", style="bold white", width=70));self.ua_mu()
        elif ua in ["1", "01"]:prints(Panel(f"[bold green]{self.single()}", style="bold white", width=70, title="[italic]anda menggunakan user agent"))
        elif ua in ["2", "02"]:self.random();print();prints(Panel(f"            Beehasil mengumpulkan [italic green]{len(self.uaa)}[/] user agent", width=70, style="bold white"))
        elif ua in ["3", "03"]:xx = input(f"[{M}?{N}] masukan user agent: ");open("assets/.xx.txt", "w").write(xx);prints(Panel(f"[bold green]{xx}", style="bold white", width=70, title="[italic]anda menggunakan user agent"))
        else:prints(Panel("[[bold red![/]] pilih yang bener", style="bold white", width=70));self.ua_mu()

    def panas(self):
        rr = random.randint
        user_agent = random.choice([f"Dalvik/2.1.0 (Linux; U; Android {str(rr(6,13))}; CPH1907 Build/RKQ1.200903.002) [FBAN/Orca-Android;FBAV/{str(rr(300,450))}.0.0.{str(rr(10,40))}.{str(rr(10,150))};FBPN/com.facebook.orca;FBLC/in_ID;FBBV/458201858;FBCR/TELKOMSEL;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1907;FBSV/11;FBCA/arm64-v8a:null;FBDM/"+"{density=3.0,width=1080,height=2268};FB_FW/1;]"])
        return user_agent

    def single(self):
        rr = random.randint
        rc = random.choice
        versi = random.choice(["9","11","12","13","14"])
        bb = f"Mozilla/5.0 (Linux; Android {versi}; MAR-LX2 Build/HUAWEIMAR-L22B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,110))}.0.{str(rr(1111,5999))}.{str(rr(45,250))} Mobile Safari/537.36; super/233212657/Android/28 [vmgApp]"
        return rc([bb])

    def random(self):
        try:
            xxxz, xaxz = 0, {}
            link = requests.get(f"{self.url}/browsers", headers={"user-agent": "chrome"}).text
            cari = re.findall("<li><a href\=\'(.*?)\'\>(.*?)\<\/a\>", link)
            prints(Panel("[italic bold green]         SILAHKAN PILIH USER AGENT YANG MENURUT ANDA COCOK", width=70, style="bold white"))
            cokz = Table(title="")
            cokz.add_column("[bold blue]No.")
            cokz.add_column("       [italic bold yellow]USER AGENT")
            for car in cari:
                xxxz+=1
                nomz = ""+str(xxxz)
                xaxz.update({str(xxxz):str(car[0])})
                xaxz.update({nomz+"0":str(xxxz)})
                cokz.add_row(f"[bold red]{nomz}", f"[italic bold green]{car[1]}")
            Console().print(cokz, justify="center", width=70)
        except:pass
        pilih = Console().input("[?] nomor : ")
        try:url = xaxz[pilih]
        except KeyError:
            prints(Panel("          [italic bold red]          pilih yang bener asu", width=70, style="bold white"));time.sleep(3);self.random()
        try:
            linz = requests.get(f"{self.url}{url}", headers={"user-agent": "chrome"}).text
            carz = re.findall("<li><a href\=\'(.*?)\'\>(.*?)\<\/a\>", linz)
            for xxz in carz:
                if "Mozilla/5.0" in xxz[1]:
                    self.uaa.append(xxz[1])
                    open("assets/.ua.txt", "a").write(f"{xxz[1]}\n")
                else:continue
                sys.stdout.write(f"\r[{M}+{N}] sedang mengumpulkan {O}{str(len(self.uaa))}{N} user agent");sys.stdout.flush()
        except:pass