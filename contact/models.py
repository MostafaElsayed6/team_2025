from django.db import models

# Create your models here.


    


from django.db import models

class ContactMessage(models.Model):
    # الحقول المطابقة لحقول النموذج
    name = models.CharField(max_length=100, verbose_name="الاسم")  # حقل الاسم (مطلوب)
    email = models.EmailField(verbose_name="البريد الإلكتروني")     # حقل البريد (مطلوب)
    adres = models.CharField(max_length=200, blank=True, verbose_name="عنوان الرسالة")  # حقل العنوان (غير مطلوب)
    message = models.TextField(verbose_name="الرسالة", blank=True)  # حقل الرسالة (غير مطلوب حاليًا في النموذج)

    # توقيت إرسال الرسالة (يضاف تلقائيًا)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإرسال")

    class Meta:
        verbose_name = "رسالة تواصل"
        verbose_name_plural = "رسائل التواصل"
        ordering = ['-created_at']  # ترتيب الرسائل من الأحدث إلى الأقدم

    def __str__(self):
        return f"رسالة من {self.name} - {self.email}"