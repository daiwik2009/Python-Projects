import requests as req
from bs4 import BeautifulSoup
import subprocess as sb
import tempfile
import os
import sys
# 'pimg' = paragraphs + images, 'pl' = paragraphs + links

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = 'https://en.wikipedia.org'

while True:
    inp = input('What do you want to search? (type "ext" to exit): ')
    if inp.strip().lower() == 'ext':
        break
    typ = input('which thing would you like to parse and get? (p = textual/l = links/iml = image links/img = image/pimg = pictures + textual info/pl = links + textual info): ')
    if inp.find(' ') != -1:
        inpm = inp.replace(' ','_')
    else:
        inpm = inp
    kol = f"{url}/wiki/{inpm}"
    finder = req.get(kol, headers=headers)
    htmlbody = finder.text
    soup = BeautifulSoup(htmlbody , 'html.parser')

    if typ.lower() == 'p':
        p_choice = input("How many paragraphs? (Type a number or 'all'): ")
        para = soup.find_all('p')

        if p_choice.lower() == 'all' or p_choice == '':
            for p in para:
                print(p.text)
        else:
    
            try:
                limit = int(p_choice)
                for p in para[:limit]:
                    print(p.text)
            except ValueError:
                print("Invalid input, showing first 5.")
                for p in para[:5]:
                    print(p.text)

    elif typ.lower() == 'l':
        link = soup.find_all('a')
        for kl in link:
            kll = kl.get('href')
            if kll and kll.startswith('/'):
                print(url + kll)
            else:
                print(kll)

    elif typ.lower() == 'iml':
        imgs = soup.find_all('img')
        for img in imgs:
            src = img.get('src')
            if src:
                if src.startswith('//'):
                    src = 'https:' + src
                elif src.startswith('/'):
                    src = url + src
                print(src)

    elif typ.lower() == 'img':
        imgs = soup.find_all('img')
        count = 0
        for img in imgs:
            src = img.get('src')
            if src:
                if src.startswith('//'):
                    src = 'https:' + src
    if typ.lower() == 'p':
        p_choice = input("How many paragraphs? (Type a number or 'all'): ")
        para = soup.find_all('p')

        if p_choice.lower() == 'all' or p_choice == '':
            for p in para:
                print(p.text)
        else:
            try:
                limit = int(p_choice)
                for p in para[:limit]:
                    print(p.text)
            except ValueError:
                print("Invalid input, showing first 5.")
                for p in para[:5]:
                    print(p.text)

    elif typ.lower() == 'l':
        link = soup.find_all('a')
        for kl in link:
            kll = kl.get('href')
            if kll and kll.startswith('/'):
                print(url + kll)
            else:
                print(kll)

    elif typ.lower() == 'iml':
        imgs = soup.find_all('img')
        for img in imgs:
            src = img.get('src')
            if src:
                if src.startswith('//'):
                    src = 'https:' + src
                elif src.startswith('/'):
                    src = url + src
                print(src)

    elif typ.lower() == 'img':
        imgs = soup.find_all('img')
        count = 0
        for img in imgs:
            src = img.get('src')
            if src:
                if src.startswith('//'):
                    src = 'https:' + src
                elif src.startswith('/'):
                    src = url + src

                if src.endswith('.jpg') or src.endswith('.png'):
                    ext = '.jpg' if src.endswith('.jpg') else '.png'
                    response = req.get(src, headers=headers)
                    if response.status_code == 200:
                        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmpfile:
                            tmpfile.write(response.content)
                            tmpfile.flush()

                            if sys.platform.startswith('linux'):
                                sb.run(['xdg-open', tmpfile.name])
                            elif sys.platform == 'darwin':
                                sb.run(['open', tmpfile.name])
                            elif sys.platform == 'win32':
                                os.startfile(tmpfile.name)
                            else:
                                print(f"Image saved at {tmpfile.name}")
                        count += 1
                        if count >= 20:
                            break
        if count == 0:
            print("No jpg/png images found.")

    elif typ.lower() == 'pimg':
        p_choice = input("How many paragraphs? (Type a number or 'all'): ")
        para = soup.find_all('p')

        if p_choice.lower() == 'all' or p_choice == '':
            selected_paras = para
        else:
            try:
                limit = int(p_choice)
                selected_paras = para[:limit]
            except ValueError:
                print("Invalid input, showing first 5.")
                selected_paras = para[:5]

        print("Textual Information:\n")
        for p in selected_paras:
            print(p.text)

        print("\nTop 20 Images:\n")
        imgs = soup.find_all('img')
        count = 0
        for img in imgs:
            src = img.get('src')
            if src:
                if src.startswith('//'):
                    src = 'https:' + src
                elif src.startswith('/'):
                    src = url + src
                if src.endswith('.jpg') or src.endswith('.png'):
                    ext = '.jpg' if src.endswith('.jpg') else '.png'
                    response = req.get(src, headers=headers)
                    if response.status_code == 200:
                        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmpfile:
                            tmpfile.write(response.content)
                            tmpfile.flush()

                            if sys.platform.startswith('linux'):
                                sb.run(['xdg-open', tmpfile.name])
                            elif sys.platform == 'darwin':
                                sb.run(['open', tmpfile.name])
                            elif sys.platform == 'win32':
                                os.startfile(tmpfile.name)
                            else:
                                print(f"Image saved at {tmpfile.name}")
                        count += 1
                        if count >= 20:
                            break
        if count == 0:
            print("No jpg/png images found.")

    elif typ.lower() == 'pl':
        p_choice = input("How many paragraphs? (Type a number or 'all'): ")
        para = soup.find_all('p')

        if p_choice.lower() == 'all' or p_choice == '':
            selected_paras = para
        else:
            try:
                limit = int(p_choice)
                selected_paras = para[:limit]
            except ValueError:
                print("Invalid input, showing first 5.")
                selected_paras = para[:5]

        print("Textual Information:\n")
        for p in selected_paras:
            print(p.text)

        print("\nLinks:\n")
        link = soup.find_all('a')
        for kl in link:
            kll = kl.get('href')
            if kll and kll.startswith('/'):
                print(url + kll)
            else:
                print(kll)
