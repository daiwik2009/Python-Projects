from youtubesearchpython import VideosSearch as vs
import subprocess as sb



while True:
    l = input("Search...: ")
    if l.strip().lower() == 'exit':
        break
    fo = input("Which Format?:(for audio type 'aud'|for video type 'vid'|for character type type 'inl')")
    if fo.lower() == 'vid':
        v = vs(l, limit=10)
        list = v.result()
        ti = []
        li = []
        for k, video in enumerate(list['result'], start=1):
            title = video['title']
            link = video['link']
            ti.append(title)
            li.append(link)
            print(f'{k}.Title: {title}')
        f = int(input('Which video?(1-5): '))
        sb.run(['mpv', '--ytdl-format=bestvideo[height<=1080][fps<=30]+bestaudio/best', li[f-1]])
    elif fo.lower() == 'aud':
        v = vs(l, limit=5)
        list = v.result()
        ti = []
        li = []
        for k, video in enumerate(list['result'], start=1):
            title = video['title']
            link = video['link']
            ti.append(title)
            li.append(link)
            print(f'{k}.Title: {title}')
        f = int(input('Which audio?(1-5): '))
        sb.run(['mpv','--no-video', li[f-1]])
    elif fo.lower() == 'inl':
        v = vs(l, limit=5)
        list = v.result()
        ti = []
        li = []
        for k, video in enumerate(list['result'], start=1):
            title = video['title']
            link = video['link']
            ti.append(title)
            li.append(link)
            print(f'{k}.Title: {title}')
        f = int(input('Which Video?(1-5): '))
        sb.run(['mpv','--vo=tct', li[f-1]])
    else:
        print('Invalid format')




    