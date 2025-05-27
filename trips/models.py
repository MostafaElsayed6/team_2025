# في ملف trips/models.py
from django.db import models
##################################################################################################
class UserInput(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    date_time = models.DateTimeField()
    trip_name = models.CharField(max_length=255)
    trip_location = models.CharField(max_length=255)
    trip_phone = models.CharField(max_length=20)
    trip_details = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.trip_name}"

###################################################################################################
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم التصنيف")
    image = models.ImageField(upload_to='category_images/', verbose_name="صورة التصنيف")

    def __str__(self):
        return self.name

class Trip(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200, verbose_name="عنوان الرحلة")
    location = models.CharField(max_length=200, verbose_name="موقع الرحلة", default="Default Location")
    responsible_phone = models.CharField(max_length=20, verbose_name="هاتف المسؤول")
    description = models.TextField(verbose_name="الوصف")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    duration = models.CharField(max_length=50, verbose_name="المدة")  # مثال: "3 ساعات"
    capacity = models.PositiveIntegerField(verbose_name="السعة")  # عدد الأماكن المتاحة
    image = models.ImageField(upload_to='trips/', verbose_name="الصورة")
    date = models.DateTimeField(verbose_name="تاريخ الرحلة")
    actve = models.BooleanField(default=True, verbose_name="مفعل")  # يُستخدم لتح
    # participants = models.ManyToManyField('userInput', related_name='trips', blank=True, verbose_name="المشاركون")
   
    def __str__(self):
        return self.title
    


###########################################################################################







# from django.db import models


# 