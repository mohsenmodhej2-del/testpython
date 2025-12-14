# Calculator - پروژه ماشین حساب پایتون

یک پروژه آماده و کامل پایتون با ساختار استاندارد

A complete Python calculator project with standard structure and best practices.

## ویژگی‌ها (Features)

- ✅ عملیات ریاضی پایه (Basic mathematical operations)
  - جمع (Addition)
  - تفریق (Subtraction)  
  - ضرب (Multiplication)
  - تقسیم (Division)
  - توان (Power)
  - جذر (Square Root)
- ✅ تست‌های کامل (Complete unit tests)
- ✅ ساختار استاندارد پروژه (Standard project structure)
- ✅ مستندات کامل (Full documentation)
- ✅ رابط خط فرمان (Command-line interface)

## نصب (Installation)

### پیش‌نیازها (Prerequisites)
```bash
python >= 3.7
```

### نصب از سورس (Install from source)
```bash
# کلون کردن مخزن
git clone https://github.com/mohsenmodhej2-del/testpython.git
cd testpython

# نصب پکیج
pip install -e .

# نصب وابستگی‌های توسعه (برای تست)
pip install -r requirements.txt
```

## استفاده (Usage)

### حالت تعاملی (Interactive Mode)
```bash
python -m calculator
```

یا اگر پکیج را نصب کرده‌اید:
```bash
calculator
```

### استفاده در کد پایتون (Use in Python Code)
```python
from calculator import Calculator

calc = Calculator()

# عملیات‌های پایه
result = calc.add(5, 3)        # 8
result = calc.subtract(10, 4)  # 6
result = calc.multiply(3, 4)   # 12
result = calc.divide(15, 3)    # 5.0
result = calc.power(2, 3)      # 8
result = calc.square_root(16)  # 4.0
```

## اجرای تست‌ها (Running Tests)

### استفاده از unittest
```bash
cd tests
python -m unittest test_calculator.py
```

### استفاده از pytest (در صورت نصب)
```bash
pytest tests/
```

با پوشش کد:
```bash
pytest --cov=calculator tests/
```

## ساختار پروژه (Project Structure)

```
testpython/
├── src/
│   └── calculator/
│       ├── __init__.py      # پکیج اصلی
│       ├── calculator.py    # کلاس Calculator
│       └── __main__.py      # نقطه ورود برنامه
├── tests/
│   ├── __init__.py
│   └── test_calculator.py   # تست‌های واحد
├── .gitignore               # فایل‌های نادیده گرفته شده
├── LICENSE                  # مجوز MIT
├── README.md                # این فایل
├── pyproject.toml          # پیکربندی پروژه
└── requirements.txt        # وابستگی‌های توسعه
```

## توسعه (Development)

### افزودن ویژگی جدید
1. کد را در `src/calculator/calculator.py` اضافه کنید
2. تست‌های مربوطه را در `tests/test_calculator.py` بنویسید
3. تست‌ها را اجرا کنید تا از صحت عملکرد اطمینان حاصل کنید

### اصول کدنویسی
- از docstring برای مستندسازی استفاده کنید
- تست برای تمام توابع بنویسید
- کد را ساده و خوانا نگه دارید

## مجوز (License)

این پروژه تحت مجوز MIT منتشر شده است. برای جزئیات بیشتر فایل LICENSE را ببینید.

## مشارکت (Contributing)

مشارکت‌ها خوش‌آمدند! لطفاً:
1. یک Fork از پروژه بگیرید
2. یک شاخه (branch) جدید ایجاد کنید
3. تغییرات خود را commit کنید
4. به شاخه push کنید
5. یک Pull Request ایجاد کنید
