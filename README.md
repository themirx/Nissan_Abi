# Nissan_Abi

## درباره پروژه
این پروژه یک وب‌سایت برای نمایشگاه خودرو و لاستیک نیسان است که با Django توسعه داده شده است.

## ویژگی‌ها
- نمایش خودروهای نیسان
- نمایش لاستیک‌های موجود
- احراز هویت با شماره موبایل
- پنل مدیریت
- جستجوی پیشرفته خودرو
- صفحه تماس با ما

## نصب و راه‌اندازی
1. پروژه را کلون کنید:
```bash
git clone https://github.com/themirx/Nissan_Abi.git
cd Nissan_Abi
```

2. محیط مجازی را فعال کنید:
```bash
python -m venv venv
source venv/bin/activate  # در لینوکس/مک
venv\Scripts\activate     # در ویندوز
```

3. نیازمندی‌ها را نصب کنید:
```bash
pip install -r requirements.txt
```

4. فایل `.env` را ایجاد کنید:
```bash
cp .env.example .env
```

5. پایگاه داده را راه‌اندازی کنید:
```bash
python manage.py migrate
```

6. یک کاربر ادمین ایجاد کنید:
```bash
python manage.py createsuperuser
```

7. سرور را اجرا کنید:
```bash
python manage.py runserver
```

## ساختار پروژه
- `cars/`: اپلیکیشن اصلی
  - `models.py`: مدل‌های داده
  - `views.py`: کنترلرها
  - `templates/`: قالب‌های HTML
  - `static/`: فایل‌های استاتیک
  - `urls.py`: مسیریابی

## نیازمندی‌ها
- Python 3.8+
- Django 5.2
- Pillow 10.2.0
- python-dotenv 1.0.1
- requests 2.31.0

## مجوز
این پروژه تحت مجوز MIT منتشر شده است.
