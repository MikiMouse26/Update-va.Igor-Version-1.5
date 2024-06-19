import random
import time
print("Войдите или зарегайте аккаунт")
time.sleep(1)
a = input("(*) Ник - ")
a1 = input("(!) Логин - ")
print("Добро пожаловать! Ваш логин и пароль:", a, a1)
time.sleep(1)
print("✤𝗟𝗢𝗔𝗗𝗜𝗡𝗚...")
time.sleep(5)
print("☰𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙏𝙃𝙀 𝙫𝙖.𝙄𝙂𝙊𝙍 𝙎𝙔𝙎𝙏𝙀𝙈")
time.sleep(1)
print("✤ 𝕊𝕋𝔸ℝ𝕋 𝕊𝕐𝕊𝕋𝔼𝕄")
print("✤ 𝔼𝕏𝕀𝕋 𝕊𝕐𝕊𝕋𝔼𝕄")
system = input("Choise: start , exit - ")
if system == 'exit':
    print("𝙂𝙊𝙊𝘿𝘽𝙔𝙀")
    main()
elif system == 'Upgrade':
    spu = input("Для того чтобы продолжить - confirm")
    if spu == 'confirm':
        time.sleep(5)
        print("☑")
        time.sleep(1)
        print("➳𝙍𝙚𝙖𝙙𝙮!")
        time.sleep(1)
        print("⌘ 𝙍𝙚𝙨𝙩𝙖𝙧𝙩 𝙨𝙮𝙨𝙩𝙚𝙢")
        main()
elif system == 'start':
    print("☑ 𝗦𝗧𝗔𝗥𝗧 𝗦𝗬𝗦𝗧𝗘𝗠...")
