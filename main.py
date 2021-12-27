import requests
import threading
import random
import os
import time
import datetime
from colorama import Fore, init
from sys import stdout

init(convert=True, autoreset=True)
green, red, white, cyan, yellow, reset = (
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTRED_EX,
    Fore.WHITE,
    Fore.LIGHTCYAN_EX,
    Fore.YELLOW,
    Fore.RESET,
)
pref = f"{white}[{red}>{white}]{reset} "

e = datetime.datetime.now()
current_date = e.strftime("%Y-%m-%d-%H-%M-%S")


def clear():
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")


lock = threading.Lock()


def free_print(arg):
    lock.acquire()
    stdout.flush()
    print(arg)
    lock.release()


if not os.path.exists("Results/"):
    os.makedirs("Results/")


class Main:
    def __init__(self):
        clear()
        try:
            self.main_menu()
        except KeyboardInterrupt:
            Main()

    def logo(self):
        print(
            f"""
        {red} █████╗  ████████╗  ██████╗  ███╗   ███╗ ██╗  ██████╗
        ██╔══██╗ ╚══██╔══╝ ██╔═══██╗ ████╗ ████║ ██║ ██╔════╝{reset}
        {white}███████║    ██║    ██║   ██║ ██╔████╔██║ ██║ ██║     
        ██   ██║    ██║    ██║   ██║ ██║╚██╔╝██║ ██║ ██║     
        ██║  ██║    ██║    ╚██████╔╝ ██║ ╚═╝ ██║ ██║ ╚██████╗
        ╚═╝  ╚═╝    ╚═╝     ╚═════╝  ╚═╝     ╚═╝ ╚═╝  ╚═════╝{reset}
        """
        )

    def main_menu(self):
        clear()
        self.logo()
        os.system("title Main Menu - Atomic Invite Keker")
        print(
            f"""
[{cyan}1{reset}] Discord Invite Keker
[{cyan}2{reset}] Discord Proxy Keker
[{cyan}x{reset}] Exit"""
        )
        while True:
            choice = input(pref)
            if choice.lower() in ("1", "2", "x"):
                break

        if choice == "1":
            InviteChecker()
        elif choice == "2":
            ProxyChecker()
        elif choice.lower() == "x":
            exit()


