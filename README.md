# Общая информация
Телеграмм бот переводчик на Python. Перевод текста осуществляется с английского на русский язык с использованием библиотеки на python от Deepl

### Как запустить?
1) Клонируем бота к себе на пк
2) Переходим в директорию с проектом
3) Устанавливаем виртуальное окружение `python -m venv venv`
4) Устанавливаем зависимости `pip install requirements.txt`
5) Заполняем создаем `.env` файл и его заполняем по примеру
     ```
     API_TOKEN = токен для перевочика
     BOT_TOKEN = токен бота
     DATABASE_URL = sqlite+aiosqlite:///./bot.db
     ```
6) Проводим миграции `alembic revision --autogenerate -m "First migration" ` `alembic upgrade head`
7) Прописываем `python main.py`
8) Просматриваем файл logger.log, если нет плохих логов, то заходим в телеграм и польтзуемся ботом

### Как получить тоекен бота?
1) Перетйи в BotFather - Бот по созданию ботов в Телеграмме `@BotFather`
2) Все по классике -> `/start` -> new bot -> следуем иструкциям -> получаем ключ в виде `1234123412:AAEXR6AF77cSbjdfyfu46qascSO0BP_9VWcMppM`
3) Подставляем в BOT_TOKEN

![image](https://github.com/iPROJEKT/translator/assets/108357574/83415e76-fe45-443c-8ff0-3a95e76a3e39)

# Пример хорошего лога (нет сбоев в программе)
![image](https://github.com/iPROJEKT/translator/assets/108357574/373a30d2-0da9-4940-a4bb-aa8ca4a96704)

# Пример *плохих* логов
![image](https://github.com/iPROJEKT/translator/assets/108357574/00db03f5-4393-4ba7-bc1d-36497d3e23c7)

### Пути решения
Проблемы вознимкают из-за некоректно заполненого .env файла
Проблему выше можно решить путем перепроверки API_TOKEN
