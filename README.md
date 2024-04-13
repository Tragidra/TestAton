Тестовое задание на стажировку.
Для правильной работы веб-приложения вам необходимо запустить фронтенд и бэкенд при помощи описанных ниже инструкций.

Руководство по запуску бэкенда:
1. Убедитесь, что на вашем устройстве установлен Python 3.11. Если у вас установлен Python меньшей версии, то можете
попробовать установить библиотеки на свой страх и риск.
2. Перейдите в папку backend через терминал при помощи команды "cd backend".
3. Установите все необходимые библиотеки при помощи команды "pip install -r requirements.txt".
4. Запустите backend при помощи команды "uvicorn main:app --host localhost --port 8000 --reload".

Руководство по запуску фронтенда:
1. Убедитесь, что на вашем устройстве установлен npm.
2. Перейдите в папку frontend через терминал при помощи команды "cd frontend".
3. Установите все необходимые библиотеки при помощи команды "npm i". Если возникнут какие-то ошибки, то выполните 
команду "npm audit fix --force", такие ошибки могут появиться из-за крупных обнолвений технологий и библиотек,
задействованных в приложении.
4. Запустите frontend при помощи команды "npm run dev".

Для входа в заранее подготовленный аккаунт используйте логин "petr" и пароль "petr".

В целях максимального соответствия тексту тестового задания вся работа выполнена согласно строго по техническому заданию.

Так как в тестовом задании не были указаны фреймворки и языки программирования, которых необходимо придерживаться, для
бэкенда был использован язык программирования Python и фреймворк Fast Api в связке с ORM SQLAlchemy, в качестве базы данных SQLite;
для фронтенда были использованы фреймворк Vue 3 (JS/HTML/CSS) в связке с Vite на принципах Composition Api.



