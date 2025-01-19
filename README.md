**Сайт: http://dlzxndev.ru/**

```markdown
# 🚀 DlzxnDev - Персональный веб-сайт

![Banner](https://via.placeholder.com/1200x400?text=Welcome+to+DlzxnDev)

Добро пожаловать на персональный сайт **DlzxnDev**, где публикуются последние новости, проекты и информация обо мне. Этот сайт создан с использованием **FastAPI**, **SQLite**, и фронтенд-части на **HTML, CSS, JavaScript**.

---

Welcome to **DlzxnDev**, a personal website where the latest news, projects, and information about me are published. This website is built using **FastAPI**, **SQLite**, and frontend with **HTML, CSS, JavaScript**.

## 🛠️ Технологии / Technologies

- **Backend:** FastAPI + SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** systemd service
- **Authentication:** OAuth2 with JWT
- **Hosting:** Self-hosted on Linux (Manjaro KDE)

---

## 📂 Структура проекта / Project Structure

```bash
├── admin/              # Админ-панель
├── models/             # Модели базы данных
├── static/             # Статические файлы (CSS, JS, Images)
├── templates/          # HTML шаблоны
├── main.py             # Основной серверный файл
├── site2.service       # Файл для systemd
├── README.md           # Документация
└── requirements.txt    # Зависимости проекта
```

---

## 🚀 Установка / Installation

### 1. Клонирование репозитория / Clone the repository

```bash
git clone https://github.com/username/dlzxnDev.git
cd dlzxnDev
```

### 2. Установка зависимостей / Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Запуск сервера / Run the server

```bash
uvicorn main:app --reload
```

Теперь сайт будет доступен по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 🔐 Аутентификация / Authentication

Для входа в панель администратора используйте:

- **Логин:** `admin`
- **Пароль:** `admin`

После авторизации токен будет сохранен в `localStorage` браузера.

---

## ⚙️ Развертывание / Deployment

Сайт настроен для работы через **systemd**, для перезапуска используйте:

```bash
sudo systemctl restart site2.service
```

Для проверки статуса сервиса:

```bash
sudo systemctl status site2.service
```

---

## 📜 API эндпоинты / API Endpoints

### Новости / News

```http
GET /api/news
POST /admin/news
```

### Проекты / Projects

```http
GET /api/projects
POST /admin/projects
```

---

## 🖼️ Галерея / Gallery

![Project Screenshot](https://via.placeholder.com/800x400?text=Project+Screenshot)
![Admin Panel](https://via.placeholder.com/800x400?text=Admin+Panel)

---

## 📧 Контакты / Contact

- **Telegram:** [@illgettomorow](https://t.me/illgettomorow)
- **GitHub:** [Dlzxn](https://github.com/Dlzxn)

---

## 📝 Лицензия / License

Этот проект лицензирован под MIT License. Подробнее см. [LICENSE](LICENSE).

---

_© 2025 DlzxnDev. Все права защищены._
```

Ты можешь просто скопировать этот текст и вставить в файл `README.md` в своем проекте. Если нужны правки или дополнения — обращайся! 😎