time.sleep(5)
print("➳𝗟𝗜𝗦𝗧 𝗢𝗙 𝗧𝗘𝗔𝗠 - ")
print("☸ 𝘽𝙍𝙊𝙒𝙎𝙀𝙍")
print("☸ 𝙊𝙐𝙍 𝘿𝙄𝙎𝘾𝙊𝙍𝘿")
print("☸ 𝙈𝘼𝙄𝙇")
print("☸ 𝙂𝘼𝙈𝙀𝙎")
print("☸ 𝙀𝙓𝙄𝙏")
all_commands = input("Choise - ")
while True:
    if all_commands == 'Browser':
        print("☰ 𝗩𝗘𝗫 ⌘ 𝗕𝗥𝗢𝗪𝗦𝗘𝗥 ☰")
        print("✤ 𝙒𝙀𝘼𝙏𝙃𝙀𝙍")
        print("✤ 𝙂𝙊𝙊𝙂𝙇𝙀")
        print("✤ 𝘿𝙄𝙎𝘾𝙊𝙍𝘿")
        print("✤ 𝙔𝘼 𝙈𝘼𝙍𝙆𝙀𝙏")
        print("✤ 𝙎𝘽𝙀𝙍")
        print("✤ 𝙂𝙄𝙏𝙃𝙐𝘽")
        print("✤ 𝙔𝙊𝙐𝙏𝙐𝘽𝙀")
        print("✤ 𝙎𝙏𝙀𝘼𝙈")
        print("✤ 𝙎𝘽𝙀𝙍 𝙋𝘼𝙔")
        print("✤ 𝙊𝙕𝙊𝙉")
        print("✤ 𝙒𝙄𝙇𝘿𝘽𝙀𝙍𝙍𝙄𝙀𝙎")
        print("✤ 𝙂𝙋𝙏")
        set_commands = input("Сhoise - ")
        if set_commands == 'Weather':
            print("https://www.gismeteo.ru/weather-tyumen-4501/")
        elif set_commands == 'Google':
            print("https://www.google.ru/?hl=ru")
        elif set_commands == 'Discord':
            print("https://discord.com/")
        elif set_commands == 'Ya market':
            print("https://market.yandex.ru/")
        elif set_commands == 'Sber':
            print("http://www.sberbank.ru/ru/person")
        elif set_commands == 'Github':
            print("https://github.com/")
        elif set_commands == 'Youtube':
            print("https://www.youtube.com/")
        elif set_commands == 'Steam':
            print("https://store.steampowered.com/?l=russian")
        elif set_commands == 'Sber pay':
            print("http://www.sberbank.com/promo/sberpay")
        elif set_commands == 'Ozon':
            print("https://www.ozon.ru/")
        elif set_commands == 'Wildberries':
            print("https://www.wildberries.ru/")
        elif set_commands == 'Gpt':
            print("https://chadgpt.ru/")
    elif all_commands == 'Our discord':
        print("https://discord.gg/tNXMsDYs")
    elif all_commands == 'Mail':
        key = input("Создаём ваш MAIL - ")
        time.sleep(1)
        print("Ваш MAIL -", key)
        print("Чтобы окончить, введите в консоль - restart")
        restart = input("Ввод - ")
        if restart == 'restart':
            main()
    elif all_commands == 'Code redactor':
        print("...")
    elif all_commands == 'Games':
        print("❖ Welcome to Game Hub!")
        time.sleep(1)
        a1 = input("Выберите игру - кейсы , камень ножницы бумага (кнб)")
        if a1 == 'кейсы':
            # Кейсы
            time.sleep(1)
            print("❖ Выбери редкость - simple , rare , legend")
            a = input("Редкость - ")
            if a == 'simple':
                time.sleep(1)
                print("Древний кейс открывается...")
                q = random.randint(1, 5)
                if q == 1:
                    q = "Сапфир"
                elif q == 2:
                    q = "Изумруд"
                elif q == 3:
                    q = "Камаз"
                elif q == 4:
                    q = "Айфон"
                elif q == 5:
                    q = "МакБук"
                time.sleep(1)
                print("Вы выбили...", q)
            elif a == 'rare':
                time.sleep(1)
                print("Древний кейс открывается...")
                q1 = random.randint(1, 5)
                if q1 == 1:
                    q1 = "Ларец сапфиров"
                elif q1 == 2:
                    q1 = "Сундук алмазов"
                elif q1 == 3:
                    q1 = "Яхта"
                elif q1 == 4:
                    q1 = "Айфон"
                elif q1 == 5:
                    q1 = "МакБук"
                time.sleep(1)
                print("Вы выбили...", q1)
            elif a == 'legend':
                time.sleep(1)
                print("Древний кейс открывается...")
                q5 = random.randint(1, 5)
                if q5 == 1:
                    q5 = "Город"
                elif q5 == 2:
                    q5 = "Банк"
                elif q5 == 3:
                    q5 = "Небоскрёб"
                elif q5 == 4:
                    q5 = "Сундук с брилиантаим"
                elif q5 == 5:
                    q5 = "Renault Capture"
                time.sleep(1)
                print("Вы выбили...", q5)
        elif a1 == "кнб":
            time.sleep(1)
            print("Начинается игра!")
            player_score = 0
            computer_score = 0
            print("Welcome!")
            while True:

                time.sleep(1)

                player = input("Выбирай - камень , ножницы , бумага -----")

                comp = random.randint(1, 3)
                if comp == 1:
                    comp = "камень"

                elif comp == 2:
                    comp = "ножницы"

                elif comp == 3:
                    comp = "бумага"

                print("Компутери выбрал -", comp)
                time.sleep(1)

                if player == "камень" and comp == "ножницы":
                    print("Победа!")
                    player_score += 1
                    computer_score += 0
                    print("Очки игрока", player_score)
                    print("Очки компа", computer_score)

                elif player == "ножницы" and comp == "бумага":
                    print("Победа!")
                    player_score += 1
                    computer_score += 0
                    print("Очки игрока", player_score)
                    print("Очки компа", computer_score)
                elif player == "бумага" and comp == "камень":
                    print("Победа!")
                    player_score += 1
                    computer_score += 0
                    print("Очки игрока", player_score)
                    print("Очки компа", computer_score)
                elif player == comp:
                    print("Ничья!")
                    player_score += 0
                    computer_score += 0
                    print("Очки игрока - ", player_score)
                    print("Очки компа - ", computer_score)

                else:
                    print("Победил комп!")
                    player_score += 0
                    computer_score += 1
                    print("Очки игрока", player_score)
                    print("Очки компа", computer_score)
                time.sleep(1)
                print("Победил - ")
                print("Вы - ", player_score)
                print("Комп", player_score)
    elif all_commands == 'Заметки':
        print("Введи заметку")
        print("Будет в следующем обновлении...")
    elif all_commands == 'Exit':
        main()

