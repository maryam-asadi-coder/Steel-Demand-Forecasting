# Steel Demand Forecast & Inventory Dashboard

این پروژه یک داشبورد پیشرفته برای **پیش‌بینی تقاضای فولاد** و **بهینه‌سازی موجودی** است که از داده‌های شبیه‌سازی‌شده استفاده می‌کند. هدف پروژه ارائه ابزاری تحلیلی برای تصمیم‌گیری داده‌محور در مدیریت زنجیره تأمین است.

## Features

- پیش‌بینی **12 هفته آینده تقاضای فولاد** با استفاده از مدل Holt-Winters (Additive Trend & Seasonal).
- محاسبه **موجودی ایمن (Safety Stock)** و **نقطه سفارش مجدد (Reorder Point)** برای کاهش ریسک کمبود موجودی.
- نمایش **شاخص‌های عملکرد کلیدی (KPIs)**:
  - OTIF (On Time In Full)
  - کاهش ضایعات مواد اولیه
- نمودار تعاملی ترکیبی شامل: Demand، Forecast، Inventory، Safety Stock و Reorder Point.
- داشبورد ساخته شده با **Streamlit** و نمودارهای **Plotly**.

## Installation

ابتدا محیط مجازی بسازید (اختیاری اما توصیه‌شده):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
سپس کتابخانه‌های مورد نیاز را نصب کنید:
pip install -r requirements.txt

برای اجرای داشبورد:
streamlit run dashboard.py
