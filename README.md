# Comic Reader

Веб-приложение для чтения комиксов с настройками внешнего вида (светлая/темная тема). Настройки сохраняются в cookies.

## Установка и запуск

1. Клонируйте репозиторий и перейдите в него:
   ```bash
   git clone <ссылка_на_репозиторий>
   cd comic_reader
   ```
2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```
3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
4. Запустите сервер:
    ```bash
    cd config
    python manage.py runserver
    ```
5. Откройте в браузере: http://127.0.0.1:8000/