class ProxyChecker:
    proxylist = []
    socks4_proxy_file = (
        f"Results/Proxy_Checker/Socks4/{current_date}/working-proxies.txt"
    )
    socks5_proxy_file = (
        f"Results/Proxy_Checker/Socks5/{current_date}/working-proxies.txt"
    )
    http_proxy_file = f"Results/Proxy_Checker/Http/{current_date}/working-proxies.txt"
    working = 0
    invalid = 0
    cpm1 = 0
    cpm2 = cpm1

    def __init__(self):
        if not os.path.exists(f"Results/Proxy_Checker/"):
            os.makedirs(f"Results/Proxy_Checker/")
        clear()
        try:
            self.ask_data()
        except KeyboardInterrupt:
            Main()
        clear()
        self.threading_part()

    def logo(self):
        print(
            f"""
        {red} █████╗  ████████╗  ██████╗  ███╗   ███╗ ██╗  ██████╗
        ██╔══██╗ ╚══██╔══╝ ██╔═══██╗ ████╗ ████║ ██║ ██╔════╝{reset}
        {white}███████║    ██║    ██║   ██║ ██╔████╔██║ ██║ ██║     
        ██   ██║    ██║    ██║   ██║ ██║╚██╔╝██║ ██║ ██║     
        ██║  ██║    ██║    ╚██████╔╝ ██║ ╚═╝ ██║ ██║ ╚██████╗
        ╚═╝  ╚═╝    ╚═╝     ╚═════╝  ╚═╝     ╚═╝ ╚═╝  ╚═════╝{reset}
        """
        )

    def title(self):
        with open(self.proxyfile) as f:
            ext = f.readlines()
        os.system(
            f"title Checking Proxies - Checked [{self.working + self.invalid}/{len(ext)}] - Working [{self.working}] - Invalid [{self.invalid}] - CPM [{self.cpm2*60}] - Atomic Invite Keker"
        )
        self.cpm2 = self.cpm1
        self.cpm1 = 0

    def ask_data(self):
        self.logo()
        os.system(f"title Choose - Atomic Invite Keker")
        print(
            f"""Proxy Type
[{cyan}1{reset}] HTTP/s
[{cyan}2{reset}] Socks4
[{cyan}3{reset}] Socks5"""
        )
        self.broxtype = input(f"{pref}")
        while True:
            print("Proxy File Path")
            proxyfile = input(f"{pref}").replace('"', "")
            if proxyfile != None or proxyfile != "" or proxyfile != " ":
                self.proxyfile = proxyfile.strip()
                break
        with open(self.proxyfile, "r+", encoding="utf-8") as f:
            ext = f.readlines()
            self.proxylist.clear()
            for line in ext:
                line = line.replace("\n", "")
                self.proxylist.append(line)
        print("Thread Count")
        self.threads = int(input(f"{pref}"))

    def proxy_keker(self, proxy_to_use):
        if self.broxtype == "1":
            working_file = self.http_proxy_file
            proxydic = {
                "http": f"http://{proxy_to_use}",
                "https": f"http://{proxy_to_use}",
            }
            try:
                if not os.path.exists(f"Results/Proxy_Checker/Http/"):
                    os.makedirs(f"Results/Proxy_Checker/Http/")

                if not os.path.exists(f"Results/Proxy_Checker/Http/{current_date}/"):
                    os.makedirs(f"Results/Proxy_Checker/Http/{current_date}/")
            except:
                pass
        elif self.broxtype == "2":
            working_file = self.socks4_proxy_file
            proxydic = {
                "http": f"socks4://{proxy_to_use}",
                "https": f"socks4://{proxy_to_use}",
            }
            try:
                if not os.path.exists(f"Results/Proxy_Checker/Socks4/"):
                    os.makedirs(f"Results/Proxy_Checker/Socks4/")

                if not os.path.exists(f"Results/Proxy_Checker/Socks4/{current_date}/"):
                    os.makedirs(f"Results/Proxy_Checker/Socks4/{current_date}/")
            except:
                pass

        elif self.broxtype == "3":
            working_file = self.socks5_proxy_file
            proxydic = {
                "http": f"socks5h://{proxy_to_use}",
                "https": f"socks5h://{proxy_to_use}",
            }
            try:
                if not os.path.exists(f"Results/Proxy_Checker/Socks5/"):
                    os.makedirs(f"Results/Proxy_Checker/Socks5/")

                if not os.path.exists(f"Results/Proxy_Checker/Socks5/{current_date}/"):
                    os.makedirs(f"Results/Proxy_Checker/Socks5/{current_date}/")
            except:
                pass
        try:
            r = requests.get(f"https://discord.com/", timeout=3, proxies=proxydic)

            if ">Discord | Your Place to Talk and Hang Out</title>" in r.text:
                with open(working_file, "a", encoding="utf-8") as f:
                    f.write(f"{proxy_to_use}\n")
                free_print(f"[{green}WORKING{reset}] {proxy_to_use}")
                self.cpm1 += 1
                self.working += 1

        except requests.ConnectionError or requests.ConnectTimeout or requests.exceptions.ProxyError or requests.exceptions.HTTPError:
            free_print(f"[{red}INVALID{reset}] {proxy_to_use}")
            self.cpm1 += 1
            self.invalid += 1

        self.title()

    def threading_part(self):
        self.logo()
        self.title()
        for proxy in self.proxylist:
            while True:
                if threading.active_count() < self.threads:
                    threading.Thread(
                        target=self.proxy_keker, args=(proxy.strip(),)
                    ).start()
                    break
        while True:
            with open(self.proxyfile) as f:
                ext = f.readlines()
            if (self.working + self.invalid) == len(ext):
                break
        time.sleep(5)
        clear()
        self.send_final()

    def send_final(self):
        self.title()
        self.logo()

        with open(self.proxyfile) as f:
            total_count = f.readlines()
        print(
            f"""
{pref}[{cyan}DONE{reset}]
{pref}Working Proxies  [{cyan}{self.working}{reset}]
{pref}Invalid Proxies  [{cyan}{self.invalid}{reset}]
{pref}Checked          [{cyan}{self.invalid + self.working}/{len(total_count)}{reset}]"""
        )
        input(f"{pref}Press enter to go back.")
        exit()


