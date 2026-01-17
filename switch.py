import platform
import json
import config as cfg


def get_path() -> str: # Функция для определения пути к файлу
    """Узнаем систему и возвращаем путь"""
    if platform.system() == "Windows":
        return r"C:\Windows\System32\drivers\etc\hosts"
    else:
        return None


def filter_site(site: str) -> str: # Фильтр для ссылок. (Для получения из ссылки вида 'https://github.com/Sk1lizz/switch_site' -> 'github.com')
    """Фильтрация текста"""
    first_check = lambda s: s.replace(r"https://", "") # lambda функция для избравления от https://
    second_check = lambda s: s.replace(r"http://", "") # lambda функция для избравления от http://
    
    """Применяем функции"""
    site_checked = first_check(site)
    site_checked = second_check(site_checked) #

    """Избаление от домена www."""
    if str(site_checked) != str(site_checked.replace("www.", "")): # Сравниваем ссылки с доменом и без, для проверки существует ли домен www. в ссылке
        s = site_checked
        if s[0] == "w" and s[1] == "w" and s[2] == "w" and s[3] == ".": # Проверка стоил ли www. в начале текста (От ложных срабатываний)
            site_checked = s.replace("www.", "")
    
    """Разбиваем ссылку по символу '/' для извлечения домена сайта"""
    site_checked = str(site_checked).split(r"/")

    return site_checked[0] # Вовзращаем только домен ссылки


def state_edit(state: bool) -> bool: # Изменение состояний для предовращения повторного включения или выключения функции
    import json
    path_state = r"files\config\current_state.json" # Указываем путь к файлу со значением

    #path_state_bot = r"bot\config\state.json" # Путь к указанию состояния программы для бота telegram

    """Извлекаем состояние функции из json файла"""
    with open(path_state, "r", encoding="utf-8") as file:
        data = json.load(file)
    state_program = bool(data["state"])

    """Сравниванием состояние программы с запросом"""
    if bool(state) != bool(state_program):
        state_program = not bool(state_program) # Изменяем состояние функции
        
        """Записываем состояние функции в файл"""
        with open(path_state, "w+", encoding='utf-8') as file:
            data_new = {"state": state_program} 

            json.dump(data_new, file, indent=4)
        
        """Повторяем запись если бот включен"""
        """ВРЕМЕННО НЕ РАБОТАЕТ"""
        """if cfg.bot_enable:
            try:
                with open(path_state_bot, "w+", encoding='utf-8') as file:
                    json.dump(data_new, file)
            
            except:
                pass"""

        return True # Если необходимо включить/выключить 


    else: return False # Если необходимо включить/выключить 



def switch(
        path_to_temp_text: str, path_to_temp_hosts: str, path_to_hosts:str
) -> bool: # Включение или выключение функции
    try:
        with open(path_to_temp_hosts, "r", encoding='utf-8') as file:
            hosts = file.read() # Забираем дефолт запись из файла

        with open(path_to_temp_text, "r", encoding='utf-8') as file:
            text = file.read() # Забираем запись с изменениями из файла

        result = hosts + text

        with open(path_to_hosts, "w+", encoding='utf-8') as file:
            file.write(result) # Записываем изменения в основной файл
        
        return True

    except:
        return False


