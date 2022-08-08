import time
import requests
from cfonts import render, say
import json
from colorama import Style
from colorama import Fore

_C = 'https://www.tiktok.com/'
_B = 'content-type'
_A = 'cookie'
print(f"{Fore.GREEN}Author: {Fore.WHITE}@{Fore.WHITE}ThieuTrungKien{Fore.WHITE}")
print(f"{Fore.GREEN}Version: {Fore.WHITE}1.0{Fore.RESET}")
print(f"{Fore.GREEN}Github: {Fore.WHITE}https://github.com/TrungKj3n{Fore.WHITE}")
print(f"{Fore.GREEN}Description: {Fore.WHITE}TikTok TraoDoiSub{Fore.RESET}")
cookie = input('Enter your cookie tiktok: ')
headers = {'accept': '*/*', 'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3', 'connection': 'keep-alive', 'content-length': '0', _B: 'application/x-www-form-urlencoded', _A: cookie, 'origin': 'https://www.tiktok.com', 'referer': _C, 'sec-ch-ua': '".Not/A)Brand";v="99","GoogleChrome";v="103","Chromium";v="103"',
           'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/103.0.0.0Safari/537.36', 'x-secsdk-csrf-request': '1', 'x-secsdk-csrf-version': '1.2.7'}
headers.update(
    {'tt-csrf-token': headers[_A].split('tt_csrf_token=')[1].split(';')[0]})
token = input(f"Nhập token TDS : ")
headers.update({'x-secsdk-csrf-token': requests.head('https://www.tiktok.com/api/comment/publish/',
               headers=headers).headers['x-ware-csrf-token'].split(',')[1]})
user = requests.get(_C, headers=headers).text
user = user.split('"uniqueId":"')[1].split('","createTime"')[0]
s = requests.session()
s.headers.update({_B: 'application/x-www-form-urlencoded; charset=UTF-8'})
while True:
    try:
        res = requests.get(
            f"https://traodoisub.com/api/?fields=tiktok_comment&access_token={token}")
        if len(json.loads(res.text)) == 0:
            print(f"{Fore.RED}Đã hết nhiệm vụ ! Vui lòng thay cookie!")
        else:
            data = json.loads(res.text)[0]
            id = data['id']
            link = data['link']
            noidung = data['noidung']
            aweme_id = id.split('_')[0]
            msToken = headers[_A].split('msToken=')[1].split(';')[0]
            getDataID = requests.get(link, headers=headers).text
            device_id = getDataID.split('"userId":"')[1].split('"')[0]
            cmt = requests.post(f"https://www.tiktok.com/api/comment/publish/?aid=1988&app_language=vi-VN&app_name=tiktok_web&aweme_id={aweme_id}&battery_info=1&browser_language=vi&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36&channel=tiktok_web&cookie_enabled=true&device_id={device_id}&device_platform=web_pc&focus_state=true&from_page=video&history_len=3&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=VN&referer=&region=VN&screen_height=768&screen_width=1366&text={noidung}&text_extra=[]&tz_name=Asia/Saigon&webcast_language=vi-VN&msToken={msToken}&X-Bogus=DFSzswjLqzGANtJ/SXzCnTXyYJAR&_signature=_02B4Z6wo00001XvzAAgAAIDAWFIupoxDiMV78wyAADwX07", headers=headers).text
            if'Bình luận được gửi đi thành công' in cmt:
                print(f"{Fore.GREEN}[ TTK ] : {Fore.WHITE}{link}")
                for i in range(30, -1, -1):
                    print(
                        f"{Fore.GREEN}[ TTK ] : {Fore.WHITE}Đang gửi bình luận {Fore.RED}{i}s{Fore.WHITE}", end=' \r')
                    time.sleep(1)
                collect = requests.get(
                    f"https://traodoisub.com/api/coin/?type=TIKTOK_COMMENT&id={id}&access_token={token}")
                print(json.loads(collect.text))
    except:
        continue
