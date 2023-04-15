import requests

import os

import time

from bs4 import BeautifulSoup as BS


RED, WHITE, CYAN, GREEN, DEFAULT, CYANCLARO, BOLD = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m', '\033[1;36m', '\033[1m'


def get_html(url):

    return requests.get(url).text


def parse_ua(tutilka):

    soup = BS(tutilka, 'html.parser')

    for date in soup.findAll('td'):

        content = date.getText().split('  ')

        for g in content:

            if g == '':

                pass

            elif '\n' in g:

                g = g.replace("\n", "")

            else:

                print(f'{CYAN}[{RED}*{CYAN}] {GREEN}'+g)


print(f'''{BOLD}\033[35m    The first creature that was made by Ray
   ⠀⠠⣤⣀⢀⠀⢀⡀⠀⡀⢠⣆⣶⣶⣰⡄⢀⠀⢀⡀⠀⡀⣀⣤⠄⠀⠀⠀
⠀⠘⣷⣤⣼⣿⣜⣿⣿⠻⣷⣷⣬⣿⣿⣿⣿⣥⣾⣾⠟⣿⣿⣣⣿⣧⣤⣾⠃⠀
⣦⡀⠈⠉⠙⠛⠛⠻⣿⣿⡿⢻⢿⣿⣿⣿⣿⡿⡟⢿⣿⣿⠟⠛⠛⠋⠉⠁⢀⣴
⣿⣿⣦⠄⠀⠀⠀⠳⠿⠿⠁⢀⣸⣿⣿⣿⣿⣇⡀⠈⠿⠿⠞⠀⠀⠀⠠⣴⣿⣿
⢘⣿⣿⠖⠀⢀⡄⠀⠀⠲⠶⢿⠟⠹⣿⣿⠏⠻⡿⠶⠖⠀⠀⢠⡀⠀⠲⣿⣿⡃
⡾⣿⣿⣦⣴⡟⠀⠀⠀⠀⠀⠈⣀⢀⣿⣿⡄⣀⠁⠀⠀⠀⠀⠀⢻⣦⣴⣿⣿⢷
⢠⣿⠛⢻⣏⠀⣄⠀⠀⠀⣀⣼⣿⣿⣿⣿⣿⣿⣧⣄⠀⠀⠀⣠⠀⣹⡟⠛⣿⡆
⢸⡟⠀⠀⠻⣷⣼⣦⣴⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣶⣴⣯⣾⠟⠀⠀⢻⡇
⢸⡇⠀⠀⠀⠙⣿⣿⠁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⣿⣿⠋⠀⠀⠀⢸⡇
⠸⣧⠀⠀⠀⣰⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣆⠀⠀⠀⣼⠇
⠀⢻⣄⣤⣾⣿⣟⠋⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠙⣻⣿⣷⣤⣠⡟⠀
⣴⣿⣿⣿⣿⠟⠁⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠈⠻⣿⣿⣿⣿⣦
⣿⣿⣿⣿⠃⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠘⣿⣿⣿⣿
⣿⣿⣿⣿⡀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⢀⣿⣿⣿⣿
⣿⣿⣿⣿⣇⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⣸⣿⣿⣿⣿

Z - Surfing by number Ukraine (This program has been created by Ray)

X - Surfing by Number

C - Surf info by IP

N - Surf torrents by IP

L - Proxy Parse

P - Surf number by Avito 

Q - BSSID

''')


while True:

    shell = input(f'{WHITE}[{RED}*{CYAN}] Choose number: {CYAN}')

    if shell == 'Z':

        num = input(f'{WHITE}[{WHITE}*{CYAN}] Car-Number: {CYAN}')

        parse_ua(get_html('https://baza-gai.com.ua/nomer/' + num))

    elif shell == 'X':

        phone = input(f'{WHITE}[{RED}*{WHITE}] Номер телефона: {CYAN}')

        try:

            response = requests.get('https://htmlweb.ru/geo/api.php?json&telcod=' + phone)

            data = response.json()

            user_country = data[ 'country' ][ 'english' ]

            user_id = data[ 'country' ][ 'id' ]

            user_location = data[ 'country' ][ 'location' ]

            user_city = data[ 'capital' ][ 'english' ]

            user_lat = data[ 'capital' ][ 'latitude' ]

            user_log = data[ 'capital' ][ 'longitude' ]

            user_post = data[ 'capital' ][ 'post' ]

            user_oper = data[ '0' ][ 'oper' ]

            uty = requests.get("https://api.whatsapp.com/send?phone="+phone)

            if uty.status_code==200:

                utl2 = "https://api.whatsapp.com/send?phone="+phone

            else:

                utl2 = 'Not founded =('

            userr_all_info = f'{CYAN}[{RED}*{CYAN}] Country: {WHITE}{str(user_country)}\n{CYAN}[{RED}*{CYAN}] ID: {WHITE}{str(user_id)}\n{CYAN}[{RED}*{CYAN}] Location: {WHITE}{str(user_location)}\n{CYAN}[{RED}*{CYAN}] City: {WHITE}{str(user_city)}\n{CYAN}[{RED}*{CYAN}] Latitude: {WHITE}{str(user_lat)}\n{CYAN}[{RED}*{CYAN}] Longitude:{WHITE} {str(user_log)}\n{CYAN}[{RED}*{CYAN}] Index post:{WHITE} {str(user_post)}\n{CYAN}[{RED}*{CYAN}] Operator:{WHITE} {str(user_oper)}'

            num_name = []

            phone_ow = requests.get(f'https://phonebook.space/?number=%2B{phone}').text

            content = BS(phone_ow, 'html.parser').find('div', class_='results')

            for i in content.find_all('li'):

                num_name.append(i.text.strip())

            name = ', '.join(num_name)

            user_all_info = f"""

\033[35m-===[Operator Info.1]===-

{userr_all_info}

\033[35m-===[Social Networks.2]===-

{CYAN}[{RED}*{CYAN}] WhatsApp: {WHITE}{utl2}

\033[35m-===[Personal Info]===-

{CYAN}[{RED}*{CYAN}] Possible names: {WHITE}{name}

    """

            print(user_all_info)

        except:

            print(f'{CYAN}[{RED}-{CYAN}] Try again ??')

    elif shell == 'C':

        query = input(f'{CYAN}[{RED}*{CYAN}] Ip For Scan: {WHITE}')

        try:

            r = requests.get(f'http://ip-api.com/json/{query}').json()

            print(f'{CYAN}[{RED}*{CYAN}] Country:{GREEN} {r["country"]}\n{CYAN}[{RED}*{CYAN}] CountryCode:{GREEN} {r["countryCode"]}\n{CYAN}[{RED}*{CYAN}] Region:{GREEN} {r["region"]}\n{CYAN}[{RED}*{CYAN}] Region Name:{GREEN} {r["regionName"]}\n{CYAN}[{RED}*{CYAN}] City: {GREEN}{r["city"]}\n{CYAN}[{RED}*{CYAN}] Zip:{GREEN} {r["zip"]}\n{CYAN}[{RED}*{CYAN}] Latinude: {GREEN}{r["lat"]}\n{CYAN}[{RED}*{CYAN}] Longitude: {GREEN}{r["lon"]}\n{CYAN}[{RED}*{CYAN}] Timezone: {GREEN}{r["timezone"]}\n{CYAN}[{RED}*{CYAN}] ISP:{GREEN} {r["isp"]}\n{CYAN}[{RED}*{CYAN}] Org:{GREEN} {r["org"]}\n{CYAN}[{RED}*{CYAN}] As: {GREEN}{r["as"]} ')

        except:

            print(f'{CYAN}[{RED}-{CYAN}] Nothing..')

    elif shell == 'N':

        query = input(f'{CYAN}[{RED}*{CYAN}] Ip For Scan: {WHITE}')

        target_ip = query

        try:

            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36","Connection": "keep-alive","Host": "iknowwhatyoudownload.com","Referer": "https://iknowwhatyoudownload.com"}

            page = requests.get("https://iknowwhatyoudownload.com/ru/peer/?ip=" + target_ip, headers=headers)

            soup = BS(page.content, "html.parser")

            table = soup.find(class_="table").find("tbody")

            torrents = table.find_all("tr")

            for torrent in torrents:

                first, last = torrent.find_all(class_="date-column")

                first, last = first.text, last.text

                category = torrent.find(class_="category-column").text

                name = torrent.find(class_="name-column").text.replace("\n", '').replace('    ', '')

                size = torrent.find(class_="size-column").text

                print(f'{CYAN}[{RED}*{CYAN}] Использовано первый раз: {WHITE}{first}{CYAN}, использовано последний раз: {WHITE}{last}{CYAN}, тип торента: {GREEN}{category}{CYAN}, название торента: {GREEN}{name}{CYAN}, размер торента: {GREEN}{size}{CYAN}\n')

        except:

            print(f'{CYAN}[{RED}-{CYAN}] Unkown error ??')

    elif shell == 'L':

        res1 = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all&anonymity=elite&ssl=yes')

        print(f'{CYAN}[{RED}*{CYAN}] Your proxy, bro:\n' + '\n'.join(res1.text.split('\r\n')))

    elif shell == 'P':

        phone = input(f'{CYAN}[{RED}*{CYAN}] Phone Number: {WHITE} ')

        try:

            page = requests.get('https://mirror.bullshit.agency/search_by_phone/'+phone)

            soup = BS(page.text, 'html.parser')

            classsell=soup.find(class_='media-heading')

            namesell= soup.find_all('h4')

            for classsell in namesell:

                print(f"{CYAN}[{RED}*{CYAN}] Name: {WHITE}", classsell.text)

            classtext = soup.find(class_='text-muted')

            nametext = soup.find_all('span')

            for classtext in nametext:

                print(f"{CYAN}[{RED}*{CYAN}] Address and data:{WHITE} ", classtext.text)

        except:

            print(f'{CYAN}[{RED}-{CYAN}] Unkown error ??')

    elif shell == 'Q':

        query = input(f'{CYAN}[{RED}*{CYAN}] BSSID: {WHITE} ')

        try:

            response = requests.get("https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=" + query)

            data = response.json()

            status = data["result"]

            if status == 200:

                lat = data["data"]["lat"]

                lon = data["data"]["lon"]

                print(f'{CYAN}[{RED}*{CYAN}] Latinude: {GREEN}{lat}{CYAN}\n{CYAN}[{RED}*{CYAN}] Longitude: {GREEN}{lon}')

            else:

                errorCode = data["message"]

                errorMessage = data["desc"]

                print(f'{CYAN}[{RED}*{CYAN}] Error code: {WHITE}{errorCode}{CYAN}\n{CYAN}[{RED}*{CYAN}] Error message: {WHITE}{errorMessage}{CYAN}')

        except:

            print(f'{CYAN}[{RED}-{CYAN}] Write correctly!')