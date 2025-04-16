# BMW نمایندگی فروش خودرو و لاستیک

این پروژه یک وب‌سایت برای نمایندگی فروش خودرو و لاستیک BMW است که با Django توسعه داده شده است.

## ویژگی‌ها

- نمایش خودروهای BMW
- نمایش لاستیک‌های موجود
- سیستم احراز هویت با شماره موبایل
- پنل مدیریت برای ادمین‌ها
- جستجوی پیشرفته خودروها
- صفحه تماس با ما

## نصب و راه‌اندازی

1. کلون کردن پروژه:
```bash
git clone https://github.com/your-username/bmw.git
cd bmw
```

2. ایجاد محیط مجازی و نصب نیازمندی‌ها:
```bash
python -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate
pip install -r requirements.txt
```

3. اجرای مایگریشن‌ها:
```bash
python manage.py migrate
```

4. ایجاد کاربر ادمین:
```bash
python manage.py createsuperuser
```

5. اجرای سرور:
```bash
python manage.py runserver
```

## ساختار پروژه

- `cars/`: اپلیکیشن اصلی پروژه
  - `models.py`: مدل‌های دیتابیس
  - `views.py`: ویوهای پروژه
  - `urls.py`: مسیرهای پروژه
  - `templates/`: فایل‌های قالب
  - `static/`: فایل‌های استاتیک
  - `media/`: فایل‌های آپلود شده

## نیازمندی‌ها

- Python 3.8+
- Django 5.2
- Pillow
- و سایر پکیج‌های موجود در `requirements.txt`

## مجوز

این پروژه تحت مجوز MIT منتشر شده است. 