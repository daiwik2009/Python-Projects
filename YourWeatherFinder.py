import requests as req
k = input("Which place's weather do you wish to see?: ")

r = req.get(f'https://wttr.in/{k.lower()}?format=3')
l = r.text

print(l)

y = input('Do you want to print the weather info in a .txt file?(Y/n)')
inp = y.lower()

if inp == 'y':
    name1 = input('Your name of the file?')
    with open(f'{name1}.txt','w') as kl:
        kl.write(l)
else:
    print('Okay')