class InviteChecker:
    proxylist = []
    working_codes_file = f"Results/Invite_Checker/{current_date}/working-codes.txt"
    custom_codes_file = f"Results/Invite_Checker/{current_date}/custom-codes.txt"
    cpm1 = 0
    cpm2 = cpm1
    working = 0
    custom = 0
    invalid = 0
    retries = 0

    def __init__(self):
        if not os.path.exists(f"Results/Invite_Checker/"):
            os.makedirs(f"Results/Invite_Checker/")

        if not os.path.exists(f"Results/Invite_Checker/{current_date}/"):
            os.makedirs(f"Results/Invite_Checker/{current_date}/")
        clear()
        try:
            self.ask_data()
        except KeyboardInterrupt:
            Main()
        clear()
        self.threading_part()

    def logo(self):
        print(
            f"""
        {red} █████╗  ████████╗  ██████╗  ███╗   ███╗ ██╗  ██████╗
        ██╔══██╗ ╚══██╔══╝ ██╔═══██╗ ████╗ ████║ ██║ ██╔════╝{reset}
        {white}███████║    ██║    ██║   ██║ ██╔████╔██║ ██║ ██║     
        ██   ██║    ██║    ██║   ██║ ██║╚██╔╝██║ ██║ ██║     
        ██║  ██║    ██║    ╚██████╔╝ ██║ ╚═╝ ██║ ██║ ╚██████╗
        ╚═╝  ╚═╝    ╚═╝     ╚═════╝  ╚═╝     ╚═╝ ╚═╝  ╚═════╝{reset}
        """
        )

    def title(self):
        with open(self.codesfile) as f:
            ext = f.readlines()
        os.system(
            f"title Checking Invites - Checked [{self.working + self.custom + self.invalid}/{len(ext)}] - Working [{self.working}] - Custom [{self.custom}] - Invalid [{self.invalid}] - CPM [{self.cpm2*60}] - Retries [{self.retries}] - Atomic Invite Keker"
        )
        self.cpm2 = self.cpm1
        self.cpm1 = 0

    def ask_data(self):
        self.logo()
        os.system("title Choose - Atomic Invite Keker")
        while True:
            print("Codes File Path")
            codesfile = input(f"{pref}").replace('"', "")
            if codesfile != None:
                self.codesfile = codesfile.strip()

                fixed_lines = []
                with open(self.codesfile, "r", errors="ignore") as f:
                    linny: list = [line.strip() for line in f.readlines()]
                    old = len(linny)
                    combo = list(dict.fromkeys(linny))
                    ext = f.readlines()
                    for i in combo:
                        fixed_lines.append(i)

                with open(self.codesfile, "w", errors="ignore") as f:
                    f.write("")
                with open(self.codesfile, "a", errors="ignore") as f:
                    for line in fixed_lines:
                        f.write(line + "\n")
                break
        print(
            f"""Proxy Type
[{cyan}0{reset}] Proxyless
[{cyan}1{reset}] HTTP/s
[{cyan}2{reset}] Socks4
[{cyan}3{reset}] Socks5"""
        )
        self.broxtype = input(f"{pref}")
        if self.broxtype != "0":
            while True:
                print("Proxy File Path")
                proxyfile = input(f"{pref}").replace('"', "")
                if proxyfile != None or proxyfile != "" or proxyfile != " ":
                    self.proxyfile = proxyfile.strip()
                    break
            with open(self.proxyfile, "r+", encoding="utf-8") as f:
                ext = f.readlines()
                self.proxylist.clear()
                for line in ext:
                    line = line.replace("\n", "")
                    self.proxylist.append(line)
        print("Minimum Member Count")
        self.min_members_count = int(input(f"{pref}"))
        print("Thread Count")
        self.threads = int(input(f"{pref}"))

    def invkek(self, code):

        if self.broxtype == "0":
            proxydic = None
        elif self.broxtype == "1":
            proxy_to_use = random.choice(self.proxylist)
            proxydic = {
                "http": f"http://{proxy_to_use}",
                "https": f"http://{proxy_to_use}",
            }

        elif self.broxtype == "2":
            proxy_to_use = random.choice(self.proxylist)
            proxydic = {
                "http": f"socks4://{proxy_to_use}",
                "https": f"socks4://{proxy_to_use}",
            }
        elif self.broxtype == "3":
            proxy_to_use = random.choice(self.proxylist)
            proxydic = {
                "http": f"socks5h://{proxy_to_use}",
                "https": f"socks5h://{proxy_to_use}",
            }
        try:
            r = requests.get(
                f"https://discord.com/api/v6/invites/{code}?with_counts=true",
                proxies=proxydic,
                timeout=3,
            )
            data = r.json()
            try:
                name = data["guild"]["name"]
                total_count = data["approximate_member_count"]
                online_count = data["approximate_presence_count"]
                if online_count <= self.min_members_count:
                    with open(self.custom_codes_file, "a", encoding="utf-8") as f:
                        self.cpm1 += 1
                        self.custom += 1
                        f.write(
                            f"discord.gg/{code} | Name: {name} | Total Count: {total_count} | Online Count: {online_count}\n"
                        )
                        free_print(
                            f"[{yellow}CUSTOM{reset}]  discord.gg/{code} | Name: {name} | Total Count: {total_count} | Online Count: {online_count}"
                        )

                elif online_count >= self.min_members_count:
                    with open(self.working_codes_file, "a", encoding="utf-8") as f:
                        f.write(
                            f"discord.gg/{code} | Name: {name} | Total Count: {total_count} | Online Count: {online_count}\n"
                        )
                    free_print(
                        f"[{green}WORKING{reset}] discord.gg/{code} | Name: {name} | Total Count: {total_count} | Online Count: {online_count}"
                    )
                    self.cpm1 += 1
                    self.working += 1

                else:
                    self.cpm1 += 1
                    self.invalid += 1
            except:
                self.cpm1 += 1
                self.invalid += 1
        except requests.ConnectionError or requests.ConnectTimeout or requests.exceptions.ProxyError or requests.exceptions.HTTPError:
            self.retries += 1
            self.cpm1 += 1
            while True:
                if threading.active_count() < self.threads:
                    threading.Thread(target=self.invkek, args=(code.strip(),)).start()
                    break
        self.title()

    def threading_part(self):
        self.logo()
        self.title()
        with open(self.codesfile, "r+", encoding="utf-8") as f:
            ext = f.readlines()
            for code in ext:
                code = code.replace("\n", "")
                code = code.replace("https://discord.gg/", "")
                code = code.replace("http://discord.gg/", "")
                code = code.replace("discord.gg/", "")
                code = code.replace("https://discord.com/invite/", "")
                code = code.replace("http://discord.com/invite/", "")
                code = code.replace("discord.com/invite/", "")
                code = code.split(" ")
                code = code[0]

                while True:
                    if threading.active_count() < self.threads:
                        threading.Thread(
                            target=self.invkek, args=(code.strip(),)
                        ).start()
                        break
            while True:
                with open(self.codesfile) as f:
                    ext = f.readlines()
                if (self.working + self.custom + self.invalid) == len(ext):
                    break
            time.sleep(5)
            clear()
            self.send_final()

    def send_final(self):
        self.title()
        self.logo()
        try:
            with open(self.working_codes_file, "r", errors="ignore") as f:
                ext = f.readlines()
                working_codes_count = len(ext)
        except FileNotFoundError:
            working_codes_count = 0
        try:
            with open(self.custom_codes_file, "r", errors="ignore") as f:
                ext = f.readlines()
                custom_codes_count = len(ext)
        except FileNotFoundError:
            custom_codes_count = 0
        with open(self.codesfile) as f:
            total_count = f.readlines()
        print(
            f"""
{pref}[{cyan}DONE{reset}]
{pref}Working Codes  [{cyan}{working_codes_count}{reset}]
{pref}Custom Codes   [{cyan}{custom_codes_count}{reset}]
{pref}Invalid Codes  [{cyan}{self.invalid}{reset}]
{pref}Retries        [{cyan}{self.retries}{reset}]
{pref}Checked        [{cyan}{self.invalid + self.working + self.custom}/{len(total_count)}{reset}]"""
        )
        input(f"{pref}Press enter to go back.")
        exit()


Main()
