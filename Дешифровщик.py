enl = 'abcdefghijklmnopqrstuvwxyz'
enu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rul = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ruu = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ntext=''
nap1=1
print('Привет, я помогу тебе расшифровать или зашифровать любое послание шифром Цезаря')
print('Что нужно сделать с текстом? 1 - зашифровка,  2 - расшифровка')
while True:
    nap=input()
    if nap.isdigit() == True and 1<=int(nap)<=2:
        nap = int(nap)
        break
    else:
        print('Не понял вас. 1 - зашифровка,  2 - расшифровка')
if nap==2:
    print('Известен ли вам сдвиг? (да\нет)')
    if input().lower()=='нет':
        nap1=0
        print('На экран будут выведены все возможные расшифровки')
print('Выберите язык (en или ru)')
while True:
    lang=input()
    if lang=='en':
        lang=1
        break
    elif lang=='ru':
        lang=2
        break
    else:
        print('В словаре два языка. en/ru')
if nap1==1:
    print('Выберите сдвиг от 1 до 25')
    while True:
        sd=input()
        if sd.isdigit()==True and 1<=int(sd)<=25:
            sd=int(sd)
            break
        else:
            print('Сдвиг может быть от 1 до 25')
print('Введите текст для преобразования')
text = input()
if nap==1 and nap1==1:
    for i in text:
        if i in enl:
            ind=enl.find(i)
            if ind+sd>25:
                ind-=26
            ntext+=enl[ind+sd]
        elif i in enu:
            ind=enu.find(i)
            if ind+sd>25:
                ind-=26
            ntext+=enu[ind+sd]
        elif i in rul:
            ind=rul.find(i)
            if ind+sd>31:
                ind-=32
            ntext+=rul[ind+sd]
        elif i in ruu:
            ind=ruu.find(i)
            if ind+sd>31:
                ind-=32
            ntext+=ruu[ind+sd]
        else:
            ntext+=i
    print(ntext)
if nap == 2 and nap1==1:
    for i in text:
        if i in enl:
            ind=enl.find(i)          
            ntext+=enl[ind-sd]
        elif i in enu:
            ind=enu.find(i)
            ntext+=enu[ind-sd]
        elif i in rul:
            ind=rul.find(i)
            ntext+=rul[ind-sd]
        elif i in ruu:
            ind=ruu.find(i)
            ntext+=ruu[ind-sd]
        else:
            ntext+=i
    print(ntext)
if nap1==0:
    if lang==1:
        for b in range(1,(len(enu))):
            ntext=''
            for i in text:
                if i in enl:
                    ind=enl.find(i)          
                    ntext+=enl[ind-b]
                elif i in enu:
                    ind=enu.find(i)
                    ntext+=enu[ind-b]
                else:
                    ntext+=i
            print(ntext, b)
    elif lang==2:
        for b in range(1,(len(ruu))):
            ntext=''
            for i in text:
                if i in rul:
                    ind=rul.find(i)          
                    ntext+=rul[ind-b]
                elif i in ruu:
                    ind=ruu.find(i)
                    ntext+=ruu[ind-b]
                else:
                    ntext+=i
            print(ntext, b)