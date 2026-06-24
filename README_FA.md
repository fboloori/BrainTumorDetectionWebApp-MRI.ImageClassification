
  
## وب اپلیکیشن تشخیص تومور مغزی براساس تصاویر MRI 🧠

این پروژه یک سیستم یادگیری عمیق برای **طبقه‌بندی تصاویر MRI مغز** در چهار کلاس مختلف است که شامل یک مدل CNN مبتنی بر Transfer Learning (ResNet) و یک رابط کاربری تحت وب با Streamlit می‌باشد.

 
<img width="1920" height="1080" alt="1" src="https://github.com/user-attachments/assets/759847e6-a7a9-4409-bf92-b043a13bc669" />


## 📊 خروجی نمونه

در این پروژه، خروجی مدل شامل موارد زیر است:

- کلاس پیش‌بینی‌شده
- احتمال (Confidence) برای هر کلاس
- نمودار میله‌ای از نتایج

<img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/c7292971-912c-4436-8f2a-8d99d3b478ee" />



 
## 📌 کلاس‌های قابل پیش‌بینی

مدل تصاویر MRI را در چهار دسته زیر طبقه‌بندی می‌کند:

- Glioma Tumor
- Meningioma Tumor
- Pituitary Tumor
- Normal

---

## 🧠 توضیح کلی از مدل آموزش داده شده (فایل ipynb)

در این پروژه از یک دیتاست شامل تصاویر MRI مغز استفاده شده است که شامل چهار کلاس بالا می‌باشد.

### مراحل اصلی کار:

### 1. اعمال فیلتر روی تصاویر و Data Augmentation
برای افزایش تنوع داده‌های آموزشی از اعمال فیلترهای Blur, sobel , Clahe روی تصاویر استفاده و در نهایت مشخص شد که استفاده از تصاویر اصلی به همراه تصاویر Blur و CLAHE عملکرد بهتری را ایجاد می‌کند، در حالی که Sobel این طورنبود.
 

### 2. معماری مدل (Transfer Learning)

برای ساخت مدل از **شبکه از پیش آموزش‌دیده ResNet** به عنوان مدل پایه استفاده شده است.

- لایه‌های ابتدایی: Frozen (عدم آموزش)
- لایه‌های انتهایی:
  - Dense Layer
  - Classification Layer (Softmax با 4 نورون)

مزیت این روش:
- استخراج بهتر ویژگی‌ها (Feature Extraction)
- کاهش زمان آموزش
- افزایش دقت مدل
 

### 3. آموزش مدل

- استفاده از **Early Stopping**
- معیار توقف: کمترین `validation loss`
- معیار ذخیره بهترین مدل: بیشترین `validation recall`
- حداکثر epoch: 300
 

### 4. ارزیابی مدل

دقت مدل بالای 99 درصد بدست آمده و مدل نهایی روی داده‌های تستی که در فرآیند آموزش و validation استفاده نشده بودند، ارزیابی شد و نتایج نشان‌دهنده عملکرد عالی (در مثال تصاویر تستی ما بدون خطا) مدل در تطبیق پیش‌بینی با برچسب واقعی بود.

---

## 🌐 وب اپلیکیشن (Streamlit)

برای نمایش مدل و استفاده تعاملی، یک وب اپلیکیشن با Streamlit توسعه داده شده است.

### قابلیت‌ها:

- آپلود تصویر MRI
- پیش‌پردازش تصویر (Resize + Normalization)
- نمایش کلاس پیش‌بینی‌شده
- نمایش نمودار Confidence برای هر کلاس

---

## 📁 ساختار ریپازیتوری
```txt

├── streamlitCNN.py # کد اجرای وب اپلیکیشن Streamlit
├── opt1Channelmodel.h5 # مدل آموزش‌دیده (Saved Model)
├── brain-tumor.ipynb # نوتبوک آموزش و تحلیل مدل
├── 1.jpg # اسکرین‌شات محیط Streamlit
├── 2.jpg # نمونه خروجی مدل
└── README.md
```


---
 
## 🚀 نحوه اجرای پروژه


1. کلون کردن ریپو و رفتن به پوشه ی مربوطه
```bash
git clone https://github.com/fboloori/BrainTumorDetectionWebApp-MRI.ImageClassification.git
cd BrainTumorDetectionWebApp-MRI.ImageClassification
```
2. دانلود کردن فایل مدل آموزش داده شده:
 
مدل را از لینک زیر دانلود کنید و در فولدر کلون شده از مرحله قبل ذخیره کنید:

https://www.kaggle.com/code/fatemehboloori/brain-tumor/output?select=opt1Channelmodel.h5  
محل دانلود در تصویر زیر نشان داده شده است.

<img width="400" height="250" alt="h5model" src="https://github.com/user-attachments/assets/9cba6f01-5d1a-44bd-96e9-0e7b0c737502" />

اطمینان حاصل کنید که فایل مدل، دقیقا با نام پیش فرض آن ذخیره شود:"opt1Channelmodel.h5".
  


3. اجرای اپلیکیشن streamlit تحت وب:

```bash
python -m venv brain_tumor_env
brain_tumor_env\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

2. اجرای Streamlit App
```bash
streamlit run streamlitCNN.py
```
یا در صورت نیاز به تعیین پورت:
```bash
python -m streamlit run streamlitCNN.py --server.port 8080
```

📌 نکات مهم
مدل از قبل آموزش داده شده و در فایل.h5ذخیره شده است.
در زمان اجرا نیازی به آموزش مجدد مدل نیست.
فقط کافی است Streamlit اجرا شود و فایل مدل در کنار فایل پایتونی در کنار فایل کدل قرار داشته باشد و بعد اجرای streamlit، فایل تصویر آپلود گردد.




##✨ تکنولوژی‌های استفاده شده
- Python
- TensorFlow / Keras
- ResNet (Transfer Learning)
- Streamlit
- NumPy
- Matplotlib
- PIL
