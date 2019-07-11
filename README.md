# urlshorter

Пример urlshorter c использованием Django

## О проекте

urlshorter выполненный на django версии 2.1, python 3.6. С SQLite.
urlshorter имеет такой функционал:
- создает уменьшенную версию ссылки;
- подсчитывает количество переходов

## Установка

В виртуальном окружении (virtualenv) выполнить данную команду:
```
pip install -r requirements.txt
```
Далее сделать миграции и запустить сервер командой:
```
manage.py makemigrations urlshotener
manage.py migrate urlshotener
python manage.py runserver
```
или
```
./manage.py runserver
```


## Автор

* **Kostuk Sergey**
