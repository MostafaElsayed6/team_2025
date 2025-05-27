from django.shortcuts import render, redirect
from .models import ContactMessage


from django.shortcuts import render, redirect
from .models import ContactMessage

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        adres = request.POST.get("adres")  # إذا كنت تقصد "address" فيمكنك تغييره
        massage = request.POST.get("massage")  # تأكد من أن هذا الحقل مطابق لقاعدة البيانات
        
        # التحقق من تعبئة الحقول المطلوبة
        if name and email and adres and massage:
            data = ContactMessage(name=name, email=email, adres=adres, message=massage)
            data.save()
            return redirect('contact_success')  # قم بتعديل 'success_url' إلى مسار الصفحة المناسبة بعد الإرسال
        else:
            error = "يرجى تعبئة جميع الحقول المطلوبة."
            return render(request, 'contact/contact.html', {'error': error})
    
    return render(request, 'contact/contact.html')


def contact_success(request):
    return render(request, 'contact/contact_success.html')



# def contact_view(request):
#     name= request.POST.get("name")
#     email=request.POST.get ("email")
#     adres=request.POST.get("adres")
#     massage=request.POST.get("massage")
#     data=ContactMessage(name=name,email=email,adres=adres,message=massage)   # name=name, # email=email,
#     data.save()


    
 
    # return render(request, 'contact/contact.html',  )
