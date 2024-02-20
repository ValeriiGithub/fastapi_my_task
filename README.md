# fastapi_my_task

# Проект FastAPI для управления задачами

Этот проект представляет собой простое веб-приложение, разработанное с использованием FastAPI, для управления задачами. Он предоставляет функциональность для создания и удаления задач.

## Основные функции

- **Создание задач**: Пользователи могут создавать новые задачи, указывая детали задачи.
- **Удаление задач**: Пользователи могут удалять существующие задачи по идентификатору задачи.

## Технологии

- **FastAPI**: Современный, быстрый (высокопроизводительный), веб-фреймворк для построения API с Python 3.6+ на основе стандартных Python типовых подсказок.
- **SQLAlchemy**: SQL Toolkit и ORM, который дает разработчикам полную свободу в написании SQL-запросов, а также предоставляет полный набор ORM-функций для обработки баз данных.

## Установка и запуск

Для установки и запуска проекта вам потребуется Python 3.6 или выше. Клонируйте репозиторий, установите зависимости и запустите сервер FastAPI.

```bash
git clone https://github.com/ValeriiGithub/fastapi_my_task.git
cd fastapi_my_task
pip install -r requirements.txt
uvicorn main:app --reload
```

Теперь вы можете перейти по адресу `http://localhost:8000` в вашем браузере, чтобы увидеть ваше приложение в действии.

# Подготовка сервера
git
```bash
sudo apt-get update
sudo apt-get install git
```

docker

# Можно воспользоваться инструкцией: https://docs.docker.com/engine/install/ubuntu/ или скопировать код ниже

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

# Запуск приложения

Создание образа (коробки) с приложением

```bash
docker build . --tag fastapi_app
```
Запуск образа в контейнере с пробросом портов для доступа к контейнеру из интернета

```bash
docker run -p 80:80 fastapi_app
```

# Запуск на локальном сервере

Команда `docker run -p 80:80 fastapi_app` запускает ваш Docker контейнер на локальном хосте. 
Опция `-p 80:80` указывает Docker пробросить порт `80` внутри контейнера на порт `80` вашего локального хоста.

Если вы хотите использовать другой порт на вашем локальном хосте, вы можете изменить первое число в опции `-p`. 
Например, если вы хотите использовать порт `8080` на вашем локальном хосте, вы можете использовать команду `docker run -p 8080:80 fastapi_app`.

После запуска контейнера вы можете получить доступ к вашему приложению, перейдя по адресу `http://localhost:8080` (или используйте номер порта, который вы выбрали) в вашем веб-браузере.

Обратите внимание, что порт `80` обычно требует административных привилегий для привязки, поэтому если вы не запускаете Docker с правами администратора, вам может потребоваться использовать порт выше `1024`.

## Лицензия

Этот проект лицензирован под лицензией MIT. См. файл `LICENSE` для подробностей.
