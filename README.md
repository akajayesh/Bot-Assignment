 Django Internship Assignment - Backend API with Celery & Telegram Bot

This project was built for an internship assignment under time constraints.
Faced issues with Celery on Windows and resolved them using --pool=solo mode.
The bot is simple but works . So it handles only /start for now.

## Tech Stack I used for building this project are :-

- Django & Django REST Framework
- Celery + Redis
- Telegram Bot API
- Python Decouple
- JWT Auth (or Token Auth)

---

##  It includes Features like :-

-  Public & Protected API Endpoints
-  User Registration with async email (Celery)
-  Telegram Bot integration (/start saves username)
-  Token-based Authentication

---

## Follow these Setup Instructions:-

### 1. Clone the Repo -


git clone https://github.com/akajayesh/Bot-Assignment.git
cd backend-assignment

### 2. Setup the virtual environement - 

python -m venv venv 
venv\Scripts\activate
pip install -r requirements.txt

### 3. Now configure your .env file -
SECRET_KEY=your-secret-key
DEBUG=True
TELEGRAM_BOT_TOKEN=your-bot-token
DEFAULT_FROM_EMAIL=admin@example.com

### 4. Run the project -

python manage.py migrate
python manage.py runserver


Last but not least - 
This project was built by me as part of an internship assignment.
Used online documentation, StackOverflow, and tools like VSCode Copilot/ChatGPT as occasional reference .
Every feature and bugfix was tested manually by me.