def switch_add(site: str) -> bool: # Добавление сайта к списку
    """Путь к json файлу со списком"""
    path_to_jsonfile = r"files\sites\site_list.json"

    """Извлечение списка"""
    try:
        with open(path_to_jsonfile , "r", encoding='utf-8') as file:
            data = json.load(file)
    except:
        data = {}

    count = 0
    for i in data.keys():
        count += 1

    """Добавление нового сайта к списку"""
    data[str(count)] = filter_site(site)

    """Попытка обновление списка в json файле"""
    try:
        with open(path_to_jsonfile, "w+", encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        
        if bool(state_edit(state=False)):

            ip_block = cfg.IP_BLOCK
            path_to_default_hosts = r"files\sites\hosts_default"
            path_to_hostsadd = r"files\sites\hosts_add.txt"
            path_to_hosts_ = get_path()


            try:
                with open(path_to_jsonfile, "r", encoding='utf-8') as file:
                    site_list = json.load(file)
            except Exception as e:
                return True
            
            text = f"\n#Site (<site>) blocked by skilizz.\n{ip_block} <site>\n"
            result = "\n"

            """Запись в временный файл"""
            for i in site_list.keys():
                result += text.replace("<site>", f"{site_list[i]}")

            with open(path_to_hostsadd, "w+", encoding='utf-8') as file:
                file.write(result)

            switch(
                path_to_temp_text=path_to_hostsadd, 
                path_to_temp_hosts=path_to_default_hosts, 
                path_to_hosts=path_to_hosts_
            )

            state_edit(state=True)

        return True
    
    except Exception as e:
        return e


def switch_delete(site: str) -> bool: # Удаление сайта из списка
    """Путь к json файлу со списком"""
    path_to_jsonfile = r"files\sites\site_list.json"

    """Извлечение списка"""
    try:
        with open(path_to_jsonfile , "r", encoding='utf-8') as file:
            data = json.load(file)
    except:
        return False
    
    switch = False
    count = 0
    count_break = 0
    site = filter_site(site)
    """Поиск ключа"""
    for i in data.keys():
        if data[i] == site:
            count = int(i)
            switch = True
        count_break = int(i)

    """Удаление сайта из списка"""
    if switch:
        data.pop(str(count), None)
        
        for i in range(count, count_break):
            data[str(i)] = str(data[str(i+1)])
            data.pop(str(i+1), None)

    """Попытка обновление списка в json файле"""
    try:
        with open(path_to_jsonfile, "w+", encoding='utf-8') as file:
            json.dump(data, file, indent=4)

        return "True"
    
    except Exception as e:
        return False


def site_list() -> str: # Извлечение всех сайтов
    path_to_jsonfile = r"files\sites\site_list.json"

    """Извлечение списка"""
    try:
        with open(path_to_jsonfile , "r", encoding='utf-8') as file:
            data = json.load(file)
    except:
        data = {}

    """Сборка списка"""
    text = "\n" 
    for i in data.keys():
        text += f"{data[i]}\n"

    
    return text


def switch_on() -> bool: # Включение программы
    """Пути к файлам"""
    path_to_default_hosts = r"files\sites\hosts_default"
    path_to_jsonfile = r"files\sites\site_list.json"
    path_to_hostsadd = r"files\sites\hosts_add.txt"
    path_to_hosts_ = get_path()
    ip_block = cfg.IP_BLOCK

    """Открытие и чтение json файла со списком сайтов"""
    try:
        with open(path_to_jsonfile, "r", encoding='utf-8') as file:
            site_list = json.load(file)
    except:
        return True
    
    text = f"\n#Site (<site>) blocked by skilizz.\n{ip_block} <site>\n"
    result = "\n"

    """Запись в временный файл"""
    for i in site_list.keys():
        result += text.replace("<site>", f"{site_list[i]}")

    try:
        if bool(state_edit(state=True)):
            with open(path_to_hostsadd, "w+", encoding='utf-8') as file:
                file.write(result)
            
            switch(
                path_to_temp_text=path_to_hostsadd, 
                path_to_temp_hosts=path_to_default_hosts, 
                path_to_hosts=path_to_hosts_
            )
            return True
        
        else:
            return False
    except:
        return False


def switch_off() -> bool: # Выключение программы
    """Пути к файлам"""
    path_to_default_hosts = r"files\sites\hosts_default"
    path_to_hostsadd = r"files\sites\hosts_add.txt"
    path_to_hosts_ = get_path()
    result = ""

    """Очищение временного файла"""
    try:
        if bool(state_edit(state=False)):
            with open(path_to_hostsadd, "w+", encoding='utf-8') as file:
                file.write(result)
            
            switch(
                path_to_temp_text=path_to_hostsadd,
                path_to_temp_hosts=path_to_default_hosts, 
                path_to_hosts=path_to_hosts_
            )

            return True
        
        else: 
            return False
    except:
        return False
