# testpython - پروژه آماده پایتون

یک پروژه آماده و کامل پایتون با امکانات مختلف

A ready-made and complete Python project with various features.

## 📋 فهرست مطالب | Table of Contents

- [ویژگی‌ها | Features](#features)
- [نصب | Installation](#installation)
- [استفاده | Usage](#usage)
- [ساختار پروژه | Project Structure](#project-structure)
- [تست | Testing](#testing)
- [توسعه | Development](#development)

## ✨ ویژگی‌ها | Features

این پروژه شامل موارد زیر است:

- **Calculator Module**: ماژول ماشین حساب با عملیات پایه ریاضی
  - جمع، تفریق، ضرب، تقسیم
  - توان
  - ذخیره نتیجه آخرین محاسبه

- **Utility Functions**: توابع کمکی کاربردی
  - تابع سلام (Greeting)
  - فرمت‌دهی تاریخ
  - بررسی زوج یا فرد بودن عدد
  - بررسی اول بودن عدد
  - تولید دنباله فیبوناچی

- **Complete Test Suite**: مجموعه کامل تست‌ها
- **Modern Python Packaging**: پیکیج‌بندی مدرن پایتون
- **Documentation**: مستندات کامل

## 🚀 نصب | Installation

### نصب از سورس | Install from Source

```bash
# کلون کردن ریپازیتوری
git clone https://github.com/mohsenmodhej2-del/testpython.git
cd testpython

# نصب پکیج
pip install -e .

# یا با dependencies توسعه
pip install -e ".[dev]"
```

### نصب dependencies | Install Dependencies

```bash
pip install -r requirements.txt
```

## 💻 استفاده | Usage

### اجرای برنامه اصلی | Run Main Application

```bash
# اجرا به صورت ماژول
python -m testpython.main

# یا با استفاده از entry point
testpython
```

### استفاده در کد | Use in Code

```python
from testpython import Calculator, greet, format_date
from testpython.utils import is_prime, fibonacci

# استفاده از ماشین حساب
calc = Calculator()
result = calc.add(10, 5)
print(f"10 + 5 = {result}")

# سلام گفتن
message = greet("محمد")
print(message)

# بررسی اول بودن عدد
if is_prime(17):
    print("17 is a prime number")

# تولید دنباله فیبوناچی
fib_sequence = fibonacci(10)
print(f"Fibonacci: {fib_sequence}")
```

## 📁 ساختار پروژه | Project Structure

```
testpython/
├── testpython/           # پکیج اصلی
│   ├── __init__.py      # فایل مقداردهی اولیه
│   ├── calculator.py    # ماژول ماشین حساب
│   ├── utils.py         # توابع کمکی
│   └── main.py          # برنامه اصلی
├── tests/               # تست‌ها
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_utils.py
├── docs/                # مستندات
├── setup.py             # فایل نصب
├── setup.cfg            # تنظیمات نصب
├── pyproject.toml       # تنظیمات پروژه
├── requirements.txt     # وابستگی‌ها
├── .gitignore          # فایل‌های نادیده گرفته شده
└── README.md           # این فایل
```

## 🧪 تست | Testing

### اجرای تست‌ها | Run Tests

```bash
# اجرای تست‌ها با unittest
python -m unittest discover tests

# یا با pytest (اگر نصب باشد)
pytest

# اجرای تست‌ها با coverage
pytest --cov=testpython --cov-report=html
```

### تست‌های موجود | Available Tests

- تست‌های ماشین حساب (Calculator tests)
- تست‌های توابع کمکی (Utility functions tests)
- پوشش کامل کد (Full code coverage)

## 🛠 توسعه | Development

### نصب ابزارهای توسعه | Install Development Tools

```bash
pip install -r requirements.txt
```

### ابزارهای موجود | Available Tools

- **pytest**: فریم‌ورک تست
- **black**: فرمت‌کننده کد
- **flake8**: بررسی‌کننده کد
- **mypy**: بررسی‌کننده نوع

### دستورات مفید | Useful Commands

```bash
# فرمت کردن کد
black testpython tests

# بررسی کیفیت کد
flake8 testpython tests

# بررسی نوع
mypy testpython
```

## 📝 مجوز | License

MIT License

## 👨‍💻 نویسنده | Author

Your Name - your.email@example.com

## 🤝 مشارکت | Contributing

مشارکت‌ها خوشایند هستند! لطفاً یک Pull Request ارسال کنید.

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 تماس | Contact

برای سوالات یا پیشنهادات، لطفاً یک Issue ایجاد کنید.

For questions or suggestions, please create an Issue.
