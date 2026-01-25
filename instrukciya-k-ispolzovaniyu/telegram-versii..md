---
description: Краткая инструкция к использованию с помощью бота.
---

# Телеграм версии.

## Активация telegram бота.



Применяем такое настройки в files\config\config.json



```json
"bot-telegram": true, 
"app": false,
"console": false,
```

Создаем бота в [BotFather](https://t.me/BotFather)

Далее <mark style="color:blue;">/newbot</mark> -> (Название бота) -> (Юз бота c bot на конце)

<figure><img src="../.gitbook/assets/{355E0A80-E99C-4C76-9E12-6FEB57051D5F}.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/{BF13521D-1A05-4C71-B948-DE868FF2D36B}.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/{B726F862-8D8B-48E4-BFAC-2092631768C2}.png" alt=""><figcaption></figcaption></figure>

После выходит сообщение с токеном и ссылкой на бота.

<figure><img src="../.gitbook/assets/{A801B984-D2C4-4EB6-8EDC-569DD49E01A0}.png" alt=""><figcaption></figcaption></figure>

Токен вставляет в files\config\bot.json

```
{
    "token": "сюда ваш токен",
    "name": "Bot - Switch Site"
}
```

После активируем программу.



Заходим в бота и пишем команду <mark style="color:blue;">/start</mark>

<figure><img src="../.gitbook/assets/{53A03B1F-16CA-4275-9DEE-FD16C17D9375}.png" alt=""><figcaption></figcaption></figure>



Далее кнопка Программа.

<figure><img src="../.gitbook/assets/{CC6192C7-D9B0-4209-B447-B5FF0A19C1E3}.png" alt=""><figcaption></figcaption></figure>



После Добавить сайт и пишем наш сайт.

<figure><img src="../.gitbook/assets/{CB672B88-9A95-4701-A9A8-DC3364065BAC}.png" alt=""><figcaption></figcaption></figure>



Если получилось такое сообщение, то функция добавления работает корректно.



После Удалить сайт и выбираем наш сайт.

<figure><img src="../.gitbook/assets/{0DB2B8CC-872C-450E-8D38-AC216583EB23}.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/{2FA75101-5F2D-4F79-86B3-E479A6592EDE}.png" alt=""><figcaption></figcaption></figure>

Если получено такое сообщение то функция удаления сайта работает корректно.



После добавляем любой сайт и включаем программу.

<figure><img src="../.gitbook/assets/{A946E0EC-3F52-4ACF-AC36-2D6B7BC98765}.png" alt=""><figcaption></figcaption></figure>

Подождав пару минут пробуем зайти на наш сайт.



<figure><img src="../.gitbook/assets/{DF8DDB74-DC0B-42C3-AB82-E5D0AA26AE23}.png" alt=""><figcaption></figcaption></figure>

Если выходит такая ошибка, а после выключения заходит, то наша программа работает корректно.



<figure><img src="../.gitbook/assets/{68960A77-A02E-4B18-8337-B30065EA3DB9}.png" alt=""><figcaption></figcaption></figure>



Для остановки бота достаточно выключить компьютер или закрыть консоль.



<mark style="background-color:$danger;">Прошу заметить, что при включенной программе и закрытии бота, программа не выключится.</mark>
