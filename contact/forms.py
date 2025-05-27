from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='الاسم', max_length=100)
    email = forms.EmailField(label='البريد الاليكتروني')
    subject = forms.CharField(label='عنوان الرسالة', max_length=200, required=False) # required=False إذا كان الحقل غير إلزامي
    message = forms.CharField(label='الرسالة', widget=forms.Textarea)