---
description: Настройка.
---

# Настройка программы.

Подробная первичная настройка для программы.



## 0. Установка всех необходимых пакетов.

Советую создать виртуальное окружение:

```
python3 -m venv (Название окружения)
```

И включение:

```
(Название окружения)\Scripts\activate
```

Для Windows.





Перечень команд для установки всех пакетов.

#### 1 Вариант:

Установка каждого пакета вручную:

```
pip install pyside6
pip install aiogram
pip install bs4
pip install requests
pip install pyfiglet
```



#### 2 Вариант:

Установки из папки проекта:

```
cd switch_siteV3
pip install -r .\requirements.txt
```



Если не скачен pip может помочь ([ссылка](https://www.reddit.com/r/learnpython/comments/18wvmp6/unable_to_install_pip_for_some_reason/?tl=ru)).





## 1. config.json

```json
files\config\config.json

{
    "name": "Switch Site",
    "version": "v3-codding",
    "creator": "skilizz",
    "ip-block": "0.0.0.0",
    "bot-telegram": false, 
    "app": false,
    "console": true,
    "language": "RU-ru",
    "path": "None"
}
```

name, creator - лучше не изменять.

version - версия программы, лучше не изменять, т.к. при консольном отображении идет проверка версии на актуальность. <mark style="background-color:$danger;">Лучше не трогать.</mark>

ip-block - ip, с помощью которого будет происходить блок. <mark style="background-color:$danger;">Лучше не трогать, если не разбираетесь.</mark>

language - язык программы, можно поставить свой, files\config\language\\{lang}.json вместо {lang} свое название, и в config.json меняем название на свое.

path - позже будет изменение пути до ключевого файла, <mark style="background-color:$warning;">если не разбираетесь, то лучше не трогать.</mark>

#### Версия программы.

```json
"bot-telegram": false, 
"app": false,
"console": true
```

Консоль -> Телеграм Бот -> Приложение

Так идет проверка состояния.

Если console - false, то идет проверка на bot-telegram, после на app, если вдруг все окажется выключенным, то запуститься консольная версия.

{% hint style="info" %}
Если окажется, что 2\3 из 3 включено, то будет включено только первое, что пройдет проверку.

Например:



```json
"bot-telegram": false, 
"app": true,
"console": true
```

тогда будет консольная версия, или



```json
"bot-telegram": true, 
"app": true,
"console": false
```

версия с telegram ботом.
{% endhint %}



## 2. bot.json

<pre class="language-json"><code class="lang-json">files\config\bot.json
<strong>
</strong><strong>{
</strong>    "token": "token",
    "name": "Bot - Switch Site"
}
</code></pre>

token - токен бота из bot-father.

name - используется для начального сообщения.



## 3.  console.json

```json
files\config\console.json

{
    "name": "Switch Site",
    "font": "slant",
    "check_version": true
}
```

name - название.

font - шрифт для pyfiglet.

check\_version - проверка обновления. <mark style="background-color:$danger;">Лучше не изменять.\\</mark>



##
